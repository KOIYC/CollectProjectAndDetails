"""临时脚本：列出全库失效 wikilink（与 kb_healthcheck ④ 同判据）。
写成文件而不是命令行内联 —— MSYS 会改写内联正则里的反斜杠，实测已导致判据静默失效两次。
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path('tools').resolve()))
import kb_common as KB

ROOT = pathlib.Path('.')
LINK = re.compile(r"\[\[(.+?)\]\]")
JUNK = set('[]"`$*' + chr(92))

notes = [p for p in ROOT.rglob('*.md')
         if not any(x.startswith('.') for x in p.relative_to(ROOT).parts)]
by_rel = {p.relative_to(ROOT).with_suffix('').as_posix() for p in notes}
by_name = {}
for p in notes:
    by_name[p.stem] = by_name.get(p.stem, 0) + 1
alias = set()
for p in notes:
    sn = KB.split_note(p.read_text(encoding='utf-8'))
    if sn:
        alias |= set(KB.fm_list(sn[0], 'aliases'))


def resolves(s: str) -> bool:
    if not s:
        return False
    if s in by_rel or s in alias:
        return True
    if s.endswith('.md') and s[:-3] in by_rel:
        return True
    t = s.split('/')[-1]
    if t.endswith('.md'):
        t = t[:-3]
    return bool(by_name.get(t)) or t in alias


total = {}
for f in sorted(ROOT.rglob('*.md')):
    if any(x.startswith('.') for x in f.relative_to(ROOT).parts):
        continue
    txt = KB.strip_code(f.read_text(encoding='utf-8'))
    if '[[' not in txt:
        continue
    for m in LINK.finditer(txt):
        raw = m.group(1).split('|')[0].strip()
        tgt = raw.split('#')[0].strip()
        if not tgt or (JUNK & set(tgt)):
            continue
        if resolves(raw) or resolves(tgt):
            continue
        total.setdefault(raw, []).append(f.relative_to(ROOT).as_posix())

print(f'失效链接目标 {len(total)} 个，涉及 {sum(len(v) for v in total.values())} 处')
for t, srcs in sorted(total.items()):
    print(f'  [[{t}]]  <-  {srcs[0]}' + (f'（共 {len(srcs)} 处）' if len(srcs) > 1 else ''))
