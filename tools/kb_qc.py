"""[遗留] 早期一次性质控探针，已被 kb_analyze / kb_content_audit / kb_healthcheck 取代。
保留仅为历史参考；不要在流程中调用，也不要按它的口径做判断。
清理需用户确认（本库无 git，删除不可恢复）。
"""
import json, glob, collections, pathlib

rows = []
for f in glob.glob('90-原始/*/*.jsonl'):
    for ln in open(f, encoding='utf-8'):
        ln = ln.strip()
        if not ln:
            continue
        try:
            rows.append(json.loads(ln))
        except Exception:
            pass

# 同一 item 跨运行会有 new + 多条 update，按 item_id 取最新一条作为“语料现状”
latest = {}
for r in rows:
    latest[r['item_id']] = r
rows = list(latest.values())

n = len(rows)
withbody = sum(1 for r in rows if (r.get('body') or '').strip())
wcomments = sum(1 for r in rows if r.get('comments'))
ncomments = sum(len(r.get('comments') or []) for r in rows)
nourl = sum(1 for r in rows if not (r.get('url') or '').strip())
trunc = sum(1 for r in rows if r.get('comments_truncated'))
bych = collections.Counter(r['source_id'] for r in rows)
top = bych.most_common(1)[0] if bych else ('-', 0)
avg_body = sum(len(r.get('body') or '') for r in rows) / max(1, n)

print(f"总条数              {n}")
print(f"有正文              {withbody} ({100*withbody/max(1,n):.0f}%)  均长 {avg_body:.0f} 字符")
print(f"有评论的条目        {wcomments}（评论总条数 {ncomments}，截断标注 {trunc}）")
print(f"缺 url（应=0）      {nourl}")
print(f"单渠道最大占比      {top[0]} {top[1]} ({100*top[1]/max(1,n):.0f}%)")
print("按渠道:", bych.most_common())
print()
print("--- 抽样 3 条（校验正文/评论/来源） ---")
for r in [x for x in rows if x.get('comments')][:2] + [x for x in rows if not x.get('comments')][:1]:
    print(f"[{r['source_id']}] {r['title'][:60]}")
    print(f"   url={r['url'][:90]}")
    print(f"   body={len(r.get('body') or '')}字符 comments={len(r.get('comments') or [])} metrics={r.get('metrics')}")
    print(f"   body 摘要: {(r.get('body') or '')[:110]!r}")
print()
print("--- 目录落盘 ---")
for d in ['90-原始', '20-语料/posts', '10-项目', '50-渠道']:
    p = pathlib.Path(d)
    files = list(p.rglob('*'))
    sz = sum(f.stat().st_size for f in files if f.is_file())
    print(f"{d:14s} {len([f for f in files if f.is_file()])} 个文件 {sz/1024/1024:.1f} MB")
