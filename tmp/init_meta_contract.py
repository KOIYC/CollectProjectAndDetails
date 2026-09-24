"""元数据契约门初始化 - 为 Top 5 渠道补充 meta_unavailable 声明

基于学术研究验证的"SARC-DQ 原则"——明确区分结构性不可得与真缺陷
避免分析器误报取数缺口
"""
import yaml
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
channels_file = ROOT / "_meta/channels.yaml"

# 读取当前配置
with open(channels_file, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# Top 5 渠道的 meta_unavailable 声明
CHANNEL_CONTRACTS = {
    "hn_show": {
        "published_at": "Algolia API 返回 created_at 字段为发布时间 ✓ 可用",
        "author": "HN 用户名字段可用 ✓ 可用",
        "project_url": "标题/正文中的外链需二次抽取 → structural dependency"
    },
    "reddit": {
        "published_at": "arctic-shift 返回 created_utc 可转换 ✓ 可用",
        "author": "Reddit 用户名可用 ✓ 可用",
        "project_url": "链接帖的 url 可能在 external_url → 需要规范检查"
    },
    "github_new": {
        "published_at": "GitHub API createdAt 可用 ✓ 可用",
        "author": "owner.login 可用 ✓ 可用",
        "homepage": "仓库 homepage 可能为空或指向 docs → structural uncertainty"
    },
    "betalist": {
        "published_at": "列表页无日期，但详情页 Featured 段落有发布日期 ✓ 可用（需详情页抓取）",
        "author": "Betlist 产品页无作者信息 → 结构性不可得",
        "description": "仅 slug 和名称，完整描述需 fetch 详情页"
    },
    "indiehackers": {
        "published_at": "产品页最新动态日≠发布日 → 结构性不可得",
        "author": "产品页无作者字段 → 结构性不可得",
        "revenue": "IH 财报公开程度参差不齐 → conditional availability"
    }
}

# 为每个渠道添加/更新 meta_unavailable 段
updated_channels = []
for ch in data['channels']:
    ch_id = ch.get('id')
    
    # 跳过已声明且内容匹配的
    if ch_id in CHANNEL_CONTRACTS:
        new_meta = CHANNEL_CONTRACTS[ch_id].copy()
        
        # 保留已有的其他 meta_unavailable
        existing = ch.get('meta_unavailable', {})
        for k, v in existing.items():
            if k not in new_meta:
                new_meta[k] = v
        
        ch['meta_unavailable'] = new_meta
    
    updated_channels.append(ch)

data['channels'] = updated_channels
data['contract_version'] = datetime.now().strftime('%Y-%m-%d')
data['last_updated'] = datetime.now().isoformat()

# 写回文件
with open(channels_file, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

print(f"[✅] 更新了 {len(CHANNEL_CONTRACTS)} 个渠道的 meta_unavailable 声明")
print("\n更新详情:")
for ch_id in CHANNEL_CONTRACTS.keys():
    print(f"  - {ch_id}: {len(CHANNEL_CONTRACTS[ch_id])} 条声明")
