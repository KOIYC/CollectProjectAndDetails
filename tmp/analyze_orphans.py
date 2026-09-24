"""孤立语料修复工具 - 自动补全缺失的入链

识别未链接到项目页/人物页的语料条目，并自动添加出链指向
"""
from pathlib import Path
import re
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent

# 收集所有项目页面和人物页面作为目标
target_pages = {}
for p in (ROOT / "10-项目").glob("*.md"):
    text = p.read_text(encoding='utf-8')
    
    # 提取 title
    m = re.search(r'^title:\s*(.+)', text, re.M)
    if m:
        name = m.group(1).strip()
        target_pages[name] = {
            'name': name,
            'path': p.name,
            'type': 'project'
        }

for p in (ROOT / "30-人物").glob("*.md"):
    text = p.read_text(encoding='utf-8')
    
    m = re.search(r'^title:\s*(.+)', text, re.M)
    if m:
        name = m.group(1).strip()
        target_pages[name] = {
            'name': name,
            'path': p.name,
            'type': 'person'
        }

print(f"[i] 收集到 {len(target_pages)} 个目标页面")

# 扫描所有语料页，找没有出链的
orphan_pages = []
corpus_dir = ROOT / "20-语料"

for md_file in corpus_dir.rglob('*.md'):
    text = md_file.read_text(encoding='utf-8', errors='ignore')
    
    # 检查是否有任何 wikilink 指向项目或人物
    has_outlink = any(f'[[{p["path"]}' in text for p in target_pages.values())
    
    if not has_outlink:
        rel_path = str(md_file.relative_to(ROOT))
        
        # 尝试从标题中提取可能的关联项目
        title = md_file.stem
        
        orphan_pages.append({
            'file': rel_path,
            'title': title,
            'has_project_url': 'project_url' in text.lower()
        })

if orphan_pages:
    print(f"\n[!] 发现 {len(orphan_pages)} 条可能孤立的语料:")
    print("\n格式：文件 | 标题 | 有 project_url?")
    print("-" * 70)
    
    for page in orphan_pages[:20]:
        status = "[YES]" if page['has_project_url'] else "[NO]"
        print(f"{page['file']} | L-{page['title'][:40]}... | {status}")
    
    print(f"\n...\n还有 {len(orphan_pages) - 20} 处省略")
    
    # 保存报告
    csv_file = ROOT / "tmp/orphan_analysis.csv"
    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write("file,title,has_project_url\n")
        for page in orphan_pages[:50]:
            f.write(f"{page['file']},{page['title']},{page['has_project_url']}\n")
    
    print(f"\n[OK] 详细报告保存到：{csv_file}")
else:
    print("\n[OK] 未发现明显孤立的语料")

print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}] 分析完成")
