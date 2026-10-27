---
type: "corpus"
item_id: "03fafb66cc4c5843"
title: "Show HN: Hatamoto batteries-included CMS in Go"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50256725"
project_url: "https://hatamoto.dev/"
author: "teslazen"
published_at: "2026-10-27T09:57:24Z"
captured_at: "2026-10-27T23:46:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_teslazen
  - story_50256725
  - show_hn
metrics: {"points": 11, "comments": 9, "engagement_velocity": 11}
comments_count: 9
comments_total: 9
discovered_via: "hn:show_hn:3d"
---

# Show HN: Hatamoto batteries-included CMS in Go

> [!info] 一句话导读
> v1.0 Open source under Apache-2.0, on GitHub →

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50256725>
> 指标：点赞=11 · 评论=9 · engagement_velocity=11
> 作者：teslazen　|　发布：2026-10-27T09:57:24Z
> 项目链接：<https://hatamoto.dev/>
> 采集：2026-10-27T23:46:32+08:00　|　id：`03fafb66cc4c5843`

## 正文

Skip to content
旗本 Hatamoto
Menu
 Plugins
 Themes
 Docs
GitHub
 Get started
v1.0 Open source under Apache-2.0, on GitHub →
 The batteries-included CMS
 for the agentic era.
A page builder, SEO, caching, forms, redirects, AI analytics and an MCP server come built in. It runs as one Go binary next to Postgres, with no PHP, Node or plugins to keep updated.
Get started
Read the code
$ git clone https://github.com/Zen-Labs-Corp/hatamoto && cd hatamoto && docker compose up Copy
The WordPress importer keeps every URL →
your-site.com//ai-analytics
AI crawler analytics Counted on the server, where crawlers show up
One binary + Postgres No PHP, Node or Redis
Plugins in a sandbox WebAssembly, only what you grant
Updates roll back Signed, checked, reverted on failure
No telemetry Your data stays in your Postgres
AI analytics, out of the box
 See which AI crawlers read each page, and which ones are fakes.
Google Analytics can't see AI crawlers: they don't run JavaScript. Hatamoto counts them on the server instead. Each fetch is checked against the operator's published IP ranges and reverse DNS, grouped by why the bot came, and tied to the page it read.
Last 30 days 46,191 AI fetches across 16 of 19 known agents
Act now 3,301 spoofed fetches from bots pretending to be ClaudeBot, GPTBot and others
Act now 11,456 error responses served to AI crawlers, with the failing paths listed
Review 863 published pages no AI has fetched yet, so none can be cited
your-site.com//ai-analytics/crawlers
Real data from a live Hatamoto site, last 30 days. Every figure above comes from these two screens.
Training Model crawlers
 Bulk crawls that feed future models. You can allow or block all of them in robots.txt from the same screen.
 GPTBot ClaudeBot CCBot
Search index Answer-engine indexers
 AI search tools answer from the indexes these bots build. A page they never fetch can't be cited.
 OAI-SearchBot PerplexityBot
User fetch Live assistant requests
 A person asked an assistant a question and it opened your page to answer. This is the closest you get to a real reader.
 ChatGPT-User Claude-User
Checked, so fakes don't count
 IP ranges and reverse DNS for nine operators. Bots using a fake user agent are flagged and left out of the totals.
Per page, in the editor
 The editor shows which agents have fetched the post you're working on, and when they first did.
AI referrals
 Visits from ChatGPT, Perplexity, Gemini and Claude, per assistant and per day.
No visitor profiles
 Counted per day in your own Postgres. No cookies and no third-party scripts.
Everything else, out of the box
 The plugin stack you'd assemble is already in core.
One content model, one settings screen, one update. No licence keys, no upsell banners, and no plugins to test against each other after every update.
Usually you add
In Hatamoto core
A page builder Elementor, Divi
 →
 Visual builder. Click to select, double-click to type, right-click menus, copy between pages, and desktop, tablet and phone views.
An SEO plugin Yoast, Rank Math
 →
 SEO and answer panel. Focus keyword, meta, canonicals and checks in the editor. JSON-LD generated from the content type.
A cache plugin WP Rocket, W3 Total Cache
 →
 In-memory page cache. Clears itself when you save, preloads from the sitemap. No Redis, no Varnish.
Redirects and 404s Redirection
 →
 Redirects with wildcards. A 404 log ranked by hits, and Explain a URL to see which rule answers.
A form plugin Contact Form 7, Gravity Forms
 →
 Form builder. A hidden spam trap, timing and rate limits, with an optional captcha. Email, CSV export and a signed webhook.
An analytics script Google Analytics, which can't see AI crawlers
 →
 AI crawler analytics. Crawlers don't run JavaScript, so a script never sees them. Hatamoto logs every fetch on the server: which agent, which page, and whether it was really them.
A security plugin Wordfence
 →
 Sealed admin. A private admin address, the same 404 for every scanner, and attack tests in the codebase.
An API and automation layer WPGraphQL, Zapier
 →
 MCP server and REST API. Scoped keys per agent or script, on the same rules as the admin.
Custom fields ACF, Pods
 →
 Your own content types. Types with typed fields, a schema.org type and an address pattern, built in the admin. Every page is a record before it is HTML.
Plugins with full access PHP that can read every file and table
 →
 Sandboxed WASM plugins. Each plugin runs in WebAssembly with memory and time limits, and only the permissions the owner ticks.
Sitemaps, schema, links three more plugins
 →
 One entity model. Sitemaps, feeds, llms.txt, internal links and structured data from the same record.
Usually a plugin per job, each with its own updates and settings. Here, one binary and one update.
Entities first
 Every page starts as one typed record, and everything machines read is built from it.
You fill in the fields once. The page, its JSON-LD, its sitemap entry and the knowledge-graph feed all come from that record, so they always agree.
Emergency plumbing Service
name Emergency plumbing
slug emergency-plumbing
area_served Melbourne
hours 24/7
price_from $149 call-out
faq 3 questions
Published · one record in Postgres
The page /services/emergency-plumbing
Emergency plumbing
 24/7 call-outs across Melbourne. From $149.
 Call now
JSON-LD in the page head
{ "@type" : "Service" , "name" : "Emergency plumbing" ,
 "areaServed" : "Melbourne" ,
 "provider" : { "@id" : "…/#organization" } }
Sitemap /sitemap.xml
  https://your-site.com/services/emergency-plumbing
  2026-10-27
llms.txt and knowledge graph /llms.txt
- [Service]( https://your-site.com/api/v1/public/knowledge-graph?schema=service ):
 12 entities as JSON-LD.
Edit the record and every output follows on the next request. Switch off Include in /llms.txt and the entity leaves llms.txt and the feed together.
What comes built in
 Everything you need to edit, rank and run a site.
編 Edit
A visual builder for pages and a plain editor for posts.
Pages open in the builder and posts open in a simple writing view. Both save to the same record.
Double-click to format text on the page. Right-click to copy, wrap, duplicate or paste into another page.
Desktop, tablet and phone views, with show and hide per device.
Slash menu, autosave, revisions, and unsaved work kept on the server, so it follows you to another device.
Page
 Hero
 Heading
 Text
 Services
 FAQ
Heading Class
 Anchor
 Show on
実 Get found
Search engines and AI get the same structured data.
Every page is a typed entity with a schema.org type. The page, its structured data, the sitemap entry and the llms.txt summary come from that one record, so they can't contradict each other.
JSON-LD for every entity, with FAQ, Person and Claim markup.
Real authors as people, with the same @id on every post they wrote.
Internal links that add themselves from rules you set once.
<!-- /services/emergency-plumbing, from the entity -->
{ "@type" : "Service" ,
 "name" : "Emergency plumbing" ,
 "areaServed" : "Melbourne" ,
 "provider" : { "@id" : "…/#organization" } }
機 Let agents publish
AI agents work through the same rules as your team.
An MCP server at /mcp and a CLI call the same services as the admin, so validation, sanitising, hooks and cache clearing always apply.
A scoped key per agent. A read key can't write.
Anything an agent creates starts as a draft. Agents can build pages in the builder, with the same checks.
Every call, allowed or refused, lands in the audit log and the version history.
速 Run it simply
Deploy one file, with no build step.
The site, the admin, the API and the MCP server are one Go binary on one port, next to Postgres 16. Pages render on the server and are served from memory in milliseconds.
No PHP version to juggle, no Node build step, no npm.
Runs its own migrations on boot, with a supervisor that restarts it.
Any Linux box, or docker compose up .
Security
 No /wp-admin for bots to find.
Every Hatamoto install gets its own private admin address. Every other path, including the ones scanners try first, answers with the same plain 404 as a random URL. Public pages don't reveal what software runs the site.
Request Answer
GET /wp-login.php 404
GET /admin 404
GET /.env 404
GET /xmlrpc.php 404
GET /k7qm-x2rf-9tdc your admin
Public pages can't reach the admin
 A script on a public page can't fetch, frame or drive the admin. Previews and the builder canvas run no page scripts at all.
Attack tests run on every change
 A CI job starts the real binary and runs 22 attacks against the admin from a public page. Each has a control, so a silent pass fails the build.
Plugins can't take the site down
 Plugins are signed WebAssembly with their own Postgres schema and only the permissions you tick. A failing plugin is switched off, not fatal.
Updates that roll themselves back
 Signed releases install in your maintenance window. If the site fails its checks for a minute afterwards, the previous version comes back.
Move from WordPress
 Move from WordPress without losing a URL.
The importer reads your site through the REST API or a WXR export, from the admin wizard or the command line. Rehearse it as often as you like, and cut over when the audit is clean.
01 · Scan See what comes over
 Counts, permalinks, SEO plugin, page builders, shortcodes and anything that won't convert. Nothing is written.
 --scan-only
02 · Import Content, media, menus, people
 Posts, pages, categories, tags and menus. Authors become people with bylines. SEO titles carry over from Yoast, Rank Math, SEOPress or AIOSEO.
 --url … or --wxr site.xml
03 · Audit Every old URL checked
 Each address from your old sitemap must answer with a page or a single 301 to one. Chains, 302s and 404s fail the run.
 --audit-url https://new…
04 · Cut over Re-sync, then switch
 Run it again the night before. It updates what it imported, never duplicates, and leaves your Hatamoto edits alone.
 --resume  --keep-edited
Comes over
Your permalink structure, copied into URL patterns
Site title, tagline, time zone, language and home page
YouTube and Vimeo embeds, galleries and featured images
Private posts and drafts, with an application password
Doesn't come over, and the scan lists it before you start
Page builder layouts: the text is kept, the page is listed to rebuild
Forms, comments and WooCommerce data
Shortcodes: removed from the body and reported
For developers
 Build on it with JSON-LD, MCP and Go.
Pull structured data from any page, connect an agent over MCP, or write a WebAssembly plugin when core doesn't cover what you need.
Read Structured data, on request Every page carries its JSON-LD in the head. Ask for application/ld+json and you get only the data.
Connect An MCP server at /mcp Point any MCP client at your site with a scoped key. Agents list, draft, edit and publish through the same rules as the admin.
Extend Plugins in WebAssembly Hook into publishing, JSON-LD, forms and rendering with the Go SDK. A plugin runs in a sandbox with only the permissions the owner ticks.
GET /services/emergency-plumbing Copy
$ curl -H 'Accept: application/ld+json' \
 https://your-site.com/services/emergency-plumbing
{
 "@context" : "https://schema.org" ,
 "@type" : "Service" ,
 "name" : "Emergency plumbing" ,
 "url" : "https://your-site.com/services/emergency-plumbing" ,
 "areaServed" : "Melbourne" ,
 "provider" : { "@id" : "https://your-site.com/#organization" }
} // mcp.json, in any MCP client
{
 "mcpServers" : {
 "hatamoto" : {
 "url" : "https://your-site.com/mcp" ,
 "headers" : {
 "Authorization" : "Bearer nxk_…"
 }
 }
 }
} package main
import (
 "hatamoto.dev/sdk"
 "hatamoto.dev/sdk/guest"
)
func init () {
 guest. OnAction (sdk.EntityPublished, func (ev sdk.EntityEvent) error {
 guest. Log (guest.LogInfo, "published " +ev.Slug)
 return nil
 })
 guest. OnFilter (sdk.JSONLDEnrich, func (d sdk.JSONLDDoc) (sdk.JSONLDDoc, error ) {
 d.Doc[ "x-hello" ] = "hi"
 return d, nil
 })
}
//go:wasmexport on_entity_published
 func onEntityPublished () int32 { return guest. Run (sdk.EntityPublished. Export ()) }
//go:wasmexport filter_jsonld_enrich
 func filterJSONLDEnrich () int32 { return guest. Run (sdk.JSONLDEnrich. Export ()) }
func main () {}
Validate any page with the MCP tool jsonld_validate .
Open source
 Open source, including the code that runs this site.
Apache-2.0 on GitHub. hatamoto.dev runs the same code. There's no paid edition, no licence server and no telemetry.
Apache-2.0 Use it for clients, fork it, sell it
0 Telemetry. One update check, and you can turn it off
3 channels Canary, edge and stable, signed
Any language Plugins in Go or anything with an Extism PDK
Star on GitHub
 Read the docs
01 Clone and boot
 Postgres and Hatamoto start, secrets are generated, migrations run.
git clone https://github.com/Zen-Labs-Corp/hatamoto
cd hatamoto && docker compose up
02 Grab your setup code and admin address
 The setup code is printed once in the logs. Your private admin address is one command away.
docker compose logs hatamoto
docker compose exec hatamoto hatamoto admin-url
03 Import your WordPress site
 Finish the wizard and pick Import from WordPress, or stay in the terminal.
hatamoto import wordpress --url https://your-site.com --scan-only
Questions Common questions
Why can't my current analytics see AI crawlers? Browser analytics only count visitors that run JavaScript, and AI crawlers don't. Hatamoto sees every request on the server, so it counts the crawler fetch itself, checks the bot is who it claims to be, and links the hit to the page. Counting crawlers needs no script, and no visitor profiles are stored.
Will my rankings survive a move from WordPress? The importer copies your permalink structure, carries SEO titles and descriptions over, and audits every URL in your old sitemap. Each one must answer with a page or a single 301 before the run passes. That's the part of a migration that usually costs rankings.
What about the plugins I rely on? Most sites run plugins for jobs Hatamoto does in core: SEO, caching, redirects, forms, sitemaps, analytics and security. For the rest there are sandboxed plugins, including first-party Search Console and Tag Manager, and a Go SDK to write your own. WooCommerce stores aren't a fit today.
Where can I host it? Anywhere that runs a Linux binary and Postgres 16: a small VPS, your own server or Docker. The binary serves the site, admin, API and MCP on one port, and the docs include a Caddy config for HTTPS.
Is it ready for a real site? It runs hatamoto.dev in production. Version 1.0 rolls out through canary, edge and stable channels, every release is signed, and an update that fails its health checks reverts on its own. The plugin SDK is still v0; what stays stable is written down in STABILITY.md.
Does it send any data home? No telemetry. The only routine outbound call is an anonymous update check for a signed file, which you can switch off with HATAMOTO_UPDATES=off .
旗本
See who reads your site, without a plugin stack.
Open source and one Go binary. AI analytics start counting from the first request.
Get started
 View on GitHub
© 2026 Hatamoto · Stand close. Serve well.
 Security Privacy Changelog

## 评论（9/9）

> **sammatilda** · 2026-10-27T10:00:09.000Z　
> Built in golang and Postgres. Looks pretty. I will give it a try. Does it need a lot of memory considering the caching is in memory ?

---

> **rajeev1123** · 2026-10-27T10:03:46.000Z　
> How is it checking the bots ? Is it doing reverse dns lookups ?

---

> **teslazen** · 2026-10-27T10:11:10.000Z　
> Hi HN, I have built Hatamoto using just Golang and HTMX. No node or compilation is necessary. Plugins are in WebAssembly , have their own schema on postgres and only have access to what you grant. Its very lightweight and very secure CMS. It has built in internal linking, redirects, theme amnd plugins platform, forms, SEO , tiptap editor support and so on..

---

> **romania1** · 2026-10-27T10:17:10.000Z　
> Visually it is stunning. Having your plugins not have access to entire database is amazing. But there are just two listed plugins and only one theme ? Congrats on the launch though.

---

> **teslazen** · 2026-10-27T10:07:57.000Z　
> For now only supports cache in memory and preloading. For close to 1K pages uses less than 5% VCPU and about 600 MB in memory cache. You should be able to run most business sites on a $5 cpu.

---

> **teslazen** · 2026-10-27T10:09:10.000Z　
> IP ranges and reverse DNS for nine operators.

---

> **nether1** · 2026-10-27T10:26:54.000Z　
> Apache 2.0

---

> **romania1** · 2026-10-27T10:16:10.000Z　
> Are the IP ranges published for example ChatGPT just stopped sending UTM parameters.

---

> **germanrabbit** · 2026-10-27T11:17:09.000Z　
> No, I think it is best guess

## 关联链接

- https://github.com/Zen-Labs-Corp/hatamoto
- https://new…
- https://schema.org
- https://your-site.com
- https://your-site.com/#organization
- https://your-site.com/api/v1/public/knowledge-graph?schema=service
- https://your-site.com/mcp
- https://your-site.com/services/emergency-plumbing

## 导航

- 项目页：[[10-项目/hatamoto.dev_43c0b2e4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
