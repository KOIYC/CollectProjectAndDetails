---
type: "corpus"
item_id: "af1d06189dc3a0b8"
title: "Show HN: Sapporta – build database applications for power users"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49499123"
project_url: "https://sapporta.com/"
author: "jasim"
published_at: "2026-08-30T14:45:48Z"
captured_at: "2026-09-21T03:11:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-08-30"
tags:
  - 语料
  - hn_show
  - author_jasim
  - story_49499123
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:52d"
---

# Show HN: Sapporta – build database applications for power users

> [!info] 一句话导读
> Skip to content Documentation Technical Overview GitHub Sapporta

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49499123>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：jasim　|　发布：2026-08-30T14:45:48Z
> 项目链接：<https://sapporta.com/>
> 采集：2026-09-21T03:11:31+08:00　|　id：`af1d06189dc3a0b8`

## 正文

Skip to content Documentation Technical Overview GitHub Sapporta
 Build custom database software for power users
Sapporta is a TypeScript + SQLite web framework for building database
applications.
Every table gets a spreadsheet-grade grid right away. Filtering, sorting,
search, export, and full keyboard navigation.
Default agentic. Use your coding agents to drive your application. For a
Calorie Tracker, you could tell the agent: “breakfast: 2 eggs and a toast”,
and it’ll find the right food entries, create them if needed, and log them
accurately.
Reports that drill down into the underlying records, shareable by URL.
Secure software despite AI code generation with patterns and skills that
enforce where user_id = {currentUser.id} and similar on all data access
code.
Get Started Try demo apps GitHub
Demo
Arrow keys for navigation. Space to expand quotes.
Sample data grid Code: schema definition
packages/api/schema/books.ts
 export const booksTable = sqliteTable ( "books" , {
 id: integer ( "id" ). primaryKey ({ autoIncrement: true }),
 title: text ( "title" ). notNull (),
 author: text ( "author" ). notNull (),
 });
export const books = sapportaTable ({
 drizzle: booksTable,
 meta: {
 label: "Books" ,
 rowScope: "systemGlobal" ,
 rowLabelColumns: [ "title" ],
 search: { columns: [ "author" , "title" ] },
 children: [
 {
 table: "quotes" ,
 foreignKey: "book_id" ,
 label: "Quotes" ,
 columns: [ "quote_text" ],
 defaultSort: "-created_at" ,
 },
 ],
 columns: {
 title: { width: 64 },
 author: { width: 36 },
 },
 },
 });
Try demo apps built with Sapporta ↓
Features
 Everything a user can do, an agent can as well
If you are building new software today then it must have an agentic surface - a way for an agent to explore and use your
entire system securely.
For instance, compare a traditional accounting system against something built for agentic operations. Instead of
manually entering transactions, we can point a coding agent at any bank statement. Then the agent can look for existing
parsers for the statement, or write one itself. It can then classify the parsed transactions according to business rules
written in freeform English, and then import them into the system. The agent can even reconcile entries, find
missing/duplicated transactions, and answer ad-hoc questions.
Sapporta makes all this possible, without needing any additional work, by exposing an /api/openapi.json endpoint that
lists every API in the application. This includes all the auto-generated APIs for every table, as well as all the domain
APIs that you write yourself.
Sapporta also lets you create agent tokens. With this you can point your coding agents at any hosted Sapporta
application, and its row-level security ensures that users are able to access only the data that belongs to them.
Agent session · calories.demo.sapporta.com
Expand
0:00
 A recorded Claude Code session - log freeform text in an agent, and have it structured and saved accurately. The agent reads /api/openapi.json, finds the food rows through the table APIs, and posts the meal; in the UI it can be seen in the Today dashboard.
A recorded Claude Code session - log freeform text in an agent, and have it structured and saved accurately. The agent reads /api/openapi.json, finds the food rows through the table APIs, and posts the meal; in the UI it can be seen in the Today dashboard. A datagrid for every table
High-density keyboard-centric interface. If you look at traditional ERP software, a large chunk of their interface
is just forms, grids, and reports. They are targeted at power-users, and so have high information density and are
keyboard-centric. Sapporta’s goal is to bring the same experience to database applications on the web.
filtering
 sorting
 search
 inline edit
 export
 master-detail
 keyboard
In Sapporta, when you declare a table, you immediately get a live, editable grid for it. It uses the
 Sapporta Grid , a custom-built React component with UX
similar to Airtable and NocoDB. Sapporta applications uses this grid as a universal surface for tabular data. You can
put a lot of heart and soul into that single component, and it benefits the entire application.
That is also what makes spreadsheets beautiful. People use them because they can work with data without having to
anticipate every requirement in advance. Sorting, searching, and filtering, are available on every sheet, and that small
set of operations covers much of what you need to change and understand data.
Filters combine directly above the grid while matching rows stay visible. Reports with drill-down
Sapporta ships with a light-weight reporting system.
The main primitive is the GridDataset type . On the server,
you only need to create an API endpoint that returns a JSON value of this type, and you can use the existing Reporting
renderer to render it.
It supports drill-down: we can navigate from a high-level entry deep down to a specific transaction.
Consider a Profit & Loss statement - it shows the consolidated revenues and expenses for a financial year.
Let’s say that the travel expenses look a bit high. We can click on it, and go to a monthly summary of the Travel Expense ledger,
and from there, we can go into a specific month this looks high, and see all the transactions for that month. And clicking on a specific transaction
immediately takes to that specific journal entry.
Report drill-down · accounting.demo.sapporta.com
Expand
0:00
 A Profit & Loss drilled down to a specific journal entry
A Profit & Loss drilled down to a specific journal entry
 Drilling down from a summary to its transactions has long been a feature of classical accounting software, and the same
cross-linking is valuable for any kind of database-backed reporting. Sapporta gives you the affordances to add it
cheaply: any report you build with Sapporta and the Sapporta skill looks for good cross-linking opportunities and wires
them up by default.
nested levels
 rollups
 subtotals
 deep links
 keyboard
 composable
URL deep-linking. A report’s parameters and drill-downs are kept in the URL, so you can share any report
configuration as a link.
Built-in primitives. Rollups, subtotals, opening rows, and closing rows are supported directly.
Full keyboard. Space expands nested rows; Enter follows the active cell’s link.
Composable. Argument inputs, error display, and summary stats are React components your code can reuse, extend, or
replace entirely.
Why Sapporta
 Why Sapporta? Why not bare AI?
Unless explicitly guided, AI agents do not build shared foundations.
Consider data filtering. If you prompt an agent to build filtering for a table, it will create a custom solution —
frontend, backend, and support for specific operators — just for that single table. When you ask it to add filtering to
a second table, it will write diverging code rather than building a well-reasoned, reusable abstraction.
A software developer can certainly spot this issue and prompt the LLM to build a shared foundation instead. But that
requires constant vigilance. We have to think through our requirements, articulate them, and then micromanage the agent
so it doesn’t create duplicate sources of truth. When the output is not exactly what we wanted, we have to
course-correct, adding significant waiting and uncertainty.
But most database applications have a common set of functionality, that spans the front-end and back-end. Sapporta
handles them out of the box. For instance, we include an
 explicit grammar for filtering that automatically maps into
valid SQL with server-side row-level security.
Demo applications
Try complete applications built with
 Sapporta
Live demos, seeded with sample data,
 no login required.
Bookkeeping Double-entry accounts, balanced transactions, budgets, and ledger reports.
Try the demo
→
Calorie tracker Foods, logged meals, nutrition goals, and a daily progress dashboard.
Try the demo
→
Depot Maintenance tracker Assets, recurring schedules, work orders, and per-asset service history.
Try the demo
→
Get Started
Get started with your coding agent
Copy the prompt and send it to your
 coding agent.
Build your project
or, try an existing prompt
 Calorie tracker Bookkeeping Maintenance tracker
[ Sapporta skill installation
 ]
Before you begin, ensure the
 Sapporta skill is installed:
npx skills add https://github.com/jasim/sapporta-skills --skill sapporta --global --yes
Load and follow the Sapporta
 skill. It owns project setup,
 modelling, implementation, and
 verification.
Using Sapporta, build a project for me
.
https://sapporta.com/docs/getting-started/create-a-project.md
 I have not described the project yet. Before doing anything else, ask me one or two questions to find out what I want to build and how I will use it. From my answers, infer the domain model — the tables, their relationships, and the key workflows — and show me that plan in a few short lines for confirmation before you build.
 Then build the complete application.
Add realistic sample data, seeded under a user with email test@example.com and password test1234. Show these credentials prominently in the log-in screen. Once the project is built, suggest three concrete changes I could make to this application: one improvement to the user interface, one report to add or change, and one new workflow. Also display these suggestions in the homepage of the app prominently.
[ Sample data, test log-in
 & next steps ]
Show the full brief
[ Sapporta skill installation
 ]
Before you begin, ensure the
 Sapporta skill is installed:
npx skills add https://github.com/jasim/sapporta-skills --skill sapporta --global --yes
Load and follow the Sapporta
 skill. It owns project setup,
 modelling, implementation, and
 verification.
Using Sapporta, build a personal calorie tracker
.
https://sapporta.com/docs/getting-started/create-a-project.md
Model foods, meals, meal items, and date-ranged nutrition goals
. Include:
a user-maintained food list where each food defines one serving — a quantity plus a measurable unit (g, kg, ml, l, piece, tbsp, tsp) — and calories, protein, carbs, fat, and fiber per serving
 one transactional workflow to log a meal (time, optional category label) with many items, each picking a food and a quantity in that food's own serving unit — no unit conversion; mismatched units are rejected server-side
 each meal item stores a snapshot of the food's details and its computed nutrition (quantity ÷ serving quantity × per-serving values), so editing a food never changes logged history or past reports
 non-overlapping date-ranged goals, optionally open-ended, holding independent daily and weekly targets for every nutrient
 a dashboard for today and the Monday-Sunday week: consumed, target, remaining, and percent progress per nutrient, plus the day's logged meals and items
Add realistic sample data, seeded under a user with email test@example.com and password test1234. Show these credentials prominently in the log-in screen. Once the project is built, suggest three concrete changes I could make to this application: one improvement to the user interface, one report to add or change, and one new workflow. Also display these suggestions in the homepage of the app prominently.
[ Sample data, test log-in
 & next steps ]
Show the full brief
[ Sapporta skill installation
 ]
Before you begin, ensure the
 Sapporta skill is installed:
npx skills add https://github.com/jasim/sapporta-skills --skill sapporta --global --yes
Load and follow the Sapporta
 skill. It owns project setup,
 modelling, implementation, and
 verification.
Using Sapporta, build a personal double-entry bookkeeping app
.
https://sapporta.com/docs/getting-started/create-a-project.md
Model accounts, transactions, postings, payees, and budgets
. Include:
one chart of accounts spanning asset, liability, equity, income, and expense accounts — income and expense accounts serve as the categories, with no separate category table
 easy entry for income, expenses, and transfers: each transaction is a thin header (date, payee, memo) over two or more balanced postings, each posting debiting or crediting exactly one account, so one purchase can split across expense accounts
 a general journal entry form for transactions that fit none of those shapes — the user picks the accounts and debit/credit amounts directly, as long as they balance
 payees with a default account to auto-categorize new entries
 monthly budgets per expense account, and reports for balances, cash flow, and spending
 the leanest schema that supports this — no archiving, soft-delete, or status fields
Add realistic sample data, seeded under a user with email test@example.com and password test1234. Show these credentials prominently in the log-in screen. Once the project is built, suggest three concrete changes I could make to this application: one improvement to the user interface, one report to add or change, and one new workflow. Also display these suggestions in the homepage of the app prominently.
[ Sample data, test log-in
 & next steps ]
Show the full brief
[ Sapporta skill installation
 ]
Before you begin, ensure the
 Sapporta skill is installed:
npx skills add https://github.com/jasim/sapporta-skills --skill sapporta --global --yes
Load and follow the Sapporta
 skill. It owns project setup,
 modelling, implementation, and
 verification.
Using Sapporta, build an equipment maintenance tracker for a small operations team
.
https://sapporta.com/docs/getting-started/create-a-project.md
Model assets, vendors, maintenance schedules, and work orders; team members are the workspace's existing users
. Include:
a workspace-shared asset register: name, location, serial number, purchase date and cost, and the vendor who services it
 recurring maintenance schedules per asset — what needs doing and an interval in days, with the next due date computed from the most recent completed work order
 work orders for all actual work, whether generated from a schedule or logged ad hoc for a breakdown or repair: assignee, priority, due date, open / in-progress / done status, completion date, cost, and notes
 vendors with contact details and their service history across assets
 views for overdue and upcoming maintenance, open work orders by assignee, and per-asset service history with total spend
 keep it simple for now: no parts inventory, meter-based triggers, approval chains etc.
Add realistic sample data, seeded under a user with email test@example.com and password test1234. Show these credentials prominently in the log-in screen. Once the project is built, suggest three concrete changes I could make to this application: one improvement to the user interface, one report to add or change, and one new workflow. Also display these suggestions in the homepage of the app prominently.
[ Sample data, test log-in
 & next steps ]
Show the full brief
Copy starter prompt
Are you a coding agent? If you want to
 build a project using Sapporta, you must
 first install the Sapporta skill with npx skills add https://github.com/jasim/sapporta-skills --skill sapporta --global --yes before creating or modifying a project.
Framework
 Sapporta projects are regular applications
sapporta init gives you a complete, pre-wired project — API server, React
frontend, auth, migrations, and a production Dockerfile — all of it plain
TypeScript that you can read and own.
api server
 react frontend
 auth
 migrations
 dockerfile
 pnpm workspace
A regular codebase. Add typed API endpoints, React screens, and whatever
business logic your application needs, the way you would in any TypeScript
project.
One declarative piece. The sapportaTable declaration is the only
declarative configuration in a Sapporta application:
// packages/api/schema/books.ts
// Regular table schema defined in Drizzle
 export const booksTable = sqliteTable ( "books" , {
 id: integer ( "id" ). primaryKey ({ autoIncrement: true }),
 title: text ( "title" ). notNull (),
 author: text ( "author" ). notNull (),
 });
// Declarative configuration for Sapporta
 // auto-generated table APIs and data grids
 export const books = sapportaTable ({
 drizzle: booksTable,
 meta: {
 label: "Books" ,
 rowScope: "workspaceUserScoped" ,
 rowLabelColumns: [ "title" ],
 children: [
 {
 table: "quotes" ,
 foreignKey: "book_id" ,
 label: "Quotes" ,
 columns: [ "quote_text" ],
 defaultSort: "-created_at" ,
 },
 ],
 columns: {
 title: { width: 64 },
 author: { width: 36 },
 },
 },
 });
 This produces both the backend APIs and frontend UI for the table:
Table APIs. Sapporta generates list, get, create, update, delete, lookup,
count, and CSV export endpoints, then publishes them to /api/openapi.json
for agentic use. Row-level security from rowScope and role-based permissions
defined with CASL apply to every call, so the APIs are safe to publish on the
internet.
Table Grid. Sapporta publishes /api/meta/tables , which the React
frontend uses to build editable grids, create forms, lookups, and nested
child-table views. These are the same grids shown above, and because they use
the table APIs they get the same authorization and permissions.
Stack
Well-established libraries wired into a conventional pnpm workspace. Nothing
proprietary, nothing hidden.
TypeScript on
 Node.js for the entire application. The generated
project is a pnpm workspace with separate API, frontend,
and shared-contract packages.
Hono and
 @hono/node-server for the HTTP
server. The same process can serve the API and the compiled frontend in
production.
Drizzle ORM for schemas and database access,
 Drizzle Kit for migrations,
and better-sqlite3 as the
database driver. SQLite is the only database
currently supported.
Zod for runtime validation of shared request,
response, and form data.
sapporta-rest , a small fork of
 ts-rest , and Sapporta’s
 Honest
 Hono adapter for contract-first APIs. You define an
API’s signature once in the shared package. The backend uses that contract to
parse and type each request, and the frontend uses it to serialize requests,
validate responses, and expose a fully typed API client. There is no second
set of parsers, serializers, or request and response interfaces to keep in
sync. The contract also becomes the
 OpenAPI 3.1 document at
 /api/openapi.json .
Better Auth with its
 Drizzle adapter for
sessions, passwords, and organizations, plus
 Nodemailer for verification, password-reset,
and application email.
CASL for role-based abilities. Sapporta combines
those abilities with table row scopes on every generated read and write.
React 19 and
 React Router for the browser application and its
routing.
TanStack Query for server-state
caching, TanStack Form for form state,
and Zustand for local application and grid
state.
Tailwind CSS v4 for styling.
 @sapporta/ui
follows shadcn/ui composition conventions, uses
 Base UI primitives for accessible interactions,
and uses Lucide for icons and
 Sonner for toast notifications.
The Temporal
polyfill for consistent
date and time values in the browser, the API, and their shared contracts.
Vite for the frontend development server and
production build, with the
 TypeScript compiler
building the API and shared packages.
Vitest and in-memory
 SQLite for automated tests.
Docker for the production image. The included
multi-stage
 Dockerfile builds the
workspace, applies Drizzle migrations at startup,
and runs the Node.js server as a non-root user.
Frequently asked questions
Why use Sapporta instead of asking an LLM to generate the whole application?
Sapporta gives agents infrastructure to build within, so they behave predictably. The agent starts with working table
APIs, grids, forms, and row security, and you can spend your prompting attention on your product. Also see:
 Why Sapporta? Why not bare AI? .
What kinds of products can I build?
Sapporta suits any web application you want to build with a TypeScript backend and a rich React single-page frontend. It
wires best in class libraries into a pnpm workspace: a package for code shared between frontend and backend, including
ts-rest for typed APIs, and a frontend set up with state management, forms, queries, and UI.
It fits database tools especially well: personal software, internal and operational tools, and vertical SaaS. Examples
include calorie and fitness trackers, personal bookkeeping systems, and home-management databases, as well as internal
tools like CRMs, case trackers, and inspection or audit systems.
These applications need purpose-built workflows, but they also need a flexible way to work with the underlying data.
Sooner or later you will want to correct old entries, investigate a discrepancy, reorganize records, or answer a
question the original interface never anticipated. Sapporta’s table grids let you do that with the freedom of a
spreadsheet rather than a static CRUD scaffold. And because the whole system is queryable and scriptable through typed
APIs, agents can work with the same data and workflows your users do.
It gives you less for products whose main content is not relational data, such as forum software, social networks, media
editors, or real-time multiplayer experiences. You can still build those features in the same TypeScript application,
but the generated grids and table APIs will not help much there.
Can I build customer-facing SaaS applications with it?
Yes, especially vertical SaaS products whose users work with structured, relational data. Sapporta includes
authentication, workspaces, roles, and row-scoped data access. You can treat a workspace as a tenant, and the integrated
CASL bindings let you serve users across tenants with full authentication and authorization boundaries.
Sapporta is currently an early alpha and supports SQLite. That deployment model fits small applications and focused SaaS
products, but check it against the workload you expect. Nothing in the architecture ties the system to SQLite; adding
Postgres, for example, just requires some effort.
Can I add custom business logic beyond generated CRUD?
Yes. The generated CRUD is only a starting point. You can add typed contracts in the shared package, Hono handlers and
domain modules in the API, transactions around multi-table changes, and custom React routes in the frontend.
That code sits beside Sapporta’s generated routes in a regular TypeScript codebase, and it can use the same
authentication context, row-scoped data helpers, mailer, and typed client conventions.
How are authentication, permissions, and tenant isolation handled?
Sapporta’s built-in conventions cover personal software as well as multi-tenant applications with row-level security and
fine-grained permissions. There are three parts:
Who is making the request? Every request to an application or generated API route passes through auth middleware
before its handler runs. The middleware accepts either a browser session managed by Better Auth or an agent access
token, resolves the user’s active workspace and membership, and builds the auth context for that request. It attaches
that trusted context to Hono—not to the client-controlled request body—so every handler can read it with
 c.get("auth") :
app. use ( "/api/*" , projectAuth.resolveMiddleware);
// Inside any API handler:
 const auth = c. get ( "auth" );
 What may that person do? Sapporta builds a CASL ability from the authenticated principal and their workspace roles.
Generated and custom routes check an action and subject before doing the work:
forbidUnless (c, auth.ability. can ( "update" , "invoices" ));
 Which records may they do it to? Every Sapporta table declares a row scope. That scope determines which ownership
columns the table must contain and which SQL predicate Sapporta adds to its queries:
Row scope Scope columns Rows available to the request
 systemGlobal None Application-wide rows
 workspaceGlobal workspace_id Rows in the active workspace
 workspaceUserScoped (default) workspace_id , scoped_to_user_id Rows in the active workspace owned by the user
The server manages the scope columns: Sapporta checks that they exist on the table, hides them from ordinary table
presentation, and does not let API callers set them directly.
Both checks apply together. A workspace member may have permission to update invoices, but that permission does not give
them every invoice in the database. The update goes through only when the CASL ability permits the action and the
invoice is inside the member’s row scope.
For generated table routes , Sapporta applies both checks
automatically before a query reaches Drizzle. Lists, lookups, counts, and exports leave out rows beyond the caller’s
scope. Reading, updating, or deleting one record returns the same 404 ROW_NOT_FOUND whether the record does not exist
or exists outside that scope, so the response does not reveal records from another tenant.
Creates are protected in the other direction: a client cannot choose a workspace or owner by submitting a scope field.
Sapporta rejects caller-supplied scope values, derives the correct values from the authenticated request, and checks
that referenced records are visible under the same rules. Tenant ownership therefore comes from trusted server context
rather than a form field, JSON property, or URL parameter.
Custom business logic can use the same boundary. For ordinary table CRUD,
 scopedRows(db, auth, table) combines typed
Drizzle predicates with row visibility, trusted insert scope, protected scope fields, and reference checks. Workflows
that need joins, transactions, or custom result shapes can use
 a per-table row-security guard around direct
Drizzle operations instead.
Raw Drizzle queries do not apply any of these rules automatically. A custom route must check its CASL ability and use
Sapporta’s scoped data helpers or row-security guards, which keeps the security boundary on the server, where the
authenticated identity, permitted action, and visible rows are evaluated together.
Is Sapporta a library, framework, or hosted platform?
Sapporta is an open-source TypeScript framework made of installable libraries and project tooling. It initializes a
conventional pnpm workspace, then runs as part of the application you own.
It is not a hosted platform and runs nothing outside your application. It is a framework in the same sense as Rails and
Django, but built with TypeScript using a curated set of libraries, and with more specific conveniences for database
applications and agentic coding.
 Contact and contribute
Sapporta is an early alpha release, built and maintained by me, Jasim A
Basheer — email jasim@protoship.io or
 open an issue in the Sapporta repository .
Use Sapporta for your personal and operational database systems, and tell me
what you want improved. Send me your use cases and the places where the tool
gets in your way. For the data grid in particular, tell me which interactions
are not fluid.
Ideas and code contributions are both welcome. If you are unsure whether an idea
fits, open an issue or email me before you start writing code.
Sapporta
Sapporta is open-source and is released under the MIT license.
Built and maintained by Jasim A Basheer , Protoship .

## 关联链接

- https://github.com/jasim/sapporta-skills
- https://sapporta.com/docs/getting-started/create-a-project.md

## 导航

- 项目页：[[10-项目/sapporta.com_9a16595c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
