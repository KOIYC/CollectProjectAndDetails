---
type: "corpus"
item_id: "a2f945e69d21275b"
title: "Show HN: WorkProof – JSON schema for skill evidence graphs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47956948"
project_url: "https://github.com/TalentProof/workproof-schema"
author: "parth4"
published_at: "2026-04-30T01:27:38Z"
captured_at: "2026-09-21T02:52:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_parth4
  - story_47956948
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: WorkProof – JSON schema for skill evidence graphs

> [!info] 一句话导读
> TalentProof/workproof-schema

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47956948>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：parth4　|　发布：2026-04-30T01:27:38Z
> 项目链接：<https://github.com/TalentProof/workproof-schema>
> 采集：2026-09-21T02:52:30+08:00　|　id：`a2f945e69d21275b`

## 正文

# TalentProof/workproof-schema

An open specification for verified professional knowledge graphs

- Stars: 4
- Forks: 0
- Watchers: 4
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-04-29T00:13:21Z

## Topics

- ai-agents
- json-schema
- mcp
- open-standard
- professional-identity
- recruiting
- schema
- verifiable-credentials

## Top Contributors

- parth4 (3 contributions)

---

## README

# WorkProof Schema

**An open specification for verified professional knowledge graphs.**

WorkProof is a structured, artifact-derived representation of what a
professional can actually do — built from verifiable work evidence, not
self-reported claims. This repository defines the open schema, evidence
model, attestation format, and agent card extension that make up the
WorkProof protocol.

> **Status:** Draft v0.1 — open for community feedback
> **Maintained by:** TalentProof
> **License:** MIT

---

## The problem

Every professional profile system in existence today is built on the same
flawed primitive: the self-reported claim. You say you know React. You say
you led a team of 10. You say you shipped at scale. There is no structural
way for the person reading your profile to know if any of it is true.

AI is accelerating the problem, not solving it. Recruiters are already
deploying AI sourcing tools — Juicebox, Moonhub, SeekOut and others — that
autonomously search millions of profiles, score candidates, and send
outreach at scale. These tools run faster than any human recruiter, but
they still depend on the same flawed input: self-reported text. The signal
problem doesn't go away when you automate around it. It compounds.

The next wave goes further. As recruiter agents and candidate agents begin
communicating directly — negotiating fit, verifying claims, routing
opportunities without human intervention at every step — the absence of
structured, machine-readable professional signal becomes a hard blocker.
An agent cannot evaluate a paragraph. It needs structured data with
explicit confidence scores derived from verifiable evidence. Something
has to replace the resume at the schema level.

WorkProof is that replacement.

---

## What WorkProof is

A WorkProof graph is generated from verifiable work artifacts — code
commits, document authorship, assessment results, project records — and
structured into named skill clusters with confidence scores derived from
evidence weight, not self-report.

It has five components:

| Component | What it captures |
|---|---|
| **Skill clusters** | Named domains with confidence scores and evidence citations |
| **Execution depth** | The scale and context in which skills were applied |
| **Growth velocity** | How fast the graph is expanding into new domains |
| **Collaboration graph** | Peer signals derived from co-authorship patterns |
| **Attestations** | Cryptographically signed employer or institution credentials (W3C VC) |

A WorkProof is not a resume. It does not contain job titles, company names
(unless attested), or self-written descriptions. It contains structured
evidence of capability, derived from artifacts, with explicit confidence
scores that reflect the quality of evidence available.

---

## Schema specification

### Root document

```json
{
  "$schema": "https://raw.githubusercontent.com/TalentProof/workproof-schema/main/schema/v0.1.json",
  "specVersion": "0.1",
  "generatedAt": "2026-04-27T10:00:00Z",
  "updatedAt": "2026-04-27T10:00:00Z",
  "summary": "string (≤280 chars, AI-generated, describes candidate strengths)",
  "growthEdge": "string (≤140 chars, where the candidate is developing toward)",
  "growthVelocity": 0.73,
  "skillClusters": [],
  "collaborationGraph": {},
  "sources": [],
  "attestations": [],
  "agentCard": {}
}
```

### Skill cluster

A skill cluster is a named professional domain, derived from artifact
analysis, with a confidence score that reflects the weight and breadth of
available evidence.

```json
{
  "id": "frontend-engineering",       // stable machine identifier, kebab-case
  "name": "frontend-engineering",     // human-readable slug (may be same as id in v0.1)
  "displayName": "Frontend Engineering", // display label for UIs
  "confidence": 0.91,
  "executionDepth": {
    "scale": "production-scale",
    "context": "React at >100k MAU, three shipped products, one open-source library with 400+ stars"
  },
  "evidence": [
    {
      "type": "github",
      "sourceId": "github:repos:react-dashboard",
      "description": "847 commits, primary author, TypeScript + React",
      "weight": 0.45,
      "verifiedAt": "2026-04-20T00:00:00Z"
    },
    {
      "type": "assessment",
      "sourceId": "talentproof:assessment:frontend-q3-2025",
      "description": "Frontend fundamentals assessment, score 94/100",
      "weight": 0.35,
      "verifiedAt": "2025-09-15T00:00:00Z"
    },
    {
      "type": "attestation",
      "sourceId": "attestation:acme-corp-2024",
      "description": "Employer-attested: shipped three production React apps",
      "weight": 0.20,
      "verifiedAt": "2024-12-01T00:00:00Z"
    }
  ],
  "lastUpdated": "2026-04-27T10:00:00Z"
}
```

#### Confidence score guide

| Range | Label | Meaning |
|---|---|---|
| 0.85 – 1.0 | Strong evidence | Multiple high-weight sources, consistent signal |
| 0.60 – 0.84 | Growing expertise | Solid evidence, some breadth still developing |
| 0.35 – 0.59 | Early signals | Emerging evidence, thinner artifact base |
| 0.00 – 0.34 | Exploratory | Initial activity, not enough to make strong claims |

Confidence scores must be derived from evidence weights — they cannot be
self-reported or manually overridden by the candidate.

#### Execution depth

```json
{
  "scale": "personal | team | org | production-scale",
  "context": "string (≤200 chars, specific and honest — not marketing copy)"
}
```

Scale definitions:
- `personal` — side project, solo work, learning context
- `team` — shipped within a team of 2–10
- `org` — cross-team impact, org-wide adoption
- `production-scale` — shipped to real users at meaningful scale

#### Evidence types

| Type | Source | Trust level |
|---|---|---|
| `assessment` | Standardized skill assessment (e.g. TalentProof) | High — third-party scored |
| `github` | GitHub contributions, commits, repos, PRs | Medium-high — artifact-derived |
| `document` | Authored documents, PRDs, specs (Google Drive, Notion) | Medium — authorship-derived |
| `jira` | Ticket ownership, resolution patterns | Medium — work record |
| `academic` | University coursework, thesis, capstone projects — institution-verified | Medium — institution-derived |
| `bootcamp` | Structured training program completion and projects — program-verified | Medium — program-derived |
| `certification` | Industry or platform certification — proctored, time-limited, provider-verifiable | Medium-high — provider-verified |
| `course` | Platform-verified course completion (Coursera, Google, Microsoft Learn) | Medium — platform-verified |
| `attestation` | Employer or institution-signed WorkProof credential | Highest — cryptographically verified |
| `peer` | Peer vouching via C2C graph (co-authorship based) | Medium — network-derived |

Evidence weight ranges:
- `attestation`: 0.15 – 0.40 per item
- `assessment`: 0.25 – 0.45 per item
- `certification`: 0.15 – 0.30 per item (scales with provider credibility and scope)
- `github`: 0.05 – 0.35 per item (scales with commit depth and consistency)
- `academic`: 0.10 – 0.25 per item
- `bootcamp`: 0.10 – 0.20 per item
- `course`: 0.08 – 0.20 per item
- `document`: 0.05 – 0.20 per item
- `peer`: 0.05 – 0.15 per item

Total evidence weights for a cluster should not exceed 1.0.
Implementations must cap and normalise when multiple sources overlap.

---

### Collaboration graph

The collaboration graph captures peer signal derived from co-authorship
and verified collaboration — not endorsements or self-reported team size.

```json
{
  "peerCount": 12,
  "verifiedCollaborations": 4,
  "domains": ["frontend-engineering", "developer-tooling"],
  "c2cEdges": [
    {
      "peerHandle": "string (opaque, platform-specific)",
      "sharedClusters": ["frontend-engineering"],
      "collaborationStrength": 0.78,
      "evidenceBasis": "github-co-authorship | attestation-cosignature | peer-vouching"
    }
  ]
}
```

`c2cEdges` are only included in full WorkProof responses (consent level L3
or higher). Public WorkProof summaries show only `peerCount`,
`verifiedCollaborations`, and `domains`.

---

### Sources

Sources record which connectors have contributed to the WorkProof graph
and when they were last indexed.

```json
[
  {
    "type": "github | google-drive | notion | jira | confluence | assessment | slack | microsoft-learn | google-learn | credly | university | bootcamp",
    "connectedAt": "2026-03-01T00:00:00Z",
    "lastIndexed": "2026-04-27T00:00:00Z",
    "status": "active | error | disconnected",
    "artifactCount": 847
  }
]
```

---

### Attestations

Attestations are employer-issued WorkProof credentials. They are
cryptographically signed, candidate-gated, and based on artifacts —
not on subjective human authorship.

The trust model: the employer reviews and signs facts they did not write.
The attestation content is generated from the employee's work artifacts.
The employer is the notary, not the author.

```json
[
  {
    "id": "att_01j8abc123",
    "issuerName": "Acme Corporation",
    "issuerDomain": "acme.com",
    "issuerDID": "did:web:acme.com",
    "issuerType": "employer | university | bootcamp | certification-body",
    "period": {
      "start": "2022-06-01T00:00:00Z",
      "end": "2024-12-01T00:00:00Z"
    },
    "attestedClusters": [
      {
        "clusterId": "frontend-engineering",
        "confidence": 0.88,
        "note": "Led three production React deployments. Primary author on core UI library."
      }
    ],
    "issuedAt": "2024-12-15T00:00:00Z",
    "candidateApproved": true,
    "revoked": false,
    "credential": "eyJ0eXAiOiJKV1Qi...",
    "credentialFormat": "jwt_vc | json_ld_vc"
  }
]
```

Attestations are based on the W3C Verifiable Credentials Data Model v2.
Implementations should support both `jwt_vc` (compact, widely supported)
and `json_ld_vc` (richer context, linked data).

#### Attestation generation flow

```
1. Employer deploys WorkProof Attestation Agent
   (reads GitHub, Jira, Confluence within company boundary)

2. Agent indexes employee's work artifacts
   → generates draft attestation (clusters + evidence + period)

3. Employee reviews draft
   → approves or requests edits
   → can revoke at any time after issuance

4. Employer reviews and signs
   → signs with company DID or registered signing key
   → issues W3C Verifiable Credential

5. Attestation stored in candidate's WorkProof graph
   → candidate controls which recruiters can see it
   → verifiable without contacting the employer
     (signature checked against employer's public DID)
```

---

### Agent Card extension

WorkProof extends the
A2A Agent Card
with professional identity fields. A WorkProof-compatible agent card
contains the standard A2A fields plus a `workproof` extension object.

```json
{
  "name": "Candidate Agent — Priya Sharma",
  "description": "Professional agent representing Priya Sharma on TalentProof",
  "url": "https://talentproof.ai/agents/priyasharma",
  "version": "1.0",
  "capabilities": {
    "streaming": false,
    "pushNotifications": false
  },
  "extensions": {
    "workproof": {
      "specVersion": "0.1",
      "profileUrl": "https://talentproof.ai/p/priyasharma",
      "availability": "passive",
      "consentLevel": 1,
      "topClusters": [
        { "name": "frontend-engineering", "confidence": 0.91 },
        { "name": "system-design", "confidence": 0.74 },
        { "name": "developer-tooling", "confidence": 0.61 }
      ],
      "hasAttestations": true,
      "sourceCount": 3,
      "trustScore": 0.82
    }
  }
}
```

The `workproof` extension exposes only public-facing fields (consent level
L1). Deeper access requires negotiation through the WorkProof consent gate.

---

## Consent gate

The WorkProof consent gate controls what a querying agent can access.
Consent levels are scoped to a specific requester identity, a specific
purpose (job spec context), and a time window.

| Level | Label | Accessible data | Who can request |
|---|---|---|---|
| **L0** | Exists | Agent endpoint URL only | Anyone |
| **L1** | Summary | Top clusters (names + confidence), availability, source count, attestation flag | Any registered agent |
| **L2** | Domain query | Answer structured questions about specific skill domains | Verified recruiter agents |
| **L3** | Cited evidence | Specific proof points for claimed clusters | Verified recruiter agents with trust score ≥ 0.6 |
| **L4** | Full graph | Complete WorkProof including collaboration edges and attestation detail | Explicit candidate approval per request |

Consent levels are managed by the candidate through their WorkProof agent
settings. Implementations must enforce consent levels server-side — the
consent level declared in the agent card is the maximum; individual
requests may be granted lower access.

Present consent to candidates as a simple availability dial:

- **Closed** → L0 only
- **Passively open** → L1 default, L2 on request
- **Actively looking** → L1 default, L2 on request, L3 available to trusted recruiters

Do not expose L0–L4 terminology in candidate-facing UIs.

---

## Growth velocity

Growth velocity is a 0–1 signal representing how actively a candidate's
WorkProof graph is expanding into new domains over a rolling 12-month
window.

```
growthVelocity = (newClusterCount × 0.4) 
               + (risingClusterDelta × 0.35) 
               + (newSourceConnections × 0.25)
```

Normalise to 0–1 based on platform-wide distribution.

A velocity of 0.7+ indicates a candidate actively expanding their
professional surface area. A velocity of 0.2 or below indicates a stable
but not actively growing practitioner. Neither is inherently better —
recruiters should filter by velocity only when growth trajectory is
explicitly required for a role.

---

## Full WorkProof example

```json
{
  "$schema": "https://raw.githubusercontent.com/TalentProof/workproof-schema/main/schema/v0.1.json",
  "specVersion": "0.1",
  "generatedAt": "2026-04-27T10:00:00Z",
  "updatedAt": "2026-04-27T10:00:00Z",
  "summary": "Frontend engineer with production-scale React experience and a secondary track record in developer tooling. Strong artifact base across three shipped products and one OSS library.",
  "growthEdge": "Moving into system design and distributed architecture, active GitHub signal in this area over the last 8 months.",
  "growthVelocity": 0.73,
  "skillClusters": [
    {
      "id": "frontend-engineering",
      "name": "frontend-engineering",
      "displayName": "Frontend Engineering",
      "confidence": 0.91,
      "executionDepth": {
        "scale": "production-scale",
        "context": "React at >100k MAU across three shipped products, one OSS library with 400+ stars"
      },
      "evidence": [
        {
          "type": "github",
          "sourceId": "github:repos:react-dashboard",
          "description": "847 commits, primary author, TypeScript + React",
          "weight": 0.45,
          "verifiedAt": "2026-04-20T00:00:00Z"
        },
        {
          "type": "assessment",
          "sourceId": "talentproof:assessment:frontend-q3-2025",
          "description": "Frontend assessment, score 94/100",
          "weight": 0.35,
          "verifiedAt": "2025-09-15T00:00:00Z"
        },
        {
          "type": "attestation",
          "sourceId": "att_01j8abc123",
          "description": "Employer-attested: led three production React deployments",
          "weight": 0.20,
          "verifiedAt": "2024-12-15T00:00:00Z"
        }
      ],
      "lastUpdated": "2026-04-27T10:00:00Z"
    },
    {
      "id": "developer-tooling",
      "name": "developer-tooling",
      "displayName": "Developer Tooling",
      "confidence": 0.61,
      "executionDepth": {
        "scale": "team",
        "context": "Built internal CLI tools adopted by 15-person engineering team"
      },
      "evidence": [
        {
          "type": "github",
          "sourceId": "github:repos:dev-cli",
          "description": "Primary author of internal CLI, 3 contributors",
          "weight": 0.55,
          "verifiedAt": "2026-02-10T00:00:00Z"
        },
        {
          "type": "peer",
          "sourceId": "peer:handle:anish-mehta",
          "description": "Co-authored tooling project, verified collaboration",
          "weight": 0.10,
          "verifiedAt": "2026-01-15T00:00:00Z"
        }
      ],
      "lastUpdated": "2026-04-27T10:00:00Z"
    }
  ],
  "collaborationGraph": {
    "peerCount": 8,
    "verifiedCollaborations": 3,
    "domains": ["frontend-engineering", "developer-tooling"]
  },
  "sources": [
    {
      "type": "github",
      "connectedAt": "2026-03-01T00:00:00Z",
      "lastIndexed": "2026-04-27T00:00:00Z",
      "status": "active",
      "artifactCount": 1204
    },
    {
      "type": "assessment",
      "connectedAt": "2025-09-10T00:00:00Z",
      "lastIndexed": "2025-09-15T00:00:00Z",
      "status": "active",
      "artifactCount": 2
    }
  ],
  "attestations": [
    {
      "id": "att_01j8abc123",
      "issuerName": "Acme Corporation",
      "issuerDomain": "acme.com",
      "issuerDID": "did:web:acme.com",
      "period": {
        "start": "2022-06-01T00:00:00Z",
        "end": "2024-12-01T00:00:00Z"
      },
      "attestedClusters": [
        {
          "clusterId": "frontend-engineering",
          "confidence": 0.88,
          "note": "Led three production React deployments."
        }
      ],
      "issuedAt": "2024-12-15T00:00:00Z",
      "candidateApproved": true,
      "revoked": false,
      "credentialFormat": "jwt_vc"
    }
  ],
  "agentCard": {
    "availability": "passive",
    "consentLevel": 1,
    "protocol": "workproof/v0.1"
  }
}
```

---

## JSON Schema file

A machine-readable JSON Schema (`schema/v0.1.json`) is included in this
repository for validation. Import it in your implementation:

```typescript
import workproofSchema from 'workproof-schema/schema/v0.1.json'
import Ajv from 'ajv'

const ajv = new Ajv()
const validate = ajv.compile(workproofSchema)
const valid = validate(workproofDocument)
```

---

## TypeScript types

```typescript
import type { WorkProof, SkillCluster, Attestation, AgentCard } 
  from 'workproof-schema/types'
```

Types are published to npm as `workproof-schema` (coming soon).

---

## Implementing WorkProof

### Minimum viable implementation

A conforming WorkProof implementation must:

1. Generate `skillClusters` from at least one non-self-reported source
 (assessment, GitHub, document, or attestation)
2. Derive `confidence` scores from evidence weights — not user input
3. Enforce consent gate levels server-side
4. Store the full WorkProof graph locally or in an encrypted
 candidate-controlled store — not exposed by default
5. Expose only L1 data in the public agent card extension

### Recommended stack

| Component | Recommended |
|---|---|
| Graph storage | KuzuDB (embedded, local), Firestore (cloud) |
| Embedding model | text-embedding-004 (Google), or any 768-dim model |
| LLM for cluster generation | Gemini 1.5 Pro, GPT-4o, Claude Sonnet |
| Attestation signing | W3C VC JWT, did:web |
| Agent protocol | MCP (tools), A2A (agent-to-agent) |

---

## WorkProof for continuous learners

Professionals who actively learn through online platforms — Coursera,
Microsoft Learn, Google Career Certificates, Udemy, LinkedIn Learning —
are well-served by WorkProof, but the schema draws a deliberate distinction
between verifiable completions and self-reported ones.

### Two new evidence types

**`certification`** — industry or platform certifications that are
externally proctored, time-limited, and verifiable against a provider
registry. These carry higher weight because they cannot be inflated and
require renewal.

**`course`** — structured learning program completions that are
platform-verified (not self-reported). Lower weight than certifications
because completion rigor varies, but valid evidence when the issuing
platform provides external verification.

### Verifiable vs self-reported: the critical distinction

WorkProof does not accept self-reported course completions as evidence.
A certificate that anyone can generate by clicking through a course with no
external verification is equivalent to typing "Python" on a resume — it
adds nothing structurally. Every platform LinkedIn lets you list on your
profile falls into this category. WorkProof draws the line differently.

| Platform / credential | Verifiable? | Evidence type | Weight range |
|---|---|---|---|
| Microsoft certifications (AZ-900, MS-900, etc.) | Yes — Microsoft Transcript | `certification` | 0.15 – 0.30 |
| Google Career Certificates | Yes — Credly badge API | `course` | 0.10 – 0.20 |
| AWS / Azure / GCP certifications | Yes — provider registry | `certification` | 0.20 – 0.35 |
| GitHub Certifications (Actions, Copilot, Security) | Yes — GitHub API | `certification` | 0.15 – 0.25 |
| Coursera (with accredited university partner) | Yes — Credly / Coursera URL | `course` | 0.08 – 0.15 |
| Cisco, CompTIA, PMP, CKAD and similar | Yes — provider registry | `certification` | 0.15 – 0.35 |
| Udemy | No — self-generated certificate | Not standalone evidence |
| LinkedIn Learning | No — self-reported completion | Not standalone evidence |
| Coursera (no accredited partner) | No — self-generated | Not standalone evidence |

### The Udemy rule: artifacts over certificates

A Udemy certificate alone has no evidential weight in WorkProof. But a
GitHub project built during or after a Udemy course does — because the
project is a verifiable artifact. The course becomes context; the project
is the evidence.

This is the correct model for all unverified learning:

```
Udemy ML course + no project     = 0 WorkProof evidence
Udemy ML course + GitHub project = GitHub evidence (course is context, not evidence)
Google ML cert  + no project     = course evidence (0.10 weight)
Google ML cert  + GitHub project = course evidence + github evidence (higher confidence)
```

Implementations should surface this to candidates clearly: “Connect your
GitHub to show what you built with what you learned.” The combination of
a verified certificate and an artifact project is meaningfully stronger
than either alone.

### Certification evidence example

```json
{
  "type": "certification",
  "sourceId": "microsoft:transcript:AZ-900-2026",
  "description": "Microsoft Azure Fundamentals (AZ-900), passed March 2026",
  "weight": 0.22,
  "verifiedAt": "2026-03-15T00:00:00Z",
  "metadata": {
    "provider": "Microsoft",
    "certificationId": "AZ-900",
    "expiresAt": null,
    "verificationUrl": "https://learn.microsoft.com/api/credentials/..."
  }
}
```

### Connectors for learning platforms

The following connectors are planned for WorkProof implementations:

| Connector | What it pulls | Status |
|---|---|---|
| `microsoft-learn` | Certifications via Microsoft Transcript API | Planned |
| `google-learn` | Google Career Certificates via Credly | Planned |
| `credly` | Any Credly-hosted badge (Coursera, IBM, etc.) | Planned |
| `github-certifications` | GitHub Actions, Copilot, Security certifications | Planned |
| `aws` | AWS certification registry | Planned |

Self-reported platforms (Udemy, LinkedIn Learning) are intentionally not
connector targets. They can appear as contextual notes on a candidate’s
profile but do not contribute to WorkProof evidence weights.

---

## WorkProof for early-career professionals

WorkProof is designed to be accurate for professionals at every stage —
including college graduates and career-changers with no employer history.
The schema handles this honestly rather than forcing a mismatch.

### The honest representation

A college graduate’s WorkProof graph will show lower confidence scores
than a senior engineer’s. That is correct, not a flaw. A graduate with
strong assessment results and active GitHub projects might generate
confidence scores in the 0.45–0.65 range. A senior engineer with
employer attestation and years of production artifacts might reach
0.85–0.95. The gap is real and the schema reflects it accurately.

This is more honest than a resume. A graduate’s resume inflates
coursework into professional claims. A WorkProof graph shows what the
evidence actually supports — with growth velocity often running higher
than experienced practitioners who have stabilised in a domain.

### Evidence sources available to graduates

Graduates have more WorkProof evidence than they realise:

| Source | What it captures |
|---|---|
| Skill assessments | Standardised scores independent of employment history |
| GitHub | Personal projects, coursework repos, open source contributions, hackathon code |
| Academic evidence (`academic` type) | University coursework, thesis, capstone project authorship |
| Bootcamp evidence (`bootcamp` type) | Structured program completion, projects built during training |
| Hackathons | GitHub repos + peer collaboration edges from team events |
| Freelance work | Client project artifacts, GitHub activity, doc authorship |

No employer history is required. Assessments and GitHub activity alone are
sufficient to generate a valid WorkProof graph.

### Institutional attestation

Universities and bootcamps can act as attestation issuers — not just
employers. An institutional attestation follows the same W3C VC format as
an employer attestation, with `issuerType` set to indicate the institution
kind:

```json
{
  "id": "att_grad_01",
  "issuerName": "University of California, Berkeley",
  "issuerDomain": "berkeley.edu",
  "issuerDID": "did:web:berkeley.edu",
  "issuerType": "university",
  "period": {
    "start": "2022-09-01T00:00:00Z",
    "end": "2026-05-15T00:00:00Z"
  },
  "attestedClusters": [
    {
      "clusterId": "frontend-engineering",
      "confidence": 0.62,
      "note": "Completed CS upper division coursework. Primary author on senior capstone: distributed task scheduler, deployed to production."
    }
  ],
  "issuedAt": "2026-05-20T00:00:00Z",
  "candidateApproved": true,
  "revoked": false,
  "credentialFormat": "jwt_vc"
}
```

A bootcamp attestation uses `"issuerType": "bootcamp"` with the same
structure. Bootcamp attestations carry slightly lower weight than university
or employer attestations in the evidence model, reflecting the shorter and
less independently-verified context.

### Growth velocity as a primary signal

Growth velocity is often the strongest signal for a recent graduate.
A candidate actively shipping projects, completing assessments, and
contributing to open source may have a growth velocity of 0.80+ even with
lower absolute confidence scores. Recruiters hiring for trainable potential
— rather than specific depth — should weight velocity heavily.

Implementations targeting graduate hiring should surface `growthVelocity`
prominently in candidate-facing UIs and recruiter query results, not treat
it as a secondary field.

### Example: recent CS graduate WorkProof

```json
{
  "specVersion": "0.1",
  "summary": "Recent CS graduate with strong frontend assessment results and active GitHub history across four personal projects. Fast learner with high growth velocity — two new technical domains added in the last six months.",
  "growthEdge": "Moving from personal projects into collaborative open-source contribution. First OSS PR merged last month.",
  "growthVelocity": 0.81,
  "skillClusters": [
    {
      "id": "frontend-engineering",
      "name": "frontend-engineering",
      "displayName": "Frontend Engineering",
      "confidence": 0.58,
      "executionDepth": {
        "scale": "personal",
        "context": "Four personal React projects, one deployed. Senior capstone: interactive data visualisation tool."
      },
      "evidence": [
        {
          "type": "assessment",
          "sourceId": "talentproof:assessment:frontend-2026",
          "description": "Frontend assessment, score 88/100",
          "weight": 0.45,
          "verifiedAt": "2026-03-10T00:00:00Z"
        },
        {
          "type": "github",
          "sourceId": "github:repos:portfolio-site",
          "description": "React portfolio, 120 commits, deployed on Vercel",
          "weight": 0.25,
          "verifiedAt": "2026-04-01T00:00:00Z"
        },
        {
          "type": "academic",
          "sourceId": "berkeley:capstone:2026",
          "description": "Senior capstone: data visualisation tool, primary author",
          "weight": 0.20,
          "verifiedAt": "2026-05-01T00:00:00Z"
        }
      ]
    }
  ],
  "sources": [
    { "type": "assessment", "status": "active" },
    { "type": "github", "status": "active" },
    { "type": "university", "status": "active" }
  ],
  "attestations": [
    {
      "id": "att_grad_01",
      "issuerName": "UC Berkeley",
      "issuerType": "university",
      "issuerDomain": "berkeley.edu",
      "period": { "start": "2022-09-01T00:00:00Z", "end": "2026-05-15T00:00:00Z" },
      "attestedClusters": [
        { "clusterId": "frontend-engineering", "confidence": 0.55 }
      ],
      "candidateApproved": true,
      "revoked": false
    }
  ]
}
```

The lower confidence scores are accurate. The high growth velocity is the
differentiating signal. A recruiter looking for trainable early-career
talent gets an honest picture of both.

---

## Roadmap

| Version | Status | What's included |
|---|---|---|
| **v0.1** | Draft | Core schema, skill clusters, evidence model, attestation format, consent gate, agent card extension |
| v0.2 | Planned | JSON Schema file, TypeScript types npm package, attestation verification library |
| v0.3 | Planned | C2C collaboration graph protocol, peer vouching spec |
| v1.0 | Planned | Stable spec, reference implementation, registry protocol |

---

## Contributing

WorkProof is an open specification. Community feedback is welcome.

- **Discuss:** Open a GitHub Discussion for questions and proposals
- **Issues:** File an issue for spec ambiguities or errors
- **PRs:** Pull requests welcome for typos, examples, and clarifications
 — schema changes require Discussion first

See CONTRIBUTING.md for guidelines.

---

## Relationship to other protocols

| Protocol | Relationship |
|---|---|
| **MCP (Anthropic)** | WorkProof graph is exposed via MCP tools. MCP handles tool/data connections; WorkProof defines what the data means. |
| **A2A (Google / Linux Foundation)** | WorkProof extends the A2A Agent Card with professional identity fields. A2A handles agent communication; WorkProof provides the professional signal. |
| **W3C Verifiable Credentials** | WorkProof attestations use the W3C VC data model for employer-signed credentials. |
| **OpenAPI** | WorkProof registry APIs are described in OpenAPI 3.1. |

---

## License

MIT License. Copyright (c) 2026 TalentProof.

See LICENSE for full text.

---

## Citation

If you implement or reference the WorkProof schema in academic or
commercial work:

```
WorkProof Schema v0.1 (2026). TalentProof.
https://github.com/TalentProof/workproof-schema
```

# ~cmt/serra -

Minimal life tracker designed for Magic: The Gathering -

sourcehut git

## 关联链接

- https://learn.microsoft.com/api/credentials/...
- https://raw.githubusercontent.com/TalentProof/workproof-schema/main/schema/v0.1.json
- https://talentproof.ai/agents/priyasharma
- https://talentproof.ai/p/priyasharma

## 导航

- 项目页：[[10-项目/github.com_5a278adb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
