---
type: "corpus"
item_id: "58266466ba00ab4d"
title: "Show HN: Send your first Peppol e-invoice in 5 minutes (EU mandate live)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47951671"
project_url: "https://getpeppr.dev/"
author: "zerolooplabs"
published_at: "2026-04-29T17:36:32Z"
captured_at: "2026-09-21T02:52:35+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_zerolooplabs
  - story_47951671
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: Send your first Peppol e-invoice in 5 minutes (EU mandate live)

> [!info] 一句话导读
> Skip to content getpeppr Features Pricing Lookup Documentation News API Reference Compliance

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47951671>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：zerolooplabs　|　发布：2026-04-29T17:36:32Z
> 项目链接：<https://getpeppr.dev/>
> 采集：2026-09-21T02:52:35+08:00　|　id：`58266466ba00ab4d`

## 正文

Skip to content getpeppr Features Pricing Lookup Documentation News API Reference Compliance
 Get Started
 Features Pricing Lookup Documentation News API Reference Compliance Get Started
Belgium live · France mandatory since 1 Sept 2026 — read the guide → Peppol infrastructure for SaaS platforms
 Regulation moves. Your code shouldn't have to. One integration puts supported customers on Peppol — and keeps them compliant as each mandate lands.
 Your customers invoice through one TypeScript SDK and one master API key. We absorb spec changes, country quirks and new mandates — so you never ship a migration to stay compliant.
 Get an API key Try the free lookup View Platform Docs
 $ npx @getpeppr/cli validate invoice.json $ npm install @getpeppr/sdk Try with npx first — no signup, no API key. Or check a receiver in the free Peppol lookup . Install the SDK when you're ready to send.
 SDK v5.8.0 · CLI v0.12.3 · latest on npm
send-invoice.ts
 import { Peppol } from "@getpeppr/sdk" ;
const peppol = new Peppol ({ apiKey: "sk_sandbox_master_..." });
const invoice = await peppol.invoices. send ({
 sender: { externalSubTenantId: "customer_8412" },
 number: "INV-2026-001" ,
 to: {
 name: "SPF Economie (test receiver)" ,
 peppolId: "9925:BE0314595348" ,
 street: "Rue du Progrès 50" ,
 city: "Brussels" ,
 postalCode: "1210" ,
 country: "BE" ,
 },
 lines: [
 { description: "Consultation" , quantity: 1 ,
 unitPrice: 90 , vatRate: 0 , vatCategory: "O" ,
 taxExemptReason: "Integration test" },
 ],
 });
console. log (invoice.status); // "submitted"
Coverage today
 Invoice from nine countries today
 Peppol is one network, but every country decides how a company proves who it is. Where we can check that automatically, you sign up and send. Where we can't, we do it with you.
Self-serve · six countries 🇫🇷 France
 🇧🇪 Belgium
 🇮🇪 Ireland
 🇳🇱 Netherlands
 🇩🇰 Denmark
 🇸🇪 Sweden
 Sign up and send on your own. We check your declared Peppol identifier automatically through the relevant verification source. No call with us and no manual approval on our side — you set yourself up from the console.
Assisted · three countries 🇩🇪 Germany
 🇳🇴 Norway
 🇬🇧 United Kingdom
 We complete the checks with you and read your first invoice before it goes out.
See where you can invoice from
 Legal mandates
 🇧🇪 Belgium
Live
 B2B mandate since 1 Jan 2026
 Structured invoices via Peppol BIS for Belgian VAT-taxable B2B.
🇩🇪 Germany
Receive live
 since 1 Jan 2025
 Issuing obligations phase in after transitional periods.
🇫🇷 France
Receive mandate live
 since 1 Sept 2026
 All receive since 1 Sept 2026; large and mid-sized businesses issue since then, SMEs follow on 1 Sept 2027.
Regulatory coverage
 Mandate-ready by design
 getpeppr is built on Storecove, a certified Peppol Access Point across the EU. BIS 3.0 revisions, country CIUS layers and network changes ship through that integration — your JSON contract stays exactly the same.
Certified Access Point backbone
 Storecove is a certified Peppol Access Point connected to the EU Peppol network. BIS 3.0 updates, format revisions, and new country onboardings flow through that integration before reaching your code.
Country layer, shipped per mandate
 When a new EU mandate lands, getpeppr ships the country-specific layer — identifier schemes, validation rules, CIUS extensions. Your JSON contract stays exactly the same.
Roadmap aligned with EU regulation
 BIS 3.0 today. Country CIUS as mandates land. ViDA Digital Reporting Requirements for cross-border B2B by 1 July 2030 — same SDK, same contract, same JSON.
Get a sandbox API key Not sure if a company can receive Peppol invoices? Look up any Peppol participant — free, no signup.
Stop wrestling with XML
 The typical Peppol integration takes 3-5 weeks of reading documentation. Ours takes minutes.
Before — Raw Peppol
 01 Read 47-page "quick start" guide
02 Understand UBL 2.1 XML schema (150+ elements)
03 Learn AS4 protocol for message delivery
04 Handle BIS 3.0 validation rules that contradict each other
05 Build 150+ lines of XML by hand per invoice
06 Contact sales for sandbox access
3-5 weeks before first invoice
After — getpeppr SDK
 01 npm install @getpeppr/sdk
02 Write JSON — we generate compliant UBL XML
03 Full TypeScript types with autocomplete
04 Actionable validation errors with fix suggestions
05 Instant self-service sandbox with API keys
06 Done. Ship it.
Minutes to first invoice
Built for platforms
 One platform account. N legal entities underneath it.
 Your customers each keep their own Peppol identity. Your team keeps one integration. getpeppr models that directly: provision a customer, capture authorisation, send on their behalf, and listen for lifecycle webhooks.
 No XML in your product, no access-point operations in your backlog, and no per-customer onboarding loop rebuilt from scratch.
 Read the Peppol API integration guide
 Your SaaS platform
 One master API key
Customer A
 Own Peppol identity
Customer B
 Own authorisation
Customer C
 Own lifecycle status
getpeppr
 Verification, UBL/BIS 3.0, Peppol delivery, webhooks
Try before you buy
 Try Peppol locally. No signup, no API key.
 Validate, look up receivers, and convert UBL invoices from your terminal. Sign up only when you're ready to send through the Peppol network.
 terminal
 $ npx @getpeppr/cli validate invoice.json
Need to check a receiver first? npx @getpeppr/cli lookup 0208:0685660237 Use the browser lookup →
 validate · BIS 3.0 offline
 init · scaffold a starter
 lookup · receiver directory
Read the CLI docs →
15,000+ tests passing
 TypeScript Native
 Minutes to first invoice
 Built on Peppol BIS 3.0
Code that speaks for itself
 Every operation is a single, intuitive method call. Full TypeScript autocomplete. No XML, no SOAP, no pain.
Send Invoice Validate Credit Note Webhooks CLI
send.ts
 import { Peppol } from "@getpeppr/sdk" ;
const peppol = new Peppol ({ apiKey: "sk_sandbox_..." });
 const identity = await peppol.identity. get ();
 if (identity.sandboxFirstSend?.status !== "ready" ) throw new Error (identity.sandboxFirstSend?.message);
const result = await peppol.invoices. send ({
 number: "INV-2026-042" ,
 // Sandbox delivers only to test recipients — in production,
 // use your customer's Peppol ID.
 to: {
 name: "SPF Economie (test receiver)" ,
 peppolId: "9925:BE0314595348" ,
 street: "Rue du Progrès 50" ,
 city: "Brussels" ,
 postalCode: "1210" ,
 country: "BE" ,
 },
 lines: [
 { description: "Consulting Q1" , quantity: 40 , unitPrice: 125 , ... identity.sandboxFirstSend.line },
 { description: "Travel expenses" , quantity: 1 , unitPrice: 350 , ... identity.sandboxFirstSend.line },
 ],
 paymentTerms: "Net 30 days" ,
 paymentIban: "BE68539007547034" ,
 });
console. log ( `Sent! ID: ${ result . id }` );
Everything you need to ship Peppol invoices
 Built by developers who spent weeks reading Peppol docs so you don't have to.
Built country by country
 Self-serve in France, Belgium, Ireland, the Netherlands, Denmark and Sweden, and we onboard you personally in three more countries. One API — the country-specific rules are ours to carry, not yours.
Built-in Validation
 Pre-send validation catches errors before they hit the network. Human-readable messages with fix suggestions, not cryptic Peppol rule IDs.
TypeScript Native
 Full type safety from invoice creation to webhook handling. Autocomplete every field. Catch errors at compile time, not runtime.
BIS 3.0 Tooling
 Peppol BIS 3.0 tooling out of the box. Generate invoices and credit notes, include allowances and attachments, and track Peppol delivery.
Real-time Webhooks
 Get notified when invoices are sent, accepted, or refused — pushed as each status lands, retried if your endpoint is down. No polling. Event-driven architecture like Stripe.
Zero XML
 Send JSON, we generate compliant UBL XML. Your developers will never see an angle bracket. That's a promise.
Peppol API comparison
 Five providers compared on tenant model, tooling, pricing, onboarding, and market focus. The source-checked guide explains where each one fits.
Provider SDKs Pricing Countries Self-Service Evaluation path
 getpeppr You are here TypeScript + CLI Business from EUR 49/mo + usage; Platform: one plan at EUR 99/mo + usage, 50 Legal Entities included, no per-customer minimum Belgium + France + Ireland + Netherlands + Denmark + Sweden self-serve · French regulated CTC in pilot · 3 more assisted Sandbox self-serve; Platform production contract-gated Free sandbox + offline CLI
 peppol.sh REST/OpenAPI + code samples; TypeScript SDK published on npm (0.1.0), Python and PHP announced as coming soon Personal EUR 0.20/document; Connect EUR 0.16→0.10 (EUR 250 top-up) Developer- and agent-first Peppol Yes (API-created sandbox) Instant API-created sandbox
 e-invoice.be 5 languages (TS, Python, PHP, Ruby, Java) + MCP From EUR 0.25/invoice; Enterprise from EUR 0.18 Belgian certified AP; claims 30+ reachable countries Yes Free sandbox, no sales call
 Storecove RESTful JSON API + OpenAPI/Swagger Quote required 31-country compliance; Peppol + DBNAlliance 30-day test account by request Requested 30-day sandbox
 Basware Network REST API + XML integrations Subscription; contact Basware Global network Support-provisioned test account Testing account via Basware Support
getpeppr You are here
 SDKs: TypeScript + CLI
 Pricing: Business from EUR 49/mo + usage; Platform: one plan at EUR 99/mo + usage, 50 Legal Entities included, no per-customer minimum
 Countries: Belgium + France + Ireland + Netherlands + Denmark + Sweden self-serve · French regulated CTC in pilot · 3 more assisted
 Self-Service: Sandbox self-serve; Platform production contract-gated
 Evaluation path: Free sandbox + offline CLI
peppol.sh
 SDKs: REST/OpenAPI + code samples; TypeScript SDK published on npm (0.1.0), Python and PHP announced as coming soon
 Pricing: Personal EUR 0.20/document; Connect EUR 0.16→0.10 (EUR 250 top-up)
 Countries: Developer- and agent-first Peppol
 Self-Service: Yes (API-created sandbox)
 Evaluation path: Instant API-created sandbox
e-invoice.be
 SDKs: 5 languages (TS, Python, PHP, Ruby, Java) + MCP
 Pricing: From EUR 0.25/invoice; Enterprise from EUR 0.18
 Countries: Belgian certified AP; claims 30+ reachable countries
 Self-Service: Yes
 Evaluation path: Free sandbox, no sales call
Storecove
 SDKs: RESTful JSON API + OpenAPI/Swagger
 Pricing: Quote required
 Countries: 31-country compliance; Peppol + DBNAlliance
 Self-Service: 30-day test account by request
 Evaluation path: Requested 30-day sandbox
Basware
 SDKs: Network REST API + XML integrations
 Pricing: Subscription; contact Basware
 Countries: Global network
 Self-Service: Support-provisioned test account
 Evaluation path: Testing account via Basware Support
See the full Peppol API comparison →
Simple, transparent pricing
 Start free. Send your first invoice in minutes. Scale without surprises.
 Business plans run from a free sandbox to EUR 399/month. The Platform plan lets SaaS products send and receive on behalf of their customer companies, with 50 companies included and no per-customer minimum.
Businesses SaaS platforms
 For companies sending their own Peppol invoices.
 Sandbox
 Free /forever
 Test everything. No credit card required.
 Unlimited test documents
 Full SDK access
 Sandbox environment
 Validation API
 Documentation & guides
 Start Building No credit card. No time limit.
Starter
 EUR 49 /mo
 For developers and early-stage SaaS.
 100 docs/mo +EUR 0.25/doc
 100 documents included (sent + received)
 Live Peppol delivery
 Webhooks & events
 Email support (< 24h)
 Management dashboard
 Up to 3 team members
 Get Started
Most Popular
 Pro
 EUR 149 /mo
 For growing businesses.
 800 docs/mo +EUR 0.22/doc
 800 documents included (sent + received)
 Live Peppol delivery
 Webhooks & events
 Management dashboard
 Email support (< 24h)
 Up to 10 team members
 Get Started
Business
 EUR 399 /mo
 For high-volume document exchange.
 2,000 docs/mo +EUR 0.20/doc
 2,000 documents included (sent + received)
 Live Peppol delivery
 Webhooks & events
 Management dashboard
 Priority email support
 Up to 25 team members
 Get Started
For SaaS products that send and receive Peppol documents on behalf of their customer companies.
 One contract, one bill for the whole platform. Your customers never pay us.
One plan for every platform
 Platform
 EUR 99 /mo
 Everything a multi-tenant product needs to put its customers on Peppol, priced by what they actually exchange.
 50 Legal Entities included +EUR 0.25/doc
 Send and receive for every customer company under one contract
 EUR 0.25 per production document, sent or received
 No per-customer fee for your first 50 companies, no setup fee, no per-customer minimum: a customer that sends two invoices costs you two documents
 50 customer Legal Entities included, then EUR 1 per registered Legal Entity per month. Deregister a customer you no longer serve and it stops counting
 One central bill for the whole platform, never one per customer. Usage is charged when it reaches EUR 50
 Identity verification of your customer companies, DPA and platform agreement included
 Free sandbox with unlimited test documents and up to 10 test customer companies, before and after you go live
 Try the sandbox Free and self-serve, no agreement. Production after a signed platform agreement and DPA.
Estimate your monthly bill
 Two numbers are enough. Move the sliders or type your own.
 Registered customer companies
Documents per company per month (sent + received, on average)
EUR 399.00 /mo
 Platform EUR 99.00
 600 documents × EUR 0.25 EUR 150.00
 150 Legal Entities beyond the 50 included × EUR 1 EUR 150.00
 That is EUR 2.00 per customer per month, EUR 0.67 per document all-in.
Estimate in EUR, excluding VAT. Plan: EUR 99/mo, EUR 0.25/doc, 50 Legal Entities included, EUR 1 per extra Legal Entity.
What counts as a document Any business document (invoice, credit note or other) that reaches the Peppol network for one of your customers, sent or received, in production. Sandbox traffic is never billed, and neither is a document refused at submission.
What counts as a Legal Entity One customer company registered with your platform in production. It counts while it is registered, because our access point reserves its place from the moment you create it, whether or not it transacts yet.
Beyond 50 customer companies Nothing changes in the formula. Each registered company beyond the 50th adds EUR 1 a month, and that is all. Above 2,000 documents a month, talk to us about a committed rate.
Tell us about your platform: how many customer companies, roughly how many documents each, and which countries.
 Email hello@getpeppr.dev and we will reply with the platform agreement + DPA path.
 Email us
All prices in EUR, excluding VAT. Business plans have no setup fees. Platform production access is contract-gated. Usage counts documents both sent and received.
Frequently asked questions
 Which countries can I send invoices to? Any participant on the Peppol network, wherever it is registered — that part does not depend on where you are. What does depend on your country is where you can invoice FROM. We check your declared Peppol identifier automatically through the relevant verification source. You are self-serve in France, Belgium, Ireland, the Netherlands, Denmark and Sweden today, and we onboard you personally in Germany, Norway and the United Kingdom. The coverage page at getpeppr.dev/countries has the full list.
 Is the sandbox really free? Yes. Free forever, unlimited test documents, no credit card required. When you're ready to go live, plans start at EUR 49/month.
 Do I need to understand Peppol or UBL? No. Send JSON, we handle the UBL XML generation, BIS 3.0 compliance, and Peppol network delivery. Zero XML knowledge required.
 Is getpeppr production-ready? Yes. We run on Storecove's certified Peppol Access Point and production sending is enabled. Our SDK and gateway carry 15,000+ automated tests and are built for Peppol BIS 3.0.
 What is the SaaS Platform plan for? It is for SaaS products that send and receive Peppol documents on behalf of many customer companies. Each customer company you register for production counts as one Legal Entity. There is one Platform plan: EUR 99 a month plus EUR 0.25 per document, with 50 Legal Entities included, then EUR 1 per registered Legal Entity per month beyond them. There is no per-customer minimum and no setup fee.
 Can SaaS platforms go live self-serve? Sandbox is free, needs no agreement and is self-serve: an organisation admin chooses “A platform for my customers” at signup, or starts the platform sandbox trial later from the console overview, then creates the sandbox master key in the console. Production platform access is contract-gated — we enable it after a signed platform agreement and DPA, so responsibilities, the entity count you are billed on, and data processing terms are clear before live customer sending.
 How is platform usage billed? One central bill for the whole platform, never one per customer: the EUR 99 platform fee, EUR 0.25 per document sent or received in production, and EUR 1 per month for each registered customer Legal Entity beyond the 50 included. Accrued usage is charged when it reaches EUR 50, so small volumes never produce noisy micro-charges. There is no per-customer setup fee and no per-customer minimum. Sandbox is free, self-serve and needs no agreement.
 How does getpeppr compare to building with raw Peppol? A typical Peppol integration takes 3–5 weeks: reading UBL 2.1 specs, implementing XML generation, handling AS4 protocol, and managing BIS 3.0 validation rules. With getpeppr, you send JSON and we handle everything. Most developers send their first test invoice in minutes, not weeks.
Roadmap
 v1.1 Live
 TypeScript SDK, webhooks, CLI (send + validate + scaffold + lookup), sandbox + production sending
v1.2 Coming next
 France CTC pilot for the French mandate (in force since 1 Sept 2026)
v2.0 On the roadmap
 More national rule cartridges
Ready to ship Peppol invoices?
 Validate locally or create a free sandbox. No credit card, full SDK access.
 Start Free View Documentation
 $ npm install @getpeppr/sdk
 Free sandbox forever. No credit card required. Production access follows the plan you choose.
Get the EU e-Invoicing Mandate Tracker
 A digest for devs building on Peppol, sent when a mandate moves.
 Subscribe →
 getpeppr
 The developer‑first SDK for EU e‑invoicing. Peppol invoices from a JSON object.
Product
 Features
 Pricing
 Documentation
 API Reference
 Compare
 Best Peppol API
 Field Service & ERP
 Peppol Lookup
 What's New
Compliance
 EU Mandates
 Belgium
 France (Sep 2026)
 Germany (receiving live)
Connect
 GitHub
 Sign Up
 Contact
 System Status
© 2026 Zero Loop Labs Ltd. Made for developers who hate XML.
 Privacy Policy · Terms of Service · Peppol is a registered trademark of OpenPeppol AISBL.
Zero Loop Labs Ltd · Company No. 17035492 · Registered in England & Wales
 End-users are responsible for the content and compliance of exchanged documents. Powered by Storecove , a certified Peppol Access Point.

## 评论（2/2）

> **nawi** · 2026-04-30T05:24:01.000Z　
> many thx for sharing, will you support US as well in the coming months?

---

> **zerolooplabs** · 2026-04-30T06:59:46.000Z　
> No signup needed to try it, just run: npx @getpeppr/cli validate invoice.json

## 导航

- 项目页：[[10-项目/getpeppr.dev_1852a59a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
