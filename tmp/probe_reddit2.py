"""临时探针 2：给定窗口内 score>=3 的帖子有多少（决定 reddit 的 settle_days / window_days）。

arctic-shift 的 `score` 近几天明显没沉淀（最新帖全 ≤2），所以要找出「多老才带分」。
limit 拉到 100（API 上限）避开「只回最新 N 条」的偏差。
"""
import datetime
import json
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
BASE = "https://arctic-shift.photon-reddit.com/api/posts/search?"
SUBS = ("SideProject", "indiehackers", "microsaas", "SaaS",
        "EntrepreneurRideAlong", "buildinpublic", "selfhosted", "indiedev")
now = datetime.datetime.now(datetime.timezone.utc)


def window(after_days, before_days, sub, limit=100):
    a = int((now - datetime.timedelta(days=after_days)).timestamp())
    b = int((now - datetime.timedelta(days=before_days)).timestamp())
    u = (BASE + f"subreddit={urllib.parse.quote(sub)}&limit={limit}&sort=desc"
         f"&after={a}&before={b}")
    req = urllib.request.Request(u, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode("utf-8")).get("data") or []


for a, b in ((13, 3), (17, 10), (24, 17), (14, 0)):
    tot = keep = 0
    mx = 0
    for s in SUBS:
        try:
            rows = window(a, b, s)
        except Exception as e:                                  # noqa: BLE001
            print(f"    {s}: ERR {str(e)[:40]}")
            continue
        tot += len(rows)
        keep += sum(1 for x in rows if (x.get("score") or 0) >= 3)
        mx = max([mx] + [x.get("score") or 0 for x in rows])
    print(f"窗口 {b}~{a} 天前：取回 {tot} 条，其中 score>=3 = {keep} 条，max_score={mx}")
