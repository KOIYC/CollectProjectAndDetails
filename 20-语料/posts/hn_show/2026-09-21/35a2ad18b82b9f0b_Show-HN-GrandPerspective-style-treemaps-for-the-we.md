---
type: "corpus"
item_id: "35a2ad18b82b9f0b"
title: "Show HN: GrandPerspective-style treemaps for the web and disk usage visualizer"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47950902"
project_url: "https://imbue-ai.github.io/gp-treemap/gallery"
author: "thad_imbue"
published_at: "2026-04-29T16:43:39Z"
captured_at: "2026-09-21T02:52:35+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_thad_imbue
  - story_47950902
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: GrandPerspective-style treemaps for the web and disk usage visualizer

> [!info] 一句话导读
> as a pie chart, but with hierarchy — every slice has its own

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47950902>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：thad_imbue　|　发布：2026-04-29T16:43:39Z
> 项目链接：<https://imbue-ai.github.io/gp-treemap/gallery>
> 采集：2026-09-21T02:52:35+08:00　|　id：`35a2ad18b82b9f0b`

## 正文

gp-treemap gallery
Introduction
Think of a
 treemap
 as a pie chart, but with hierarchy — every slice has its own
 pie-chart breakdown inside it, and so on, all the way down. Nested
 rectangles stand in for slices, each sized in proportion to a numeric
 value, so the whole distribution — and the relative weight of every
 part at every level — is visible at a glance. A hat tip to
 GrandPerspective ,
 the classic macOS disk-usage viewer whose dense, label-free mosaic
 inspired gp-treemap's visual style.
Below: interactive sample visualizations built with
 gp-treemap .
 Each entry is a self-contained HTML file — bundle and dataset
 are inlined, so they render from any URL (or file:// )
 with no server.
Features you'll find in every view below:
Breadcrumb bar along the top, showing the ancestor chain from
 the root down to the currently clicked cell:
The
home icon on the far left is the tree root — click it to focus
 the root, double-click to zoom back out all the way.
Each segment after the home is a clickable ancestor; single-click
 focuses it (highlights its subtree), double-click zooms in so
 that node becomes the new root.
A
magnifying glass marks the current zoom anchor — everything to
 its right lives inside the zoomed-in subtree.
Mouse-wheel focusing : with a cell clicked, scroll the wheel
 to walk focus up and down its ancestor chain — scroll down toward
 the root (shallower), scroll up toward the clicked leaf (deeper).
 It's the fastest way to see where a cell sits in the hierarchy.
Depth truncation via the −/+ depth stepper in the toolbar.
 Capping the depth prunes levels below the budget and rolls their
 contents up into the parent, which makes those parent cells big
 enough to actually carry a readable label. Lift the cap back to
 ∞ to see every leaf. The budget re-applies from the
 current zoom root, so you can drill in and still get a labelled,
 uncluttered view at each level.
Plus the usual: hover for exact values, click to select, double-click
 to zoom, and Size / Color / Path controls in the header of the
 tabular views.
See also: Three treemap libraries, side by side
 — gp-treemap vs Plotly.js vs D3 on the same datasets.
Examples
gp-treemap source tree — disk usage
The gp-treemap repository looking at itself — the working tree plus
 .git and node_modules . Cells are sized by
 bytes on disk and colored by file extension; hover for exact sizes,
 click to select, scroll-wheel to focus an ancestor, double-click to
 zoom. To scan any directory on your own machine and get a
 self-contained HTML like this one:
npx -p @imbue-ai/gp-treemap gpdu ~/path/to/dir
Open full-page →
LLM continuation density — "Time flies like an arrow. Fruit flies like a"
A treemap of the joint probability distribution that a real LLM
 assigns to continuations of a starter prompt. Each cell is one
 token; cell area is the joint probability of the prefix
 from the root to that token (so sibling areas at any subtree sum
 to the parent's joint, and the whole tree sums to 1.0).
Aside — two things this
 visualization is really sensitive to:
1. Trailing whitespace is poison.
 I first ran this with "...Fruit flies like a "
 (trailing space) and the top of the distribution collapsed to
 numbered-list digits and punctuation — same model , no
 banana anywhere near the top. BPE tokenizers ship most content
 words with the leading space pre-baked in (the token is
 " banana" , not "banana" ), so a prompt
 ending in a literal space forces the model to predict a
 no-leading-space token, which content words rarely are. Drop
 the trailing space and banana climbs straight to rank 1.
2. The BOS token matters — a lot.
 The HuggingFace tokenizer auto-prepends <|begin_of_text|>
 to a Llama prompt; node-llama-cpp 's
 tokenize() does not. Without BOS the model is
 conditioned on "this is mid-document text" and produces a
 flatter, weirder distribution; with BOS it's conditioned on
 "this is the start of a new document" and the canonical joke
 completion (which it has seen verbatim in pretraining)
 dominates. Same model, same prompt: banana goes from 9% to
 62% just by flipping the BOS prepend. The tool prepends BOS
 by default to match HuggingFace; --no-prepend-bos
 disables it for direct comparison.
npx -p @imbue-ai/gp-treemap gp-visualize-llm-continuation-density \
 --backend=real --model hf:QuantFactory/Llama-3.2-1B-GGUF:Q4_K_M \
 --prompt "Time flies like an arrow. Fruit flies like a" \
 --continuation-max-depth=4 --top-p=0.80
Down-sampled from a much larger ~24-hour Llama 3.2 1B depth-6 run
 (3.66 M token paths). The sample below is depth-4 + top-p=0.80
 — ~64 k visible nodes, plenty to see the structure without
 bloating the repo. The full original tree lives outside git;
 tools/repack-scan.js derives this slim view from
 it in a few seconds.
Open full-page →
Trees from Tables
The entries below use the path / tabular treemap
 ( gp-columnar-treemap ), which builds the hierarchy on the fly
 from a flat table of rows. The Path control in the header lists
 the columns used to group the data, from outermost to innermost:
Drag the chips to reorder them and the nesting re-computes immediately:
 with Fuel first (as above) you get one cell per fuel with
 continents inside; drag Continent to the front instead
 and the same rows re-tile as one cell per continent with fuels inside.
 Same data, totally different story — and no re-export, just a drag.
 Click the × on a chip to drop that column from the
 hierarchy entirely, or the + to add another.
Global electricity generation — path: fuel → continent → country
Ember's Yearly Electricity Data
 (2023, TWh by country and fuel). Built with
 tools/table-treemap.js from tabular JSONL: use the Size,
 Color and Path controls in the header to re-group on the fly — drag the
 Path chips to reorder the hierarchy. Colored by fuel, Catppuccin
 Mocha theme.
Reproduce it from the pre-filtered JSONL in this repo:
curl -LO https://github.com/imbue-ai/gp-treemap/raw/main/samples/data/table/energy-2023.jsonl
npx -p @imbue-ai/gp-treemap gp-columnar-treemap \
 --size=Generation_TWh --color=Fuel \
 --path=Fuel,Continent,Country \
 --theme=catppuccin \
 energy-2023.jsonl
Open full-page →
 ·
 Source: Ember — Yearly Electricity Data
California city wages 2024 — where do city payrolls go?
Every California city employee with reported wages in 2024 — about
 334,000 rows from the state's
Government Compensation in California raw export, cell size =
 TotalWages . Grouped by
 department → county → city → position → _row , but
 with depth = 1 at first so only the top-level
 Department bucket is drawn — a cleaner first read of where the
 money goes. Police and Fire dominate; Parks & Rec, Public
 Works and Transportation come next. Click the + in the
 component toolbar to reveal another level, or double-click any
 cell to zoom in — the depth budget re-applies from the new root,
 so you can drill in without losing your orientation.
Trivia: DepartmentOrSubdivision is a free-text field
 with no normalization, so each spelling is a separate top-level
 cell. Police alone shows up as Police ,
 Police Department , Police Services Agency ,
 Police Administration , and Police Field Services .
 Fire is Fire , Fire Department ,
 Fire-Rescue , Fire Operations ,
 Fire Suppression , and
 Fire Suppression & Rescue . Parks & Rec is
 Recreation And Parks ,
 Recreation and Park Commission ,
 Parks and Recreation , Parks & Recreation ,
 and Parks & Recreation Administration . And
 Airports and Airport Commission are two
 different cells too.
Open full-page →
 ·
 Source: Government Compensation in California — 2024_City.zip
California city wages 2024 — one cell per employee
Same file as above, but with the depth budget lifted so every one
 of the 334k rows gets its own pixel-sliver cell inside its
 position / city / county / department grouping. Cell size is the
 employee's total wages, so the layout itself reveals pay
 distribution: zoom into Police or a big city and you can see a
 handful of disproportionately large cells (the top earners)
 alongside a vast mosaic of small, similarly-sized cells (the bulk
 of staff at comparable pay).
(See the intro above for the Police / Fire / Parks & Rec
 spelling carnival.)
To reproduce this plot from scratch, grab the raw GCC zip and pipe
 its CSV into gp-columnar-treemap :
curl -LO https://github.com/imbue-ai/gp-treemap/raw/main/samples/data/table/ca-raw/2024_City.zip
unzip 2024_City.zip
npx -p @imbue-ai/gp-treemap gp-columnar-treemap \
 --size=TotalWages --color=DepartmentOrSubdivision \
 --path=DepartmentOrSubdivision,EmployerCounty,EmployerName,Position,_row \
 --theme=one-dark \
 2024_City.csv
Open full-page →
 ·
 Source: Government Compensation in California — 2024_City.zip
UC wages 2024 — campus → position → individual ( Nord theme)
Public-record compensation for every University of California
 employee paid at least $1,000 in 2024 (~334k rows). Each top-level
 cell is one of the 11 campuses, sized by total wages and colored by
 campus; zoom into one to see its positions, and zoom again to see
 individual employees. UCLA and UCSF (both home to big medical
 centers) dominate; the Office of the President is the smallest.
Trivia: the state's raw export lists one of the campuses as
 "Univeristy (sic) of California - Santa Cruz". Hi, Santa Cruz!
 Also curious: ~10,000 employees, including some of UCLA's top
 earners at $3–4M, are filed under
 Blank Assistant 1 / 2 / 3 .
 That's an actual
UC clerical/administrative title series ("Class B – Clerical
 and Allied Services"), so the low-end Blank Assistants are
 clerical workers as advertised — but the million-dollar ones at
 UCLA (a big one is pre-focused) are clearly not clerical staff.
 We don't know what they really are; the public export doesn't
 say.
Open full-page →
 ·
 Source: Government Compensation in California — 2024_UniversityOfCalifornia.zip
UC wages 2024 — position → campus → individual ( Nord theme)
Same dataset as above, regrouped the other way: each top-level
 cell is now one job title, and inside that cell you see how that
 title's payroll divides among the 11 campuses. Where the previous
 view let you compare "what does a campus do?", this one lets you
 compare "who pays more for the same title?" — e.g. clinical
 nurses at UCSF vs. UCLA vs. UCSD, or the mutual-fund-like
 Professor series versus the Athletics coaches hiding inside
 Blank Assistant .
Open full-page →
 ·
 Source: Government Compensation in California — 2024_UniversityOfCalifornia.zip
US federal outlays FY2024 — Treasury MTS Table 5
Gross fiscal-year-to-date outlays as of 2024-09-30, from the US
 Treasury's
 Monthly Treasury Statement . Path: Category → Agency → Bureau,
 colored categorically by top-level category with the Viridis
 palette. Click into a cell to zoom; change Color to
 YoY_Change_Pct to see which areas grew or shrank.
Open full-page →
 ·
 Source: U.S. Treasury Fiscal Data — MTS Table 5
US federal outlays FY2024 — colored by year-over-year % change
Same outlays data, now colored quantitatively with a diverging
 Cool–Warm palette: blue = spent less than FY2023, red = spent
 more. A crisp example of how swapping Color between a categorical and a
 numeric column transforms the story the treemap tells.
Open full-page →
 ·
 Source: U.S. Treasury Fiscal Data — MTS Table 5

## 关联链接

- https://github.com/imbue-ai/gp-treemap/raw/main/samples/data/table/ca-raw/2024_City.zip
- https://github.com/imbue-ai/gp-treemap/raw/main/samples/data/table/energy-2023.jsonl

## 导航

- 项目页：[[10-项目/imbue-ai.github.io_e618118b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
