---
type: "corpus"
item_id: "7136e91a70c9f676"
title: "Show HN: STE-Code a distillation and adaptation of ASD-STE100 for code"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49120690"
project_url: "https://github.com/NikolaRHristov/STE-Code"
author: "nikolahristov"
published_at: "2026-07-31T08:58:16Z"
captured_at: "2026-09-21T03:11:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_nikolahristov
  - story_49120690
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:83d"
---

# Show HN: STE-Code a distillation and adaptation of ASD-STE100 for code

> [!info] 一句话导读
> NikolaRHristov/STE-Code

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49120690>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：nikolahristov　|　发布：2026-07-31T08:58:16Z
> 项目链接：<https://github.com/NikolaRHristov/STE-Code>
> 采集：2026-09-21T03:11:08+08:00　|　id：`7136e91a70c9f676`

## 正文

# NikolaRHristov/STE-Code

Simplified Technical English for Code — extract, adapt, and enforce ASD-STE100 rules for software documentation. 9-agent pipeline, 59-test benchmark (96.6%), multi-language scaffolding.

- Stars: 4
- Forks: 0
- Watchers: 4
- Open issues: 0
- License: Other
- Homepage: https://github.com/NikolaRHristov/STE-Code
- Default branch: Current
- Created: 2026-07-29T20:02:25Z

## Languages

- Python
- Shell

## Topics

- asd-ste100
- benchmark
- code-quality
- code-review
- documentation
- llm-pipeline
- multi-agent
- simplified-english
- ste-code
- technical-writing

## Top Contributors

- NikolaRHristov (166 contributions)

---

## README

# STE-Code — Simplified Technical English for Code Documentation

License: MIT
Standard
Spec
Benchmark

---

STE-Code is a documentation standard adapted from ASD-STE100 Issue 9 for code documentation. It gives you 51 writing rules, 4 grammar recommendations, a controlled vocabulary, and system prompt templates at five levels. The standard removes ambiguity, jargon, and hedging from README files, API documentation, docstrings, commit messages, and error messages.

---

## Adaptation Levels

Choose the level that fits your token budget:

| Level | File | Tokens | Best For |
|:-----:|------|:------:|----------|
| **1** | `level1/system-prompt.txt` | ~1.2K | Interactive sessions, tight token budgets |
| **2** | `level2/system-prompt.txt` | ~4.5K | Code review, PR feedback |
| **3** | `level3/system-prompt.txt` | ~8K | Full document rewriting |
| **4** | `level4/system-prompt.txt` | ~45K | Strict compliance checking |

Level 5 (the full specification) has 51 rule summaries at `ste-code/artifacts/level5/`.

---

## How It Works

Copy a system prompt into your LLM. The model writes clear, unambiguous documentation.

```
You: Copy level1/system-prompt.txt into the system prompt field.
LLM: You are an STE-Code technical writer. Apply these rules...
You: Check this docstring.
     /** This function basically handles user stuff. */
LLM: /** Creates a user or updates the data of a user. */
```

The LLM applies the controlled vocabulary, the synonym table, and the sentence-length limits. It replaces jargon with approved words. It uses active voice and imperative mood.

---

## The Rules

The 51 rules cover nine sections:

| Section | Rules | Covers |
|---------|:-----:|--------|
| 1 — Words | 14 | Approved vocabulary, parts of speech, technical nouns and verbs |
| 2 — Noun Phrases | 2 | Article use, noun clusters |
| 3 — Verbs | 7 | Tense, voice, mood, verb forms |
| 4 — Sentences | 5 | Length, clarity, contractions, completeness |
| 5 — Procedures | 5 | Instructional writing, step structure |
| 6 — Descriptions | 5 | Descriptive writing, comparisons |
| 7 — Warnings | 3 | BREAKING, DEPRECATED, NOTE formatting |
| 8 — Punctuation | 6 | Commas, hyphens, parentheses, lists |
| 9 — Document Structure | 4 | Headings, lists, tables, organization |

Each rule has a code-domain adaptation with paradigm-specific guidance for object-oriented, functional, procedural, declarative, and systems programming. The full rules are in `ste-code/adapted/`.

---

## Benchmark

STE-Code against a plain assistant on 59 documentation tests across 14 categories:

| | STE-Code | Plain Assistant | Improvement |
|---|:--------:|:---------------:|:-----------:|
| Pass rate | 96.6% | 11.9% | **+84.7%** |
| Average score | 0.919 | 0.471 | **+0.448** |

Top categories: comments, error messages, and config files.

---

## Repository

```
STE-Code/
├── README.md
├── ste-code/
│   ├── artifacts/
│   │   ├── level1/system-prompt.txt     ★ ~1.2K tokens
│   │   ├── level2/system-prompt.txt     ★ ~4.5K tokens
│   │   ├── level3/system-prompt.txt     ★ ~8K tokens
│   │   ├── level4/system-prompt.txt     ★ ~45K tokens
│   │   └── level5/                      ★ 51 rule summaries
│   ├── adapted/               The standard (57 adapted files)
│   ├── data/                  Structured JSON (vocabulary, synonyms)
│   ├── templates/             Additional system prompts
│   ├── merged/                master.md (full spec consolidation)
│   ├── refined/               Stage 2 — formatted extraction
│   └── extracted/             Stage 1 — raw extraction
├── spec/                      ASD-STE100 Issue 9 source (434 pages)
├── translations/              Translation scaffolding (9 locales)
└── .agents/                   Pipeline orchestration (agents, skills, config)
    ├── config/agents.yaml     Agent backend configuration
    └── tools/                 Assembly scripts (agent-agnostic)
```

---

## Agent-Agnostic Tools

All assembly scripts use the agent runner at `.agents/tools/agent-runner.py`. The default backend is Hermes. Add other agents in `.agents/config/agents.yaml`.

```bash
# Assemble prompts (default: Hermes)
python3 .agents/tools/assemble-level3.py
python3 .agents/tools/assemble-level2.py
python3 .agents/tools/assemble-level1.py

# Use a different agent
python3 .agents/tools/assemble-level1.py --agent claude

# List available agents
python3 .agents/tools/agent-runner.py --list
```

For full documentation, see `.agents/AGENTS.md`.

---

## Pipeline

The standard was built from ASD-STE100 Issue 9 through a five-stage automated pipeline:

```
Extract → Refine → Merge → Adapt → Artifacts
(434pp)   (109f)    (1f)    (57f)    (5 levels)
```

Nine specialized agents orchestrated 109 parallel workers. The adaptation replaced aerospace terms with code-domain equivalents.

---

## License

MIT. See LICENSE.

## Citation

```bibtex
@misc{ste-code-2025,
  title        = {{STE-Code}: Simplified Technical English for Code Documentation},
  author       = {{Nikola Hristov}},
  year         = {2025},
  howpublished = {\url{https://github.com/NikolaRHristov/STE-Code}},
  note         = {Adapted from ASD-STE100 Issue 9 (January 2025)}
}
```

## Credits & References

STE-Code stands on decades of controlled-language research, documentation
theory, and verification tooling.

### Primary Standard

- **ASD-STE100 Simplified Technical English, Issue 9 (January 2025)** —
 the foundational standard STE-Code adapts to the code domain. Owned by
 **ASD — Aerospace, Security and Defence Industries Association of Europe**,
 Brussels; maintained by the **Simplified Technical English Maintenance
 Group (STEMG)**. Copyright and trademark of ASD.

- **AECMA / AIA Simplified English lineage** — STE's origin: developed in the
 late 1970s–1980s by the **European Association of Aerospace Industries
 (AECMA, now ASD)** with the **Aerospace Industries Association of America
 (AIA)**, at the request of the **Association of European Airlines (AEA)**.
 Working group founded 30 June 1983, Amsterdam; first Guide release 1986;
 became ASD-STE100 specification in 2005 and an international standard in
 2025. Historical basis for STE-Code's core principle: enforceability
 determines survival (Caterpillar Fundamental English, unenforced, died 1982).

### Controlled Natural Language Theory

- **Tobias Kuhn** — *A Survey and Classification of Controlled Natural
 Languages* (Computational Linguistics, 2014; 636+ citations). Source of
 the PENS classification (Precision, Expressiveness, Naturalness,
 Simplicity) used to profile STE-Code rules.

- **Norbert E. Fuchs & Rolf Schwitter** (University of Zurich) — *Attempto
 Controlled English (ACE)* (1996). Precedent for machine-processable
 controlled English and explicit quoting conventions for the use–mention
 distinction.

- **Rimay CNL research** — *On systematically building a controlled natural
 language for functional requirements* (PubMed). Source of the coverage
 methodology (88% of 460 real statements expressible).

### Documentation & Readability Research

- **John M. Carroll** — *Minimalism* tradition in technical documentation
 (ACM SIGDOC). Learning-theoretic basis for register stratification: users
 act first and read at the moment of need.

### Verification & Executable Documentation Tooling

- **asciidoctest** (PyPI) — *Verifiable, stateful, and interactive
 documentation with AsciiDoc*. Reference implementation for code-block
 verification.

### Adjacent Standards & Catalogues

- **Google Style Guides** — precedent for public, per-language style standards.

- **Kristories/awesome-guidelines** — community catalogue of coding standards.

- **github/codeql-coding-standards** — precedent for machine-enforceable
 standards as executable queries.

### Intellectual-Property Note

ASD-STE100 is a copyright and trademark of ASD, Brussels. STE-Code adapts
its *principles and rule categories* to the software domain; it does not
reproduce the standard's dictionary or rule text. Users requiring the
authoritative aerospace standard should obtain Issue 9 directly from ASD
(free of charge via the official form):.

# Lywald/zfrontpage

## 关联链接

- https://github.com/NikolaRHristov/STE-Code}},

## 导航

- 项目页：[[10-项目/github.com_5e309835]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
