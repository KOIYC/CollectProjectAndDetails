"""临时脚本：列出「孤立语料」（无任何入链），并给出渠道 / kind 分布。

healthcheck ⑥ 只打印前 8 条，看不到全貌；这里复刻同判据（路径 / 文件名 / alias 三路解析）
并把结果按渠道聚合，便于判断是「结构问题」还是「本来就没有实体页」。
"""
import collections
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
name_to_paths: dict[str, list] = {}
alias_to_paths: dict[str, list] = {}
for p in notes:
    name_to_paths.setdefault(p.stem, []).append(p)
    sn = KB.split_note(p.read_text(encoding='utf-8'))
    if sn:
        for a in KB.fm_list(sn[0], 'aliases'):
            alias_to_paths.setdefault(a, []).append(p)

inbound: set = set()
for p in notes:
    txt = KB.strip_code(p.read_text(encoding='utf-8'))
    if '[[' not in txt:
        continue
    for m in LINK.finditer(txt):
        raw = m.group(1).split('|')[0].strip()
        tgt = raw.split('#')[0].strip()
        if not tgt or (JUNK & set(tgt)):
            continue
        for s, form in ((raw, 'rel'), (tgt, 'rel')):
            if s in by_rel:
                inbound.add((ROOT / (s + '.md')).resolve())
            if s.endswith('.md') and s[:-3] in by_rel:
                inbound.add((ROOT / s).resolve())
        for s in {raw.split('/')[-1], tgt.split('/')[-1]}:
            stem = s[:-3] if s.endswith('.md') else s
            for q in name_to_paths.get(stem, []):
                inbound.add(q.resolve())
            for q in alias_to_paths.get(stem, []):
                inbound.add(q.resolve())

corpus = [p for p in (ROOT / '20-语料').rglob('*.md')]
iso = [p for p in corpus if p.resolve() not in inbound]
print(f'孤立语料 {len(iso)} / {len(corpus)}')
by_ch = collections.Counter(p.relative_to(ROOT).parts[2] for p in iso)
by_shard = collections.Counter(p.relative_to(ROOT).parts[3] for p in iso)
print('  渠道:', dict(by_ch))
print('  批次:', dict(by_shard))
kinds = collections.Counter()
for p in iso:
    sn = KB.split_note(p.read_text(encoding='utf-8'))
    fm = KB.fm_scalars(sn[0]) if sn else {}
    kinds[fm.get('kind') or '?'] += 1
print('  kind:', dict(kinds))
print('  样例:')
for p in iso[:12]:
    print('   ', p.relative_to(ROOT).as_posix())
