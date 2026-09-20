# AGENTS.md — 任何 AI Agent 进入本库的统一说明

> **本页是唯一入口**：项目是什么、数据在哪、规范是什么、命令怎么跑、什么不许做 —— 全在这一页。
> 目标：**读完这一页就能正确操作本库**，不需要先跑脚本、翻目录、或自己重新推断结构。
> 维护：本库自动化与助手。最后核对：2026-09-20。
> 配套深读：`Home.md`（给人看的全景）· `00-索引/命名与目录规范.md`（命名与目录唯一规范）·
> `00-索引/字段字典.md`（字段定义）。

---

## 0. 30 秒速览（先记红线，再干活）

**项目**：独立开发项目知识库（Indie Project KB）—— 每天自动采集全网独立开发项目语料，
落成本地 Markdown 证据库，供 AI 做痛点/定价/增长/方法论分析。**证据库，不是结论库。**

**六条红线（违反会当场被不变量抓住）**：

1. ❌ **不手改生成页**：`浏览.md`、`项目地图`、`归档与申诉`、`报告总览`、`10-项目/`、`20-语料/`、`50-渠道/` 全由脚本再生成，手改会被覆盖。
2. ❌ **不手改文件名**：改名只有 `kb_navfix.py --fix-names` 一条路（manifest + seen 同步 + 链接改写，手改必漏三件套）。
3. ❌ **不手改 `_meta/`**（seen.json / channels.yaml / manifest…），由脚本读写。
4. ❌ **不 `pip install`**：工具链零第三方依赖（本机 PyPI 不可达），只用 stdlib。
5. ❌ **不改 `90-原始/`**：唯一事实源，只追加、不可变；口径变化只加新字段。
6. ❌ **收工不过 `kb_healthcheck.py` = 没收工**：八项不变量全绿才算完（①-⑤硬门 + ⑥⑦⑧软门须逐条说明），数字对不上是改动错了。

---

## 1. 数据分层与事实源（medallion 式）

| 层 | 位置 | 事实源地位 | 怎么读 |
|---|---|---|---|
| **bronze · 原始归档** | `90-原始/<渠道>/<日期>.jsonl` | **唯一事实源，只追加、不可变** | AI 批量读这里；字段见 `_meta/schema.json` |
| **silver · 语料** | `20-语料/posts/<渠道>/<日期>/*.md` | 清洗后可读语料；每页底部有「导航」段 | 按渠道/日期分片 |
| **gold · 实体页** | `10-项目/`、`30-人物/` | 汇总页 + **观测历史表** | 追项目随时间变化看这里 |
| **导航层** | `00-索引/*.md` | **不是事实**，是指路牌 | 任何会话从这里开始 |
| **生成物** | `00-索引/报告/*.md` | 可随时重建 | 引用数字必须带口径与分母 |
| **归档** | `80-归档/posts/`、`80-归档/项目/` | 移出检索面，**不是删除，可撤销** | 捞回入口：`00-索引/归档与申诉.md` |
| **状态与账本** | `_meta/` | seen/channels/manifest（轮转保留：manifest 12 份 / run 记录 80 份，更早在 git 历史） | 脚本读写，勿手改 |
| **版本控制** | `.git` → GitHub `KOIYC/CollectProjectAndDetails`（main） | 工具/结构改动后 commit；`.gitignore` 排除 pycache/.workbuddy/workspace | 删除有了第二份保险，但**红线照旧**：不手改生成页、不手改文件名 |
| **工具** | `tools/kb_*.py` | 采集/体检/诊断/回填/订正/归档/洞察/地图/审计 | 12 个工具，职责见下表 |

**目录框架速记**（完整规范见 `00-索引/命名与目录规范.md`）：
`00-索引`（导航）`10-项目` `20-语料` `30-人物` `40-方法论`（唯一人工创作区）`50-渠道`
`60/70`（保留位，启用前先改规范页）`80-归档`（冻结区）`90-原始`（bronze）+ `_meta` + `tools`；
根目录只放 `Home.md` 与本页。**MOC/地图只放 `00-索引/`** —— 数据目录被计数脚本按 `*.md` glob，
塞 index 页会污染计数（647 变 648）。

## 2. 工具链（12 个 runbook 工具，顺序不能乱；另有 `kb_selftest.py` 自测 / `kb_render.py` 批量重渲染；渠道层已拆为 `kbc_channels.py`——15 个 adapter + enricher，kb_collect facade re-export）

| 工具 | 何时跑 | 干什么 |
|---|---|---|
| `kb_audit.py` | 采集前 | 渠道探活 + agent-reach doctor 对账 → 渠道台账 |
| `kb_collect.py` | 每轮 | 13 渠道取数 → 主题准入过滤 → raw JSONL + 语料页 + 实体页；支持 `--since/--until` 显式窗口、`--throttle-ms` 评论节流（run JSON 带 `write_errors` 计数） |
| `kb_analyze.py` | 采集后 | **取数诊断**（按渠道 profile 判真缺口）→ 分析报告 + 回填队列 |
| `kb_backfill.py` | 采集后 | 回填粘性缺口（正文+评论）+ 死信账本；`--report` 出回填队列 |
| `kb_content_audit.py` | 采集后 | **内容审计**（相关性/完整性/重复）—— 与取数诊断**正交** |
| `kb_prune.py` | 规则变更后/每周 | 存量重判归档（undo 清单）；`--liveness`；`--archive-entities` |
| `kb_reclassify.py` | 按需 | 实体订正 / 孤儿页合并 / frontmatter 自愈 / 补 project_url |
| `kb_insight.py` | 每周/大增时 | 洞察报告；`--browse` 重生成入口页（首屏=意图路由） |
| `kb_moc.py` | 结构变更后/每周 | 三张 MOC：项目地图 / 归档与申诉 / 报告总览 |
| `kb_navfix.py` | 结构变更后/按需 | 补 topic/shard/pub_day/导航段；`--fix-links`；`--fix-names`（均幂等） |
| `kb_name_audit.py` | 命名改动后/每周 | 命名与框架审计（只读），要求**全部通过** |
| `kb_healthcheck.py` | 任何改动后 | **八项不变量**自检（①-⑤硬门 + ⑥⑦⑧软门），收工门 |

## 3. 执行流程（runbook）

**环境前缀（每条命令都要）**：

```bash
export PATH="/c/Users/yangcan/.workbuddy/binaries/PortableGit/versions/1.2.0/usr/bin:/c/Users/yangcan/.workbuddy/binaries/PortableGit/versions/1.2.0/bin:$PATH"
export PYTHONUTF8=1
PY="C:/Users/yangcan/.workbuddy/binaries/python/versions/3.13.12/python.exe"
```

**每日**（自动化 09:30 触发；人工重跑按此序）：

```bash
"$PY" tools/kb_audit.py            # 1 渠道体检（含 doctor 对账，改渠道只改 _meta/channels.yaml）
"$PY" tools/kb_collect.py --fulltext-budget 8   # 2 采集（周一加 --force-weekly）
"$PY" tools/kb_analyze.py          # 3 取数诊断
"$PY" tools/kb_backfill.py --limit 60           # 4 回填（必做：离开窗口的缺口永不自愈）
"$PY" tools/kb_content_audit.py    # 5 内容审计（与 3 正交，都要汇报）
"$PY" tools/kb_healthcheck.py      # 6 收工门
```

**每周一追加**：

```bash
"$PY" tools/kb_prune.py                     # 存量重判（先报告后 --apply）
"$PY" tools/kb_reclassify.py --merge-orphans
"$PY" tools/kb_prune.py --liveness --apply  # 实体页存活标记
"$PY" tools/kb_prune.py --archive-entities  # 先报告再 --apply（顺序：先 kb_moc 再搬，否则地图链接会拦下）
"$PY" tools/kb_insight.py --browse
"$PY" tools/kb_moc.py
"$PY" tools/kb_name_audit.py                # 必须全部通过；有违规走 --fix-names 流程
```

**结构/搬家之后**：`kb_navfix.py --dry` → 补齐 → **连跑两次第二次必须为空**（幂等验证）→
`kb_healthcheck.py`。任何 move/rename = **搬家三件套**（undo manifest + seen 同步 + 链接改写）。

**质检门槛**（10b）：缺 url=0 · 有正文≥70% · 评论抓取≥40%（discussion 渠道）·
单渠道占比≤50% · **可用语料≥70%**；不达标必须说明原因与下一步，不允许含糊汇报。

## 4. 判定纪律（动任何「这个是不是项目」之前必读）

1. **先分「内容问题」还是「渠道语义问题」**——判错方向会得出相反结论。
2. **契约型渠道**（producthunt / indiehackers / betalist / uneed，或标题带 Show HN / I built）：
   条目存在 ≈ 这是项目，**不因缺关键词判无关**。
3. **话题型渠道**（hn_front / lobsters / reddit）：必须靠关键词，且**只匹配标题**
   （长正文顺带出现 launch/startup 是假阳性来源）。
4. **信号层渠道**（bilibili / apple_rss 等 `layer: signal`）不产出正文，**不用正文层的尺子量它**。
5. **已知结构性限制（不要当 bug 修）**：视频帖/社交账号页天然无正文 → 死信账本；
   小红书/X 需登录态（未解锁记 `auth`）；sov2ex 只给正文不给回复；B 站仅元数据。
6. **`projecthunt` / `betalist` / `exa_discovery` 的 project_url 结构性不可得** →
   跨渠道强信号数偏低是**归并键缺失**，不是真没信号。

## 5. 哪些结论不能从这个库得出（防误用）

1. **不能说「某赛道机会大」**：语料来自 HN Show / GitHub / 发布站 = 「开发者在做什么」，不是「市场缺什么」（幸存者样本 + 渠道偏向）。
2. **不能把条数当热度**：信号只按「跨渠道独立观测数」算。
3. **痛点线索未经验证**：正则捞的是线索，不是需求验证。
4. **历史深度有限**（约 90 天铺底 + 滚动）：「趋势/增长率」类判断不成立。
5. **可用 ≠ 是项目**：讨论帖/经验帖是好语料但不能当项目计数（库内单列 `项目型 N 条`）。

## 6. 按意图取用

| 你想干什么 | 去哪 |
|---|---|
| 库里有什么 | `00-索引/项目地图.md` |
| 现在什么在变热 | `00-索引/报告/` 最新 `洞察-*.md`（结论先行） |
| 某项目全部历史 | `10-项目/` 该页「观测历史」表 |
| 某条内容原文与评论 | 项目页观测历史指向的 `20-语料/...` |
| 渠道能不能采 | `00-索引/渠道台账.md` |
| 判废了什么、怎么捞回 | `00-索引/归档与申诉.md` |
| 报告怎么选 | `00-索引/报告/报告总览.md` |
| 字段含义 | `00-索引/字段字典.md` |
| 命名/目录规则 | `00-索引/命名与目录规范.md` |
| 给人看的全景 | `Home.md` |

**机器可读入口**：`90-原始/*.jsonl`（批量分析）· `_meta/insight_latest.json`（最新洞察数据）·
`_meta/seen.json`（item→页路径+观测史）· `_meta/channels.yaml`（13 启用/9 停用/2 未解锁）·
`_meta/schema.json`（字段定义）· `_meta/backfill_queue.json`。

## 7. 本机环境约束（Windows / yangcan）

- **Git Bash PATH 缺 coreutils**：每条命令先 export PATH（见第 3 节前缀），否则 `dirname/sed/uname` 全 not found。
- **Python 用绝对路径**：`C:/Users/yangcan/.workbuddy/binaries/python/versions/3.13.12/python.exe`；不要裸 `python`。
- **MSYS 内联正则陷阱**：`python -c "...re.search(r'^x\s*y'...)"` 里的 `\s` 会被改写成 `/s` → 判据静默失效（实测踩过两次）。**需要正则就写成 .py 文件再跑**。
- **零第三方依赖**：tools/ 只用 stdlib；PyPI 不可达，不要 pip install。
- **git/gh**：git 在 PortableGit（前缀已含）；gh 已登录 `KOIYC`（PAT 走 GCM 凭证助手）。
  收工提交：`git add -A && git commit` 即可推送（**不 force push**）。状态文件（seen/body_cache）
  损坏时脚本会自动隔离成 `.corrupt-*.bak` 并告警——看到这行先查原因再重跑。
- **网络**：`github.com` web 超时但 `api.github.com` 通（gh 用 PAT）；Jina Reader 不可用（doctor 却报 ok → 对账时记 delta）；通用正文唯一后端是 Exa（mcporter，注意 `.cmd` shim）；npm 全局装包要 `--cache="C:/Users/yangcan/.workbuddy/npm-cache" --omit=optional --no-audit --no-fund`。
- **未解锁**：小红书 / X 需 OpenCLI 浏览器扩展（未连接），状态记 `auth`，不算已覆盖。

## 8. 失败处理速查

| 现象 | 处理 |
|---|---|
| 渠道连续空/报错 | 调阈值或写 `channels.yaml` 的 `disabled` 段（原因+复活条件），不静默删 |
| doctor 报 ok 但实测坏 | 写进 `channels.yaml` 的 `backends` 段 + 汇报 delta |
| 出现断链（④ 红） | `kb_navfix.py --fix-links`；短名链接本就有效，不算断链 |
| 路径漂移（⑤ 红） | `kb_navfix.py --fix-names --dry` 核对 → `--apply` → 复跑为空 |
| 文件名带 `[ ] # ^` 或反引号 | 同上（`--fix-names`）；**不许手改文件名** |
| 实体页数对不上 | 跑 `--liveness --apply`，再 `--archive-entities`（先报告后 apply） |
| 语料计数不平（① 红） | 先查是否「改 slug 没同步改名」（两份语料），不是「差不多」放行 |
| 命名审计报违规 | 按 `00-索引/报告/命名审计.md` 的修复路径走，改完须清零 |
| 要回滚归档/改名 | `kb_prune.py --undo <manifest>` / `--undo-entities <manifest>`（manifest 在 `_meta/`，工作区保 12 份，更早在 git 历史） |
| 要回滚工具/配置改动 | `git log --oneline` 找点 → `git revert <sha>`（main 已推远端，**不 force push**） |

## 9. 变更纪律（改完之后）

1. 工具改动 → `kb_selftest.py` 全过（现 38 例）；任何改动 → `kb_healthcheck.py` 八项全绿；
   命名/框架改动 → 另跑 `kb_name_audit.py` 清零；收工前 commit（推送远端）。
2. 产出的报告/决定 → 追加 `00-索引/运行日志.md`；跨会话约定 → 更新本页与 `Home.md`。
3. 汇报格式：新语料条数 · 渠道 ok/异常/未解锁 · 渠道决定 · 回填数量 · 可用率 · 结构维护结果 · 八不变量 · 命名审计 · delta · 质检达标与否。
