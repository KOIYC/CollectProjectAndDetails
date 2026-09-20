"""kb_selftest — 判据自测（stdlib unittest，零第三方依赖）。

为什么需要：tools/ 里全是「一句话判据」，判据错了不会报错、只会静默给出错误答案。
实测踩过的两次：① `make_item` 引用局部变量 `links` 让 13/13 渠道全 error
（一行回归，靠人工发现）；② 读 JSONL 用 `str.splitlines()` 把含 U+2028 的记录
静默丢掉（raw 计数与 kb_analyze 当场打架）。这两个都不是「跑起来就报错」的类型，
所以必须有断言把它钉住。

用法：python tools/kb_selftest.py
      python -m unittest discover -s tools -p "kb_selftest.py"
覆盖：JSONL 读写纪律、project_url 校验、正文完整度分级、评论缺口判定、
      命名规则（slugify / item_id）、以及「raw 计数与 kb_analyze 同口径」的回归断言。
"""
from __future__ import annotations

import glob
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import kb_backfill as BF      # noqa: E402
import kb_collect as KC       # noqa: E402
import kb_common as KB        # noqa: E402


class JsonlDiscipline(unittest.TestCase):
    """读 JSONL 必须按 \\n 切；写 JSONL 必须把 U+2028 类字符清掉。"""

    def test_splitlines_would_lose_the_record(self):
        # 先钉住「为什么不能用 splitlines」：同一份内容，两种切法结果不同。
        text = '{"body": "a\u2028b"}\n'
        self.assertEqual(len(text.split("\n")) - 1, 1)          # 按 \n 切 = 1 条
        self.assertEqual(len(text.splitlines()), 2)             # splitlines = 2 段（全废）

    def test_append_then_load_roundtrip(self):
        with tempfile.TemporaryDirectory() as td:
            p = pathlib.Path(td) / "x.jsonl"
            KB.append_jsonl(p, [{"item_id": "a", "title": "t\u2028x",
                                 "body": "line1\u2028line2",
                                 "comments": [{"text": "c\u2028d"}]}])
            raw = p.read_text(encoding="utf-8")
            self.assertEqual(len(raw.split("\n")) - 1, 1)       # 写盘后仍是「一行一条」
            self.assertNotIn("\u2028", raw)                     # 地雷已在写入侧清掉
            rows = KB.load_ndjson(p)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["body"], "line1\nline2")   # 行分隔符归一成 \n
            self.assertEqual(rows[0]["comments"][0]["text"], "c\nd")
            self.assertEqual(rows[0]["title"], "t\nx")


class ProjectUrlGuard(unittest.TestCase):
    """project_url 是项目页文件名 + 跨渠道归并键，错值会静默合并两个项目。"""

    def test_rejects_obviously_wrong_values(self):
        bad = ["", "not-a-url", "https://localhost:8080/`", "http://127.0.0.1/x",
               "https://liqi.io/creators:", "https://blog.cloudflare.com/saving-100-tb-of-ram",
               "https://news.ycombinator.com/item?id=1", "https://github.com",
               "http://intranet-host/x"]
        for u in bad:
            with self.subTest(u=u):
                self.assertTrue(KC.project_url_reject(u), f"应被拒绝: {u!r}")

    def test_accepts_real_project_sites(self):
        for u in ["https://cursor.com/", "https://github.com/owner/repo",
                  "https://page-rage.com/", "https://koieditor.com/"]:
            with self.subTest(u=u):
                self.assertEqual(KC.project_url_reject(u), "", f"不该拒绝: {u!r}")

    def test_derive_skips_bad_link_and_picks_next(self):
        body = "看这里 https://localhost:8080/` 还有 https://real.app/ 就这样"
        url = "https://www.v2ex.com/t/1"
        self.assertEqual(KC.derive_project_url(url, body), "https://real.app/")


class BodyCompleteness(unittest.TestCase):
    def test_levels(self):
        self.assertEqual(KB.body_completeness(""), "empty")
        self.assertEqual(KB.body_completeness("x" * 50), "snippet")
        self.assertEqual(KB.body_completeness("x" * 500), "full")
        self.assertEqual(KB.body_completeness("x" * 500, {}, "signal"), "metadata_only")
        self.assertEqual(KB.body_completeness("x" * 500 + " 阅读全文"), "summary")
        self.assertEqual(KB.body_completeness("x" * 500, {"body_truncated": True}), "summary")


class CommentsGap(unittest.TestCase):
    """评论缺口判定：与「平台计数」比，而不是「抓到 0 条就当没人评论」。"""

    def test_gap_visible_below_old_threshold(self):
        # 旧判据要求 platform >= 20 → 平台报 3 条、抓到 0 条的条目永远进不了队列
        r = {"comments": [], "metrics": {"comments": 3}}
        self.assertTrue(BF.comments_gap(r))

    def test_no_gap_when_platform_says_zero(self):
        self.assertEqual(BF.comments_gap({"comments": [], "metrics": {"comments": 0}}), "")

    def test_no_gap_when_fully_grabbed(self):
        r = {"comments": [{"text": "a"}], "metrics": {"comments": 1}}
        self.assertEqual(BF.comments_gap(r), "")

    def test_truncated_is_not_a_gap_and_error_is(self):
        self.assertEqual(BF.comments_gap({"comments": [], "comments_truncated": True,
                                          "metrics": {"comments": 99}}), "")
        r = {"comments": [], "metrics": {"comments": 1},
             "extra": {"comments_error": "FetchError"}}
        self.assertIn("取数失败", BF.comments_gap(r))


class NamingRules(unittest.TestCase):
    def test_slugify_strips_wikilink_syntax(self):
        for ch in "[]#^`":
            self.assertNotIn(ch, KB.slugify(f"a{ch}b"))

    def test_slugify_idempotent(self):
        once = KB.slugify("Show HN: Test [beta] #1", 50)
        self.assertEqual(KB.slugify(once, 50), once)

    def test_item_id_stable_and_short(self):
        a = KB.item_id_for("https://Example.com/x?a=1", "T", "ch")
        b = KB.item_id_for("https://Example.com/x?a=1", "T", "ch")
        self.assertEqual(a, b)
        self.assertEqual(len(a), 16)


class RawCountRegression(unittest.TestCase):
    """回归断言：两种读法必须给出同一个事实源条数（曾经差 7 条）。"""

    def test_ndjson_total_matches_kb_analyze(self):
        import kb_analyze as KA
        files = glob.glob(str(KB.DIR_RAW / "*" / "*.jsonl"))
        if not files:
            self.skipTest("库里还没有原始归档")
        by_lines = sum(len(KB.load_ndjson(pathlib.Path(f))) for f in files)
        self.assertEqual(by_lines, len(KA.load_records()),
                         "load_ndjson 与 kb_analyze.load_records 必须同口径")


class InvariantsGreen(unittest.TestCase):
    """收工门：kb_healthcheck 的 ① ~ ⑤ 必须全绿（跑真库，只读不写）。"""

    def test_healthcheck_hard_gates(self):
        import subprocess
        p = subprocess.run([sys.executable, "-X", "utf8",
                            str(KB.ROOT / "tools" / "kb_healthcheck.py")],
                           capture_output=True, text=True, encoding="utf-8",
                           cwd=str(KB.ROOT))
        self.assertEqual(p.returncode, 0, p.stderr[:500])
        out = p.stdout
        for gate in ("①", "②", "③", "④", "⑤"):
            line = next((ln for ln in out.splitlines() if ln.startswith(gate)), "")
            self.assertTrue(line, f"缺 {gate} 的输出")
            self.assertNotIn("!!", line, f"{gate} 不是绿的：{line}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
