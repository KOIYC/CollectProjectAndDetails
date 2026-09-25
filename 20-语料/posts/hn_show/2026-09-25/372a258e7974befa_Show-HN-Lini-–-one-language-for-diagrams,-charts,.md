---
type: "corpus"
item_id: "372a258e7974befa"
title: "Show HN: Lini – one language for diagrams, charts, schematics and drawings"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49835704"
project_url: "https://lini.rs/"
author: "monfared"
published_at: "2026-09-24T19:28:30Z"
captured_at: "2026-09-25T13:42:25+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_monfared
  - story_49835704
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Lini – one language for diagrams, charts, schematics and drawings

> [!info] 一句话导读
> One small language for every kind of figure — pretty by default,

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49835704>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：monfared　|　发布：2026-09-24T19:28:30Z
> 项目链接：<https://lini.rs/>
> 采集：2026-09-25T13:42:25+08:00　|　id：`372a258e7974befa`

## 正文

Play
 Tour
 Gallery
 Docs
System
 Light
 Dark
From mindmap
to blueprint.
One small language for every kind of figure — pretty by default,
 precise when it has to be.
Play in the browser
 Docs
source
{
 direction : column ; gap : 72 ;
 | - | { stroke : --gray-deep ; font-size : 12 ; }
 .rose { fill : --rose-wash ; stroke : --rose-deep ; }
 .sky { fill : --sky-wash ; stroke : --sky-deep ; }
 .amber { fill : --amber-wash ; stroke : --amber-deep ; }
 .lime { fill : --lime-wash ; stroke : --lime-deep ; }
 .iconic { direction : row ; gap : 8 ; padding : 12 18 ; }
 | icon | { fill : --rose-soft ; stroke : --rose-deep ; }
 }
 | box # users | .rose.iconic [ | icon | "users" ; "Users" ]
 | group # svc | "Service" { layout : grid ; columns : repeat ( 2 ) ; gap : 50 ; padding : 26 ; } [
 | box # api | "API" .sky
 | slant # db | "Postgres" .amber
 | oval # worker | "Worker" .lime
 | box # mail | .rose.iconic [ | icon | "envelope" ; "Mail" ]
 api -> db
 api --> worker "jobs"
 worker -> mail
 ]
users : bottom -> svc.api "HTTPS"
 {
 layout : tree ; direction : row ; gap : 50 ;
 .eng { fill : --sky-wash ; stroke : --sky-deep ; color : --sky-ink ; }
 .des { fill : --rose-wash ; stroke : --rose-deep ; color : --rose-ink ; }
 .ops { fill : --amber-wash ; stroke : --amber-deep ; color : --amber-ink ; }
 #eng | - | { stroke : --sky-deep ; }
 #des | - | { stroke : --rose-deep ; }
 }
 | topic # co | "Founders" [
 | topic # eng | "Engineering" .eng [
 | topic | "Platform" .eng
 | topic | "Product" .eng
 ]
 | topic # des | "Design" .des [
 | topic | "Brand" .des
 ]
 | topic # ops | "Operations" .ops
 ]
 | chart | "Signups" {
 width : 440 ; height : 280 ;
 categories : "Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat" , "Sun" ;
 } [
 | bars | "Free" { data : 24 , 31 , 28 , 44 , 39 , 22 , 18 ;
 fill : --purple-soft ; radius : 6 ; }
 | line | "Paid" { data : 8 , 11 , 14 , 13 , 19 , 9 , 7 ;
 stroke : --rose ; curve : smooth ; marker : circle ; }
 ]
 {
 layout : sequence ; gap : 45 55 ;
 .app { fill : --sky-wash ; stroke : --sky-ink ; }
 .auth { fill : --purple-wash ; stroke : --purple-ink ; }
 .api { fill : --lime-wash ; stroke : --lime-ink ; }
 }
 | box # app | "App" .app
 | box # auth | "Auth" .auth
 | box # api | "API" .api
app -> auth "sign in"
auth --> app "token"
app -> api "GET /me"
api --> app "profile"
 {
 layout : grid ; columns : repeat ( 2 ) ; gap : 75 ;
 .a { fill : --purple-wash ; stroke : --purple-ink ; }
 .b { fill : --teal-wash ; stroke : --teal-ink ; }
 .c { fill : --amber-wash ; stroke : --amber-ink ; }
 }
 | entity # author | "Author" .a {
 columns : repeat ( 3 ) ; cell : 1 1 ;
 } [
 "PK" "id" "int"
 "" "name" "varchar"
 ]
 | entity # post | "Post" .b {
 columns : repeat ( 3 ) ; cell : 2 1 ;
 } [
 "PK" "id" "int"
 "FK" "author_id" "int"
 "" "title" "varchar"
 ]
 | entity # tag | "Tag" .c {
 columns : repeat ( 3 ) ; cell : 2 2 ;
 } [
 "PK" "id" "int"
 "" "name" "varchar"
 ]
author + -< post
post >-< tag
 {
 .edge { fill : none ; stroke : --stroke-dark ; }
 }
 | drawing # plate | "COVER PLATE" { scale : 1 ; clearance : 20 } [
 | rect # body | .edge { width : 80 ; height : 50 ; radius : 16 ; }
| hole # bolt | { width : 8 ; translate : -24 0 ;
 pattern : grid ( 2 , 1 , 48 , 0 ) ; }
body : left ( - ) body: right { side: bottom ; }
 body : top ( - ) body: bottom { side: right ; }
 bolt ( o )
 ]
 {
 layout : schematic ; padding : 5 20 ;
 | v3 :: label | { symbol : power ; } [ "3V3" ]
 | gpio :: label | { symbol : power ; } [ "GPIO" ]
 }
 | R # r1 | "220R"
 | LED # d1 | "STATUS"
 | Q # q1 | "2N3904"
 | R # r2 | "10k"
| v3 | - r1 - d1.a
d1.k - q1.c
q1.e - | gnd |
 | gpio | - r2 - q1.b
figure
Edit the code, then run it ↗
diagram tree chart sequence entity drawing schematic
One syntax, draw it all
The same six building blocks, from a flowchart to a circuit. Combine shapes, nest layouts, and make a style your own, or take the tour ↗ .
{
 direction : row ; gap : 58 ; clearance : 14 ;
 | - | { stroke : --gray-deep ; }
 .dry { fill : --purple-wash ; stroke : --purple-ink ; }
 .wet { fill : --rose-wash ; stroke : --rose-ink ; }
 }
| group # mix | "Larder" { direction : column ; gap : 20 ; } [
 | box # flour | "Flour" .dry
 | box # sugar | "Sugar" .dry
 | oval # binder | "Binder" .wet
 | cyl # water | "Water" .wet
 ]
 | oval # bowl | "Bowl"
 | slant # stack | "Pancakes" .dry
 mix.flour & mix.sugar & mix.binder & mix.water -> bowl
 bowl -> stack "fry"
Identity |type#id| Pick a shape, and give it an id.
 Label "label" An id for the source. A label for the drawing.
 Style { style } Set colours, spacing, or a whole layout.
 Content [ children ] Nest a group, a room, or a set of parts.
 Class .class Style once. Reuse it on any element.
 Link a -> b Connect by id, even inside another group.
A figure your agent can read back
Give your agent SKILL.md and it can read a figure, change one line, and hand back the diff.
Flow Circuit Drawing
 1 Draw
 2 Read
 3 Change
+-- CI ---------------+
 | |
+------+ | +-------+ +-------+|
| Push |---->| Build |-->| Tests ||
+------+ | +-------+ +-------+|
 +----------------|--|-+
 fail | | pass
 v v
 +--------+ +--------+
 | Report | | Deploy |
 +--------+ +--------+
 5V
 |
 +----------+
 | |
=== [ AMS1117 ]
10u 3 vin vout 2
 | |
GND +----+------ 1 [ J1 ]
 | 2 3V3 OUT
 === |
 22u GND
 |
 GND
 .-""""""-.
 .' '.
 / .-""""-. \
| / \ |
| | () | |
| \ / |
 \ '-....-' /
 '. .'
 '-......-'
ci.build" data-nodes="push,build" aria-pressed="true"> push -> ci.build Push starts the build deploy" data-nodes="tests,deploy" aria-pressed="false"> ci.tests -> deploy "pass" Passing tests lead to a deployment report" data-nodes="tests,report" aria-pressed="false"> ci.tests -> report "fail" Failing tests lead to a report
J1.p1" data-nodes="U1,J1" aria-pressed="true"> U1.vout - J1.p1 "3V3" The regulator’s output feeds pin 1 of the header C1.p1,C1.p2>lini-cap-2" data-nodes="U1,C1" aria-pressed="false"> U1.vin - C1 - | gnd | The input cap sits between 5 V and ground C2.p1,C2.p2>lini-cap-3" data-nodes="U1,C2" aria-pressed="false"> U1.vout - C2 - | gnd | The output cap does the same on the 3.3 V rail
| oval # od | { width : 56 ; height : 56 ; } The flange, and the ⌀56 measured off it | oval # bore | { width : 16 ; height : 16 ; } The bore the section calls ⌀16 | plane # a | "A" { at : 0 x-axis ; } The plane the section is cut on
Select a line to find what it drew.
+ report : left -> ci.build "retry"
“When tests fail, send the report back to Build so we can retry.”
+ U1.vout - | TP # TP1 |
“Put a test point on the 3.3 volt rail so we can probe it.”
− body : bore ( o ) { side: right ; }
 + body : bore ( o ) { side: right ; tol : H7 ; }
“The bore is a press fit — put the tolerance on it.”
Dark mode ships inside the file
Every colour carries its own dark twin, so one exported SVG suits the page it lands on.
Light
 Dark
Name a hue, not a hex.
.drawing { fill : --purple-soft ; stroke : --purple-ink ; }
 .review { fill : --rose-soft ; stroke : --rose-ink ; }
 .revise { fill : --teal-soft ; stroke : --teal-ink ; }
 .ship { fill : --amber-soft ; stroke : --amber-ink ; }
More than diagrams
Charts and mindmaps, circuits and floor plans — open
 any of them in the playground.
Mindmaps |mindmap|
Charts layout: chart
ER schemas |entity|
Sequences layout: sequence
Diagrams layout: flow
Engineering drawings layout: drawing
Circuit schematics layout: schematic
Line charts curve: smooth
Pies & donuts layout: pie
Tables |table|
Floor plans layout: floorplan
Bubbles |bubble|
The Lini logo layout: stack
Browse the gallery
Getting started
Point it at a .lini file and it writes the SVG
 beside it.
cargo install lini
 copy
lini figure.lini -o figure.svg
Or hand your agent SKILL.md
 and ask it for the figure — the grammar is the file.
Play in the browser
 Docs
Every figure on this page was drawn by Lini, from the source
 beside it. Lini is open source, under the
 MIT licence .
Learn
Play
 Tour
 Gallery
 Docs
Project
GitHub
Specification
SKILL.md
crates.io

## 导航

- 项目页：[[10-项目/lini.rs_6c023e85]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
