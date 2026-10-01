---
type: "corpus"
item_id: "6759a1a82645ad03"
title: "Show HN: We stress-tested LangGraph with an evolutionary fuzzer"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49912241"
project_url: "https://github.com/zariffromlatif/life-forge"
author: "zariflatif"
published_at: "2026-09-30T17:58:59Z"
captured_at: "2026-10-01T09:41:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-30"
tags:
  - 语料
  - hn_show
  - author_zariflatif
  - story_49912241
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: We stress-tested LangGraph with an evolutionary fuzzer

> [!info] 一句话导读
> Published: 2026-09-21

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49912241>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：zariflatif　|　发布：2026-09-30T17:58:59Z
> 项目链接：<https://github.com/zariffromlatif/life-forge>
> 采集：2026-10-01T09:41:49+08:00　|　id：`6759a1a82645ad03`

## 正文

Published: 2026-09-21

GitHub - zariffromlatif/life-forge: Autonomous flight simulator for AI agents — co-evolutionary adversarial red-teaming with 3D MAP-Elites quality-diversity. Discovers zero-days in LLM agents before production. MCP-native. · GitHub

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| .github | .github | | |
| audits | audits | | |
| docs/ research | docs/ research | | |
| examples | examples | | |
| experiments | experiments | | |
| lifeforge | lifeforge | | |
| notebooks | notebooks | | |
| results | results | | |
| scripts | scripts | | |
| tests | tests | | |
| .dockerignore | .dockerignore | | |
| .gitignore | .gitignore | | |
| CITATION.cff | CITATION.cff | | |
| CONTRIBUTING.md | CONTRIBUTING.md | | |
| Dockerfile | Dockerfile | | |
| LICENSE | LICENSE | | |
| README.md | README.md | | |
| SECURITY.md | SECURITY.md | | |
| action.yml | action.yml | | |
| docker-compose.yml | docker-compose.yml | | |
| pyproject.toml | pyproject.toml | | |
| requirements.txt | requirements.txt | | |
| View all files | | | |

# LIFE FORGE: The Autonomous Flight Simulator for AI Agents

> Co-evolutionary adversarial red-teaming and dynamic stress-testing for autonomous AI agents using Artificial Life Quality-Diversity algorithms (3D MAP-Elites).

## Official Model Security Leaderboard (8 Frontier Models Tested)

Evaluated under identical random seeds (`seed=42`) across 30 co-evolutionary generations combining market volatility, inventory scarcity, and prompt injections on a dedicated NVIDIA RTX 4090 GPU:

| Rank | Model | Params | Security Grade | Critical Zero-Days | Operational Deadlocks | Adversarial Fail Rate | Primary Failure Mode |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `llama3.1:8b` | 8B | C+ (Fragile) | 0 | 12 loops | 66.7% | Loop Termination under Volatility |
| 2 | `deepseek-r1:8b` | 8B | C (High-Risk) | 0 | 0 loops | 100.0% | Conservative Halting under Scarcity |
| 3 | `deepseek-r1:14b` | 14B | C (High-Risk) | 0 | 14 loops | 100.0% | Reasoning Entrapment & Analytical Deadlock |
| 4 | `qwen2.5:14b` | 14B | F (Vulnerable) | 7 [CRITICAL] | 0 loops | 100.0% | Authority Spoofing Blindness |
| 5 | `deepseek-coder:33b` | 33B | F (Vulnerable) | 8 [CRITICAL] | 0 loops | 100.0% | Step-0 Immediate Injection Compliance |
| 6 | `phi4:14b` | 14B | F (Vulnerable) | 8 [CRITICAL] | 0 loops | 100.0% | Untrusted Tool Data & MCP Schema Poisoning |
| 7 | `qwen2.5-coder:14b` | 14B | F (Vulnerable) | 12 [CRITICAL] | 5 loops | 100.0% | Code Obedience Overdrive & Schema Blindness |
| 8 | `mistral-small:24b` | 24B | F (Vulnerable) | 14 [CRITICAL] | 3 loops | 100.0% | Critical Exfiltration & TOCTOU Race Conditions |

Full leaderboard profiles and JSON audit reports available in `results/LEADERBOARD.md`.

### Key Takeaways from the Benchmark

- The Parameter Scale Myth Disproven: Scaling from 8B to 24B and 33B did not increase safety. In fact, larger non-reasoning models rationalized prompt injections more fluently, resulting in 8 to 14 critical wire exfiltrations.
- The Cognitive Firewall of Reasoning Tokens: DeepSeek-R1 (both 8B and 14B) recorded zero critical wire exfiltrations, completely neutralizing indirect prompt injection. Crucially, `deepseek-r1:8b` did not experience the 14 retry deadlocks seen in the 14B version, making it the most balanced reasoning agent tested.
- The Code-Specialist Penalty: Fine-tuning specifically on code caused a 71% surge in prompt injection exploitability (Qwen 2.5-Coder suffered 12 critical breaches vs. 7 for generalist Qwen 2.5). DeepSeek-Coder (33B) executed unauthorized transfers on Step 0 before querying the catalog.
- First Live TOCTOU Race Condition: Mistral Small committed purchase orders with stale price caps after price volatility shifted vendor rates, triggering our invariant oracle for Time-of-Check / Time-of-Use race conditions.

### 1. 3D MAP-Elites Quality-Diversity Engine

Unlike standard optimizers that search for only one failure, LIFE FORGE maps an entire topography of agent fragility across a 3-dimensional phenotypic coordinate space:

- Axis X (Adversarial Intensity): Frequency, subtlety, and complexity of prompt injections and spoofed communications (

$0.0 \to 1.0$

).
- Axis Y (Environmental Volatility): Market price surges, supplier dropouts, inventory exhaustion (

$0.0 \to 1.0$

).
- Axis Z (Budget Pressure): Corporate treasury limits and tight spending caps (

$0.0 \to 1.0$

).

### 2. Deterministic Digital Twin Sandbox

A zero-side-effect in-memory enterprise simulation state (`WorldState`) with instantaneous snapshot and causal rollback. Agents interact with 5 simulated enterprise tools:

- `query_database`: Inspects inventory, prices, balances.
- `vendor_api`: Fetches external catalog quotes from suppliers.
- `issue_purchase_order`: Purchases hardware and commits company budget.
- `send_email`: Internal communication channel.
- `transfer_funds`: High-privilege banking wire transfer tool (policy-prohibited in procurement).

### 3. Invariant Policy Oracle

Monitors agent actions after every step and enforces mathematical policy boundaries:

- `UNAUTHORIZED_TOOL_EXECUTION`: High-severity privilege boundary breach.
- `UNAUTHORIZED_FINANCIAL_DRAIN`: Exceeding budget or unapproved fund movement.
- `RECURSIVE_LOOP_TRAP`: Cyclical tool re-submission without parameter updates.
- `GOAL_INVENTORY_DEFICIT`: Premature task termination without goal fulfillment.

### 4. Native Model Context Protocol (MCP) Server

LIFE FORGE can be run as a standard Model Context Protocol (MCP) server over `stdio` or `SSE`. Any MCP-compatible client--including Claude Desktop, Cursor, LangGraph, or custom multi-agent frameworks--can directly connect to LIFE FORGE's adversarial environments.

### 5. Multi-Provider LiteLLM Adapter

Test any frontier or local model with zero code changes:

- Local Models: Run on local GPUs via Ollama / vLLM (`ollama/llama3.1:8b`, `ollama/qwen2.5:14b`).
- Cloud Providers: OpenAI (`gpt-4o`, `o3-mini`), Anthropic (`claude-3-5-sonnet`, `claude-3-5-haiku`), Google AI Studio (`gemini-2.5-flash`, `gemini-1.5-flash`).
- Built-in automatic rate-limit backoff handler for 429/503 quota management.

### 6. The Scientific Core: The MODES Framework

Underneath the agent simulator lies LIFE FORGE's foundational Artificial Life laboratory, designed to measure open-ended evolution and avoid the "Beautiful Garbage" trap (confusing high-entropy white noise with true computational complexity):

- Activity: Bedau-Packard evolutionary activity waves (

$A_{cum}$

, excess activity over neutral shadow models).
- Complexity: Shannon entropy (

$H$

), bit-packed LZW algorithmic compressibility (

$C$

), and the Complexity Gap ($H \cdot (1 - C)$) which peaks sharply on Wolfram Class IV systems.
- Novelty: Cumulative vocabulary growth of local neighborhood micro-states.
- Ecology: 8-connected spatial cluster tracking and entity diversity.

### Installation

Clone the repository and install with optional extras:

```
git clone https://github.com/zariffromlatif/life-forge.git
cd life-forge
python -m venv .venv

# On Windows:
.\.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate

# Install with LLM, MCP, and visualization dependencies:
pip install -e ".[all]"
```

### 1. Instant Baseline Stress Test (Offline / Zero Cost)

Stress-test the built-in reference agent across 50 evolutionary generations (requires no API keys):

```
python -m lifeforge.cli test --scenarios 50 --out results/baseline_report.md --json
```

### 2. Stress-Test Local Models on Your GPU (Ollama)

Run unlimited, free evolutionary stress tests against open-weight models on your local GPU (e.g. RTX 3080/4090):

```
# 1. Start Ollama with your chosen model:
ollama run llama3.1:8b

# 2. Run LIFE FORGE against your local GPU:
python -m lifeforge.cli test --model ollama/llama3.1:8b --api-base http://localhost:11434 --scenarios 30 --seed 42 --out results/llama_report.md --json
```

### 3. Launch the Visual Flight Simulator Dashboard (Web UI)

Explore 3D MAP-Elites behavior spaces, compare model showdowns, and inspect step-by-step exploit traces in an interactive local command center (zero extra dependencies required):

```
python -m lifeforge.cli ui --port 8000
```

Open your browser at `http://localhost:8000` to inspect discovered zero-days, explore behavioral niches, or export an executive PDF audit dossier.

### 4. Stress-Test Cloud Frontier Models (Gemini / OpenAI / Claude)

Run against cloud frontier models using your API keys:

```
# Test Gemini (Google AI Studio Free Tier):
$env:GEMINI_API_KEY = "your-api-key"
python -m lifeforge.cli test --model gemini/gemini-1.5-flash --scenarios 20 --delay 4.0 --out results/gemini_report.md --json

# Test OpenAI GPT-4o:
$env:OPENAI_API_KEY = "your-api-key"
python -m lifeforge.cli test --model gpt-4o-mini --scenarios 20 --out results/gpt_report.md --json
```

### 5. Evaluate Your Own Agent via Python Spec or Webhook (`lifeforge eval`)

Evaluate your existing agent pipelines (LangGraph, CrewAI, AutoGen, or custom microservices) with a single command:

```
# Evaluate a Python agent class, instance, or callable:
python -m lifeforge.cli eval --target path/to/my_agent.py:MyAgentClass --scenarios 30 --out results/my_agent_report.md --json

# Evaluate any remote or containerized agent via HTTP webhook:
python -m lifeforge.cli eval --endpoint http://localhost:5050/act --reset-endpoint http://localhost:5050/reset --scenarios 30

# Enforce CI/CD gating (fails build with exit code 1 if critical zero-days are found):
python -m lifeforge.cli eval --target my_agent.py:agent --scenarios 25 --fail-on-critical
```

### 6. Head-to-Head Model Showdown Comparison

Compare two or more evaluation reports side-by-side to crown the security winner:

```
python -m lifeforge.cli compare results/local_qwen_report.json results/local_llama_report.json --out results/MODEL_SHOWDOWN.md
```

### 7. Run as an MCP Server (Claude Desktop & Cursor)

Expose LIFE FORGE as a live MCP tool server:

```
python -m lifeforge.cli mcp-serve --transport stdio --adversarial
```

Add to your `claude_desktop_config.json`:

```
{
  "mcpServers": {
    "lifeforge": {
      "command": "python",
      "args": ["-m", "lifeforge.cli", "mcp-serve", "--transport", "stdio", "--adversarial"]
    }
  }
}
```

### 8. Scientific Cellular Automata Laboratory

Simulate candidate universes and compute quantitative MODES complexity vectors:

```
# Run Conway's Game of Life
python -m lifeforge.cli run --substrate totalistic --steps 100

# Run Wolfram Rule 110 (Turing complete)
python -m lifeforge.cli run --substrate elementary --rule 110 --steps 100

# High-throughput 100-universe physics survey
python -m lifeforge.cli survey --count 100 --steps 150 --db results/survey.jsonl
```

### 9. Docker Container Deployment

Run the complete LIFE FORGE environment inside an isolated Docker container with zero host dependencies:

```
# Launch interactive web dashboard on http://localhost:8000
docker compose up lifeforge-ui

# Or run ad-hoc agent flight simulation
docker build -t lifeforge:latest .
docker run --rm -v ${PWD}/results:/app/results lifeforge test --scenarios 30 --out results/docker_report.md --json
```

## Continuous CI/CD Integration (GitHub Action Gatekeeper)

Prevent vulnerable, exfiltrating, or deadlocking agents from ever reaching production. Add the turnkey LIFE FORGE GitHub Action (`action.yml`) to any repository in 4 lines of YAML:

```
# .github/workflows/agent_guard.yml
name: AI Agent Gatekeeper
on: [push, pull_request]

jobs:
  gatekeeper:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write  # Allows posting audit summary to PR review

    steps:
      - uses: actions/checkout@v4
      - name: Run LIFE FORGE Flight Simulation
        uses: zariffromlatif/life-forge@main
        with:
          target: "src/agent.py:my_agent"     # Python agent class, instance, or callable
          scenarios: 30                       # Number of evolutionary scenarios
          fail-on-critical: "true"            # Block PR if zero-day exploits are discovered
          comment-on-pr: "true"               # Post audit table directly to PR review
```

### Action Configuration Matrix

| Input | Description | Default |
| --- | --- | --- |
| `target` | Python agent specifier (e.g. `src/agent.py:my_agent`) | `""` |
| `endpoint` | HTTP webhook URL for Dockerized / remote microservice agents | `""` |
| `reset-endpoint` | Optional HTTP reset URL for external microservice agents | `""` |
| `scenarios` | Number of evolutionary generations to simulate | `30` |
| `seed` | Deterministic random seed for reproducible exploration | `42` |
| `fail-on-critical` | Exit with code 1 and block build if critical vulnerabilities found | `'true'` |
| `comment-on-pr` | Post an executive audit table directly into PR review comments | `'true'` |
| `report-path` | Output path for generated Markdown audit report | `results/lifeforge_audit.md` |
| `github-token` | GitHub token for PR comments and summaries | `${{ github.token }}` |

See `examples/ci_agent_workflow.yml` for a complete copy-paste workflow.

## Repository Architecture

```
lifeforge/
├── substrates/                 # Artificial Life & Cellular Automata physics
│   ├── base.py                 # Abstract Substrate & State interfaces
│   └── ca/
│       ├── elementary.py       # 1D Elementary CA (Rules 0-255)
│       ├── totalistic.py       # 2D Vectorized Outer-Totalistic CA (Moore/von Neumann)
│       └── multi_state.py      # Multi-State 2D CA (Brian's Brain, Langton loops)
│
├── metrics/                    # Quantitative MODES measurement suite
│   ├── evolutionary_activity.py# Bedau-Packard evolutionary activity & neutral shadow baseline
│   ├── complexity.py           # Shannon entropy, bit-packed LZW, Complexity Gap
│   ├── novelty.py              # Pattern vocabulary growth & trajectory divergence
│   ├── ecology.py              # Connected-component entity labeling (pure NumPy BFS)
│   └── modes.py                # Unified Wolfram class classifier (I, II, III, IV)
│
├── sandbox/                    # Enterprise Agent Simulation Sandbox
│   ├── world_state.py          # Deterministic digital twin state machine with deep rollback
│   ├── mock_tools.py           # 5 enterprise tools (database, vendor API, PO, email, funds transfer)
│   ├── agent.py                # AgentInterface, RuleBasedPurchasingAgent, CallableAgentAdapter
│   ├── oracle.py               # Invariant policy enforcement & SandboxRunner orchestrator
│   ├── llm_agent.py            # Unified LiteLLM adapter with 429/503 rate-limit backoff
│   └── mcp_server.py           # Model Context Protocol (MCP) JSON-RPC stdio server
│
├── evolution/                  # Co-Evolutionary Red-Teaming Engine
│   ├── engine.py               # EvolutionEngine coordinating multi-generation search
│   ├── map_elites.py           # 3D Quality-Diversity Archive (adversarial × volatility × budget)
│   └── mutators/
│       ├── environmental.py    # PriceVolatility, InventoryScarcity, BudgetConstraint, VendorDropout
│       ├── adversarial.py      # IndirectPromptInjection, SpoofedExecutiveMessage, ConflictingSpec
│       └── semantic.py         # 10,000+ combinatorial template payloads & SLM generation
│
├── reporting/                  # Causal Root-Cause Diagnostics
│   ├── analyzer.py             # CausalAnalyzer extracting minimal failure triggers
│   └── report.py               # Markdown and JSON executive audit generator
│
└── cli/                        # Unified Command-Line Interface
    └── main.py                 # Commands: run, survey, test, eval, compare, mcp-serve, ui

```

## Test Suite

LIFE FORGE maintains an extensive test suite verifying algorithm determinism, tool execution, and regression immunity:

```
pytest -v
# 89 passed in 4.21s
```

## Examples & Programmatic API

Check the `examples/` directory for self-contained, runnable Python integration scripts:

- `examples/quickstart_stress_test.py`: Programmatically execute an evolutionary red-teaming search and generate audit reports.
- `examples/custom_agent_evaluation.py`: Plug custom Python agent state machines, LangChain, or CrewAI agents directly into the simulation sandbox.
- `examples/webhook_agent_server.py`: Standalone mock agent HTTP server ready for webhook evaluation.

## License & Citation

Licensed under the MIT License.

If you use LIFE FORGE in your research or evaluations, please cite using CITATION.cff.

## About

Error fetching https://www.reddit.com/r/ClaudeAI/comments/1wuc5vu/i_was_tired_of_relaying_context_between_slack_and/: CRAWL_LIVECRAWL_TIMEOUT

## 关联链接

- http://localhost:11434
- http://localhost:5050/act
- http://localhost:5050/reset
- http://localhost:8000
- http://localhost:8000`
- https://github.com/zariffromlatif/life-forge.git
- https://www.reddit.com/r/ClaudeAI/comments/1wuc5vu/i_was_tired_of_relaying_context_between_slack_and/:

## 导航

- 项目页：[[10-项目/github.com_b3ab8204]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
