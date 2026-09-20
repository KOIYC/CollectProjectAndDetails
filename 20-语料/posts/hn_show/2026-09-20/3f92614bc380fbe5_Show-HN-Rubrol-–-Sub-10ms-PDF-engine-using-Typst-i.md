---
type: "corpus"
item_id: "3f92614bc380fbe5"
title: "Show HN: Rubrol – Sub-10ms PDF engine using Typst instead of Headless Chrome"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49770890"
project_url: "https://rubrol.com/"
author: "halfradaition"
published_at: "2026-09-19T23:08:24Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_halfradaition
  - story_49770890
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Rubrol – Sub-10ms PDF engine using Typst instead of Headless Chrome

> [!info] 一句话导读
> Author: Max Comperatore

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49770890>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：halfradaition　|　发布：2026-09-19T23:08:24Z
> 项目链接：<https://rubrol.com/>
> 采集：2026-09-20T09:48:16+08:00　|　id：`3f92614bc380fbe5`

## 正文

Author: Max Comperatore

Rubrol - Fast PDF Engine | Puppeteer, Headless Chrome & Gotenberg Alternative

# Turn Document Infrastructure Into Instantaneous Precision.

 The sub-millisecond document engine replacing Headless Chrome, Puppeteer, and Gotenberg. Compile pixel-perfect SaaS billing invoices, reports, statements, and receipts in <6ms on 96% less compute. Includes turnkey EU Factur-X / ZUGFeRD compliance out of the box.

● 5.8ms Mean Compile

● < 28MB Resident Memory

● Native PDF/A Archival (2b/3b)

● Zero V8 Virtualization

AI Assistant Skills & Rules

### Use AI to integrate Rubrol

 If you use an AI coding assistant like Claude Code, Cursor, or GitHub Copilot, you can add sub-millisecond PDF generation to your app in minutes using agent skills.

 $ npx skills add maxcomperatore/rubrol --skill rubrol

Once installed, prompt your AI coding assistant with instructions like:

 “Add Rubrol PDF invoice generation to my Express backend with sub-millisecond latency”

## Live Interactive Compilation Studio

 Edit live JSON variables on the left. Watch the local Rubrol engine recompile vector SVG in real time. Download certified ISO 19005-3 PDF/A-3b & ISO 19005-2 PDF/A-2b binaries instantly.

## Turn compute waste into raw competitive advantage.

 Legacy document generation relies on headless browser virtualization. Spawning Chrome or Gotenberg instances requires 250MB resident memory per worker, unpredictable GC pauses, and 2,000ms+ render latencies. Rubrol embeds a native vector layout engine directly into your process or sidecar, compiling production PDFs in under 6 milliseconds with absolute mathematical determinism.

### The Chromium Bottleneck

 Every invoice generated via Puppeteer spins up a full WebKit/Blink layout engine, executing JavaScript, evaluating CSS cascades, and allocating huge DOM node trees before rasterizing to print media.

- 250MB - 400MB RAM per concurrent worker
- 1,800ms - 3,500ms p95 cold start latency
- Frequent out-of-memory container crashes under batch loads
- Non-deterministic line breaking across Linux distributions

### The Rubrol Architecture

 Rubrol compiles structured documents into native vector PDF/A-3b, PDF/A-2b, and SVG. Zero browser overhead, zero Node.js bridging, and native ISO 19005-3 & ISO 19005-2 compliance built directly into the binary.

| Vector Spec | Chromium / Puppeteer | Rubrol Sidecar |
| --- | --- | --- |
| Compile Latency | 2,400ms | 5.8ms |
| Memory Footprint | 250MB | 24MB |
| Max Concurrency | 40 req/s | 1,200 req/s |
| PDF/A-3b & Factur-X (ISO 19005-3) | Requires 3rd party CLI | Native Zero-Copy |

● LIVE PIPELINE TELEMETRY 10,000 DOCS / MIN

 INV-2026-9041 Acme Corp SaaS PDF/A-3b EN 16931 5.2ms

 REC-2026-8819 Stripe Checkout PDF/A-2b ARCHIVAL 4.8ms

 SOC-2026-4402 Enterprise Audit SHA-256 SIGNED 6.1ms

 MED-2026-1104 Clinical Record HIPAA SECURE 5.4ms

## See the operational impact of every document run.

 When processing 200,000 monthly invoices, running headless browser clusters drains tens of thousands of dollars in AWS Fargate and CPU allocations. By reducing compute times by 96% and shrinking RAM from 250MB to 24MB, Rubrol amortizes its cost within days.

### "We retired our 16-node Chromium Puppeteer cluster and replaced it with a single Rubrol sidecar container."

 During high-volume month-end billing cycles, generating 300,000 corporate invoice runs regularly caused V8 memory leaks and pod evictions. Rubrol lowered our 99th-percentile response time from 2,400ms to 5.8ms while reducing compute overhead by over \$180,000 annually.

 2,400ms to 5.8ms p99 Latency Drop (413× Faster) \$180,000 / yr AWS Fargate Compute Eliminated 0 Evictions Zero OOM Container Restarts

96%† COMPUTE REDUCTION ACROSS CLUSTER

> Rubrol replaced our 16-pod Chromium cluster with a single sidecar. Our p99 latency dropped from 2,400ms to 5.8ms while completely eliminating out-of-memory container restarts during end-of-month billing cycles.

 Staff Infrastructure Engineer - Global B2B FinTech Platform VERIFIED DEPLOYMENT

5.8ms Average document compilation latency on single vCPU

< 28MB Resident memory consumption per container instance

100% EN 16931 & ISO 19005-3 PDF/A-3b compliance validation

## Point, Click, & Connect.

 Deploy as a microsecond sidecar in Kubernetes, run serverless via Docker, or link natively into Python, Node, Go, and Rust via REST or Unix sockets.

 Docker ghcr.io image

 Kubernetes Micro-Sidecar

 Python FastAPI Async

RUBROL ENGINE

 Node.js TypeScript SDK

 Go gRPC / HTTP/2

 Rust Native FFI

#### Sub-Millisecond Sidecar

Runs alongside your application containers with zero external database or Redis dependency. Pure in-memory compilation.

#### Embedded Factur-X & CII

Automatically packages syntactically validated Cross-Industry Invoice XML directly into the PDF/A-3b catalog stream.

#### Mathematical Determinism

The layout engine guarantees identical pixel-level layout and kerning across any architecture or cloud provider.

#### Zero Memory Leaks

Written in memory-safe compiled Rust. No V8 garbage collection storms, no lingering zombie Chrome renderer processes.

## The Truth About Document Infrastructure

 No marketing fluff. Brutalist engineering breakdowns of why legacy Chromium breaks under European e-invoicing laws, and the exact code to fix it before the 2026 mandates hit.

### How to Make Your Stripe Invoices Factur-X / ZUGFeRD Compliant in 5 Minutes

 Your standard Stripe PDF invoice is legally non-compliant for French and German B2B clients under EN 16931. Here is why Stripe won't solve it, why legacy EDI charges €1,200/month, and the exact 5-line webhook fix using Rubrol.

- The Lie: Why European ERPs (SAP, DATEV) reject standard Stripe PDFs
- The Code: Copy-paste Node.js/Express webhook to generate PDF/A-3b
- Zero Bloat: Full ISO 19005-3 validation in under 160ms

### Why Puppeteer Cannot Generate Legal EN 16931 E-Invoices (And What to Use Instead)

 Every engineering team treats PDF generation as a web-page printing problem. Here is the deep technical autopsy of why Chrome's Skia engine fails ISO 19005-3 and burns $500/month on zombie Fargate containers.

- Skia Engine Flaw: Zero native support for PDF/A-3b or ICC profiles
- Catalog Attachment: Why Puppeteer cannot create valid `/AFRelationship`
- The Alternative: Sub-15ms Rust Typst compilation with 96% less RAM

### Rubrol vs Mustangproject: Why Modern Cloud Services Don't Want a 300MB Java JVM

 Mustangproject is the reference German ZUGFeRD tool. But deploying a heavy JVM with Apache PDFBox in Kubernetes leads to memory leaks, exit code 137 OOM kills, and the fact that Mustangproject cannot even render visual invoices.

- The Missing Renderer: Mustangproject only attaches XML to pre-existing PDFs
- JVM Memory Spikes: Why PDFBox DOM buffering triggers container OOM kills
- Atomic Pipeline: Render visual Typst layout + embed XML in one 14ms pass

### Rubrol vs Ghostscript: Why ZUGFeRD via PostScript Scripts Is an Infrastructure Hazard

 Artifex recommends Ghostscript command lines with zugferd.ps. But underneath lies AGPL-3.0 copyleft traps, decades of remote code execution CVEs, and complete absence of EN 16931 schema validation.

- Blind Embedding: Ghostscript will embed invalid XML without error
- AGPL-3.0 Contagion: Risking proprietary SaaS IP or paying $10k+ OEM fees
- Memory-Safe Rust: Zero PostScript attack surface with pre-compile validation

### Rubrol vs Gotenberg: Why Headless Chromium Clusters Are the Wrong Tool for E-Invoicing

 Gotenberg requires CHROMIUM_RESTART_AFTER to survive memory leaks and needs 2GB-4GB of RAM per pod. Discover why high-throughput billing systems drop Chromium for 14ms Typst compilation.

- Memory Leaks: Periodic browser killing needed to avoid container crashes
- Bloated Containers: 1.8GB image size with Chromium, LibreOffice, and Java
- 70x Faster: 14ms response time, 42MB Docker image, and < 28MB RAM

## Invest in speed. Eliminate compute waste.

 Open-source core under LGPLv3. Scale with production-grade financial templates and enterprise compliance validation. Flat transparent billing.

 Monthly Documents Generated 50,000 / mo

50000

 2,000 / mo 100,000 / mo 250,000 / mo 500,000+ / mo

Puppeteer Compute Waste $4,860/yr

Senior Dev Hours Saved $14,400/yr (120 hrs)

Total Cost of Ownership (TCO) Saved $19,080/yr

Total Annual Cost of Ownership (TCO) Saved

$19,080

 Includes AWS Fargate compute savings ($0.0081 vs $0.0003/doc) plus eliminating 120 senior dev hours wasted on broken CSS page breaks and pod crashes.

 Recommended Tier: Rubrol Pro ($1,800/yr) Net Positive ROI: +$17,280 / year saved after license cost

 ANNUAL COMMERCIAL LICENSES / ON-PREMISE SIDECAR / ZERO CLOUD DATA PRIVACY RISK

 Flat annual pricing. Billed annually upfront. Zero hidden fees.

### Rubrol Community

Open-source vector engine for local CLI development & Docker evaluation.

### Rubrol Pro

Annual commercial license for SaaS startups & high-throughput billing systems.

 $ 1,800 / year ($150/mo)

 ● Unlimited Local Nodes • Replaces LGPLv3

- Unlimited Local Sidecar Execution (No Limits)
- Full Commercial Production License Grant
- Pre-Built B2B SaaS Invoice & Receipt Templates
- Standard ISO 19005-2 PDF/A-2b Compilation
- Private GitHub Vault (rubrol-pro-vault) Access
- Cryptographic 1-Year Offline License Key
- Direct Developer Email Support

### Rubrol Enterprise

Turnkey EU compliance suite with certified EN 16931 & Schematron validation.

 $ 4,800 / year ($400/mo)

 ● Turnkey EN 16931 & Schematron Engine

- Certified ISO 19005-3 PDF/A-3b + Factur-X / ZUGFeRD 2.2
- Built-in Schematron Semantic Validator (XRechnung 3.0)
- German DIN 5008 & French Chorus Pro XML/PDF Templates
- Dual Vault Access (rubrol-pro-vault + rubrol-enterprise-vault)
- Guaranteed Compliance Updates for 2025-2028 EU Mandates
- Private Container Registry & Air-Gapped License Key
- Priority Engineering Slack Channel & Direct Support

### How Rubrol Licensing Works: The Sidekiq Model

 Just like Sidekiq, Rubrol Community is 100% free and open source under the GNU Lesser General Public License v3.0 (LGPLv3). You are free to run it locally, inspect the source, and use it in your development infrastructure without paying a dime.

 ● Open Source (GNU LGPLv3)

 Free forever for local development, Docker evaluation, CLI scripts, and open-source projects. You can dynamically link or invoke the sidecar without having to open-source your proprietary business code.

 ● Commercial License (Pro & Enterprise)

 Replaces the LGPLv3 with a traditional commercial agreement for production SaaS deployments. Unlocks unlimited execution, turnkey EU Factur-X / Schematron verification, and private GitHub repository access.

## Commercial Licensing FAQ

 Rubrol operates on the transparent Sidekiq commercial open-core model. Everything you need to know about subscriptions, private template vaults, and commercial rights.

### What are Rubrol Pro and Rubrol Enterprise?

Rubrol Pro and Rubrol Enterprise are commercial extensions and licensing agreements for the Rubrol engine. They provide commercial SaaS rights that replace the GNU LGPLv3, private GitHub template vault access, cryptographic 1-year offline license keys, turnkey European e-invoicing compliance (Enterprise), and direct developer support.

### Is there a trial version?

We do not offer pre-sales sales demos or trial keys. Rubrol Community is 100% free, open-source, and available on GitHub under GNU LGPLv3 for evaluation and local development. If Rubrol works for your architecture, you can purchase an annual subscription to Pro or Enterprise. If you are not satisfied with the result, write to support@rubrol.com within 14 days and we will issue a full refund.

### Can I get a discount?

For Rubrol Pro ($1,800/yr), pricing is flat and transparent with zero discounts or promotions. For Rubrol Enterprise ($4,800/yr), multi-year commitments or custom cluster volume agreements are available for high-throughput organizations. Email enterprise@rubrol.com for custom quotes.

### What is the license?

The open-source core is licensed under the GNU Lesser General Public License v3.0 (LGPLv3). Rubrol Pro and Enterprise are commercial licenses that replace the LGPLv3 with a traditional proprietary agreement for production SaaS deployments, removing open-source linking obligations.

### How does Pro licensing work?

Every organization running Rubrol in production for commercial SaaS applications must purchase an annual subscription ($1,800/yr). There is no limit to the number of Docker containers, Kubernetes pods, CPU cores, or developer machines used by that organization. Your subscription renews automatically each year.

### How does Enterprise licensing work?

Every organization deploying Rubrol for European e-invoicing compliance (EN 16931) must purchase an Enterprise subscription ($4,800/yr). It includes certified ISO 19005-3 PDF/A-3b container generation, embedded Factur-X / ZUGFeRD 2.2 XML, built-in Schematron semantic validation (XRechnung 3.0), French Chorus Pro and German DIN 5008 templates, dual vault access (`rubrol-pro-vault` + `rubrol-enterprise-vault`), 2025-2028 regulatory updates, and priority Slack/email support.

### How do I purchase?

You can purchase in seconds via Stripe Checkout:

 • Buy Rubrol Pro ($1,800/yr) • Buy Rubrol Enterprise ($4,800/yr)

Enter your GitHub Username during checkout. You will automatically receive an invitation granting access to the private template vault, and a signed 1-year cryptographic license key (`RUBROL_LICENSE_KEY=RBL-LIC-...`) will be issued immediately.

### Can I upgrade from Rubrol Pro to Enterprise?

Yes. Purchase a Rubrol Enterprise subscription and email support@rubrol.com. We will cancel your existing Pro subscription and prorate the unused balance back to your credit card immediately.

### What happens if my subscription lapses?

We email you an automated reminder one week before annual subscription renewal. If your card cannot be charged, Stripe retries 3 times over a 7-day period. If payment continues to fail, your subscription is canceled, private GitHub vault repository access is revoked, and your offline license key will not be renewed upon expiration.

### Can I distribute Rubrol as an on-premise appliance to customers?

The standard commercial license covers your organization's own SaaS infrastructure and internal servers. If you need to distribute Rubrol binaries or containers embedded directly inside an on-premise software appliance delivered to external third-party customer hardware, contact enterprise@rubrol.com for an OEM Appliance License.

### Can you transfer a license?

Licenses are not transferable between different corporate entities. You can transfer a license between employees or GitHub accounts within the same organization by emailing support@rubrol.com with your Stripe customer email.

### What does the license require me to do?

Your purchase provides private GitHub vault repository access and an offline cryptographic license key. The license agreement requires you to keep these access credentials confidential. Do not commit your license key to public git repositories or public container registries.

### Do I have to share the license key with all developers?

Yes. Your developers and CI/CD runners require the `RUBROL_LICENSE_KEY` environment variable to compile production documents without evaluation limits. Store it securely in your secret manager (e.g. AWS Secrets Manager, GitHub Actions Secrets, HashiCorp Vault, Doppler, or local `.env`).

### How do I debug a license validation error?

Ensure your environment variable `RUBROL_LICENSE_KEY` starts with `RBL-LIC-`. Run `rubrol license verify` from the CLI or inspect container logs on startup. If the key has expired or the signature was modified, the engine will output a clear error message indicating whether the token was malformed or expired.

### Can I get a refund?

Yes, up to 14 days after purchase. If Rubrol does not fit your infrastructure or workload, write to support@rubrol.com and we will refund 100% of your payment.

### Can I pay via invoice and purchase order?

Rubrol Pro is credit card only via Stripe. For Rubrol Enterprise, annual invoicing with payment via ACH, wire transfer, or corporate purchase order is available for qualified corporate accounts. Contact enterprise@rubrol.com to arrange an invoice.

### Disputing a charge

If an unfamiliar charge appears on your card statement, please contact support@rubrol.com before initiating a bank dispute. Disputes result in immediate automated suspension of license keys and vault access. We resolve billing issues and refunds quickly and politely.

### Security, Privacy, and Data Sovereignty

Rubrol runs 100% locally within your own Docker containers, Kubernetes pods, or bare-metal servers. Customer documents, invoice data, and PII are processed entirely in memory and never leave your infrastructure. There are zero outbound document telemetry calls, zero third-party analytics scripts, and zero cloud dependencies.

# sutro-sh/jev-align

## 导航

- 项目页：[[10-项目/rubrol.com_cb4a2df5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
