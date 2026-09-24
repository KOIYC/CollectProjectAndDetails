"""临时探针：arctic-shift 在几个窗口下各返回多少帖（判断 reddit empty 是渠道挂了还是窗口问题）。"""
import datetime
import json
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
BASE = "https://arctic-shift.photon-reddit.com/api/posts/search?"
now = datetime.datetime.now(datetime.timezone.utc)


def probe(sub, after_days, before_days, min_score=0, limit=25):
    a = int((now - datetime.timedelta(days=after_days)).timestamp())
    b = int((now - datetime.timedelta(days=before_days)).timestamp())
    u = (BASE + f"subreddit={urllib.parse.quote(sub)}&limit={limit}&sort=desc"
         f"&after={a}&before={b}")
    try:
        req = urllib.request.Request(u, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        print(f"  {sub:18s} {after_days}~{before_days}d  ERR {str(e)[:60]}")
        return
    rows = data.get("data") or []
    scores = sorted((x.get("score") or 0 for x in rows), reverse=True)
    keep = [s for s in scores if s >= min_score]
    print(f"  {sub:18s} {after_days}~{before_days}d  返回 {len(rows)} 条 "
          f"| score>=3 的 {len(keep)} 条 | max_score={scores[0] if scores else '-'}")
    for x in rows[:2]:
        print(f"       · [{x.get('score')}] {str(x.get('title'))[:70]}")


print(f"now(UTC)={now.isoformat()}")
for sub in ("SaaS", "SideProject", "indiehackers"):
    for a, b in ((3, 0), (10, 3), (30, 10), (90, 0)):
        probe(sub, a, b)
