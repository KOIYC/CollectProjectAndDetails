"""精简数据库视图 — Phase 1 任务 2

只展 6 列核心字段，默认按赛道分组，新增"需要人工复核"视图
"""
from pathlib import Path

browse_md_path = Path(__file__).resolve().parent.parent / "00-索引" / "浏览.md"
if not browse_md_path.exists():
    print(f"[!] {browse_md_path.name} not found")
    exit(1)

content = browse_md_path.read_text(encoding='utf-8')

# Find and replace the Bases view section with simplified columns
old_view_start = content.find("```base\nfilters:\n  and:")
if old_view_start < 0:
    print("[!] Could not find base view section")
    exit(1)

# Build new simplified view config
new_views = """```base
filters:
  and:
    - file.hasProperty("type")
views:
  - type: table
    name: 语料·精简版
    filters:
      and:
        - 'type == "corpus"'
    columns:           # 只展这 6 列，其余折叠
      - title
      - topic
      - source_name
      - published_at  
      - comments_count
      - quality_flag    # 新增：质量标记
    groupBy:
      property: topic   # 默认按赛道分组
    order:
      - title
      - source_name
      - kind
      - pub_day
      - comments_count
      - url
    limit: 400
    
  - type: table
    name: 需要人工复核 (低质/异常)
    filters:
      and:
        - 'type == "corpus"'
        - or:
          - 'body.length() < 200'       # 正文不完整
          - 'comments_count > 100'      # 超常热度（可能误判）
          - 'published_at == null'      # 缺发布时间
          - 'project_url == null'       # 缺归并键
    order:
      - quality_flag DESC
      - comments_count DESC
    limit: 100
  
  - type: table
    name: 语料·按赛道 (完整版)
    filters:
      and:
        - 'type == "corpus"'
    groupBy:
      property: topic
      direction: ASC
    order:
      - title
      - source_name
      - kind
      - pub_day
      - comments_count
      - url
    limit: 400
  
  - type: table  
    name: 语料·按渠道 (完整版)
    filters:
      and:
        - 'type == "corpus"'
    groupBy:
      property: source
      direction: ASC
    order:
      - title
      - topic
      - kind
      - pub_day
      - comments_count
      - url
    limit: 400
      
  - type: table
    name: 语料·按发布日 (最新发布)
    filters:
      and:
        - 'type == "corpus"'
    groupBy:
      property: pub_day
      direction: DESC
    order:
      - title
      - topic
      - source_name
      - kind
      - pub_day
      - comments_count
      - url
    limit: 400

  - type: table
    name: 项目池 (只有“是项目”的条目)
    filters:
      and:
        - 'type == "corpus"'
        - is_project_ish(body) == true
    order:
      - topic DESC
      - comments_count DESC
    limit: 500
    
  - type: table
    name: 历史实体 (已归档的)
    filters:
      and:
        - 'extra.stale == true'
    order:
      - archived_at DESC
    limit: 200
    
  - type: table
    name: 人物 (maker 维度)
    filters:
      and:
        - 'kind == "person"'
    order:
      - name
    limit: 100
    
  - type: table
    name: 渠道健康度
    filters:
      and:
        - 'type == "channel"'
    order:
      - status DESC
      - last_verified DESC
    limit: 30
```
"""

# Insert new views before the closing of old content
new_content = content[:old_view_start] + new_views + "\n```\n" + content[old_view_start+7:]

browse_md_path.write_text(new_content, encoding='utf-8')
print(f"[OK] Updated {browse_md_path.relative_to(Path(__file__).resolve().parent.parent)}")
print(f"    Added 9 views: 精简版 + 人工复核 + 8 个原版本")
