---
type: "corpus"
item_id: "84b9e59a88c6fde4"
title: "Show HN: Composing domain-specific harness on Python in 10 mins"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49746313"
project_url: "https://cayu.dev/walkthrough"
author: "zamir_akimbekov"
published_at: "2026-09-17T20:46:00Z"
captured_at: "2026-09-20T09:36:46+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_zamir_akimbekov
  - story_49746313
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Composing domain-specific harness on Python in 10 mins

> [!info] 一句话导读
> Build a domain-specific agent — walkthrough

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49746313>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：zamir_akimbekov　|　发布：2026-09-17T20:46:00Z
> 项目链接：<https://cayu.dev/walkthrough>
> 采集：2026-09-20T09:36:46+08:00　|　id：`84b9e59a88c6fde4`

## 正文

Build a domain-specific agent — walkthrough | Cayu

# Build an agent that buys the right potatoes.

Start with a framework. Give the model a job, tools, and rules. Let the runtime carry the work through.

We’ll rebuild the logic of the campus dining demo. One agent helps a university choose a feasible purchase, drafts a proposal, and waits for approval before recording an order.

A walkthrough of the actual repository, using its native-tool path to keep the code readable. All supplier data and purchases are fictional. Code excerpts show parts of the application; they are not a complete script to paste into one file.

## Dinner for 400. A shortage to solve.

A university dining team needs to serve dinner tomorrow, but its usual potatoes are unavailable. The kitchen has some stock left and fewer staff than usual. Someone must find a replacement that provides enough food, arrives on time, and meets the budget and dietary requirements.

### The problem

The cheapest box is not always the best purchase. Whole potatoes cost less but take longer to prepare. Peeled potatoes cost more but may be the only option the available kitchen team can handle. Choosing well means checking supplier information against the meal plan, inventory, purchasing rules, and preparation time.

### Our solution

We build a dining purchasing agent with Cayu. It reads the kitchen’s requirements, investigates products, uses Python tools to calculate quantities and check constraints, and explains its recommendation. It saves a proposal for the team to review.

If the team later says more staff are available, the agent revisits the choice in the same session. When asked to place the order, it pauses for approval of the exact proposal. After approval, the application rechecks the facts, records the order, and the agent checks the receipt before reporting success. All purchases in this demo are fictional.

### What tools can the agent use?

The agent gets specific tools for the job:

- Read the dining plan: inspect the recipe, stock on hand, budget, delivery deadline, and staffing schedule.
- Find supplier products: search the catalog in the native-tool path used here. The browser version instead inspects a local supplier portal.
- Check a product: calculate whole cases needed, usable cooked quantity, total cost, and preparation time; check whether the option meets the purchasing rules.
- Read guidance and ask questions: find purchasing knowledge and ask the user for missing information. It can also request approval to save new knowledge and list available artifacts.
- Update the plan: record changes the user explicitly requests, such as staffing or attendance, and invalidate an outdated proposal.
- Prepare and submit a proposal: save a specific product and quantity for review, then request approval before recording an order.
- Verify the result: read the receipt for that proposal to confirm the purchase was recorded.

See the registered tools and their business operations.

Cayu supplies the framework and integrated runtime. The dining tools, knowledge, instructions, and approval rules form the domain-specific harness. The steps below show how those pieces become a working agent.

## The whole idea

| Part | What it does |
| --- | --- |
| Framework | Gives you the Python building blocks. |
| Harness | Combines those blocks with your domain code, tools, knowledge, and rules. |
| Runtime | Executes that setup, records progress, and handles pauses and continuation. |
| Agent | The product the user interacts with. |

Cayu includes the runtime. The harness is the system you assemble with Cayu. These are responsibilities within one application.

## Get the building blocks.

Cayu gives you types for agents, tools, policies, environments, and sessions. You decide what work they should do.

### Start a Cayu project.

For a new application, install Cayu and generate the project structure:

Commands for a new project

```
python3.11 -m venv .venv
source .venv/bin/activate
pip install cayu
cayu new dining-agent
cd dining-agent
```

The generated folders give each responsibility a home. Put the agent in `agents/`, its instructions in `prompts/`, actions in `tools/`, and rules in `policies/`. Keep business calculations in domain code.

To use the existing demo instead

The demo repository already has this structure. Clone it and use its dependency lock:

Existing demo · requires Python 3.11+ and uv

```
git clone https://github.com/cayu-tech/campus-dining-demo.git
cd campus-dining-demo
uv sync --extra dev --extra viewer --frozen
uv run --no-sync python demo.py init
```

The demo pins a specific Cayu Git revision. It does not simply track the newest PyPI package. The full browser showcase also needs Node, Docker, browser installation, and viewer setup; follow its README for that path. Live model calls require a separately configured provider credential.

### Define the job before the agent.

The user’s request is concrete:

> Dinner for 400 students tomorrow. Our usual potatoes are unavailable. We’re short-staffed. Prepare a draft only.

A good result is a purchase proposal that covers the meal shortfall, arrives on time, fits the kitchen’s capacity, and respects the budget and dietary requirements.

Write down what “done” means:

- Draft request: save a feasible proposal and explain the choice.
- Submission request: get approval for the exact proposal, record the order, and verify its receipt.

That definition drives the tools and tests you build next.

### Give the agent an identity and a model.

`AgentSpec` is a Cayu building block. The demo uses it for the agent’s name and model defaults. The factory adds the configured provider and prompt.

Source excerpt · agents/agent.py

```
"""Agent identity and settings; no application construction at import time."""

from cayu import AgentSpec

from prompts.agent import system_prompt

AGENT = AgentSpec(name="cayu-campus-dining-demo", model="gpt-5.6-sol")

def build_agent(settings, provider_name):
    return AGENT.model_copy(
        update={
            "model": settings.model,
            "provider_name": provider_name,
            "system_prompt": system_prompt(settings.customer, settings.browser),
        }
    )
```

This defines the agent. It does not give it access to meal plans or permission to place orders. You attach those capabilities next.

## Give the model a way to do the job.

Your harness is the combination of instructions, tools, data, policies, and checks around the model. This is where the agent becomes specific to campus dining.

### Put business truth in Python.

The meal needs 80 kg of cooked potatoes. The kitchen has 20 kg. The purchase must cover the remaining 60 kg.

The application calculates the number of cases using each product’s cooked yield. It rounds up to whole cases.

Source excerpt · catalog-app/catalog_app/planning.py

```
def assess(product, plan, cases=None):
    needed = max(
        0, plan["portions"] * plan["cooked_grams_per_portion"] - plan["available_cooked_grams"]
    )
    usable_per_case = (
        product["pack_count"] * product["grams_each"] * product["cooked_yield_bps"] // 10000
    )
    minimum_cases = (needed + usable_per_case - 1) // usable_per_case
    cases = minimum_cases if cases is None else cases
    if type(cases) is not int or not 0 <= cases <= 100:
        raise ValueError("Cases must be an integer from 0 to 100")
    total = cases * product["case_price_cents"]
    usable = cases * usable_per_case
    prep = cases * product["prep_minutes_per_case"]
```

The rest of `assess` checks recipe compatibility, supplier approval, dietary evidence, stock, budget, preparation time, and delivery.

| Option | Purchase | Cooked yield | Prep |
| --- | --- | --- | --- |
| Peeled potatoes | 7 cases / $175 | 66.5 kg | 35 minutes |
| Whole potatoes | 4 cases / $96 | 64 kg | 180 minutes |

With 45 minutes of kitchen capacity, peeled potatoes fit. Whole potatoes do not. The model gets these results from code, then explains the tradeoff.

Your contribution: the meaning of a feasible purchase. Cayu’s contribution: a way to run this calculation as an agent tool and return its result.

### Turn business operations into tools.

A tool gives the model a named action with defined inputs. Here is the assessment tool:

Source excerpt · tools/business.py

```
class AssessProduct(BusinessTool):
    @property
    def spec(self):
        return ToolSpec(
            name="assess_product",
            description="Calculate the minimum whole cases required after inventory and cooked yield, exact cost, prep time and eligibility against the current meal plan and purchasing policy. Compare plausible options; this tool does not rank or choose for you.",
            input_schema=schema({"meal_id": MEAL, "sku": SKU}),
            effect=ToolEffect.NONE,
        )

    def execute(self, ctx, args):
        return {
            "sku": args["sku"],
            **self.store.assess(self.customer, ctx.session_id, args["meal_id"], args["sku"]),
        }
```

Read it in three pieces:

1. `ToolSpec` tells Cayu and the model what the tool does and what arguments it accepts.
2. `ToolEffect.NONE` declares its read-only effect contract.
3. `execute` calls the business implementation.

`self.customer` is bound by the application. `ctx.session_id` comes from Cayu. The model supplies the meal and product IDs, not arbitrary customer scope or SQL.

The shared `BusinessTool` base class wraps the return value in a Cayu `ToolResult`. Cayu can then record it and pass it back to the model.

The demo exposes other narrow actions too: inspect a plan, revise it, prepare a proposal, request submission, and verify a receipt.

### Tell the model how to work.

The prompt supplies a method. It tells the model to read the policy, inspect the meal, and use actual quantities and constraints.

Source excerpt · prompts/agent.py

```
Read the known knowledge entry "purchasing-policy" with read_knowledge. Inspect the relevant meal
with inspect_dining_plan before asking questions: dinner is the potato side, rice-lunch the rice side,
and vegetable-side the carrot side. These are current meal records, not a rule limiting purchases
to one ingredient. If the request does not match a meal, clarify its use and requirements rather than
pretending the existing meal plan describes it.

Use the plan's recipe quantities, inventory, remaining budget, receiving deadline, staffing capacity,
and verified dietary requirements. Do not invent missing information or silently override a customer's
explicit quantity. Existing kitchen stock reduces what must be purchased. A cheap case can cost more
per usable cooked kilogram or require more labor. Price, delivery, product form and preparation effort
all matter. Explain meaningful tradeoffs using the actual data you obtain.
```

The prompt does not name a winning SKU. The model investigates candidates, calls the assessment tool, and recommends an option using the returned evidence.

In native development mode, `search_catalog` finds products. In the browser showcase, `browser_session` inspects a local supplier portal. Both paths use the same purchasing calculations.

Instructions guide the model. Checks in the tool and business code enforce the rules when an action runs.

### Add knowledge and control what enters context.

The demo stores purchasing guidance in Cayu’s knowledge store. The agent can read the known `purchasing-policy` entry. Its context policy can also recall relevant knowledge.

The recall source is configured explicitly:

Source excerpt · memory/context.py

```
sources=AutomaticRecallSourceConfig(
    include_knowledge=True,
    include_transcript=False,
    knowledge_required=True,
    transcript_required=False,
    knowledge_namespace=(settings or settings_from_environment()).namespace,
```

This selects knowledge from the configured namespace. It does not enable retrieval of older transcript episodes. The current session still has its conversation history.

Keep three things separate:

- Knowledge: durable purchasing guidance.
- Business records: inventory, plans, proposals, and receipts.
- Context: what the model sees for its next decision.

Cayu supplies storage and recall components. You decide what to store, who can access it, and what the model should receive.

### Make approval a real gate.

A proposal is a draft. Submitting it is a separate action. The demo’s tool policy requires approval for that action:

Source excerpt · policies/tools.py

```
def build_tool_policy(names):
    rules = {
        "ask_user": (RequiredFieldRule("question"),),
        "remember_knowledge": (DenyPatternRule("text", patterns=(r"(?s).*",)),),
        "submit_proposal": (DenyPatternRule("proposal_id", patterns=(r"(?s).*",)),),
    }
    if "browser_session" in names:
        rules["browser_session"] = (RequiredFieldRule("operation"),)
    return ParameterConstrainedToolPolicy(
        rules,
        decision=ToolPolicyDecision.REQUIRE_APPROVAL,
        execution_profile_identity=ExecutionProfileBehaviorIdentity(
            name="campus-demo:approval-policy",
            behavior_version="1",
            implementation_version="2026-09-09.1",
        ),
    )
```

The catch-all rule on `proposal_id` combines with `REQUIRE_APPROVAL`. When the model requests submission, Cayu pauses before the tool executes.

The application also defines the review fields: product, quantity, cost, plan revision, preparation, delivery, proposal ID, and digest. The digest is a fingerprint of the proposal’s contents.

The model saying “approved” does not resolve the gate. The application submits a structured decision for the exact pending call.

Tool visibility is configured separately. The demo uses `StaticToolExposurePolicy` to decide which registered tools the model can see.

### Assemble the harness.

This is the key call in the example:

Source excerpt · agents/registration.py

```
def register_agents(
    app, settings, provider_name, store, context_policy, bridge=None, recorded_tools=()
):
    tools = build_agent_tools(store, settings)
    if bridge is not None:
        tools.extend(recorded_tools or bridge.tools)
    names = [t.spec.name for t in tools]
    app.register_agent(
        build_agent(settings, provider_name),
        tools=tools,
        execution_requirements=bridge.execution_requirements if bridge else None,
        context_policy=context_policy,
        tool_policy=build_tool_policy(names),
        tool_exposure_policy=build_tool_exposure_policy(names),
    )
```

Each argument attaches a part of the system:

- `build_agent(...)`: identity, model, and instructions.
- `tools`: the actions this agent can request.
- `context_policy`: how context is assembled.
- `tool_policy`: what may execute and when approval is needed.
- `tool_exposure_policy`: what the model can see.

This composition is the domain-specific harness. It lives across normal Python modules. It does not require one large class named “Harness.”

## Run the system you assembled.

The harness defines the behavior. Cayu’s runtime carries out the model-and-tool loop and maintains the execution record.

### Wire the application and durable stores.

`build_app()` creates stores, configures the provider, selects an environment, and registers the dining agent.

The demo passes the stores into Cayu explicitly:

Source excerpt · app.py

```
app = CayuApp(
    human_review_policy=OrderReview(settings),
    browser_control=browser_control_options(settings),
    session_store=stores.session_store,
    task_store=stores.task_store,
    knowledge_store=stores.knowledge_store,
    knowledge_access_scope=scope,
    config=runtime.config,
    enable_logging=runtime.enable_logging,
    request_footprint=runtime.request_footprint,
    knowledge_review_namespace=runtime.knowledge_review_namespace,
)
```

The stores come from `configuration/storage.py`. It constructs `SQLiteSessionStore`, `SQLiteTaskStore`, and `SQLiteKnowledgeStore`.

A bare `CayuApp()` defaults to in-memory stores. Durable behavior depends on configuring persistent stores and keeping the underlying data.

| Cayu records | The dining app records |
| --- | --- |
| Session identity, transcript, events, checkpoints, pending approval. | Meal revisions, product stock, proposals, order receipts. |

The application’s `PortalStore` owns purchasing transactions. Cayu’s session store owns execution state. Both are needed.

An environment supplies tool resources. The native path uses artifacts and knowledge; the browser path adds a restricted browser environment. Native Python business tools are trusted application code, not automatically sandboxed by Cayu.

### Start a session and consume its events.

The demo constructs a request with the user’s message and execution limits:

Source excerpt · operations/interaction.py

```
def request(message, session_id=None):
    return RunRequest(
        agent_name="cayu-campus-dining-demo",
        session_id=session_id,
        messages=[Message.text("user", message)],
        max_steps=28,
        limits=run_limits(),
        retry_policy=RetryPolicy(max_attempts=1, max_unknown_attempts=1),
    )
```

It then calls `app.run(request)`. Cayu repeats this loop:

The model may request another action, ask for input, or finish. Your application consumes the event stream to display progress and outcomes.

The demo limits its main interaction path to 24 tool calls, 28 steps, and 300 elapsed seconds, plus a configured token ceiling. Those runtime limits are separate from the meal’s purchasing budget.

For the original request, the agent should finish with a seven-case peeled-potato draft for $175. No order should exist.

### Continue when the facts change.

> We now have the full kitchen team. Reconsider.

The demo loads the existing session and uses `app.resume` for the new message:

Source excerpt · operations/interaction.py

```
async def run_or_resume(app, message, session_id=None):
    existing = await app.session_store.load(session_id) if session_id else None
    events = (
        app.resume(ResumeRequest(session_id=session_id, messages=[Message.text("user", message)], max_steps=28, limits=run_limits(), retry_policy=RetryPolicy(max_attempts=1, max_unknown_attempts=1)))
        if existing is not None else app.run(request(message, session_id))
    )
    async for event in events:
        yield event
```

The model requests a plan revision. Application code changes preparation capacity from 45 to 240 minutes and invalidates the old proposal.

Whole potatoes now fit: four cases, 64 kg cooked, 180 minutes of preparation, $96. The agent can recommend a new draft that saves $79.

Cayu preserves the conversation and execution record. The domain code controls plan revisions and stale proposals. The model uses the new evidence to make the next decision.

### Approve, execute, and verify.

When the user asks to submit, the model calls `submit_proposal` with the exact proposal ID and digest.

1. Cayu pauses. The configured policy requires approval.
2. The application presents the proposal. The reviewer sees the exact business facts.
3. The human decides. The application resolves the pending call with `app.resolve_tool_approval(...)`.
4. Business code rechecks. The plan, policy, product facts, stock, and proposal must still match.
5. Business code writes a receipt. The stock decrement and receipt are recorded in one transaction.
6. The agent verifies. It reads the receipt for that proposal before claiming success.

Source excerpt · tools/business.py

```
class VerifySubmission(BusinessTool):
    @property
    def spec(self):
        return ToolSpec(
            name="verify_submission",
            description="Independently read the purchase receipt for the exact proposal and current customer/session. Only a matching recorded receipt proves purchase.",
            input_schema=schema({"proposal_id": {"type": "string", "maxLength": 64}}),
            effect=ToolEffect.NONE,
        )

    def execute(self, ctx, args):
        self.store.proposal(args["proposal_id"], self.customer, ctx.session_id)
        return {
            "orders": [
                o
                for o in self.store.orders(self.customer)
                if o["proposal_id"] == args["proposal_id"]
            ]
        }
```

Repeated submission of the same proposal returns the existing receipt. That safe repeat behavior is implemented by the dining application.

#### Where “long-horizon” enters

Work can span decisions, new facts, human waits, and process boundaries. Durable records let the application continue from what is known instead of relying on one live process.

A production integration must still handle uncertain external effects. If a supplier accepted an order but its response was lost, query the supplier or reconcile before retrying.

Cayu offers optional worker, task, and recovery machinery. This demo’s core dining flow uses direct run/resume calls. Registering a task store does not start a background worker, and this short example does not prove days-long production execution.

## Prove the business outcome.

A plausible answer is easy to generate. Test whether the agent’s actions produce the right result.

### Test the rules, then test the model.

Start with deterministic business tests. The demo checks the exact short-staffed outcome:

Source excerpt · tests/test_agent.py

```
def test_short_staffed_meal_requires_prepared_option(settings):
    store = PortalStore(settings.portal_database)
    options = {
        p["sku"]: store.assess(CUSTOMER, "s1", "dinner", p["sku"])
        for p in store.products("potatoes")
    }
    assert [sku for sku, r in options.items() if r["eligible"]] == ["POT-PEELED-10KG"]
    result = options["POT-PEELED-10KG"]
    assert (
        result["shortfall_cooked_grams"],
        result["cases"],
        result["usable_cooked_grams"],
        result["total_cents"],
        result["prep_minutes"],
    ) == (60000, 7, 66500, 17500, 35)
    assert any("preparation" in r for r in options["POT-WHOLE-20KG"]["reasons"])
    assert any("deadline" in r for r in options["POT-FROZEN-10KG"]["reasons"])
    assert any("dietary" in r for r in options["POT-MASH-10KG"]["reasons"])
```

Then test the runtime path with a scripted provider. It emits predetermined tool calls so you can check that submission pauses, denial creates no order, and approval produces the expected receipt.

Credential-free checks in the configured demo checkout

```
uv run --no-sync pytest -q tests/test_agent.py tests/test_application.py
uv run --no-sync python -m evals.run
```

The nine-case contract eval suite checks exact purchasing outcomes and the submission gate. It does not approve an order.

Finally, run live-model evaluations to check whether the model chooses the right actions from the user’s request. These require provider credentials and incur usage.

Scripted tests prove execution behavior. Live evaluations test the model’s decisions. You need evidence for both.

## What you built

You used Cayu’s framework to assemble a purchasing harness: instructions, knowledge, business tools, approval policy, and verification.

You configured its runtime to execute that harness with persistent sessions, controlled tool calls, and human pauses.

The result is an agent that can investigate a shortage, produce a feasible proposal, adapt to new facts, and record a purchase only through the configured approval path.

Cayu provides the machinery. You define what good work means in your domain.

## Source and scope

This guide follows the campus dining demo at `d297d9eb…`. Its Cayu dependency is pinned to `c5816d06…`. Every source excerpt links to the inspected revision.

The excerpts are tied to the inspected demo revision. Use the demo’s dependency lock and README to reproduce that version. The browser showcase and live-model path require additional setup; the tests described above cover different parts of the application.

This walkthrough does not execute an agent or place an order. Follow the linked source and setup instructions to run the fictional demo yourself.

# https://easiest.ai/

## 关联链接

- https://easiest.ai/
- https://github.com/cayu-tech/campus-dining-demo.git

## 导航

- 项目页：[[10-项目/cayu.dev_1eb9e80e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
