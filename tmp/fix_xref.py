"""补充交叉引用 - 扫描实体页提及的其他项目并建立 wikilink 连接"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

# 读取所有项目页面作为参考库
project_pages = list((ROOT / "10-项目").glob("*.md"))
print(f"[i] 在 {len(project_pages)} 个项目页面中查找引用关系...")

# 提取项目名称
project_names = []
for p in project_pages:
    text = p.read_text(encoding='utf-8')
    # 提取 frontmatter title
    m = re.search(r'^title:\s*(.+)', text, re.M)
    if m:
        name = m.group(1).strip()
        project_names.append(name)

print(f"[i] 找到 {len(project_names)} 个项目名称")

# 扫描语料页，找已提及但未链接的
corpus_dir = ROOT / "20-语料"
missing_refs = []

for md_file in corpus_dir.rglob('*.md'):
    text = md_file.read_text(encoding='utf-8', errors='ignore')
    
    # 检查是否提到某个项目但未用 wikilink 链接
    for proj_name in project_names[:50]:  # 只查前 50 个避免性能问题
        if proj_name in text and f'[[{proj_name}]]' not in text:
            # 记录缺失
            rel_path = md_file.relative_to(ROOT)
            missing_refs.append({
                'file': str(rel_path),
                'mentioned': proj_name,
                'url': md_file.name
            })
            if len(missing_refs) >= 20:  # 只报告前 20 个
                break
    
    if len(missing_refs) >= 20:
        break

# 输出结果
if missing_refs:
    print(f"\n[!] 发现 {len(missing_refs)} 处可能缺少的交叉引用:")
    for ref in missing_refs[:10]:
        print(f"  - {ref['file']}: 提到 [[{ref['mentioned'}]] 但未链接")
else:
    print("\n[OK] 未发现明显缺少交叉引用的情况")
