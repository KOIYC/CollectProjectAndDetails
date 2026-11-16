---
type: "corpus"
item_id: "2afb1df3f2eeb55c"
title: "Show HN: Attest – Test what AI agents do, not just what they say"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50509107"
project_url: "https://attest-framework.github.io/"
author: "tommathews"
published_at: "2026-11-15T18:03:01Z"
captured_at: "2026-11-16T10:00:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-15"
tags:
  - 语料
  - hn_show
  - author_tommathews
  - story_50509107
  - show_hn
metrics: {"points": 6, "comments": 0, "engagement_velocity": 6}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Attest – Test what AI agents do, not just what they say

> [!info] 一句话导读
> Skip to content Attest Framework

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50509107>
> 指标：点赞=6 · 评论=0 · engagement_velocity=6
> 作者：tommathews　|　发布：2026-11-15T18:03:01Z
> 项目链接：<https://attest-framework.github.io/>
> 采集：2026-11-16T10:00:05+08:00　|　id：`2afb1df3f2eeb55c`

## 正文

Skip to content Attest Framework
 Search Ctrl K Cancel
GitHub
 Overview
 Python SDK
 TypeScript SDK
 Guides
 Architecture
 Reference
 Migration
 Changelog
Attest
 Test what your AI agent says, does and changes. Replay recorded model responses. Check the results before merging.
Get Started (Python) Get Started (TypeScript) Run the demo (refund-desk)
Attest 1.1.0 is a testing framework for AI agents in Python and TypeScript. Check a reply, a sequence of tool calls or a change to external state with pytest or Vitest. Start with deterministic checks; add a model judge only for criteria those checks cannot express.
rec → replay → gate
 Section titled “rec → replay → gate”
A support agent refunded a customer twice after a payment timeout. Its output-only tests stayed green. That synthetic incident — INC-1042 — becomes a regression test in three moves:
● rec Capture the incident
 attest capture records the trace and model exchanges, applies redaction and drafts contracts from the run. A fixture marked consistent with the recording is not proof that the behavior is correct: review the fixture and choose independent business invariants.
▶ replay Replay in CI
 Strict replay runs your agent’s real code against recorded model responses through a local proxy, with zero live model calls for matching requests. It removes live-model variability, not other sources of flaky tests; tool dependencies and test isolation still need control.
✓ gate Gate the merge
 Checks report pass , fail or not_evaluated with a reason. Failed tests block by default ( tests_failed: block ); not_evaluated warns unless the policy sets not_evaluated: block . Require the policy check in branch protection. The gate covers the contracts and baselines you supply, not every possible regression.
The tour follows the double-refund ledger, reviewed contracts, a blocked revert PR, mutation scores and the HTML viewer. Its outputs illustrate the synthetic demo; the demo README has the current executable walkthrough.
expect ( trace ). tool_cardinality ( " issue_refund " , per = " order_id " , at_most = 1 )
attestExpect (trace) . toolCardinality ( " issue_refund " , { per: " order_id " , atMost: 1 });
One line of behavior contract states the rule INC-1042 broke — over the trace’s tool calls, not the reply text.
Six evaluated layers plus plugins
 Section titled “Six evaluated layers plus plugins”
The replay and gate run on deterministic checks. The layers are the full ladder of checks a contract or test can use, from free and instant to LLM-judged. Plugins add your own assertions. The table is generated from attest-engine capabilities --json .
1 Schema validation
 Checks the output against a JSON Schema.
Free
 2 Constraint checks
 Checks cost, token, latency and step-count limits.
Free
 3 Trace and behavioral checks
 Checks which tools ran, in which order, with which arguments, how often per business key, across the agent tree and against the world's final state.
Free
 4 Content pattern matching
 Checks the output text against substrings, patterns and keywords.
Free
 5 Embedding similarity
 Scores semantic similarity against a reference with an embedding model: OpenAI embeddings are paid, the local ONNX model is free.
Depends on provider
 6 LLM-as-judge
 Scores the output against a rubric with a judge model: OpenAI, Anthropic and Gemini judges are paid, a local ACP agent or an OpenAI-compatible local endpoint is not.
Depends on provider
 + Plugins
 Custom assertions that run in the SDK process; cost and determinism are the plugin's.
Defined by the plugin
What it looks like
 Section titled “What it looks like”
Python
 Section titled “Python”
from attest import agent, expect
@agent ( " weather-agent " )
def weather_agent ( builder , query : str ) -> dict :
# Recorded sample data: no model or weather API is called.
builder. add_tool_call (
" get_weather " ,
args = { " city " : " Tokyo " } ,
result = { " temperature_c " : 22 , " conditions " : " Sunny " } ,
)
return {
" message " : " Current weather conditions in Tokyo: sunny, 22°C. " ,
" structured " : { " city " : " Tokyo " , " temperature_c " : 22 },
}
def test_weather_agent ( attest ) :
result = weather_agent ( query = " What's the weather in Tokyo? " )
chain = (
expect ( result )
. required_tools ( [ " get_weather " ] ) # L3, free
. output_contains ( " Tokyo " ) # L4, free
. output_matches_schema ( { # L1, free
" type " : " object " ,
" required " : [ " city " , " temperature_c " ] ,
" properties " : {
" city " : { " type " : " string " },
" temperature_c " : { " type " : " number " },
},
} )
)
attest. evaluate ( chain )
dict: # Recorded sample data: no model or weather API is called. builder.add_tool_call( "get_weather", args={"city": "Tokyo"}, result={"temperature_c": 22, "conditions": "Sunny"}, ) return { "message": "Current weather conditions in Tokyo: sunny, 22°C.", "structured": {"city": "Tokyo", "temperature_c": 22}, }def test_weather_agent(attest): result = weather_agent(query="What's the weather in Tokyo?") chain = ( expect(result) .required_tools(["get_weather"]) # L3, free .output_contains("Tokyo") # L4, free .output_matches_schema({ # L1, free "type": "object", "required": ["city", "temperature_c"], "properties": { "city": {"type": "string"}, "temperature_c": {"type": "number"}, }, }) ) attest.evaluate(chain)">
Save this as test_weather_agent.py , install with uv add "attest-ai>=1.1.0" pytest , then run uv run pytest -v . Every assertion above is deterministic and requires no API key. For semantic checks, add output_similar_to or passes_judge after configuring the corresponding embedding or judge provider.
TypeScript
 Section titled “TypeScript”
import { agent, attestExpect } from ' @attest-ai/core ' ;
import { evaluate } from ' @attest-ai/vitest ' ;
import { test } from ' vitest ' ;
const weatherAgent = agent ( ' weather-agent ' , ( builder ) => {
// Sample data: no model or weather API is called.
builder . addToolCall ( ' get_weather ' , {
args: { city: ' Tokyo ' },
result: { temperature_c: 22 , conditions: ' Sunny ' },
} ) ;
return { message: ' Current weather conditions in Tokyo: sunny, 22°C. ' };
} );
test ( ' weather agent returns weather data ' , async () => {
const result = weatherAgent ( { query: ' What is the weather in Tokyo? ' } );
const chain = attestExpect (result)
. requiredTools ([ ' get_weather ' ]) // Layer 3: Free
. outputContains ( ' Tokyo ' ) // Layer 4: Free
. outputNotContains ( ' error ' ); // Layer 4: Free
await evaluate (chain);
});
{ // Sample data: no model or weather API is called. builder.addToolCall('get_weather', { args: { city: 'Tokyo' }, result: { temperature_c: 22, conditions: 'Sunny' }, }); return { message: 'Current weather conditions in Tokyo: sunny, 22°C.' };});test('weather agent returns weather data', async () => { const result = weatherAgent({ query: 'What is the weather in Tokyo?' }); const chain = attestExpect(result) .requiredTools(['get_weather']) // Layer 3: Free .outputContains('Tokyo') // Layer 4: Free .outputNotContains('error'); // Layer 4: Free await evaluate(chain);});">
Save as weather.test.ts and install with npm install -D "@attest-ai/core@>=1.1.0" "@attest-ai/vitest@>=1.1.0" "vitest@^4" . Run npx attest doctor once to download and check the engine before npx vitest run : a cold first download can exceed Vitest’s default timeout. This test makes no provider calls.
Features
 Section titled “Features”
Framework Adapters
 Provider and framework adapters for Python and TypeScript, each with a maturity tier - the table below lists them.
Multi-Agent Testing
 Beta: trace delegation chains and check parent-child relationships, ordering and cross-agent data flow.
Simulation Mode
 Beta: use mock tools, seeded faults and user personas. Your application’s own network calls still need mocks or replay.
Continuous Evaluation
 Experimental: sample application traces and alert on hard failures or score drift through Slack or webhooks.
Stable workflows include capture , strict replay , behavior contracts , world effects and CI policies and baselines . The overview links every feature and its maturity tier.
Adapter Python TypeScript
 OpenAI stable stable
 Anthropic stable stable
 Manual stable stable
 Gemini beta beta
 Ollama beta beta
 LangChain beta beta
 CrewAI beta Not available
 OpenTelemetry beta beta
 Google ADK experimental Not available
 LlamaIndex experimental Not available
 beta : Shipped and tested, but the interface or behavior can still change in a minor release.
 experimental : Shipped without a stability commitment and without demonstrated demand; it can change or be removed in any release.
 stable : Covered by the parity and conformance suites; a change in behavior is a breaking change.
 From attest-engine capabilities --json at engine 1.1.1.
How it compares
 Section titled “How it compares”
Capability Attest DeepEval Promptfoo Ragas LangWatch LangSmith
 SDK languages Python and TypeScript Python (pytest) and TypeScript (Vitest) CLI and library; "Use Python, Javascript, or any other language" Not assessed Python and TypeScript Not assessed
 Framework and provider integrations named on the page 10 Python and 7 TypeScript adapters 11 for Python and 6 for TypeScript, including LangChain, OpenAI, Anthropic, LlamaIndex, CrewAI, Google ADK Not assessed LangChain, LlamaIndex, "and more" Not assessed OpenAI, Anthropic, CrewAI, Vercel AI SDK, Pydantic AI
 Runs inside the unit-test runner pytest and Vitest pytest and Vitest Not assessed Not assessed Not assessed Not assessed
 LLM-as-judge Yes (layer 6) Yes (GEval) Not assessed Not assessed Not assessed Not assessed
 Deterministic assertions and per-layer cost classes Yes (layers 1-4 free; layers 5-6 depend on the provider) Not assessed Not assessed Not assessed Not assessed Not assessed
 Multi-agent traces and simulation Yes (beta) Not assessed Not assessed Not assessed Not assessed Not assessed
"Not assessed" means the cited page does not say. Primary sources, accessed on the date shown:
DeepEval: https://deepeval.com/docs/getting-started (accessed 2026-11-06)
 Promptfoo: https://www.promptfoo.dev/docs/intro/ (accessed 2026-11-06)
 Ragas: https://docs.ragas.io/en/stable/ (accessed 2026-11-06)
 LangWatch: https://langwatch.ai/docs/introduction (accessed 2026-11-06)
 LangSmith: https://docs.langchain.com/langsmith/observability.md (accessed 2026-11-06)
Get started
 Section titled “Get started”
Terminal window # Python
uv add " attest-ai>=1.1.0 " pytest
# TypeScript
npm install -D " @attest-ai/core@>=1.1.0 " " @attest-ai/vitest@>=1.1.0 " " vitest@^4 "
npx attest doctor
=1.1.0" pytestnpm install -D "@attest-ai/core@>=1.1.0" "@attest-ai/vitest@>=1.1.0" "vitest@^4"npx attest doctor">
Check the Python quickstart or TypeScript quickstart for a complete walkthrough.
Edit page

## 关联链接

- https://deepeval.com/docs/getting-started
- https://docs.langchain.com/langsmith/observability.md
- https://docs.ragas.io/en/stable/
- https://langwatch.ai/docs/introduction
- https://www.promptfoo.dev/docs/intro/

## 导航

- 项目页：[[10-项目/attest-framework.github.io_1f3625b9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
