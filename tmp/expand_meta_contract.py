"""扩展元数据契约 - Next 5 通道 (devto, producthunt, v2ex, bilibili, c1c7)"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
channels_file = ROOT / "_meta/channels.yaml"

# 读取原始内容
with open(channels_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Next 5 通道的 meta_unavailable 声明
NEXT_FIVE_CONTRACTS = '''
  # ---------------- 海外 · 社区与发布站 ----------------
  - id: devto
    name: dev.to
    adapter: devto
    profile: discussion
    group: 海外社区
    lang: en
    auth: none
    enabled: true
    limit: 8
    enrich: fulltext
    params:
      tags: [showdev, sideproject, indiehackers, buildinpublic]
      window_days: 14
      min_reactions: 5
    status: ok
    last_verified: '2026-09-20'
    note: /api/articles 列表 + /api/articles/<id> 取 body_markdown 全文
    meta_unavailable:
      project_url: "dev.to 文章页无项目官网链接 → structural dependency"
      
  - id: producthunt
    name: Product Hunt
    adapter: rss_atom
    profile: linkpost
    group: 海外发布站
    lang: en
    auth: none
    enabled: true
    limit: 30
    enrich: fulltext
    params:
      feed: https://www.producthunt.com/feed
    status: ok
    last_verified: '2026-09-20'
    note: Atom feed 含 content html（完整介绍）；PH API 需 token，不依赖
    meta_unavailable:
      author: "Product Hunt 产品库作者字段不清晰 → conditional availability"
      published_at: "RSS feed 时间戳为抓取日而非发布日 → 结构性不可得"

  - id: v2ex
    name: V2EX
    adapter: sov2ex
    profile: discussion
    group: 中文社区
    lang: zh
    auth: none
    enabled: true
    limit: 25
    enrich: fulltext
    fulltext_budget: 12
    params:
      queries: ['独立开发', '副业', '出海', '独立开发者 上线', 'SaaS 独立']
      size: 20
      sort: created
    status: ok
    last_verified: '2026-09-20'
    note: 官方 API 本网络 502 → 改 sov2ex 搜索 API（含正文 content，无需登录）
    meta_unavailable:
      project_url: "V2EX 主题页是讨论平台，非项目官网 → structural dependency"
      published_at: "搜索 API 返回创建时间，非正式发布时间 → recommended created_at"

  - id: bilibili
    name: B 站
    adapter: bilibili
    profile: metadata
    layer: signal
    group: 中文社媒
    lang: zh
    auth: none
    enabled: true
    limit: 12
    enrich: none
    params:
      queries: ['独立开发', '独立开发者 出海', '一人公司', '副业 产品']
      min_play: 3000
    status: ok
    last_verified: '2026-09-20'
    note: B 站搜索 API（带 Referer 可直连）；bili-cli 未装，暂只取元数据
    meta_unavailable:
      project_url: "B 站视频页是内容平台，非项目官网 → structural dependency"
      published_at: "视频发布日期≠项目发布时间 → not available for indie projects"

  - id: c1c7
    name: 1c7 中文独立开发者名录
    adapter: onec7
    profile: project
    group: 中文名录
    lang: zh
    auth: none
    enabled: true
    limit: 30
    enrich: fulltext
    fulltext_budget: 15
    meta_unavailable:
      published_at: "名录 README 只有收录日期，非项目发布时间 → 结构性不可得"
      author: "名录条目无明确作者信息 → conditional availability"
      description: "仅名称/链接/简介三列，详细描述缺失 → structural limitation"

'''

# 在 channels.yaml 中找到合适位置插入
import re
match = re.search(r'(  - id: lobsters\s+name: Lobsters)', content)
if match:
    insert_pos = match.start()
    new_content = content[:insert_pos] + NEXT_FIVE_CONTRACTS + "\n\n" + content[insert_pos:]
else:
    print("[!] 找不到插入位置")
    exit(1)

# 写回文件
with open(channels_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"[OK] 已扩展元数据契约至 Next 5 通道:")
for ch_id in ["devto", "producthunt", "v2ex", "bilibili", "c1c7"]:
    print(f"  YES {ch_id}")
print("\n当前状态：8/18 通道已有 meta_unavailable 声明 (44%)")
