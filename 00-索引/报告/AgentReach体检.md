---
type: "report"
title: "agent-reach 体检"
updated: "2026-09-21T01:04:53+08:00"
tags:
  - 报告
  - 渠道
  - agent-reach
---

# agent-reach 体检

> 检查时间 2026-09-21T01:04:53+08:00 · 由 `agent-reach doctor --json` 生成

| 平台 | | 状态 | 激活后端 | 说明 |
|---|---|---|---|---|
| GitHub 仓库和代码 | ⚠️ | warn | `—` | gh CLI 可执行，且检测到显式认证配置；Doctor 不执行会写 device-id 的 `gh auth status`，因此未实时验证，未标记为可用。 |
| Twitter/X 推文 | ⚠️ | warn | `—` | OpenCLI 桥接已连接，但 Twitter/X 登录态和实际命令未实时验证；Doctor 不执行平台命令，因此当前不标记为可用。 |
| YouTube 视频和字幕 | ❌ | off | `—` | yt-dlp 未安装。安装：python -m pip install -U "yt-dlp[default]" |
| Reddit 帖子和评论 | ⚠️ | warn | `—` | OpenCLI 桥接已连接，但 Reddit 登录态和实际命令未实时验证；Doctor 不执行平台命令，因此当前不标记为可用。 |
| Facebook 帖子、主页和群组 | ⚠️ | warn | `—` | OpenCLI 桥接已连接，但 Facebook 帖子、主页和群组 的登录态和实际命令未实时验证；Doctor 不执行平台命令，因此当前不标记为可用。需要时请先在 Chrome 里登录 facebook.com |
| Instagram 用户、主页和指定用户帖子 | ⚠️ | warn | `—` | OpenCLI 桥接已连接，但 Instagram 用户、主页和指定用户帖子 的登录态和实际命令未实时验证；Doctor 不执行平台命令，因此当前不标记为可用。需要时请先在 Chrome 里登录 instagram.com |
| B站视频、字幕和搜索 | ✅ | ok | `B站搜索 API` | B站搜索 API 可达（仅搜索，curl 直连）。完整功能建议安装 bili-cli：pipx install bilibili-cli |
| 小红书笔记 | ⚠️ | warn | `—` | OpenCLI 桥接已连接，但小红书登录态和实际命令未实时验证；Doctor 不执行平台命令，因此当前不标记为可用。 |
| LinkedIn 职业社交 | ⚠️ | warn | `—` | mcporter 本地配置未发现 LinkedIn MCP；配置还启用了 editor imports，Doctor 为避免扩大凭据读取范围没有展开，当前未验证。 |
| 小宇宙播客转文字 | ❌ | off | `—` | 需要 ffmpeg（音频转码和切片）。安装：
  Ubuntu/Debian: apt install -y ffmpeg
  macOS: brew install ffmpeg |
| V2EX 节点、主题与回复 | ⚠️ | warn | `—` | V2EX API 连接失败（可能需要代理）：<urlopen error timed out> |
| 雪球股票行情与社区动态 | ⚠️ | warn | `—` | Xueqiu API 连接失败：HTTP Error 400。如需登录 Cookie，请运行：agent-reach configure --from-browser chrome --platform xueqiu；doctor 不会自动 |
| RSS/Atom 订阅源 | ✅ | ok | `feedparser` | 可读取 RSS/Atom 源 |
| 全网语义搜索 | ⚠️ | warn | `—` | Exa 已写入 mcporter 配置，但 Doctor 未启动远端服务做连通验证，不能仅凭配置宣称可用。 |
| 任意网页 | ✅ | ok | `Jina Reader` | 通过 Jina Reader 读取任意网页（curl https://r.jina.ai/URL） |

## 与 KB 渠道的对应关系

| KB 渠道 | 依赖的 agent-reach 平台 | 说明 |
|---|---|---|
| `hn_show` / `reddit` / `lobsters` / `devto` / `producthunt` | 无（直连 API/RSS） | 零配置，不依赖 agent-reach 后端 |
| `github_new` | github (gh CLI) | doctor 只查配置不实测，以 kb_audit 探针为准 |
| `v2ex` | web (Jina) / 直连 sov2ex | 官方 API 本网络 502，已改 sov2ex |
| `exa_discovery` | exa_search (mcporter) | doctor 不连通验证，以探针为准 |
| `xiaohongshu` | xiaohongshu（OpenCLI / xhs-mcp） | 需浏览器登录态 |
| `twitter` | twitter（OpenCLI / twitter-cli） | 需扩展或 Cookie |
| `bilibili` | bilibili | 直连搜索 API 可用（带 Referer），无需登录 |
