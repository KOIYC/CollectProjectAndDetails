---
type: "corpus"
item_id: "6e0a8eb9835608f5"
title: "Show HN: Viaduct – C4 models that coding agents can read and update"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49790729"
project_url: "https://c4.quietgridlabs.com/"
author: "igrlgkv"
published_at: "2026-09-21T17:50:35Z"
captured_at: "2026-09-22T12:53:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_igrlgkv
  - story_49790729
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Viaduct – C4 models that coding agents can read and update

> [!info] 一句话导读
> Integrations Docs Sign up Log in

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49790729>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：igrlgkv　|　发布：2026-09-21T17:50:35Z
> 项目链接：<https://c4.quietgridlabs.com/>
> 采集：2026-09-22T12:53:31+08:00　|　id：`6e0a8eb9835608f5`

## 正文

V I A D U C T
by Quiet Grid Labs
Viaduct
 Integrations Docs Sign up Log in
 Sign up
 See the whole system.
 Model every level of your architecture in one connected place — for the people who build it and the agents that work with it.
 Quick start Log in
 Quick start opens the editor right here in your browser, with no account and nothing sent anywhere. Export the model whenever you want.
Four levels, one model
 Open a system to see its containers, a container to see its components. Every level is a view of the same model, so a rename or a new dependency shows up everywhere it belongs.
The technology picks the colour
 Pick a technology and the element takes its colour and logo. Datastores are drawn as cylinders, people as actors — so a diagram is scannable before anyone reads a label.
Docs, diagrams and schemas live on the element
 Documentation Sequence diagrams ER schema & API
 Every element carries its own Markdown pages — a design note on a service, a runbook on a worker, an ADR on a system. Write in the editor with a live preview, insert a stored sequence diagram or an API endpoint as a block, and the page keeps rendering the current version instead of a screenshot that rotted last quarter.
What teams say once the model is theirs
 The tool earns its place when the diagram stops being a screenshot someone has to remember to update.
I built Viaduct because I kept redrawing the same diagram to answer the same question. Now the model answers it, and my agent reads it too.
Igor Golovko
 Founder, Quiet Grid Labs
The C4 levels finally match how we actually talk about the system. Drilling from context into containers takes one click instead of three diagrams.
Marta Kowalczyk
 Backend lead, fintech
Our architecture diagram used to be a screenshot in Confluence, six months stale. Now it is the thing we open during incident review.
Daniel Osei
 SRE, marketplace platform
The MCP server is the part that sold the team. Cursor answers questions about our services without anyone pasting a diagram into the chat.
Priya Raghunathan
 Staff engineer, logistics
I built Viaduct because I kept redrawing the same diagram to answer the same question. Now the model answers it, and my agent reads it too.
Igor Golovko
 Founder, Quiet Grid Labs
The C4 levels finally match how we actually talk about the system. Drilling from context into containers takes one click instead of three diagrams.
Marta Kowalczyk
 Backend lead, fintech
Our architecture diagram used to be a screenshot in Confluence, six months stale. Now it is the thing we open during incident review.
Daniel Osei
 SRE, marketplace platform
The MCP server is the part that sold the team. Cursor answers questions about our services without anyone pasting a diagram into the chat.
Priya Raghunathan
 Staff engineer, logistics
Change sets let us review an architecture change the way we review code. The diff is the conversation.
Tomas Lindqvist
 Head of platform, SaaS
Sequence diagrams next to the model, not in a separate tool that nobody updates. That alone saved us the weekly sync.
Elena Duarte
 Tech lead, healthtech
We imported an OpenAPI spec and had the endpoints on the container in a minute. No one had to draw a box by hand.
Ahmed Barakat
 Integration engineer, telecom
New joiners read the model on day one and ask better questions on day two.
Hannah Brecht
 Engineering manager, e-commerce
Change sets let us review an architecture change the way we review code. The diff is the conversation.
Tomas Lindqvist
 Head of platform, SaaS
Sequence diagrams next to the model, not in a separate tool that nobody updates. That alone saved us the weekly sync.
Elena Duarte
 Tech lead, healthtech
We imported an OpenAPI spec and had the endpoints on the container in a minute. No one had to draw a box by hand.
Ahmed Barakat
 Integration engineer, telecom
New joiners read the model on day one and ask better questions on day two.
Hannah Brecht
 Engineering manager, e-commerce
A request, played back across the canvas
 A Magic flow is an ordered walk through the model: each step names a hop, the elements it goes from and to, and the connection it uses. Steps that happen at the same time share a stage, so a fan-out reads as a fan-out.
 Build a flow from the elements you already modelled — no second diagram to maintain.
 Play it on the canvas: everything dims except the current hop, and the camera follows the request.
 Generate a sequence diagram from the flow, and attach the docs and diagrams that explain each step.
Playing “Payment leaves the bank”, step by step.
Endpoints are stored as OpenAPI
 Describe an endpoint in the editor — typed parameters, request body, a card per status — and the container holds the OpenAPI document for the whole service. Import a spec to fill the canvas from it; export it back as a file.
{
 "openapi" : "3.1.0" ,
 "info" : { "title" : "Accounts API" , "version" : "1.4.0" } ,
 "paths" : {
 "/api/accounts/{id}" : {
 "get" : {
 "operationId" : "getAccount" ,
 "summary" : "Get account" ,
 "parameters" : [
 { "name" : "id" , "in" : "path" , "required" : true ,
 "schema" : { "type" : "string" } , "example" : "acc_42" }
 ] ,
 "responses" : {
 "200" : { "description" : "OK" , "content" : { "application/json" : {
 "example" : { "id" : "acc_42" , "currency" : "EUR" } } } } ,
 "404" : { "description" : "No account with that id" }
 }
 }
 }
 }
 } This is accounts-api-openapi.json, exported from one container.
One server, one token, the whole architecture
 Cursor, Claude Code, Claude Desktop and any other MCP client can read the architecture straight from Viaduct: systems and services, API endpoints with their contracts, WebSocket channels, documentation and sequence diagrams. One hosted MCP server, one personal token, no repository to clone.
 Your agent answers “what talks to what, and over which contract?” from the model instead of guessing from the codebase.
 It can write back too — new services, endpoints, connections and docs land in the same model your team reads.
 Hand it a change set: a piece of work pinned to a fixed version, with the constraints and acceptance criteria it has to prove.
 How the MCP server and change sets work
Work an agent can finish, and you can verify
 A change set is scoped to one pinned version, so nothing shifts under the agent while it builds. It reports each finished piece with the criterion it proves and the commit that proves it — the status moves itself from draft to done, live on your screen.
 What a change set looks like once the agent has reported on it
 done Expose account limits on GET /api/accounts/{id} AC-1 proven · commit 4f1c9e2
 done Ledger publishes payment.settled to the Notifier channel AC-2 proven · commit b83d07a
 draft Retire the Legacy Billing endpoint AC-3 open · pinned to v14
Your designers already use Figma. Now the model does.
 Connect a Figma account in settings and the frames your interface is drawn in become part of the architecture: components point at real nodes, and the values they are allowed to use are read from the file rather than retyped. Nothing is written back, and no picture is copied here.
It tells you when the design moved
 Work is pinned to the file as it was. When somebody edits the frame afterwards, the change set says which components are now behind — instead of that turning up in review.
One palette, not forty hexes
 The colours, spacing and type in the file come in by name. A component may use those, and a value that is not among them is flagged rather than quietly shipped.
Your coding agent gets it too
 Everything here rides along in what an agent reads over MCP — the frame, its states, the palette. It builds the loading and error states because they were written down, not because someone remembered.
The boring half of documenting, done for you
 Not every team keeps an agent of their own, and the parts of a model that go undocumented are the dull ones: descriptions nobody wrote, flow steps still called "Step 4". Viaduct's built-in assistant writes those. It is in the editor, it needs no key and no setup, and it never changes your model on its own — every suggestion is shown, and applying it is a button you press.
 A description for any element that lacks one — one at a time, or every blank in a system at once.
 A review of the whole model: what is undescribed, what nothing talks to, what looks like the same job done twice. Every finding names a real element, and clicking it takes you there.
 Names for the steps of a Magic flow that nobody got round to naming — written into the draft, so saving is accepting.
 Included with an account, with a monthly allowance per person. Guests draw; the assistant needs a sign-in.
What a model review comes back with
 High Order Service No description — nothing says what it is responsible for, and three services depend on it.
 Medium Notification Worker Nothing connects to it and it connects to nothing; either the flow is missing or the service is.
 Low Legacy Billing Appears to do the same job as Billing Service — one of the two is probably the old one.
Your architecture, on terms you can check
 An architecture model is a map of everything you run, which makes “where does it live?” the first fair question about a tool like this. Three answers, all of them verifiable.
It stays where you put it
 Without an account the model never leaves your browser. With one it lives on servers in the Netherlands, inside the EU, and so do the backups.
You can take it with you
 The whole model exports as JSON, and a container’s endpoints as an OpenAPI document — any time, without asking us. Nothing here is a one-way door.
The agent gets in only if you let it
 MCP access needs a personal token you issue yourself, scoped to your projects. Revoke it and the access ends that moment.
Read the privacy policy
Answered before you have to ask
 What does it cost?
 Nothing. Viaduct is free — every level, the MCP server, collaboration and change sets included. There is no trial that ends and no feature held back behind a plan. If you want the work to continue you can donate, and that buys nothing but the work continuing.
What is the AI assistant, and what does it cost me?
 It writes the parts of a model people leave blank: descriptions for elements that have none, names for unnamed flow steps, and a review of the whole model that points at real elements rather than giving generic advice. It runs on our provider, so there is no key to obtain and nothing to configure, and every account gets a monthly allowance of it. Nothing it suggests is applied on its own — you see the text and press a button, or you do not.
Do I need an account?
 Not to draw. The editor opens with a sample model and works entirely in your browser, where the model stays on your machine and never reaches our servers. An account is for the things a browser cannot do alone: keeping a project across devices, sharing it with your team, and serving it over MCP.
Where does my architecture live?
 On servers inside the EU, along with the backups. Without an account it lives in your browser and nowhere else. Either way you can export the whole model as JSON, and any container’s contracts as an OpenAPI document, whenever you like.
What can an AI agent do with it?
 Read the model and write to it: Cursor, Claude Code, Claude Desktop or any other MCP client can ask what talks to what and over which contract, and can add services, endpoints, connections and documentation back. Access needs a personal token you issue yourself, scoped to your projects, and revoking it ends the access immediately.
How is this different from a diagramming tool?
 A diagram is a picture; this is a model. An element exists once and appears on every level it belongs to, so a rename or a new dependency shows up everywhere at once. The endpoints on a container are a real OpenAPI document, not labels on a box — which is what makes the whole thing readable by something other than a person.
Can I bring what I already have?
 Import an OpenAPI specification and the endpoints land on the container with their parameters, request bodies and responses. Models export and import as JSON, so moving a workspace — or keeping a copy outside this service — is a file.
The sample model is already loaded
 Open the editor and an Internet Banking system is waiting, modelled across every level, with docs, flows and contracts attached. Clear it when you want to start your own.
Quick start Log in
Viaduct
A C4 modelling tool with a hosted MCP server, so your architecture is readable by your team and by the tools they code with.
Product
 Open the editor Documentation Sign up
 Company
 Support/Feedback support@quietgridlabs.com
 Legal
 Terms of Service Privacy Policy
© 2026 Quiet Grid Labs. All rights reserved. Terms of Service Privacy Policy

## 导航

- 项目页：[[10-项目/c4.quietgridlabs.com_04952ed8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
