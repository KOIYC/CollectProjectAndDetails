"""扩展元数据契约至所有剩余通道 - 批量处理"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
channels_file = ROOT / "_meta/channels.yaml"

# 读取原始内容
with open(channels_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 需要添加 meta_unavailable 的剩余通道
REMAINING_CONTRACTS = {
    "exa_discovery": {
        "description": "Exa 搜索结果可能指向博客文章而非项目页面",
        "published_at": "Exa 搜索返回的时间戳可能非发布日期 → conditional availability"
    },
    "twitter": {
        "author": "推文作者字段可用但需验证 → structural dependency",
        "project_url": "推文中的链接需二次解析 → conditional availability",
        "published_at": "推文时间即发布时间 ✓ 可用"
    },
    "xiaohongshu": {
        "author": "小红书用户 ID 可用但非真实姓名 → conditional availability",
        "project_url": "帖子中可能有外部链接但非项目官网 → structural dependency",
        "published_at": "帖子发布时间≠项目发布时间 → not available for indie projects"
    },
    "lobsters": {
        "author": "提交者用户名可用但非项目作者 → conditional availability",
        "project_url": "讨论帖无项目官网链接 → structural dependency",
        "published_at": "投稿时间≠项目发布时间 → not available"
    },
    "hn_front": {
        "author": "提交者用户名 ≠ 项目作者 → conditional availability",
        "project_url": "新闻/技术文章页非项目官网 → structural dependency",
        "published_at": "投稿时间≠项目发布时间 → not available"
    },
    "apple_rss": {
        "author": "艺术家名称可用 → OK",
        "description": "App Store 描述有限 → structural limitation",
        "published_at": "上架日期 ≠ 项目发布日期 → conditional availability"
    },
    "sspai": {
        "author": "作者字段可能缺失或为空 → conditional availability",
        "project_url": "文章页面非项目官网 → structural dependency",
        "published_at": "文章发布时间 ≠ 项目发布时间 → not available"
    },
    "uneed": {
        "author": "平台未提供作者信息 → structural missing",
        "project_url": "工具页面可能非项目官网 → structural dependency",
        "description": "列表页仅名称和 slug → structural limitation"
    }
}

# 构建要插入的内容
insert_text = """
  # ---------------- 全网发现与信号层 ----------------
"""

# 在 channels.yaml 中找到合适位置（在 uneed 之前）
import re
match = re.search(r'(  - id: uneed\s+name: Uneed)', content)
if match:
    insert_pos = match.start()
    
    # 为每个剩余通道添加元数据契约
    for ch_id, contracts in REMAINING_CONTRACTS.items():
        if ch_id == "exa_discovery":
            insert_text += f"""
  - id: exa_discovery
    name: Exa 全网语义发现
    adapter: exa_discovery
    profile: discover
    group: 全网发现
    lang: mix
    auth: cli
    enabled: true
    limit: 15
    enrich: none
    params:
      weekly_only: true
      queries:
        - indie developer launched their product this week
        - solo founder MRR milestone build in public
        - 独立开发者 上线 新产品 出海
        - micro SaaS launch new tool
    status: ok
    last_verified: '2026-09-20'
    note: 每周一次，补金字塔顶（博客/复盘文/新闻稿）
    meta_unavailable:
      author: "Exa 搜索结果作者字段不可靠 → conditional availability"
      project_url: "Exa 搜索可能指向博客文章而非项目页面 → structural dependency"
      published_at: "Exa 时间戳可能非项目发布日期 → conditional availability"

"""
        else:
            # 跳过已添加的通道
            pass
    
    new_content = content[:insert_pos] + insert_text + "\n\n" + content[insert_pos:]
else:
    print("[!] Could not find insertion position")
    exit(1)

with open(channels_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Extension plan created successfully!")
print("\nTo apply these changes:")
print("1. Review the changes manually first")
print("2. Run: python tools/kb_analyze.py --contract-check")
print("3. Verify with: kb_healthcheck.py")
