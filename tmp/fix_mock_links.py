"""把 `统计优化方案-20260922.md` 里的**示意性** wikilink 包成行内代码。

为什么：那份文档是在演示「浏览页长什么样」，里面 `[[Project A]]` / `[[ObsidianMSA]]`
这类是**举例**，不是真链接。留着会被 healthcheck ④ 计成断链（实测 8 个目标 / 14 处），
也误导 Obsidian 里点开的人。包成 `` `[[X]]` `` 后：语义变清楚（这是语法示例），
且 `strip_code` 会把行内代码剥掉 → 检查器不再计入。
只动这一份文档，不做全库替换。
"""
import pathlib

TARGET = pathlib.Path("00-索引/报告/统计优化方案-20260922.md")
MOCK = [
    "Project A", "Project B", "Project X", "Project Alpha", "Tool Beta",
    "ObsidianMSA", "产品 Gamma", "工具 Z",
]
# 括号不配对的写法单独修（原文档里是 `[[Plugin X], [Plugin Y]]`）
FIXES = {
    "[[Plugin X], [Plugin Y]]": "`[[Plugin X]]`、`[[Plugin Y]]`",
}

text = TARGET.read_text(encoding="utf-8")
n = 0
for m in MOCK:
    old = f"[[{m}]]"
    new = f"`[[{m}]]`"
    c = text.count(old)
    text = text.replace(old, new)
    n += c
    print(f"  {old} → 包裹 {c} 处")
for old, new in FIXES.items():
    c = text.count(old)
    text = text.replace(old, new)
    n += c
    print(f"  {old} → {c} 处")

TARGET.write_text(text, encoding="utf-8")
print(f"共处理 {n} 处")
