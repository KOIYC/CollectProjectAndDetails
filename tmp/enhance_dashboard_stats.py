"""Enhance dashboard stats — Phase 1 quick fix.

Adds: 今日变化、赛道分布饼图数据、质量漏斗到洞察报告
"""
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
META = ROOT / "_meta"

# Read latest insight report
insight_file = META / "insight_latest.json"
if not insight_file.exists():
    print(f"[!] {insight_file.name} not found, skipping enhancement")
    exit(0)

data = json.load(open(insight_file, 'r', encoding='utf-8'))

# Add today's changes (placeholder - need comparison with previous run)
data["today"] = {
    "new": 0,          # TODO: compare with previous seen.json
    "updated": 0,      # TODO: compare with previous seen.json  
    "archived": 0,     # TODO: from prune manifest
}

# Add body quality funnel
data["body_quality_funnel"] = {
    "full": data.get("body_median", 0) > 160,  # Simplified for now
    "summary": 0,   # Need to count items with truncated flag
    "snippet": 0,   # Need to count short bodies
    "empty": 0,     # Need to count empty bodies
}

# Add missing fields count
data["quality_issues"] = {
    "missing_project_url": data.get("missing_project_url", 0),
    "missing_published_at": data.get("missing_published_at", 0),
    "low_body": data.get("low_quality_count", 0),
}

# Write back
insight_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')

print(f"[OK] Enhanced {insight_file.name}")
print(f"    Today: new={data['today']['new']}, updated={data['today']['updated']}")
print(f"    Quality issues: {sum(data['quality_issues'].values())} total")
