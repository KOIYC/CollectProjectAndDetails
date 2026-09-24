"""孤立语料修复工具 - 自动补全缺失的入链 (P2 级优化)

用法:
  python tools/kb_fix_orphans.py --scan          # 扫描孤立条目
  python tools/kb_fix_orphans.py --suggest-links # 根据内容建议关联项目
  python tools/kb_fix_orphans.py --apply-auto    # 自动补充出链（保守模式）
  python tools/kb_fix_orphans.py --dry-run       # 只预览不修改
"""
from __future__ import annotations

import argparse
import collections
import csv
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parent.parent

def scan_orphans():
    """扫描没有入链的语料页"""
    orphan_files = []
    corpus_dir = ROOT / "20-语料"
    
    target_paths = set()
    for p in (ROOT / "10-项目").rglob("*.md"):
        target_paths.add(p.name)
    for p in (ROOT / "30-人物").rglob("*.md"):
        target_paths.add(p.name)
    
    for md_file in corpus_dir.rglob('*.md'):
        text = md_file.read_text(encoding='utf-8', errors='ignore')
        
        # 检查是否有 wikilink 指向任何目标页面
        has_outlink = any(f'[[{p}' in text for p in target_paths)
        
        if not has_outlink:
            orphan_files.append(str(md_file.relative_to(ROOT)))
    
    return orphan_files


def suggest_links(file_path: str) -> list[str]:
    """根据内容建议关联的项目"""
    suggestions = []
    md_file = ROOT / file_path
    
    try:
        text = md_file.read_text(encoding='utf-8', errors='ignore')
        
        # 提取可能的项目名称（简单示例）
        # TODO: 实现更智能的内容理解
        
        return suggestions
    except Exception:
        return []


def apply_auto_corrections(orphan_files: list[str], dry_run=True):
    """自动补充出链（保守模式）"""
    corrected = 0
    
    for file_path in orphan_files:
        md_file = ROOT / file_path
        
        try:
            text = md_file.read_text(encoding='utf-8')
            lines = text.splitlines()
            
            # 找到导航段位置（通常在底部）
            nav_section_idx = -1
            for i, line in enumerate(lines):
                if '## 导航' in line or '# 导航' in line:
                    nav_section_idx = i
                    break
            
            if nav_section_idx >= 0:
                # 在导航段添加出链
                # TODO: 根据内容判断应该链接到哪个项目
                
                if not dry_run:
                    md_file.write_text('\n'.join(lines), encoding='utf-8')
                    corrected += 1
                    
        except Exception as e:
            print(f"  [ERR] {file_path}: {str(e)[:50]}")
    
    return corrected


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true", help="扫描孤立条目")
    ap.add_argument("--suggest-links", type=str, help="指定文件路径，建议关联项目")
    ap.add_argument("--apply-auto", action="store_true", help="自动补充出链")
    ap.add_argument("--dry-run", action="store_true", help="只预览不修改")
    args = ap.parse_args(argv)
    
    if args.scan:
        orphans = scan_orphans()
        print(f"[INFO] 发现 {len(orphans)} 条可能的孤立语料")
        for o in orphans[:10]:
            print(f"  - {o}")
        if len(orphans) > 10:
            print(f"  ... 还有 {len(orphans) - 10} 条省略")
        return 0
    
    if args.suggest_links:
        links = suggest_links(args.suggest_links)
        print(f"[INFO] 建议关联 {len(links)} 个项目:")
        for l in links:
            print(f"  - {l}")
        return 0
    
    if args.apply_auto:
        orphans = scan_orphans()
        corrected = apply_auto_corrections(orphans, dry_run=args.dry_run)
        print(f"[OK] {'(预览模式)' if args.dry_run else ''} 处理 {corrected} 条")
        return 0
    
    # 默认扫描
    scan_orphans()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
