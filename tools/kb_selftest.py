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
import types
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import kb_backfill as BF      # noqa: E402
import kb_collect as KC       # noqa: E402
import kb_common as KB        # noqa: E402
import kbc_channels as KCH    # noqa: E402


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

    def test_rejects_profile_pages_even_without_trailing_punct(self):
        # R7 撞车案例的「根形态」：liqi.io/creators（无冒号）是人务页，不是项目站点。
        for u in ["https://liqi.io/creators", "https://example.com/users/tom",
                  "https://example.com/u/tom", "https://example.com/profile",
                  "https://example.com/people/tom", "https://example.com/@tom"]:
            with self.subTest(u=u):
                self.assertTrue(KC.project_url_reject(u), f"应被拒绝: {u!r}")

    def test_accepts_real_project_sites(self):
        for u in ["https://cursor.com/", "https://github.com/owner/repo",
                  "https://page-rage.com/", "https://koieditor.com/"]:
            with self.subTest(u=u):
                self.assertEqual(KC.project_url_reject(u), "", f"不该拒绝: {u!r}")

    def test_rejects_www_variants_of_non_project_hosts(self):
        # 回归：早先拿 netloc 直接比 NON_PROJECT_HOSTS，`www.` 前缀一律漏网（实测 5/5 放行），
        # 讨论页/聚合站于是被当成项目官网写进 project_url（healthcheck ⑦ 可疑值的根因）。
        for u in ["https://www.bilibili.com/video/BV1Q5QgB5EGT",
                  "https://www.youtube.com/watch?v=abc",
                  "https://www.reddit.com/gallery/1abc",
                  "https://www.producthunt.com/products/snotch?utm_source=other",
                  "https://www.v2ex.com/go/create",
                  "https://www.github.com",
                  "https://www.notion.so/some-page"]:
            with self.subTest(u=u):
                self.assertTrue(KC.project_url_reject(u), f"应被拒绝: {u!r}")

    def test_accepts_www_variant_of_real_project_site(self):
        # 去 www 只为「比对名单」，不能把合法的 www 项目站一起误杀。
        for u in ["https://www.page-rage.com/", "https://www.cursor.com/"]:
            with self.subTest(u=u):
                self.assertEqual(KC.project_url_reject(u), "", f"不该拒绝: {u!r}")

    def test_link_re_does_not_swallow_markdown_escape(self):
        # 回归：LINK_RE 未排除反斜杠 → 抓到 `...?utm\_source=other`，
        # norm_url 把 `\` 编码成 `%5C` 写进 project_url（实测 1 条 live 脏值）。
        body = (r"[https://www.producthunt.com/products/snotch?utm\_source=other]"
                r"(https://www.producthunt.com/products/snotch) 正文")
        found = KC.LINK_RE.findall(body)
        self.assertTrue(found, "至少应抓到 markdown 链接里的 URL")
        for u in found:
            with self.subTest(u=u):
                self.assertNotIn("\\", u, f"不该把 markdown 转义反斜杠带进来: {u!r}")

    def test_derive_skips_bad_link_and_picks_next(self):
        body = "看这里 https://localhost:8080/` 还有 https://real.app/ 就这样"
        url = "https://www.v2ex.com/t/1"
        self.assertEqual(KC.derive_project_url(url, body), "https://real.app/")


class NameAuditScope(unittest.TestCase):
    """命名审计范围：去重暂存区不参与（否则 live 页与它的同 stem 副本稳定误报）。"""

    def test_dedupe_quarantine_excluded_but_real_archive_checked(self):
        import kb_name_audit as NA
        self.assertTrue(NA._is_quarantined(
            KB.ROOT / "80-归档/重复副本/20260921T020724/20-语料/posts/betalist/2026-09-21/a.md"))
        self.assertFalse(NA._is_quarantined(
            KB.ROOT / "80-归档/posts/hn_show/2026-09-21/a.md"), "冻结区正文仍要查语法字符")
        self.assertFalse(NA._is_quarantined(
            KB.ROOT / "20-语料/posts/hn_show/2026-09-21/a.md"))


class FrontmatterRoundtrip(unittest.TestCase):
    """frontmatter 读写必须对称：write_note 用 json.dumps 写双引号标量，fm_scalars 必须解码。

    不对称的后果不是「显示难看」：project_url 多一个反斜杠就换一个项目页 hash，
    navfix 于是写出指向不存在页面的死链（healthcheck ④ 红，实测 3 条）。
    """

    def test_backslash_and_quote_values_survive_roundtrip(self):
        with tempfile.TemporaryDirectory() as td:
            p = pathlib.Path(td) / "n.md"
            pu = "https://store.steampowered.com/app/1/Besos\\_Shawarma"
            KB.write_note(p, {"type": "corpus", "project_url": pu,
                              "title": 'He said "hi"'}, "body")
            head, _body = KB.split_note(p.read_text(encoding="utf-8"))
            fm = KB.fm_scalars(head)
            self.assertEqual(fm["project_url"], pu, "反斜杠不能被 YAML/JSON 转义放大")
            self.assertEqual(fm["title"], 'He said "hi"')

    def test_plain_and_unquoted_values_still_read(self):
        fm = KB.fm_scalars('---\nitem_id: "abc"\ntopic: 游戏\nshard: 2026-09-21\n---')
        self.assertEqual(fm["item_id"], "abc")
        self.assertEqual(fm["topic"], "游戏")          # set_fm_scalar 写的是裸值
        self.assertEqual(fm["shard"], "2026-09-21")


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


class BodyCacheGuard(unittest.TestCase):
    """BodyCache：只增不减 + 只在更长时更新 + 损坏隔离（损坏=重烧 Exa 额度）。"""

    def _cache(self, td):
        return KB.BodyCache(path=pathlib.Path(td) / "body_cache.json")

    def test_only_longer_wins(self):
        with tempfile.TemporaryDirectory() as td:
            c = self._cache(td)
            self.assertFalse(c.put("a", "short"))                    # < BODY_MIN 直接拒
            self.assertTrue(c.put("a", "x" * KB.BODY_MIN))
            self.assertFalse(c.put("a", "y" * KB.BODY_MIN))          # 等长不覆盖
            self.assertTrue(c.put("a", "z" * (KB.BODY_MIN + 10)))    # 更长才更新
            self.assertEqual(len(c.get("a")["body"]), KB.BODY_MIN + 10)

    def test_roundtrip_and_dirty_flag(self):
        with tempfile.TemporaryDirectory() as td:
            p = pathlib.Path(td) / "body_cache.json"
            c = KB.BodyCache(path=p)
            c.put("a", "x" * KB.BODY_MIN)
            self.assertTrue(c.dirty)
            c.save()
            self.assertFalse(KB.BodyCache(path=p).dirty)             # 重载后 clean
            self.assertEqual(len(KB.BodyCache(path=p).get("a")["body"]), KB.BODY_MIN)

    def test_corrupt_file_is_quarantined_not_silent(self):
        with tempfile.TemporaryDirectory() as td:
            p = pathlib.Path(td) / "body_cache.json"
            p.write_text('{"version": 1, "items": {broken', encoding="utf-8")
            c = KB.BodyCache(path=p)
            self.assertEqual(c.items, {})                            # 从零开始（而非崩溃）
            baks = list(p.parent.glob("*.corrupt-*.bak"))
            self.assertEqual(len(baks), 1, "损坏现场必须被隔离保留")     # 且响亮告警已打印


class SeenLedger(unittest.TestCase):
    """seen 账本：metric_history 去重 + content_hash 存取。"""

    def test_touch_dedups_unchanged_metrics(self):
        with tempfile.TemporaryDirectory() as td:
            s = KB.Seen(path=pathlib.Path(td) / "seen.json")
            s.touch("a", "ch", "n.md", {"stars": 10})
            self.assertFalse(s.touch("a", "ch", "n.md", {"stars": 10}), "指标没变不该追加历史点")
            self.assertTrue(s.touch("a", "ch", "n.md", {"stars": 11}))
            rec = s.get("a")
            self.assertEqual(len(rec["metric_history"]), 2)
            s.touch("a", "ch", "n.md", content_hash="h1")
            self.assertEqual(s.content_hash("a"), "h1")


class MakeItemGuard(unittest.TestCase):
    """make_item：project_url 校验 + 推导 + url 兜底（13 渠道全挂事故的发生地）。"""

    def test_explicit_bad_project_url_is_rejected_and_recorded(self):
        it = KC.make_item(source_id="v2ex", source_name="V2EX", title="t",
                          url="https://www.v2ex.com/t/1", project_url="https://liqi.io/creators:")
        self.assertIsNone(it["project_url"])
        self.assertIn("尾部有标点", it["extra"]["project_url_rejected"])

    def test_good_project_url_is_normalized(self):
        it = KC.make_item(source_id="x", source_name="X", title="t", url="https://a.com/1",
                          project_url="http://www.MyApp.io/?utm_src=x")
        self.assertEqual(it["project_url"], "https://myapp.io/")

    def test_body_link_used_as_fallback(self):
        it = KC.make_item(source_id="v2ex", source_name="V2EX", title="t",
                          url="https://www.v2ex.com/t/1",
                          body="我做了一个工具 https://mytool.app/ 欢迎试用")
        self.assertEqual(it["project_url"], "https://mytool.app/")

    def test_url_falls_back_to_project_url(self):
        it = KC.make_item(source_id="s", source_name="S", title="t",
                          url="", project_url="https://app.io/")
        self.assertEqual(it["url"], "https://app.io/")
        self.assertEqual(it["item_id"], KB.item_id_for("https://app.io/", "t", "s"))


class MiniYamlParser(unittest.TestCase):
    """channels.yaml 子集解析器（从 kb_collect 迁入 kb_common 后钉住行为）。"""

    def test_subset_roundtrip(self):
        text = "\n".join([
            "# 注释行",
            "version: 1",
            "debug: true",
            "ratio: 0.5",
            "name: \"带引号: 值\"",
            "empty_list: []",
            "inline: [a, b, 3]",
            "channels:",
            "  - id: hn_show",
            "    enabled: true",
            "    limit: 40",
            "    params:",
            "      window_days: 3",
            "      tags: [show_hn]",
            "  - id: v2ex",
            "    enabled: false",
        ])
        with tempfile.TemporaryDirectory() as td:
            p = pathlib.Path(td) / "c.yaml"
            p.write_text(text, encoding="utf-8")
            reg = KB.load_channels_yaml(p)
        self.assertEqual(reg["version"], 1)
        self.assertTrue(reg["debug"])
        self.assertEqual(reg["ratio"], 0.5)
        self.assertEqual(reg["name"], "带引号: 值")
        self.assertEqual(reg["inline"], ["a", "b", 3])
        c1 = reg["channels"][0]
        self.assertEqual(c1["params"]["window_days"], 3)
        self.assertEqual(c1["params"]["tags"], ["show_hn"])
        self.assertFalse(reg["channels"][1]["enabled"])

    def test_load_registry_picks_enabled(self):
        with tempfile.TemporaryDirectory() as td:
            p = pathlib.Path(td) / "c.yaml"
            p.write_text("channels:\n  - id: a\n    enabled: true\n"
                         "  - id: b\n    enabled: false\n", encoding="utf-8")
            reg = KB.load_registry(p)
        self.assertEqual([c["id"] for c in reg["_enabled_channels"]], ["a"])


class FrontmatterHelpers(unittest.TestCase):
    """frontmatter 定点读写（navfix/reclassify 的自愈都靠它）。"""

    NOTE = "---\ntype: corpus\ntitle: \"你好\"\ntags:\n  - 语料\n  - hn\n---\n\n# 正文\n"

    def test_split_and_scalars(self):
        head, rest = KB.split_note(self.NOTE)
        self.assertTrue(head.startswith("---"))
        self.assertTrue(rest.startswith("\n---"))
        fm = KB.fm_scalars(head)
        self.assertEqual(fm["type"], "corpus")
        self.assertEqual(fm["title"], "你好")
        self.assertEqual(fm["tags"], "")             # 列表块的 key 会带空值出现，但**值**读不到

    def test_set_scalar_insert_and_replace(self):
        head, rest = KB.split_note(self.NOTE)
        head2 = KB.set_fm_scalar(head, "kind", "project")
        self.assertIn("kind: project", head2)
        head3 = KB.set_fm_scalar(head2, "kind", "person")
        self.assertNotIn("kind: project", head3)
        self.assertIn("kind: person", head3)
        self.assertEqual(KB.split_note(head3 + rest)[1], rest)   # 正文不动

    def test_write_note_roundtrip(self):
        with tempfile.TemporaryDirectory() as td:
            p = pathlib.Path(td) / "n.md"
            KB.write_note(p, {"type": "project", "title": "T", "n": 3,
                              "tags": ["项目", "hn"], "params": {"k": 1}}, "# H\n\nbody")
            text = p.read_text(encoding="utf-8")
        head, _ = KB.split_note(text)
        fm = KB.fm_scalars(head)
        self.assertEqual(fm["type"], "project")
        self.assertEqual(fm["n"], "3")
        self.assertIn('"k": 1', head)                # dict 必须走 JSON，不能 str(dict)
        self.assertIn("- hn", text)


class RotationPolicy(unittest.TestCase):
    """_meta 轮转：同前缀只留最新 N 份（undo 凭证由 git 历史兜底）。"""

    def test_rotate_files_sorts_by_name_not_mtime(self):
        # 轮转必须按**文件名**（内嵌时间戳）排序：紧密循环里 mtime 分辨率不可靠，
        # 且任何 touch（git checkout/复制回放）都会骗过它（2026-09-20 实测保留错 3 份）。
        with tempfile.TemporaryDirectory() as td:
            d = pathlib.Path(td)
            names = [f"prune_manifest_20260920T00000{i}.json" for i in range(5)]
            for i, n in enumerate(names):                      # 反序写：最新的先落盘
                (d / n).write_text("{}", encoding="utf-8")
                import os as _os
                _os.utime(d / n, (1e9, 1e9 + (4 - i) * 3600))  # mtime 与名字序**相反**
            removed = KB.rotate_files(d, "prune_manifest_", 3)
            self.assertEqual(removed, 2)
            left = sorted(p.name for p in d.glob("prune_manifest_*"))
            self.assertEqual(left, names[2:])                   # 按名字留最新 3 份

    def test_rotate_files_keeps_newest(self):
        with tempfile.TemporaryDirectory() as td:
            d = pathlib.Path(td)
            for i in range(5):
                (d / f"prune_manifest_20260920T00000{i}.json").write_text("{}", encoding="utf-8")
            removed = KB.rotate_files(d, "prune_manifest_", 3)
            self.assertEqual(removed, 2)
            left = sorted(p.name for p in d.glob("prune_manifest_*"))
            self.assertEqual(len(left), 3)
            self.assertIn("prune_manifest_20260920T000004.json", left)   # 保留最新

    def test_rotate_runs_keeps_latest_json(self):
        with tempfile.TemporaryDirectory() as td:
            d = pathlib.Path(td) / "runs"
            d.mkdir()
            (d / "latest.json").write_text("{}", encoding="utf-8")
            for i in range(4):
                (d / f"20260920T00000{i}.json").write_text("{}", encoding="utf-8")
            removed = KB.rotate_runs(keep=2, directory=d)
            self.assertEqual(removed, 2)
            left = sorted(p.name for p in d.glob("*.json"))
            self.assertIn("latest.json", left)                       # 永远保留
            self.assertEqual(len(left), 3)
            self.assertIn("20260920T000003.json", left)              # 保留最新


class PublishedWindow(unittest.TestCase):
    """--since/--until 通用裁剪：无发布时间的条目不丢（丢它=放大数据缺口）。"""

    def test_filter_bounds(self):
        from datetime import datetime as DT
        items = [
            {"item_id": "old", "published_at": "2026-07-01T00:00:00+08:00"},
            {"item_id": "in", "published_at": "2026-08-15T12:00:00+08:00"},
            {"item_id": "new", "published_at": "2026-09-20T00:00:00+08:00"},
            {"item_id": "unknown", "published_at": None},
        ]
        since = int(DT(2026, 8, 1, tzinfo=KB.CST).timestamp())
        until = int(DT(2026, 9, 1, tzinfo=KB.CST).timestamp())
        kept, dropped = KCH.filter_published(items, since, until)
        self.assertEqual({it["item_id"] for it in kept}, {"in", "unknown"})
        self.assertEqual(dropped, 2)

    def test_no_bounds_is_noop(self):
        items = [{"item_id": "a", "published_at": "2026-01-01"}]
        kept, dropped = KCH.filter_published(items)
        self.assertEqual(kept, items)
        self.assertEqual(dropped, 0)

    def test_pub_ts_lenient(self):
        self.assertIsNotNone(KCH._pub_ts("2026-09-20T10:00:00Z"))
        self.assertIsNotNone(KCH._pub_ts("2026-09-20"))
        self.assertIsNone(KCH._pub_ts("not-a-date"))
        self.assertIsNone(KCH._pub_ts(None))


class InPlaceRefresh(unittest.TestCase):
    """语料 note 原地刷新与归档不穿透（2026-09-21 零点 45 孤儿事故的钉死断言）。"""

    def test_note_bucket_keeps_existing_shard(self):
        seen = types.SimpleNamespace(items={"a": {"note": "20-语料/posts/hn_show/2026-09-20/x.md"}})
        self.assertEqual(KB.note_bucket(seen, "a", "2026-09-21"), "2026-09-20")

    def test_note_bucket_falls_back_for_new(self):
        seen = types.SimpleNamespace(items={})
        self.assertEqual(KB.note_bucket(seen, "new", "2026-09-21"), "2026-09-21")

    def test_free_dup_name_walks_chain(self):
        # -dup 被占时必须顺延 -dup2/-dup3……单发后缀会**静默覆盖**冻结区历史
        import kb_prune as PR
        with tempfile.TemporaryDirectory() as td:
            d = pathlib.Path(td)
            (d / "x.md").write_text("a", encoding="utf-8")
            (d / "x-dup.md").write_text("b", encoding="utf-8")
            self.assertEqual(PR._free_dup_name(d / "x.md").name, "x-dup2.md")
            (d / "x-dup2.md").write_text("c", encoding="utf-8")
            self.assertEqual(PR._free_dup_name(d / "x.md").name, "x-dup3.md")


if __name__ == "__main__":
    unittest.main(verbosity=2)
