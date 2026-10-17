---
type: "corpus"
item_id: "45b19dcb67eafa0c"
title: "Show HN: Proa – A Rust web framework with fast SSR and multi-target rendering"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50105467"
project_url: "https://proa.so/"
author: "burnrate"
published_at: "2026-10-15T15:52:08Z"
captured_at: "2026-10-16T09:52:04+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_burnrate
  - story_50105467
  - show_hn
metrics: {"points": 90, "comments": 26, "engagement_velocity": 90}
comments_count: 26
comments_total: 26
discovered_via: "hn:show_hn:3d"
---

# Show HN: Proa – A Rust web framework with fast SSR and multi-target rendering

> [!info] 一句话导读
> Proa Docs Ecosystem app Apps Products shipped on Proa

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50105467>
> 指标：点赞=90 · 评论=26 · engagement_velocity=90
> 作者：burnrate　|　发布：2026-10-15T15:52:08Z
> 项目链接：<https://proa.so/>
> 采集：2026-10-16T09:52:04+08:00　|　id：`45b19dcb67eafa0c`

## 正文

Proa Docs Ecosystem app Apps Products shipped on Proa
 dev Developer tools Components, adapters, and more
Proa UI
 Search ⌘ K
The next era of web interfaces. Built in Rust.
 An extremely performant , batteries-included Rust web framework built around a new programming model for composable, multi-target rendering.
 Get started Watch intro
One object. Every render target.
 HTML, Markdown, and other render targets, from one typed component.
 Watch multi-target rendering
ProductCard :: new (product)
 impl  MdRenderSync  for ProductCard {
 fn render_md (self, cx: &mut WebContext ) -> Result <(), WriteError > {
 md_sync! { r###"
 # {self.product.name}
{ Link :: new ( "Buy now" , self.product.url) }
 "###
 }
 . render_md (cx)
 }
}
 md_sync! { r###"
 [ {self.label} ]( {self.href} )
 "###
}
 impl  WebRenderSync  for ProductCard {
 fn render (self, cx: &mut WebContext ) -> Result <(), WriteError > {
 html_sync! {

 {self.product.name}
 { Link :: new ( "Buy now" , self.product.url) }

 }
 . render (cx)
 }
}
 html_sync! {

 {self.label}

}
Build fast, information-dense apps.
 Explore re-creations of GitHub, Sentry, and Airbnb, built in Proa with fast server rendering and selective interactivity.
 View Showcase Benchmarks
GitHub Sentry Airbnb
 oven-sh / bun
 Type / to search
 Code Issues 5k+ Pull requests 1.9k Actions Security Insights
 [tracking] Zig/C++ fork: Rust->Zig port progress #31136
 Closed MaurerAnton wants to merge 8 commits into oven-sh:main
New issue
 Conversation 9 Commits 8 Checks 1 Files changed 16 +461 -10
⌕ src
 install
 PackageJSONEditor.zig
 events.ts
 lexer.zig
 bun-add.test.ts
src/install/PackageManager/PackageJSONEditor.zig +3 -1
 @@ -459,7 +459,9 @@ pub fn edit(
 459 459 }
 460 460 break;
 462 - if (request.version.tag == .github or request.version.tag == .git) {
 462 + if (request.e_string == null and !request.is_aliased and
 463 + (request.version.tag == .github or request.version.tag == .git or request.version.tag == .tarball))
 463 465 for (query.expr.data.e_object.properties.slice()) |item| {
SD Traces / 3a6f53d4f70e4b37b0f14c9b Ask Seer ! ⌁ ▦ ◫ PX GET /api/0/organizations/proa/events/
 production · React · Chrome
1 replay
 Issues 1
 Spans 18
 Age 4m
 Duration 238ms
 Logs 400
 Waterfall Logs
 LCP 108ms INP 64ms TTFB 12ms
⌕ Search logs for this event Auto-refresh
 09:41:08 info request completed status=200 duration=17ms
 09:41:08 info cache hit key=organization:proa
 09:41:08 warn slow query detected db.system=postgresql
 09:41:08 info span finished op=http.server status=ok
 09:41:09 info trace export complete batch.size=64
Malibu Beach House
 Entire home · 4.92 rating · Malibu, California
$350 night
{DatePicker {}} 12 Mon
 13 Tue
 14 Wed
 15 Thu
 16 Fri
 17 Sat
 18 Sun
{BookingBar {}} $700 - 2 nights - all fees
 Reserve
23.5 us
 Proa render p50
5.56 ms
 React renderToString p50
237x
 faster
Warm production p50s measured on an 8-vCPU AMD EPYC-Milan VPS.
Independent demos. Not affiliated with or endorsed by GitHub, Sentry, or Airbnb.
The numbers behind the speed.
Render speed HTTP capacity Suspense under load
Apple M4 Max · September 2026 Scroll horizontally to explore each chart.
 Open full-size SVG View benchmarks
Build your design system.
 Proa UI offers Shadcn style Proa components. Source in your repo, in typed Rust. Theme it, compose it, ship it.
 Browse Components
Does it need JavaScript? No. This build opens and closes with radio inputs and CSS alone.
Is it accessible? Yes. It follows the WAI-ARIA disclosure pattern.
Can I restyle it? The source lives in your repo, so yes.
Accordion
 Free
 Single or multiple open panels, with a CSS-only build that ships no JavaScript at all.
Invoice Status Amount
 INV-2041 Paid $1,499.00
 INV-2042 Pending $399.00
 INV-2043 Paid $399.00
 INV-2044 Refunded $399.00
Table
 Free
 Header, body, footer, and caption parts that compose into dense record views.
Get started Read the docs
 Secondary Ghost
 Delete Cancel Learn more
Button
 Free
 Solid, outline, ghost, and link variants across three sizes and three intents.
Workspace Used in your deploy URL.
Server render by default
 Ship islands only when needed
Field
 Free
 Labels, descriptions, and error text wired to any control, in either orientation.
Deploy preview
 Pushed 2 minutes ago to main.
Render 41 µs
 Client JS 0 kB
Built from source in your repo.
Card
 Free
 Header, content, and footer slots for the surface most product screens are built from.
« March 2026 »
 Mo Tu We Th Fr Sa Su
 23 24 25 26 27 28 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 1 2 3 4 5
Calendar
 Pro
 Single and range selection, month paging, and keyboard navigation, rendered as plain HTML.
Weekly requests 36.2k
Chart
 Pro
 Area, bar, line, donut, and stacked series drawn as pure SVG on the server.
Enter the code we sent to [email protected]
-
Resend available in 0:28
Input OTP
 Pro
 Grouped one-time-code slots with separators, size variants, and a caret you can style.
ME
 You Can an agent add a settings page to this app?
 9:41
AI
 Proa Yes. Every component is typed Rust in your repo, so the compiler checks the edit before it ever reaches a browser.
 9:41
ME
 You How much JavaScript does that ship?
 9:42
Chat
 Pro
 Message bubbles, avatars, timestamps, and typing indicators for assistant surfaces.
Copy html_sync ! {
 { Card {
 class : None ,
 children : Some ( html_sync! {
 { CardTitle { class : None ,
 children : Some ( row . id ) } }
 { CardFooter { class : None ,
 children : Some ( row . due ) } }
 } ) ,
 } }
 }
Code Block
 Pro
 Syntax highlighting done on the server, so no highlighter ships to the browser.
58 components, every one with a live example, a props table, and Rust you can copy.
See more in the docs
 The full catalog, from primitives to paid product surfaces.
Scroll sideways or use the arrow keys to move through the component demos.
Everything people want from a modern web app, without the render tax underneath it.
 A component system and a framework surface, not a templating engine.
Framework render
WebContext
Route
DataLoader
Stream
Framework
 Framework primitives beyond template glue.
 Proa keeps streaming, request data, routing, metadata, and response control inside the same typed WebContext as your components.
Streaming SSR, in order or out of order
 Flush HTML in document order when sequence matters, or let Suspense boundaries stream ready chunks out of order when slow data should not block the page.
DataLoader-backed WebContext
 Every render has typed access to request-scoped data, response metadata, route state, and loader caching through the same WebContext components already receive.
Typed SSR framework semantics
 Layouts, routing, metadata, static assets, forms, mutations, and progressive navigation compose through the same Rust component model instead of template glue.
Interactive SSR page
SSR
 RSJS
"RSJS island"
SearchIsland
Rust SSR
rsjs query
MapViewport
rsjs handler
on_click
Interactivity
 Add interactivity without giving up native SSR.
 Keep the page as server-rendered HTML, then opt specific controls into client behavior with typed signals and event handlers. Proa compiles only the moving pieces into JavaScript.
RSJS islands
 Use signal(...), bind_value, typed events, and named handlers in Rust. The compiler lowers the client behavior.
Tiny per-island JavaScript
 Each hydrated RSJS island emits a small vanilla-JS module plus seed state, served with a shared runtime around 1.3 KB gzipped.
Adopt incrementally
Node
Python
Ruby
Go
ffi
Proa render core
Axum-native when you want it. Shared library when you do not.
Adoption
 Keep the stack you already have. Move one route first.
 Go Axum-native for Proa routing and responses, or call Proa over FFI from Node, Go, Python, Ruby, or Java.
Run alongside your existing app
 Proxy one route to Proa, leave the rest on Next.js or Rails, then compare latency and cost in production.
Security by default
 Auto-escaped output, cross-origin request protection, security headers, and fixed-upstream proxying are part of the framework surface.
Accessibility at compile time
 WCAG and WAI-ARIA checks run during cargo build so common markup defects fail before deploy.
Start building with Proa.
 Read the quickstart
Proa The next era of web interfaces. Built in Rust.
Explore
 Apps
 Ecosystem
Resources
 Docs
 Sitemap
© Proa Labs, Inc. All rights reserved.
 Rendered by Proa.
Search
 ESC
 Type at least 2 characters
↑ ↓ navigate ↵ open esc close

## 评论（26/26）

> **kianN** · 2026-10-15T17:39:07.000Z　
> This looks really cool! I’ve been really appreciating the revival of old-school server side rendering and foundational web components, but with modern tools or approaches.

---

> **airstrike** · 2026-10-15T18:05:18.000Z　
> Why does `fn render` need to borrow WebContext mutably?

---

> **egeozcan** · 2026-10-15T18:24:43.000Z　
> Very cool idea, I'm going to test this!One nit: Forgive me if I'm missing something but why do you have pro components? Won't people vibe-code clones anyway? I'd rather have a donate button these days.

---

> **lwhsiao** · 2026-10-15T19:06:50.000Z　
> Can I get a TLDR of why Proa is seemingly so much faster tha existing Rust web frameworks (Dioxus, Leptos, Topcoat)?

---

> **trnvll** · 2026-10-15T21:09:06.000Z　
> Damn, projects like these really spark my curiosity about Rust. I guess it's time to try it out, fomo is getting too big haha

---

> **canadiantim** · 2026-10-15T21:47:53.000Z　
> This looks amazing, really appreciate your minimal JavaScript approach. I’ll definitely try it out, could see myself potentially doing pro version in future.

---

> **contingencies** · 2026-10-15T22:13:47.000Z　
> So... Multi-target = {chat, web, markdown}; Audience = {human, bot}; USPs = {speed, unified model}Since I don't believe the maintenance challenges of a non-unified model are particularly high-friction in the LLM era (even if they may be error-prone, since that is usually solved with CI/CD or TDD), the nominal utility of this angle of architectural enhancement is considered dubious.With regard to speed, there is no hardware shortage at present for any of these simple rendering tasks.Overall, a nice efficient codebase but suffering a bit from NIH syndrome solving no particularly acute problem. Unless a community forms rapidly, this will probably die.I'd like to see the benchmark compared to, eg. static files served with binserve.

---

> **farmeroy** · 2026-10-15T22:44:27.000Z　
> This might be a silly question, but why 2 views for html and markdown? isn't there a broad base of cases where one can just be inferred from the other?Also, I think it's exciting to see so many rust web frameworks popping up but I'm in total decision paralysis. If I want to build something with rust now there are at least 3 complete frameworks: loco, topcoat and now proa... plus actix, rocket, axum, and ...more?

---

> **yieldcrv** · 2026-10-15T22:57:28.000Z　
> I would be mostly curious about CI/CD and build and deployment times on underpowered compute instancesI could drop the react ecosystem given considerable improvement over it at the deployment partEspecially since years of experience with frameworks doesnt matter anymore and won’t matter with recruitment soon

---

> **jakswa** · 2026-10-15T23:32:09.000Z　
> I was recently scanning for newer, more-batteries-included options and this looks well-scoped at first bluff. Thanks for spreading it, might end up in my next experiment!

---

> **burnrate** · 2026-10-15T19:05:41.000Z　
> That's very kind of you, appreciate it man! Thanks!

---

> **burnrate** · 2026-10-15T19:03:25.000Z　
> Hey great question! WebContext owns an output buffer (i.e., RenderBuffer) that components write HTML into directly, avoiding intermediate allocations and copying. It needs to be mutable for this reason. This is one of the key ways we're able to make Proa the fastest server-side rendering engine on the market.By default, WebContext composes RenderBuffer (but it can be overriden via generics) which uses fixed-size 4 KiB pages. When a page runs out of room, it adds another page without moving the HTML already written. This avoids copying the accumulated output during growth! Its designed to be a performance improvement over VecFor context, the problem with Vec is that every time a vector reaches maximum capacity, it has to reallocate a new area of memory (typically 2x larger than the previous allocation) and then copy everything into that new buffer. This adds a ton of overhead, especially if you're writing large pages.Checkout https://github.com/Proa-Labs/proa/blob/384136f87fc9f91747477... if you're curious about RenderBuffer's design

---

> **burnrate** · 2026-10-15T18:43:14.000Z　
> Hey! Author of Proa here, thanks for checking it out! The idea is to just accelerate the time it takes to create components, similar to Shadcn or other component libraries. You can create a new component and modify them however you like. It’s nice because they have both the WebRender and MdRender trait implemented, and saves you a bit of time. Also for slightly more complex components like Calendar, we’ve crafted the component with all the JS interactivity required to do things like switch months, select start and end date, etc

---

> **burnrate** · 2026-10-15T19:44:21.000Z　
> I can't speak for the others as I am not as familiar with how they're engineered, but with Proa I spent a painstaking amount of time to try and move as much of the work to compile time as possible and being really careful about how memory is allocated. And a lot of those small improvements add up over time!

---

> **burnrate** · 2026-10-15T22:57:36.000Z　
> I highly recommend! I've been writing Rust professionally for 5 years now. Compile times are slow but I love the language. https://cheats.rs/ is a resource i go back to often in case you're interested in learning more. Especially since as you get more into it, Rust has a lot of weird types like RefCell and Cell and OnceCell and disambiguating between them is a chore sometimes. Hope it helps!

---

> **burnrate** · 2026-10-16T00:04:33.000Z　
> Thank you so much, that's very kind of you! Sounds great! Please feel free to provide any feedback or ways I can make it better for you.

---

> **burnrate** · 2026-10-15T23:31:02.000Z　
> > This might be a silly question, but why 2 views for html and markdown?No such thing as silly questions! Yes there are cases where it can be inferred from one to the other, but in many cases you may want to be very specific about how you author the markdown view. I'll give you a few examples:1. Custom components: For example, let's say you have a carousel component. It's not really straightforward to infer the markdown from this. But you probably want the carousel to render as a series of markdown image tags. A custom view would be helpful for this. Same goes for Calendars, SVG charts, Diagrams, form inputs, tabs, popovers, and more.2. Information omission: Agents don't need all of the information on your page. For example, a dark/light button... probably doesn't need a markdown equivalent. But a button that is an anchor tag that links to another page, probably you should keep. So having the ability to custom author the markdown render target based on the data it's rendering is helpful.One of the unique aspects of Proa's authoring model is that it supports composability of Markdown components, just like JSX, which is I think one of its standout features. And you can embed native control flow (if, loops, match, etc.) directly in the md!{} macro just like you could with JSX. https://www.youtube.com/watch?v=pJx84jdBDKU&t=21s explains it quite well if you're interested. Makes the readability and code ergonomics much much better.> it's exciting to see so many rust web frameworks popping up but I'm in total decision paralysis.I am a bit biased here but I think Proa is the most complete framework currently for building a production web application in Rust. I know its newer and doesn't have as many stars, but maybe I can point you to three things to see if it gives you more confidence:1. Data loading: https://proa.so/docs/framework/data-loading
> 2. Browser interactivity: https://proa.so/docs/rsjs/signals (all in rust btw)
> 3. Security: https://proa.so/docs/framework/security-headersProa, Proa UI, latency.so, and a few other sites are all using Proa in production. It's the fastest SSR framework in production (https://github.com/Proa-Labs/proa-benchmarks) and supports streaming SSR (checkout the streaming SSR benchmark), suspense, etc. And it's server framework agnostic so you can use it with actix, axum, and other frameworks if you want.

---

> **burnrate** · 2026-10-15T23:52:46.000Z　
> Compile times generally take longer with Rust. It's a trade-off you're making when using anything rust related, but in exchange, you get some pretty sweet runtime perf. But with efficient caching of crates you can claw back a lot of time in CI.

---

> **burnrate** · 2026-10-15T23:35:52.000Z　
> That's very kind of you, thank you! Yes the goal is to make it usable in production! It already powers proa.so, ui.proa.so, latency.so, and a few other sites. Let me know when you build it and I can add it to https://proa.so/ecosystem/apps!

---

> **raddikal** · 2026-10-16T00:14:14.000Z　
> I remember a friendly member around here recently remarking that rustc is a high quality project, with lots of eyes on it and lots of effort put into it.And then this shows up.https://github.com/rust-lang/rust/issues/164348#issuecomment...A bug as careless as can be. Relying wantonly on hashing for equality checking, without even wondering about the specific hash's collision probability.

---

> **DrammBA** · 2026-10-15T19:49:15.000Z　
> You answered "Why do you have a component library?" but I think the original question was more along the lines of "Why bother monetizing components that can be copyright-washed in minutes with LLMs instead of having a Donations funnel?"

---

> **farmeroy** · 2026-10-15T23:48:59.000Z　
> Ah ok so it's more of the ui layer? because when I look at for instance loco, it handles background jobs, emails, auth - it's a battery included framework. So proa is something that could be used in place of askama + htmx but still with another full featured (or totally minimal) framework?

---

> **jakswa** · 2026-10-16T01:20:46.000Z　
> I think you were meaning to reply to another comment?

---

> **killingtime74** · 2026-10-15T20:22:47.000Z　
> Aren't Pro components the same as a donation, but then giving you something extra as well.

---

> **skrtskrt** · 2026-10-15T20:27:05.000Z　
> In any corporate structure it's 10000x easier to get approved to just buy something from a vendor than it is to set up donations for an open-source project/foundation.PLus you're missing the licensing aspect, part of this is AGPL if you use the free version, lots of places are happy to throw down money to get a commercial license rather than hem and haw over AGPL.

---

> **DrammBA** · 2026-10-15T20:53:55.000Z　
> Kind of, not really, in this case it's a subscription that renews monthly/yearly so you have to remember to cancel it when your reach the amount you wanted to donate, maybe you didn't want to donate as much as 1 month costs so you're left not sending them any money in the end, right now you can't even subscribe cause their console 404's. You got to make it as easy as possible for people to part with their money, component library subscription is not it.

## 导航

- 项目页：[[10-项目/proa.so_c0174e89]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
