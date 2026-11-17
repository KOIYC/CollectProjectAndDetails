---
type: "corpus"
item_id: "4eb296f9901966fc"
title: "Show HN: Sutra-OS – A self-hosted ontology platform"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50525052"
project_url: "https://github.com/0nelight/sutra-os"
author: "0nelight"
published_at: "2026-11-16T23:25:41Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_0nelight
  - story_50525052
  - show_hn
  - front_page
metrics: {"points": 37, "comments": 13, "engagement_velocity": 37}
comments_count: 13
comments_total: 13
discovered_via: "hn:show_hn:3d"
---

# Show HN: Sutra-OS – A self-hosted ontology platform

> [!info] 一句话导读
> Scarce Units, Typed, Related, Actionable. An open-source, self-hosted ontology platform.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50525052>
> 指标：点赞=37 · 评论=13 · engagement_velocity=37
> 作者：0nelight　|　发布：2026-11-16T23:25:41Z
> 项目链接：<https://github.com/0nelight/sutra-os>
> 采集：2026-11-17T11:09:12+08:00　|　id：`4eb296f9901966fc`

## 正文

# 0nelight/sutra-os

Scarce Units, Typed, Related, Actionable. An open-source, self-hosted ontology platform.

- Stars: 36
- Forks: 4
- Watchers: 36
- Open issues: 0
- License: Other
- Default branch: master
- Created: 2026-10-12T14:05:40Z

## Languages

- CSS
- Clojure
- Go Template
- HTML
- JavaScript
- Lua
- Python
- Shell
- Tape

## Top Contributors

- 0nelight (1 contributions)

---

## README

 Sutra-OS

 S carce U nits, T yped, R elated, A ctionable.

 An open-source, self-hosted ontology platform.
 Your data becomes one model you own: typed, linked, changed only through
 rules the server enforces, and every number traces back to its source.

 Quick start ·
 How it works ·
 Proposals ·
 Python SDK ·
 Contributing

Your ontology. Your digital twin. Your data becomes one model of your organisation, practice or household. Under a Data Lineage graph of the example farm, from its sources through datasets and transforms to object types, links and actions, nine core features: one door for every write (an action the server refuses with its reason), deciding is not doing (every change is a proposal until approved), AI agents only propose, every number has a past (lineage back to the source), model and data on branches, access control enforced by the server through markings, the model as a generated typed API, credentials held by a separate egress agent, and Writer, Calc and Visio documents co-edited live on the model. Web apps, the Python SDK, the CLI, the REST API, AI agents and git all work under the same rules.

> **Beta.** Only small parts are still alpha: the model language and APIs may
> still change between versions, and parts of the user interface and docs are
> unfinished.

> **Maintainers wanted.** Sutra-OS is a one-person project so far. See
> Contributing.

## Motivation

Sutra-OS began in late 2025 as a thought experiment: a free version of the
system described in
Ontology-Oriented Software Development,
whose creators I deeply admire.

Much talent today goes into software that sells attention, while the
software everything else runs on is mostly free: by a rough estimate,
70–90% of US economic output depends on free software at some critical
point. That openness is not guaranteed. In November 2026, Nvidia's board
parted with the founder who had its AI models released openly. Sutra-OS adds
to the commons under the AGPL, so that it stays readable by anyone.

The past ten years have shown what it costs when nobody can see what depends
on what. In 2017, NotPetya spread through a single Ukrainian accounting
program and stopped Maersk's ports and Merck's factories. In 2023, a
corrupted file in one FAA system halted every domestic departure in the US.
In 2024, one faulty CrowdStrike update crashed millions of Windows machines,
and airlines, hospitals and banks stood still. In November 2026, a single
vendor took Outlook down for a day and some cities went back to fax. That
same week, data flooded the FAA's telecommunications network, aging routers
buckled, and the US saw only the third nationwide ground stop in its history.
No one, it seems, had those routers on the map of what keeps planes in the
air, so no one could ask beforehand what would stop if they failed.

That question is what Sutra-OS is built for. Every system, device, dataset
and decision becomes an object with links to what it feeds and what feeds
it, and every number can be traced back to its source. Whoever holds such a
model can ask, before the outage, what stops when one piece fails, and get
an answer, at every scale from a single person to a government (hopefully
never a world government). **Many small ontologies, each held by those it
describes, keep power spread out; one model of everything would not.**

**S**carce **U**nits: energy, water, land, housing and time will shape the
coming decades. Whoever counts what is scarce decides how it is shared, and
today that bookkeeping sits with a few platforms; for most people, the only
trace their own data leaves in their life is the tendinitis from the hundredth
weary click on "Accept all" in a cookie banner. Sutra-OS keeps the bookkeeping
with those it concerns, under rules everyone can read: households, farms,
workshops, clubs,
newsrooms and public administrations get their records back, and their wrist
with them. That is what a democracy needs from its software: a council that
can trace the number behind a decision to its source, a change that stays a
proposal until someone answers for it, and a public administration
accountable to its voters rather than to a vendor under another country's
law.

## Who it is for

Almost everyone. Whoever you are, someone else keeps a better-connected
record of your affairs than you do. Sutra is for anyone who wants their own.

## Quick start

**Requirements:** Linux x86_64, JDK 21, the
Clojure CLI, Node.js, Python 3, git.

```sh
git clone <repository-url> sutra && cd sutra
(cd clients/frontend && npm install)
bin/sutra-solo
```

This starts an embedded PostgreSQL and the server on `127.0.0.1` and prints the
address. Data lives in `$SUTRA_HOME` (default `~/.local/share/sutra`). The admin
password is in `zugang.edn` ("access") there. Run the `bin/sutra bind …` line it
prints once.

## How it works

Three ideas carry the whole platform: **object types**, **link types** and
**action types**. The examples below use the farm model in
`resources/presets`.

### 1. Object types: what *is* there

You start by saying what exists: a lot of hay, from one field and one cut; a
sale, to one buyer. Each is a typed thing with a kind and a key.

```clojure
:objects
{:lot
 {:name "Hay lot" :plural "Hay lots" :symbol "🌾" :title :name
  :primary-key :name :match-keys [:name]
  :attributes
  [[:name    :string  {:name "Lot"}]                    ; "North Meadow, 1st cut 2026"
   [:baled   :integer {:name "Bales made" :constraints {:min 0}}]
   [:sold    :integer {:derived {:expression [:connected-sum :sales :bales]}}]
   [:in-barn :integer
    {:name "In the barn" :visibility :prominent
     :derived {:language :clojure
               :expression [:- [:get :baled] [:get :sold]]
               :inputs [:baled :sold]}}]]}

 :sale
 {:name "Sale" :symbol "🤝" :primary-key :sale-nr :match-keys [:sale-nr]
  :attributes
  [[:sale-nr        :string]
   [:lot            :string]
   [:buyer          :string]
   [:bales          :integer {:constraints {:min 1}}]
   [:price-per-bale :decimal]
   [:sold-on        :date]
   [:sold-by        :string]]}}
```

Nobody types or counts `:in-barn`: it is the bales made minus every bale sold,
computed by the server. `:bales` is an integer, so "about forty" or `-3` is
refused before anything is written.

An object type is a typed table with a name, a face in the UI and a class in the
generated SDK. Properties are typed, constrained and can be **derived**, so a
value nobody typed in still shows up like any other column.

The object workspace: every object type of the farm with its count on the left, and the five hay lots as a table with what is left in the barn.

The Object View of the hay lot North Meadow, 1st cut 2025: 25 bales in the barn, 120 made, 95 sold for € 462.50, its three sales, the last one sold by tom, and the field it was cut from.

### 2. Link types: who belongs to whom

A sale on its own is just a number. A sale linked to the lot it came out of is
a fact everyone can see.

```clojure
:links
[[:sale-lot :sale :lot :many-to-one
  {:fk :lot :forward-api-name :lot :reverse-api-name :sales}]]
```

The sale names its lot and the link follows it: from the lot you see its
sales, from a sale its lot, and `:connected-sum` above sums across that link.
One line, and the barn knows what is in it.

Links are first-class: named in both directions, navigable in the UI, traversable
in the SDK (`lot.sales`), and usable in derived values, filters and object
sets.

The object graph of North Meadow, 1st cut 2025, one compact node per object: its three sales linked through sale-lot, and the field North Meadow through lot-field, whose margin already counts the hay sold from it.

### 3. Action types: what you're *allowed* to do

In most systems anybody may change anything, and nobody can say who did. Here
there is no "update row". There are only **actions**: named decisions with
typed inputs and rules the server enforces. Selling hay is one of them, and it
has a condition.

```clojure
:sell-hay
{:on     :lot
 :params {:lot            {:type :lot :required true}
          :sale-nr        {:type :string :required true}
          :buyer          {:type :string :required true}
          :bales          {:type :integer :required true :constraints {:min 1}}
          :price-per-bale {:type :decimal}
          :sold-on        {:type :date :prefill :now}
          :sold-by        {:type :string :exposure :hidden :prefill :current-user}}
 :submission-criteria
 [{:message "Not that many bales in the barn."
   :test    {:want [:get :bales] :have [:get :lot :in-barn]}
   :pred    [:<= :want :have]}]
 :rules  [{:op :create :object-type :sale
           :values {:sale-nr [:get :sale-nr] :lot [:get :lot :name]
                    :buyer [:get :buyer] :bales [:get :bales]
                    :price-per-bale [:get :price-per-bale]
                    :sold-on [:get :sold-on] :sold-by [:get :sold-by]}}]
 :edits  [{:object-type :sale}]}
```

Ask to sell more bales than are in the barn and the server refuses and says
why, with the same sentence for the phone, the CLI, the Python script and the
AI agent. A refused action writes nothing. Every sale records who made it, and
nobody can put someone else's name there.

Actions are the only write path: typed parameters, validation, submission
criteria and state transitions, defined once and enforced everywhere.

Every rule you would otherwise keep in your head has this shape: a fact the
server computes, and an action that checks it. Declare it once, and stop
remembering it.

The same three ideas run the arable side of the farm. A field's margin is
derived from its paid harvests and the hay sold off it, two links away. A
harvest moves from *planted* to *harvested*, *delivered* and *paid* only
through its actions, and *Sell harvest* refuses to run without a signed
delivery note and a quality test of your own.

The Object View of the field Hilltop: a margin of € 8,270.00 from € 17,630.00 paid for 12 hectares of wheat that cost € 9,360.00 to grow, and three harvests: spring barley delivered, winter wheat paid, and winter wheat planted.

## Nothing happens until you say so

In most software, deciding and doing are one step. In Sutra they are two.
When you sell hay, the server first writes down what *would* change: one new
sale, forty bales, your name on it. Nothing has happened yet. Only when that
note is approved does the barn change.

Everything else follows from that:

- **You can always ask first.** "Would this work?" is the same question,
 without the last step.
- **An agent can only make suggestions.** What it hands back is the note,
 never the change. You decide.
- **You can try things out.** Run the same decisions on a copy, compare, and
 keep the real one untouched.
- **You can look back.** Every approved change is kept, so last Tuesday's
 state is still there to read.
- **The answer is the same everywhere.** The rule is checked in one place, so
 the phone, the script and the agent hear the same *no*.

And it is not a promise. A test fails if the part that decides ever does
anything but decide.

## More capabilities

- **Your data comes in as it is.** Mail over IMAP, CSV exports, REST APIs,
 PostgreSQL, MySQL, SQL Server and SSH, shaped by transforms in Python, SQL
 or Clojure.

- **Every number has a past.** Lineage runs from each object back through the
 transforms and datasets to the mail, statement or row it came from
 (`sutra lineage `). When someone else's figures disagree with yours,
 you open the source.

 The lineage of the hay lots: the baling_log dataset feeds Lot, Sale links to it, and Lot links on to the Field it was cut from.

- **Agents get only the tools you name.** An action, a function, a query on
 one type. By default (`:writes :propose`) their changes are staged as
 proposals; a rejected one doesn't come back, and the model's prompt and
 answer are kept with the run.

- **The model is versioned like code.** Model *and* data live on branches. You
 stage a change, commit it, open a proposal, see who consumes what you
 touched, and merge into `main` only when it's reviewed. Webhooks and
 notifications stay silent on a branch unless you say otherwise.

- **Share exactly what you choose.** Markings on types and properties are
 mandatory access control; grants on projects decide who may read, act and
 invoke. A group (a co-op, a tenants' association, a family) can pool what
 its members agree to share, and nothing else, and the server enforces it on
 every read: lists, filters, counts and totals. One person's data can't
 show what everyone else was offered. A group's can.

- **Builders and users are different people.** One person writes the model;
 everyone else gets apps with the build tools locked away, and a server that
 says *no* when no is the right answer.

- **Secrets stay out of reach.** A separate egress agent holds every external
 credential, so the code that reads your mail never sees the password.

## The model as the SDK

You described the farm once. Generate a Python SDK from it, and your code
speaks the farm's language: *lots*, *harvests* and *buyers*, and the things
you are allowed to do with them, not tables and joins.

```sh
pip install ./clients/python-platform-sdk
sutra-platform-sdk generate --base-url http://127.0.0.1:<port> \
                            --username admin --password "…" --out farm_sdk.py
```

`farm_sdk.py` is plain, typed Python: a class per object type, an attribute
per property and link, a method per action with the action's parameters as
its signature. Sutra's language server (clients/ent-lsp)
runs pyright for Python and labels each completion as what it is in the model
(*property*, *link-type*, *action*, *state*); any editor that lets you pick the
language server can run it (Neovim config).

**An action is a method.** Its signature comes from the model; a missing
argument is flagged before anything runs.

```python
lot = Lot.get("North Meadow, 1st cut 2025")

lot.sell_hay(bales=20, buyer="Neighbour")
# error: Argument missing for parameter "sale_nr"

lot.sell_hay(bales=20, buyer="Neighbour", sale_nr="S-2026-010")   # ok
```

**States are types.** A harvest's `status` is
`Literal['planted', 'harvested', 'delivered', 'paid']`, so the editor offers
exactly those four.

```python
for h in Field.get("hilltop").harvests:
    if h.status == "planted":       # completes: planted, harvested, delivered, paid
        h.record_harvest(harvested_on=date(2027, 7, 28), tonnes=61.5)
```

**Filters are checked too.** Comparing bales with a string, or reading a link
that may be empty, fails in the editor, not on the farm.

```python
Lot.where(Lot.in_barn < "forty")   # error: Operator "<" not supported for types
                                   #   "Property[int]" and "Literal['forty']"
Lot.where(Lot.in_barn < 50)        # ok

lot.field.margin                   # error: "margin" is not a known attribute of "None"
if lot.field:
    lot.field.margin               # ok
```

 The walkthrough in code: objects with their links, acting, asking
first, proposing, lifecycles, server-side aggregates, sets, branches and
revisions

```python
from sutra_platform_sdk import SutraClient, sum_, avg, count, by, bucket
from farm_sdk import Lot, Sale, Field, Buyer, register_all

client = register_all(SutraClient("http://127.0.0.1:<port>", username="admin", password="…"))
```

**An object, not a row.** A lot brings its derived values and its links along.
Nobody stored `in_barn`; the server computes it.

```python
lot = Lot.get("North Meadow, 1st cut 2025")   # a Lot, or NotFound
lot.baled, lot.sold, lot.in_barn            # (120, 95, 25)
lot.field                                   # <Field 'North Meadow'>: the field it was cut from
[(s.buyer, s.bales) for s in lot.sales]     # its three sales, each a Sale
```

**Act on it.** Selling hay is something you do *to a lot*. The server checks
the rule, writes the sale, stamps your name on it and tells you what changed.

```python
lot.sell_hay(sale_nr="S-2026-010", buyer="Neighbour", bales=20, price_per_bale=4.50)
Lot.get(lot.name).in_barn                   # 5
```

**Ask first, or only propose.** The same call can be a question (nothing is
written) or a proposal (staged until someone approves it). That is how an
agent gets to use it.

```python
from sutra_platform_sdk.actions import ActionConfig, ActionMode

ask = ActionConfig(mode=ActionMode.VALIDATE_ONLY)
lot.sell_hay(sale_nr="S-2026-011", buyer="Neighbour", bales=40,
             action_config=ask).validation.submission_criteria
# ('Not that many bales in the barn.',)

lot.sell_hay(sale_nr="S-2026-011", buyer="Neighbour", bales=5,
             publish=False).staged          # True: a proposal, the barn is unchanged
```

**Walk a lifecycle.** A harvest goes from *planted* to *harvested*,
*delivered* and *paid*, one action per step, and the rules travel with them.
The states are declared in the model, so `status` is typed
`Literal['planted', 'harvested', 'delivered', 'paid']` and your editor offers
exactly those four.

```python
from datetime import date

wheat = next(h for h in Field.get("hilltop").harvests if h.status == "planted")
mill  = Buyer.get("stone-mill")

wheat.record_harvest(harvested_on=date(2027, 7, 28), tonnes=61.5)
wheat.sell_harvest(buyer=mill, price_per_tonne=212)
# ServerError: HTTP 422: No signed delivery note. Without one, the buyer decides later what you delivered.
wheat.sell_harvest(buyer=mill, price_per_tonne=212, delivery_note=True, quality_tested=True)
Buyer.get("stone-mill").unpaid              # 13038: what the mill owes you, until …
wheat.record_payment()
Field.get("hilltop").margin                 # … the wheat lands in the field's margin
```

**Ask the whole farm, in one line.** Who bought how much hay, month by month,
at what price. Grouped, summed and sorted on the server; nothing is
downloaded to be counted.

```python
Sale.aggregate(
    sum_(Sale.bales), avg(Sale.price_per_bale), count(),
    group_by=[bucket(Sale.sold_on, "month"), by(Sale.buyer)],
    order_by=sum_(Sale.bales), desc=True,
).flat()
# [{'sold_on_month': '2025-12', 'buyer': 'Riding stables', 'bales_sum': 80,
#   'price_per_bale_avg': Decimal('4.5000000000000000'), 'count': 2}, …]
```

Money stays `Decimal` all the way from the database; nothing is rounded
through a float.

**Sets, not lists.** On the class, a property is a filter and a link is a hop.
Combine sets with `|`, `&` and `-`; the server plans it, and you fetch only
what you iterate. Each set knows what it holds: `running_low` is an
`ObjectSet[Lot]`, and one hop along `Lot.sales` makes it an `ObjectSet[Sale]`.

```python
running_low = Lot.where(Lot.in_barn < 50)
neighbours  = Sale.where(Sale.buyer == "Neighbour").around(Sale.lot)

(running_low - neighbours).count()          # 3: running low, and the neighbour never bought from them
running_low.around(Lot.sales).aggregate(sum_(Sale.bales), group_by=[by(Sale.buyer)])   # who emptied them
```

**Try tomorrow's rule on today's farm, or look at last Tuesday.** Everything
above runs unchanged against a branch, and every action tells you the
revision it landed in, a state you can read again later.

```python
with client.branch("new-rule"):             # made with: sutra branch new-rule
    lot.sell_hay(sale_nr="S-2026-012", buyer="Neighbour", bales=5)   # main never notices

sale = lot.sell_hay(sale_nr="S-2026-013", buyer="Neighbour", bales=1)
client.at(sale.revision).objects("sale")    # the sales as they stood right then
```

**And what it refuses.** Wrong names, missing arguments and wrong types fail
in your editor, before anything runs. Broken rules fail on the server, with
the same sentence for every client. If the model changes underneath you,
`register_all` refuses to run until you regenerate.

```python
lot.sell_hay(bales=20, buyer="Neighbour")   # error: Argument missing for parameter "sale_nr"
lot.sell_hay(sale_nr="S-1", buyer="Neighbour", bales="20")
                                            # error: "Literal['20']" is not assignable to "int"
Lot.where(Lot.in_barn < "about forty")      # error: Operator "<" not supported for types
                                            #   "Property[int]" and "Literal['about forty']"
lot.field.margin                            # error: "margin" is not a known attribute of "None"
```

These are pyright's messages against the generated farm SDK. The SDK's tests
run the same lines through pyright, against an SDK generated from a schema
captured from a running server, not from a hand-written imitation of one.

None of this is a reporting layer bolted on afterwards. The UI, the CLI, the
REST API and the agents ask the same questions and take the same actions
through the same door, which is why an agent can be handed `Lot` and
`sell_hay` and nothing else.

## Development

```sh
./bin/start.sh   # backend + shadow-cljs watch; PostgreSQL from SUTRA_PG_URL
./bin/stop.sh
(cd tests/frontend && npm install)   # once: the browser tests' driver (playwright-core)
bin/test         # full suite; integration tiers start PostgreSQL in podman
```

| Path | What lives there |
|------|------------------|
| `src/` | the server |
| `libs/` | libraries the server, the clients and the tests share: `kernel` (reference interpreter), `world` (the world as a db value), `commits`, `service`, `dialect`, `core`, `lib` (the `.ent` dialect as a library), `calx`, `store`, `store-pg` |
| `clients/` | frontend, CLI, language server, Python SDK, and the babashka tools behind `bin/change` and `bin/enta` |
| `plugins/` | optional modules (SSO, LLM, packages, …) |
| `boundaries/` | the published interfaces, conformance kits and their register (`resources/sutra/boundaries.edn`), Apache-2.0 |
| `resources/` | the `.ent` grammar and example models (`presets`), platform config, the web client's static files |
| `distributions/` | ready-to-run bundles (`sutra-solo`) |
| `tests/` | backend suites, the scenario, and `tests/frontend` |
| `bin/` | start, stop, test and tooling scripts |

The semantics are pinned by an executable scenario, an aircraft maintenance
shop in `tests/scenario`: "no release while a
defect is open" is the barn rule above in another world.

**Security:** set `SUTRA_HTTP_BIND` when running the plain server (it defaults
to `0.0.0.0`). `./bin/start.sh` allows anonymous access, so never expose it.
Transforms run user code on the server, so grant that right accordingly.

## Contributing

**Maintainers wanted.** Sutra-OS needs people who will take responsibility
for part of it over time: the server, the web client, the Python SDK,
connectors, packaging and installation, docs, or the example models. You
don't need to know all of it. Start with a few contributions in one area;
if you'd like to stay, say so in an issue.

The most useful contributions are not always code:

- **A model for an everyday problem.** A tenancy, a pension, a medical bill,
 a small association's membership. If a rule protects someone, it belongs in
 `resources/presets`.
- **Plain-language guides** for the person who sets Sutra up for others.
- **Translations.** Parts of the code base and the examples are in German;
 the user interface should speak more languages than two.
- **Code.** Send a failing test or a fix.

Open an issue for questions, ideas and bug reports. Be kind: the person on the
other side may be the one this was built for.

The code is offered as is, in the spirit of Rich Hickey's
Open Source is Not About You:
nobody is owed a feature, a fix or an answer, and that includes the
maintainers. What keeps it going is people choosing to help.

## Acknowledgements

The ontology model of objects, links and actions follows the one popularised
by Palantir Foundry; Sutra-OS was built from its public documentation.
The web client is built on Palantir's Blueprint
UI toolkit (Apache-2.0), vendored as a ClojureScript port in
`clients/frontend/vendor/blueprint-cljs`.
The implementation owes everything to Rich Hickey and Clojure, and to his
almost spiritual talk
Are We There Yet?,
which will perhaps continue to transform the software craft into eternity.
Claude Code wrote all of the code.

## License

AGPL-3.0-or-later, with a section 7 exception for linking with EPL libraries
such as Clojure. See LICENSE. The AGPL means anyone who runs a
modified Sutra as a service for others must offer them the source, so the
tool stays in the hands of the people it serves.

No patent search has been carried out. The AGPL licenses contributors'
patents only; checking third-party patents where they apply is up to
you. Palantir and Foundry are trademarks of Palantir Technologies Inc.;
Sutra-OS is independent and not affiliated with or endorsed by Palantir.

# formgong/dead-forms-study

## 评论（13/13）

> **_def** · 2026-11-17T00:06:34.000Z　
> Many small ontologies, each held by those it describes, keep power spread out; one model of everything would not.
>
> Same with self-hosted vs SaaS or any other organizational structures that relate to people and power over them.

---

> **whalesalad** · 2026-11-17T00:15:33.000Z　
> Written in clojure and also looks like Farmlogs - wild. Do I know you? lol

---

> **acgourley** · 2026-11-17T00:43:04.000Z　
> I am intrigued but want to know more about how I might use it. Suggestion - lots of people like me are heavy airtable/coda-like users who setup relational DBs for various projects. Should I be looking at this to replace any of these efforts?

---

> **wangii** · 2026-11-17T01:16:34.000Z　
> I feel bad for people applying ontology to their life and work. it seldom works, and fundamentally questionable.

---

> **voidhorse** · 2026-11-17T01:18:30.000Z　
> Readme is covered in slop hallmarks. LLM prose, LLM UI design. This just means I can generate something better and more preferential myself. The experience doesn't reflect any understanding of the domain beyond what I could generate. Not interested. Sorry.

---

> **jameslian** · 2026-11-17T01:52:13.000Z　
> Few people think and reason with rigorous ontology in real life. That's why ontology is hard to popularize—but it's also exactly why most people drift through life mediocrity intact.

---

> **0nelight** · 2026-11-17T01:08:25.000Z　
> oh I researched what farmlogs is - no, that is a coincidence ^^ could have used any other example too like aviation or stuff

---

> **electric_mayhem** · 2026-11-17T01:08:47.000Z　
> It’s turtles all the way down.

---

> **0nelight** · 2026-11-17T01:14:25.000Z　
> it is not so much about replacing stuff (although also possible) but more about abstracting everything into a general layer above all your databases. you can then query and writeback this layer and sutra then communicates with all your databases. you talk human language (objects, relations, actions) and sutra then translates this into every dialect the computer needs (csv, sqlite, pg, mssql, mysql, your mails... extendable)

---

> **0nelight** · 2026-11-17T01:36:04.000Z　
> that was because they had no idea what they were talking about :)

---

> **mmargenot** · 2026-11-17T02:47:59.000Z　
> I understand not applying it to life, but have you run into specific issues with ontologies at work? Structured categorization and organization of information is good on first principles to me, provided that you can maintain it.

---

> **0nelight** · 2026-11-17T01:34:42.000Z　
> pull requests are very welcome to make it less slop :)

---

> **staticshock** · 2026-11-17T02:29:44.000Z　
> The maintainer sets the tone. Contributor pull requests, if merged, may temporarily improve the state of the repo, sure, but they're much less likely to influence the maintainer's quality bar for the repo.And so the current state of the repo, before anyone else contributes, must communicate that tone, because that is a trust-building exercise. What you have to communicate is, "I will cherish your efforts; I will not let them go to waste." The AI-isms in the repo currently communicate the opposite.

## 关联链接

- http://127.0.0.1:

## 导航

- 项目页：[[10-项目/github.com_ee6fcd65]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
