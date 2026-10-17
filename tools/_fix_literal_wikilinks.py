"""统计 / 修复：正文段落里的字面 wikilink 语法字符（[[ ]]）。

来源：原始内容本身含 `[[...]]`（如 HN 标题 "a [[slopcore]] production"），
写进 note 的「正文 / 摘要正文」段落后被 Obsidian 解析成 wikilink → ④ 断链。

判定只落在两个段落（不碰「导航」段与观测历史表里的真链接）：
  - 语料页：`## 正文` 到下一个 `## ` 之间
  - 实体页/人物页：`## 摘要正文` 到下一个 `## ` 之间

用法：
  python tools/_fix_literal_wikilinks.py --dry
  python tools/_fix_literal_wikilinks.py --apply
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ("## 正文", "## 摘要正文")
HEAD_RE = re.compile(r"^## ", re.M)
LINK_RE = re.compile(r"(?<!\\)\[\[([^\[\]\n]{1,120})\]\](?!\])")


def escape(s: str) -> str:
    return s.replace("[[", "\\[[").replace("]]", "\\]]")


def fix_text(text: str) -> tuple[str, int]:
    lines = text.split("\n")
    out: list[str] = []
    inside = False
    hits = 0
    for ln in lines:
        if ln.startswith("## "):
            inside = ln.strip() in SECTIONS
            out.append(ln)
            continue
        if inside and "[[" in ln:
            new = LINK_RE.sub(lambda m: escape(m.group(0)), ln)
            if new != ln:
                hits += len(LINK_RE.findall(ln))
                out.append(new)
                continue
        out.append(ln)
    return "\n".join(out), hits


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    dry = not a.apply

    targets = []
    for d in ("20-语料", "10-项目", "30-人物", "40-方法论", "80-归档"):
        p = ROOT / d
        if p.exists():
            targets.extend(p.rglob("*.md"))

    total_files = 0
    total_links = 0
    for f in targets:
        try:
            raw = f.read_text(encoding="utf-8")
        except Exception:
            continue
        new, hits = fix_text(raw)
        if hits:
            total_files += 1
            total_links += hits
            print(f"  {hits:3d} 处  {f.relative_to(ROOT)}")
            if not dry:
                f.write_text(new, encoding="utf-8", newline="\n")
    print(f"{'[dry]' if dry else '[apply]'} 文件 {total_files} 个 · 字面链接 {total_links} 处")


if __name__ == "__main__":
    main()
