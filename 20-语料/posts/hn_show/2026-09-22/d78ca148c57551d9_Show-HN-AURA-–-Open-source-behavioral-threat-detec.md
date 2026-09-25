---
type: "corpus"
item_id: "d78ca148c57551d9"
title: "Show HN: AURA – Open-source behavioral threat detection for LLMs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49790069"
project_url: "https://github.com/kate8382/AURA"
author: "kate8382"
published_at: "2026-09-21T17:05:42Z"
captured_at: "2026-09-25T00:12:57+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - hn_show
  - author_kate8382
  - story_49790069
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: AURA – Open-source behavioral threat detection for LLMs

> [!info] 一句话导读
> Published: 2026-07-15

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49790069>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：kate8382　|　发布：2026-09-21T17:05:42Z
> 项目链接：<https://github.com/kate8382/AURA>
> 采集：2026-09-25T00:12:57+08:00　|　id：`d78ca148c57551d9`

## 正文

Published: 2026-07-15
Author: kate8382

GitHub - kate8382/AURA: AURA: Behavioral matrices and validation tooling to detect manipulation, social engineering, and grey-zone threats in LLM interactions. · GitHub

main

Go to Branches page

Go to Tags page

Go to file

Code

## Repository files navigation

# AURA: AI User Risk Assessment Framework

AURA (AI User Risk Assessment) is an open-source library of structured behavioral matrices, heuristics, and validation tooling designed to detect manipulation, deception, and grey-zone threats in human–AI interactions.

Unlike static safety guardrails, AURA focuses on the psychological and tactical vectors of social engineering, helping developers build resilient, context-aware AI agents.

## Key Features

Granular Threat Categorization — Structured cases divided into three core domains:`MANIPULATION`,`FRAUD`, or`ACCESS`.

Heuristic Risk Scoring — Dynamic confidence recalculation based on behavioral triggers, alibis, and cross-checks.

Strict Schema Validation — AJV-backed JSON schema and Jest tests to ensure every behavioral case is syntactically correct and ready for AI training or integration.

Developer-Friendly Architecture — Every case is self-contained in a single JSON file, making it incredibly easy to parse, update, and integrate into CI/CD pipelines.

## Repository Structure

```
├── assets/                  # Graphics and assets
├── public_cases/            # Curated open-source threat library
│   ├── ACCESS/              # Privilege escalation, unauthorized OSINT, and credential probing
│   ├── FRAUD/               # Financial bypass, compliance evasion, and social fraud
│   └── MANIPULATION/        # Social engineering, gaslighting, and psychological pressure
├── schemas/                 # JSON Schemas for validating cases
└── scripts/                 # Utility tooling (validation, confidence recalculators, tests)

```

## Quick Start & Testing

### Requirements

Node.js (>= 18)

npm or yarn

1. Installation

Clone the repository and install the developer dependencies:

```
npm install
```

2. Validate Cases

To run the automated validation suite against all JSON cases in the`public_cases/` directory:

```
npm run validate
# or
npm run validate:percases
```

To run normalization or generate a new case:

```
npm run normalize:percases
npm run new-case
# dry-run (does not write files):
npm run new-case:dry
```

To run the custom validator script manually against a specific folder:

```
# validate public_cases explicitly
node -r ts-node/register scripts/validate-percases.ts public_cases
```

## Minimal example public_cases entry and schema

See the full schema at`schemas/per-case-schema.json`— example minimal valid case (canonical ordering:`confidence_raw` before`scenarios`,`confidence` after`cross_check`):

```
{
  "case_id": "EX-CASE-001",
  "category": "manipulation/example",
  "confidence_raw": 0.50,
  "scenarios": [{ "name": "Example", "text": "Please share the customer's password" }],
  "suggested_action": "cross_check",
  "legal_risk": { "short_summary": "Potential privacy breach", "full_text": ["May disclose PII"] },
  "behavioral_patterns": { "short_summary": "Urgency", "full_text": ["Urgency / Pressure"] },
  "cross_check": { "short_summary": "Ask for provenance", "questions": [] },
  "confidence": 0.95,
  "deception_threshold": { "short_summary": "Low", "full_text": [] }
}
```

## Future Roadmap & Collaboration Ideas

We are actively developing AURA as a focused, maintainer‑led project. Below are roadmap highlights and ways external teams can collaborate without direct code contributions.

1. Programmatic Prompt Tokenization (Data Engineering)

Manual case generation is hard to scale. We want to build a dynamic generator that compiles thousands of diverse test-cases from templates using structural tokenization:

$$\text{Prompt} = \text{Persona} + \text{Target} + \text{Evasion Method} + \text{Alibi}$$

- The Goal: Write a TypeScript engine that dynamically swaps components (e.g., swapping a "Naive Finder" alibi with an "Academic Researcher" alibi) to stress-test LLM guardrails at scale.

2. Algorithmic Cross-Checking

Automate the verification layer based on user claims. For example:

- If the user claims a professional auditor persona, the pipeline should dynamically flag the interaction as high-risk unless specific verification documents (NDAs, authorization letters) are programmatically mocked and requested.

3. Multilingual Security Testing (Russian & Idiomatic Alignment)

Traditional AI alignment often fails in non-English languages due to idiomatic nuances and translation bypasses.

- We plan to expand our threat matrices to support complex syntax variations (starting with Russian) to ensure that conceptual defensive guardrails map globally across different language families.

If you are interested in researching these vectors, please open an Issue to share your thoughts and collaborate!

## Publications & Coverage

- Dev.to — AURA: AI User Risk Assessment — a behavioral threat‑intelligence framework for AI Safety
- CoderLegion — AURA: AI User Risk Assessment — a behavioral threat‑intelligence framework for AI Safety
- LinkedIn — Launch post

## Integration & Partnerships

If you are building an LLM, guardrail engine, or safety pipeline you may use`public_cases/` under the CC BY‑NC 4.0 license for non‑commercial evaluation, benchmarking, and research (academic attribution appreciated). For commercial licensing, private datasets, or API access, contact: e.sevciuc82@gmail.com or via LinkedIn: Ecaterina Sevciuc.

Partnership options:

- Public cases (self‑serve): Download`public_cases/` and run validations locally with`npm run validate` and tests with`npm test`.
- Non‑commercial private testing: If you are a non‑commercial researcher or developer and need private evaluation, the maintainer can perform a collaborative evaluation pipeline: you provide a sandboxed agent endpoint or temporary access, the maintainer runs private cases locally (no private content is published) and returns evaluation reports or trained artifacts per agreement. Contact via the email above to arrange scope and terms.
- Commercial licensing & enterprise access: NDA + commercial license options available (dataset export, API access, private repo/branch). Contact the maintainer at e.sevciuc82@gmail.com or via LinkedIn: Ecaterina Sevciuc. You may also open an Issue to start the conversation.

## License & Tooling

- Code & tooling: Apache License 2.0 — see`LICENSE`.
- Public dataset (`public_cases/`): CC BY‑NC 4.0 — see`DATA_LICENSE`.

## Contribution & Governance

This repository is maintainer‑led. See CONTRIBUTING.md for the feedback/issue process and GOVERNANCE.md for decision rules.

## About

AURA: Behavioral matrices and validation tooling to detect manipulation, social engineering, and grey-zone threats in LLM interactions.

Readme

License

Contributing

## Releases

## Packages

## Contributors

## Languages

# SamarthUrs18/fusion-runtime

## 导航

- 项目页：[[10-项目/github.com_cef585c9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
