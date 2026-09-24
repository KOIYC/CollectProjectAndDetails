"""元数据契约门初始化 - 手动更新 channels.yaml (无第三方依赖)"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
channels_file = ROOT / "_meta/channels.yaml"

# 读取原始内容
with open(channels_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 要插入的内容（在 v2ex 之前添加 3 个新渠道声明）
NEW_CONTRACTS = '''  # ---------------- 海外 · 发布与社区（核心） ----------------
  - id: hn_show
    name: HN Show HN
    adapter: hn_show
    profile: discussion
    group: 海外发布
    lang: en
    auth: none
    enabled: true
    limit: 40
    enrich: comments
    enrich_extra: fulltext
    fulltext_budget: 60
    params:
      tags: show_hn
      min_points: 2
    status: ok
    last_verified: '2026-09-20'
    note: algolia API 列表 + /items/<id> 取全量评论树（全量，mega 帖截断 800 条并标 truncated）
    meta_unavailable:
      project_url: "标题/正文中的外链需二次抽取 → structural dependency"
    
  - id: reddit
    name: Reddit 独立开发版块
    adapter: reddit_arctic
    profile: discussion
    group: 海外社区
    lang: en
    auth: none
    enabled: true
    limit: 30
    enrich: comments
    enrich_extra: fulltext
    fulltext_budget: 80
    params:
      subs: [SideProject, indiehackers, microsaas, SaaS, EntrepreneurRideAlong, buildinpublic, selfhosted, indiedev]
      window_days: 7
      settle_days: 3
      min_score: 3
      sort: desc
    status: ok
    last_verified: '2026-09-20'
    note: arctic-shift 镜像（匿名可用）。① 本网络 www.reddit.com 直连 502；② after 只吃 epoch 秒/纯日期，带时区 ISO 会 400；③ **score 有装载延迟**——近 3 天帖子分数未沉淀（实测近 3 天 max=1、7-14 天前 max=42），故用 settle_days=3 取「3~10 天前」窗口
    meta_unavailable:
      project_url: "链接帖的 url 可能在 external_url → 需要规范检查"
    
  - id: github_new
    name: GitHub 新星仓库
    adapter: github_new
    profile: project
    group: 海外发布
    lang: en
    auth: cli
    enabled: true
    limit: 30
    enrich: readme
    fulltext_budget: 30
    params:
      window_days: 14
      min_stars: 20
      queries:
        - 'created:>{since} stars:>={min_stars}'
        - 'topic:indie-hacker'
        - 'topic:side-project'
        - 'topic:microsaas'
    status: ok
    last_verified: '2026-09-20'
    note: gh CLI（api.github.com 可达）；README 用 gh api .../readme 取全文
    meta_unavailable:
      homepage: "仓库 homepage 可能为空或指向 docs → structural uncertainty"
    
  - id: betalist
    name: BetaList
    adapter: betalist
    profile: linkpost
    group: 海外发布站
    lang: en
    auth: none
    enabled: true
    limit: 12
    enrich: fulltext
    fulltext_budget: 12
    params: {}
    status: ok
    last_verified: '2026-09-21'
    note: >-
      列表页只有 slug（无日期、无简介）；发布日改从**详情页**抽取，锚点 = `Featured\\n<Month D, YYYY>`
      （2026-09-21 实测样本稳定）。抽不到留空，不用其它日期凑数。存量 56 条走
      `tools/kb_backfill.py --fix-meta` 回填。
    meta_unavailable:
      author: "Betlist 产品页无作者信息 → 结构性不可得"
      description: "仅 slug 和名称，完整描述需 fetch 详情页"
      
  - id: indiehackers
    name: Indie Hackers 产品库
    adapter: ih_products
    profile: linkpost
    group: 海外发布站
    lang: en
    auth: none
    enabled: true
    limit: 20
    enrich: fulltext
    fulltext_budget: 20
    meta_unavailable:
      published_at: "产品页最新动态日≠发布日 → 结构性不可得"
      author: "产品页无作者字段 → 结构性不可得"
      revenue: "IH 财报公开程度参差不齐 → conditional availability"
    params:
      pages: 3
    status: ok
    last_verified: '2026-09-20'
    note: /products 列表页 HTML 解析 /product/ 链接；详情补充走 Jina。旧 Algolia key 已 403


'''

# 找到插入位置（在 "# ---------------- 海外 · 发布与社区（核心） ----------------" 行）
insert_index = None
for i, line in enumerate(lines):
    if "# ---------------- 海外 · 发布与社区（核心） ----------------" in line:
        insert_index = i
        break

if insert_index is None:
    print("[!] 找不到插入位置")
    exit(1)

# 写入修改后的内容
new_lines = lines[:insert_index] + [NEW_CONTRACTS + "\n"] + lines[insert_index:]

with open(channels_file, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("[OK] 为 Top 5 渠道添加了元数据契约声明")
print("更新通道：hn_show, reddit, github_new, betalist, indiehackers")
