---
type: "corpus"
item_id: "0c31997df9ce1fda"
title: "Show HN: Ovok – FHIR R4 back end for remote patient monitoring apps"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50325772"
project_url: "https://ovok.com/"
author: "0xsarwagya"
published_at: "2026-11-01T14:01:11Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_0xsarwagya
  - story_50325772
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Ovok – FHIR R4 back end for remote patient monitoring apps

> [!info] 一句话导读
> THESIS: Let product teams choose patient enrollment for Signals while supported device data remains available through FHIR; refuse the generic centered SaaS her…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50325772>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：0xsarwagya　|　发布：2026-11-01T14:01:11Z
> 项目链接：<https://ovok.com/>
> 采集：2026-11-02T09:37:22+08:00　|　id：`0c31997df9ce1fda`

## 正文

<!--
THESIS: Let product teams choose patient enrollment for Signals while supported device data remains available through FHIR; refuse the generic centered SaaS hero.
OWN-WORLD: White ground, Ovok lilac #B2A5CD to purple #694D98, open editorial space, tracked engineering labels, hairline guides, flat shadcn controls, striated signal bands.
STORY: Device data is stored in FHIR. Only eligible vital-sign readings from patients enrolled in Signals are sent for alert evaluation; enrollment is configurable.
FIRST VIEWPORT: At 1586×992, a two-line promise and actions fill the left 40%; labeled device flows and the app endpoint fill the right 60%, with a visible Signals enrollment note; AWS Frankfurt, per-patient pricing, and Signals status close in a bottom strip.
FORM: Signal Chord, third of six rolled challengers, selected under seed 87f03636; approved split-hero comp.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
-->
 Platform
 Use cases
 Solutions for
 Plans
 Blog
 English English Deutsch Français Español
Read the docs Start free
 FHIR backend for remote monitoring
 Build your own digital health apps.
 Supported-device data is stored in FHIR. Your team configures Signals enrollment per patient; only eligible vital-sign readings from enrolled patients are sent to Signals for alert evaluation.
 Start free Read the docs
Supported devices Example destinations
 Supported devices
 BP monitors
 Sleep radars
 SpO₂ monitors
 Urine analysers & wearables
 FHIR backend
 Signals
Example destinations
 Your app
 Clinician dashboard
 EHR
 Other systems
Signals enrollment is configurable per patient. Ovok stores device data in FHIR and forwards eligible vital-sign readings only for enrolled patients, for alert evaluation. AWS Frankfurt hosting
Priced per monitored patient
Signals is MDR Class IIa Ovok is not a certified medical-device product. UDI-DI: 42700031203-API-XG · EUDAMED search
Actimi network
 Ovok is an Actimi product.
Actimi works with the research, healthcare, and innovation organizations shown here.
Features and benefits
 Build the digital health product. Start with the foundations.
 Explore our remote patient monitoring use case , then build the web and mobile workflows your product needs with Ovok SDKs and platform services. We share new FHIR and connected- health articles on the Ovok blog as they publish.
01 Supported device data
 Bring readings from 50+ supported devices , including BP monitors, sleep radars, SpO₂ monitors, urine analysers, and wearables. Explore our sleep monitoring use case and respiratory monitoring use case for related measurement workflows.
02 React and React Native SDKs
 Build web apps with the React SDK and @ovok/core , or use the React Native SDK for mobile UI and integrations.
03 FHIR backend and platform services
 Build on FHIR , with access policies , CMS , video calls , and FHIR questionnaires .
04 RPM app and implementation guides
 Explore the out-of-the-box RPM app , then build from guides for CHF monitoring , type 2 diabetes , and medication reminders .
05 Vital-sign alert decisions
 Signals evaluates eligible vital-sign readings for enrolled patients. Enrollment is configurable. Signals is MDR Class IIa.
For product teams and care providers
 Build for your product stage and care setting.
 Start with the FHIR and device infrastructure for digital-health startups , explore the platform for growing teams in our scaleup solution , or review the details for an enterprise deployment.
Startups
 Evaluate the FHIR foundation and supported device data hands-on in the Developer sandbox.
 Explore startup solutions Scaleups
 Build on supported measurements and Signals as your remote monitoring product grows.
 Explore scaleup solutions Enterprises
 Review Frankfurt hosting, per-patient pricing, and commercial terms with Actimi.
 Explore enterprise solutions
 Healthcare ecosystem
 What exists today, and what your team builds.
Status labels distinguish available capabilities, documented implementation guidance, and roadmap work. Project capabilities and app-specific integrations still matter.
01 In the docs
 Labs
 FHIR references cover lab orders and results; check your project’s CapabilityStatement for enabled interactions. The docs describe resource patterns, not a ready-made lab connector.
 FHIR resource reference
 02 In the docs
 Medications
 The medication guide covers plans, adherence, and local reminders. Ovok provides medication resources; your app schedules device notifications.
 Medication reminder guide
 03 Roadmap
 Billing & RCM
 Patient billing and RCM APIs are not available today. Billing support is deferred until a developer contract exists; no delivery date is published.
 04 Available
 FHIR interoperability
 FHIR R4 APIs are available. The interactions enabled for your project are listed in its CapabilityStatement.
 FHIR R4 docs
 05 Available
 SDKs & modules
 Use the web SDK or React Native SDK; optional native imports let your app include only the integrations it needs.
 Web SDK React Native SDK
 06 In the docs
 Third-party tools
 The LiveKit video-call API is documented. Scheduling, imaging, CRM, and other external systems need app-specific integrations.
 Video-call docs
Start building at your own pace.
 Pricing is per monitored patient. Review per-patient pricing and plan details ; every paid plan includes a data processing agreement.
View pricing details Read the docs
Developer
 For trying the sandbox
Start free Growth
Start with Growth Scale
Start with Scale Enterprise
 Custom contract and Signals terms
Build a business case Want to talk to us?
FHIR backend for remote monitoring.
 Start free Contact us
Platform
 Overview
 Pricing
 Solutions
 Startups
 Scaleups
 Enterprise
 Hospital at Home, virtual wards, and Spitex
 Resources
 Use cases
 FHIR and connected-health articles
 Documentation
 System status
 Company
 Imprint
 Privacy policy
 Cookie and browser storage policy
 FHIR and API developer pages
 FHIR backend
 FHIR API
 FHIR server
 Remote monitoring API
 Medical device integration
 Bluetooth medical device SDK
 React Native healthcare SDK
 FHIR server in Europe
© 2026 Ovok. Ovok is a registered trademark.
 Status All systems operational

## 评论（2/2）

> **shrey69420** · 2026-11-01T14:10:28.000Z　
> What Devices Are Supported?

---

> **0xsarwagya** · 2026-11-01T14:11:42.000Z　
> https://docs.ovok.com/native-sdk/guide/supported-devices
> We Have 849 Supported Devices Are You Looking For Something Specific?
> Maybe We Can Help If You Get In Touch :D

## 导航

- 项目页：[[10-项目/ovok.com_91369a6b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
