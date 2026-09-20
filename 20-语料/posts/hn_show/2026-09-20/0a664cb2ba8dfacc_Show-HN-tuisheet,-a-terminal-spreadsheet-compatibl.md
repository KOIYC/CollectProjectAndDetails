---
type: "corpus"
item_id: "0a664cb2ba8dfacc"
title: "Show HN: tuisheet, a terminal spreadsheet compatible with OpenXML (xlsx) files"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49752129"
project_url: "https://github.com/krackout/tuisheet"
author: "krackout"
published_at: "2026-09-18T09:55:28Z"
captured_at: "2026-09-20T14:02:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_krackout
  - story_49752129
  - show_hn
metrics: {"points": 2, "comments": 4, "engagement_velocity": 2}
comments_count: 4
comments_total: 4
discovered_via: "hn:show_hn:90d"
---

# Show HN: tuisheet, a terminal spreadsheet compatible with OpenXML (xlsx) files

> [!info] 一句话导读
> A terminal user interface spreadsheet.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49752129>
> 指标：点赞=2 · 评论=4 · engagement_velocity=2
> 作者：krackout　|　发布：2026-09-18T09:55:28Z
> 项目链接：<https://github.com/krackout/tuisheet>
> 采集：2026-09-20T14:02:30+08:00　|　id：`0a664cb2ba8dfacc`

## 正文

# krackout/tuisheet

A terminal user interface spreadsheet.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: The Unlicense
- Default branch: main
- Created: 2026-09-17T09:00:59Z

## Languages

- Go

## Top Contributors

- krackout (1 contributions)

---

## README

Presenting **tuisheet**: A love letter to VisiCalc and Lotus 1-2-3.

The motive was to code a programme inspired by VisiCalc and Lotus 1-2-3 interface, running on terminal, but fully compatible with the current universal standard of OpenXML (xlsx files for spreadsheets). Coded in Go lang; apart from my being more familiar with this programming language, it helps making a single executable, low on resources. Also, I like Go's compiler ability to cross compile to many platforms and OSes (which I personally often meet through my daily job). By the way, **tuisheet** is much more thoroughly tested and used on Linux than on Windows (or Solaris, AIX, BSD).

Mostly vibe coded. Yet with no subscription available, I used a variety of platforms and LLMs to reach a respectful stage to publish it. Started with questions on LLM web sites, then saw an advertisment for Codex with ChatGPT which I used a bit; but free tokens ran out quickly. Moved to OpenCode agent with which I went all along, changing LLMs whenever they stopped being available on the platform (Deepseek free, 0x Alpha, Muse Spark Free). A happy journey of acquittance with LLMs and agents. I can't tell of the effect of LLM switching on the code; I tried to cleanup and optimize, either by my actions or by prompts. Nevertheless the programme is stable and fast for my daily usage, having completely replaced LibreOffice or Excel.

Quick info:

- **F1** key shows help.

- **/ (slash)** presents menu. You can navigate either by pressing the capital letter of each option (usually the first letter of its name but not always) or by arrow keys.
For example, to open a file, the key sequence is: / F R
To quit, / Q

- Mouse can be used to click to cells. Right click is available in cells, rows, columns and sheets/tabs bar.

Screenshots:

**Formulas:**

**Undo history:**

**Search results:**

**File selector to load file:**

**Perspective view:**

---
Enjoy! Regarding your precious xlsx files, I quote from licence,

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Rabbit Hole — Daily Wikipedia Racing

## 评论（4/4）

> **ukadakal** · 2026-09-18T12:23:07.000Z　
> Very cool project! For those of us old enough to remember working this way, it’s really nice to see a modern take on it.Curious how extensive the formula support is. How many Excel functions do you currently support, and how do you handle more complex formulas and dependencies between cells or dynamic array formulas, etc.?

---

> **krackout** · 2026-09-18T12:54:26.000Z　
> Thank you! Perhaps I should add the supported functions in README.md. There is a list in programme's help (F1) with a small summary from each one. I copy from there:ABS, AND, AVERAGE, AVERAGEIF, COLUMN, COUNT, COUNTA, COUNTIF, COUNTIFS, DATE, DAY, DAYS, EXACT, EXP, FILTER, FIND, HLOOKUP, IF, IFERROR, IFNA, IFS, INDEX, INDIRECT, INT, IPMT, ISBLANK, ISERROR, ISNUMBER, ISTEXT, LEFT, LEN, LET, LN, LOWER, MATCH, MAX, MID, MOD, MONTH, NA, NOT, NOW, OFFSET, OR, PI, PMT, POWER, PPMT, PRODUCT, RIGHT, ROUND, ROUNDUP, ROW, ROWS, SQRT, SUBSTITUTE, SUBTOTAL, SUM, SUMIF, SUMIFS, SUMPRODUCT, TEXT, TEXTJOIN, TODAY, TRIM, TRUE/FALSE, UPPER, VALUE, VLOOKUP, WEEKDAY, XLOOKUP, YEAR,Regarding the 2nd part of your question, I quote from the LLM: Complex scalar formulas with deep, cross-sheet, and indirect dependencies are fully evaluated with cycle safety; range/array inputs compose inside aggregations, but dynamic-array spilling is not implemented — multi-cell results surface as #VALUE! instead of spilling.

---

> **ukadakal** · 2026-09-18T13:01:19.000Z　
> That’s actually quite impressive. Supporting functions like XLOOKUP, FILTER, INDIRECT, and LET is already a pretty capable calculation engine. Thanks for sharing the details!

---

> **krackout** · 2026-09-18T13:29:55.000Z　
> I actually searched the web for popular functions to implement; I don't personally use all of them. If you have any other functions in mind, tell me to implement them also.

## 导航

- 项目页：[[10-项目/github.com_681d49db]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
