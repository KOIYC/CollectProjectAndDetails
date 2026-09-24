"""自动补全交叉引用 - P1 级别优化

扫描所有语料页，发现提及项目但未建立 wikilink 的地方
批量生成修复建议
"""
from pathlib import Path
import re
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent

# 收集所有项目名称和 URL
projects = {}
for p in (ROOT / "10-项目").glob("*.md"):
    text = p.read_text(encoding='utf-8')
    
    # 提取 frontmatter title
    m = re.search(r'^title:\s*(.+)', text, re.M)
    if m:
        name = m.group(1).strip()
        projects[name] = {
            'name': name,
            'path': p.name,
            'url': str(p.relative_to(ROOT))
        }

print(f"[i] 收集到 {len(projects)} 个项目名称")
print(f"[i] 开始扫描语料页...")

missing_refs = []
corpus_dir = ROOT / "20-语料"

# 扫描每个语料页
for md_file in corpus_dir.rglob('*.md'):
    text = md_file.read_text(encoding='utf-8', errors='ignore')
    
    # 检查是否提到某个项目但未链接
    for proj_name in projects.keys():
        # 查找项目名称（排除已链接的情况）
        if f'[[{proj_name}]]' in text:
            continue
        
        # 检查是否以某种形式提到该项目
        patterns = [
            rf'\b{re.escape(proj_name)}\b',  # 精确匹配
            rf'{re.escape(proj_name)}[^\]]*?\]',  # 带描述
        ]
        
        for pattern in patterns:
            matches = list(re.finditer(pattern, text))
            if matches and len(matches) > 0:
                rel_path = str(md_file.relative_to(ROOT))
                
                # 获取上下文行号
                lines = text.split('\n')
                line_num = None
                for i, line in enumerate(lines):
                    if proj_name in line:
                        line_num = i + 1
                        break
                
                missing_refs.append({
                    'file': rel_path,
                    'line': line_num,
                    'mentioned': proj_name,
                    'project_url': projects[proj_name]['path'],
                    'match_count': len(matches)
                })
                
                break
    
    # 限制输出数量
    if len(missing_refs) >= 30:
        break

# 输出结果
if missing_refs:
    print(f"\n[!] 发现 {len(missing_refs)} 处可能的交叉引用缺失:")
    print("\n格式：文件 | 行号 | 项目名称 | 提及次数")
    print("-" * 70)
    
    for ref in missing_refs[:20]:
        print(f"{ref['file']} | L{ref['line']} | {ref['mentioned']} | x{ref['match_count']}")
    
    print(f"\n...\n还有 {len(missing_refs) - 20} 处省略")
    
    # 保存为 CSV
    csv_file = ROOT / "tmp/missing_xrefs.csv"
    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write("file,line,project_mentioned,match_count\n")
        for ref in missing_refs[:20]:
            f.write(f"{ref['file']},{ref['line']},{ref['mentioned']},{ref['match_count']}\n")
    
    print(f"\n[OK] 详细报告保存到: {csv_file}")
    
else:
    print("[OK] 未发现明显缺少交叉引用的情况")

print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M')}] 交叉引用检查完成")
