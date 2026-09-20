---
type: "corpus"
item_id: "b06bf4c938bddbcf"
title: "Show HN: Aclif – Agent CLI framework: one grammar, canonical names across SaaS"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49743382"
project_url: "https://aclif.ai/"
author: "chris_marino"
published_at: "2026-09-17T16:48:17Z"
captured_at: "2026-09-20T14:03:17+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_chris_marino
  - story_49743382
  - show_hn
metrics: {"points": 34, "comments": 17, "engagement_velocity": 34}
comments_count: 17
comments_total: 17
discovered_via: "hn:show_hn:90d"
---

# Show HN: Aclif – Agent CLI framework: one grammar, canonical names across SaaS

> [!info] 一句话导读
> aclif, the Agent CLI Framework

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49743382>
> 指标：点赞=34 · 评论=17 · engagement_velocity=34
> 作者：chris_marino　|　发布：2026-09-17T16:48:17Z
> 项目链接：<https://aclif.ai/>
> 采集：2026-09-20T14:03:17+08:00　|　id：`b06bf4c938bddbcf`

## 正文

aclif, the Agent CLI Framework

# The Agent CLI Framework

aclif builds command-line tools for AI agents. An agent gets a single tool that provides a unified abstraction across every SaaS provider: one grammar, and canonical names that reach the same record by the same name on any platform.

## Try it now

Install the binary, list the providers, and read a command's schema, examples, and safety metadata.

```
npm install -g @aclif/core

aclif discover --json
aclif learn salesforce --json
aclif learn servicenow --json
aclif salesforce data query --schema
aclif salesforce data query --examples
aclif salesforce data query --query "SELECT Id FROM Account LIMIT 3" --dry-run
aclif servicenow data query --table incident --query "active=true^priority=1" --dry-run
```

## Why agents need their own CLI

An MCP server publishes a fixed list of tools, and every tool on the list occupies the agent's context on every turn. The server's author trades coverage for cost when the server is built. Publishing every operation (a typical API has hundreds of definitions) keeps the whole API reachable and consumes tokens for all of it on every turn. Publishing a handful of broad operations keeps the token count small, and any operation the author left off the list is out of the agent's reach. An agent that spans several platforms needs a server, a login, a grammar, an error format, and a set of names for each.

aclif loads a command's definition only when the agent asks for it, so the whole API of every provider is reachable at no standing cost in context. One grammar, one envelope, and one error vocabulary cover every provider, so the agent's context stays about the same size whether it reaches one platform or five.

An agent that runs a defined workflow can leave the model out of the call altogether. A person or an authoring tool works out the exact command at design time and embeds it in the workflow as a string. At run time the agent executes that string as ordinary code, with no tool definition loaded and no inference. The command is chosen at design time, and the authority to run it, the credential, the acting identity, and the policy, is supplied at run time by whatever runs it. Neither side ever holds both.

### One grammar

One command structure, one JSON envelope, and one error vocabulary across every provider. An agent learns the tool once, and a new platform adds commands without adding grammar. A JSON manifest adds a command over one HTTP endpoint in the same grammar, with no code.

### Canonical names

Alias sets map `customer` to `Account` in one Salesforce instance and `core_company` in ServiceNow. A tenant catalog, captured from each instance at deploy time, teaches the CLI each instance's custom objects and fields with no change to the provider.

### Errors an agent can act on

An agent recovers in one turn. Every error names the failure, the command that fixes it, and, where the provider's classifier has a rewrite rule for the mistake, the corrected input ready to resend. The classifier is plain code with no model behind it. A command validated in a shell at design time returns the same error at run time under any host, because the same command classes run in both.

### Introspection without execution

`--schema`, `--examples`, `--shape`, and four more flags return before the command runs, need no credentials, and count against no API quota. An agent can discover, learn, introspect, and preview against a rate-limited instance and spend nothing.

### An embeddable runtime

The same command classes run in-process inside a host that supplies credentials, identity, and policy per request, keeps connections warm, and caches expensive logins per instance. A gateway built on it works with the enterprise's own identity provider and secrets vault.

### Declared safety

Mutability, blast radius, reversibility, and idempotency are declared on every command. A policy check can refuse it before its code loads. Every mutation accepts `--dry-run`, demands `--confirm` where its metadata says so, and writes an audit line after every run.

## The introspection-first workflow

An agent needs no documentation beyond the binary, and nothing before the last step touches the API.

```
aclif discover --json                          # every provider, its tier, whether credentials are configured
aclif learn salesforce --json                  # a briefing: topics, key fields, query syntax, auth paths
aclif salesforce data query --schema           # flags, args, safety metadata, no execution
aclif salesforce data query --examples         # runnable examples with the responses they produce
aclif salesforce data query --query "SELECT Id, Name FROM Account LIMIT 5" --dry-run
aclif salesforce data query --query "SELECT Id, Name FROM Account LIMIT 5" --json
```

The envelope's `_context` block holds pagination with the exact next command, the fields available, and related commands worth running. Exit codes are 0, 1 (API), 2 (usage), 3 (authentication). The contract and its JSON Schemas are in CONTRACT.md.

## Three ways to run it

A vendor CLI is built for one deployment: installed on a machine, logged in by the person at the keyboard, one process per command. Behind a gateway that fails. Every call spawns a process and logs in again, the acting user's identity cannot be forwarded, nothing declares what a command will do, and nothing is uniform to audit. aclif's command classes run unchanged in three places, and whoever runs them decides who supplies credentials, enforces policy, and keeps the audit trail.

- Run by the agent. The agent process spawns the binary, executes the command, and reads the JSON it returns. Credentials come from flags, environment variables, or a profile in the agent's own environment. Use this when one agent, one operator, and one set of credentials share a trust boundary.
- Run by a host application, the design-time case. An application sits between the model and aclif and holds the credentials. The model calls a tool the application defines, and the application executes the command, in-process or by passing a command string to the CLI. A person or an authoring tool uses this to let a model discover providers, introspect commands, and validate the exact command it will write into an agent. Use this when the model must never hold credentials and tool definitions must stay out of its context.
- Run by a gateway, the runtime case. A deployed agent submits commands, and one long-lived process serves many such agents. The gateway resolves credentials from the enterprise vault per request, checks policy against the acting user, records every call, and keeps connections warm. The agents hold no provider credentials and cannot widen their own scope. Use this when many agents share providers and one place must hold policy and audit.

| | Run by the agent | Run by a host application | Run by a gateway |
| --- | --- | --- | --- |
| Credentials | flags, env, `config.yaml` | host-supplied resolver | vault-backed resolver, per request |
| Policy | `config.yaml` | `capabilityGate` hook | `capabilityGate` plus the host's middleware |
| Identity | `--identity-token` or env | the acting user on the invocation | the acting user and SSO claims from the request |
| Audit | stderr line per run | reporter events | reporter events, recorded by the host |
| Connections | file session cache | runtime pool | runtime pool, keyed per instance and identity |

Details on the Embedding page.

## Gateway deployments

Long-lived, embeddable deployment enables a gateway topology where additional security policy can be applied. One process the enterprise operates executes every command for every agent, and the arrangement provides:

- Credentials in one place. Resolved inside the gateway, per request, from the enterprise's vault. Agents hold none.
- Enterprise-wide canonical names. Tenant catalogs and alias sets are held by the gateway, so every agent uses the same names for the same records across every provider and instance.
- Every call attributed to a person. The acting user's identity travels with each call into the policy check and the audit record, even through a shared service account.
- Policy enforced once. Every command declares what it will do, and the gateway checks that declaration before the command's code loads. Agents cannot widen their own scope.
- One audit trail. The same event for every command from every agent, naming the user, the command, and the outcome.

## Install, or build your own

```
npm install -g @aclif/core

# Your org's My Domain URL, no trailing slash
export SF_INSTANCE_URL=https://example.my.salesforce.com

# A session token from the Salesforce CLI (sf org login web first if needed)
export SF_ACCESS_TOKEN=$(sf org auth show-access-token -o me@example.com --json | jq -r .result.accessToken)

aclif salesforce data query --query "SELECT Id, Name FROM Account LIMIT 3" --json
```

Without the Salesforce CLI, use an API user. Salesforce emails the security token when the password is set or reset:

```
export SF_INSTANCE_URL=https://example.my.salesforce.com SF_USERNAME=me@example.com SF_PASSWORD=... SF_SECURITY_TOKEN=...
aclif salesforce data query --query "SELECT Id, Name FROM Account LIMIT 3" --json
```

The `aclif` binary ships with every built-in provider and needs Node 22 or later. The binary you ship is yours: one scaffold command produces a CLI with its own name, its own config directory, its own environment variables, and only the providers it chose. See Getting started and Build a CLI.

## Providers

Salesforce, ServiceNow, DocuSign, and Agentforce are native and are included in every release. Google Workspace (Gmail, Calendar) is contributed. A private tier holds providers a fork keeps to itself, under a path upstream never commits to. Writing a provider takes little effort: it is a direct translation of the platform's API specification onto the command surface, a coding agent does it from a sample prompt in the repository, and the conformance suite checks the result. See Providers.

aclif is MIT licensed. Contributions follow CONTRIBUTING.md; the guide for people and coding agents changing the framework is AGENTS.md.

## 评论（17/17）

> **chris_marino** · 2026-09-17T17:03:58.000Z　
> We found after deploying many enterprise agents that letting the model choose tools at run time can cause problems. The agent holds the credential and sometimes chooses the wrong tool. Using the same tool every time prevents this.

---

> **charlie_martin9** · 2026-09-17T17:43:48.000Z　
> I have to build a cli for every provider? Seems like a lot of effort.

---

> **rvz** · 2026-09-17T18:25:41.000Z　
> This does not make any sense whatsoever.

---

> **Cameri** · 2026-09-17T18:28:14.000Z　
> How does this differ from the printing press?

---

> **tikimcfee** · 2026-09-17T17:37:06.000Z　
> Absolutely in love. I'll be testing this after the daily grind.I've had nothing but success with converting daily work into "notes" that then translate into runnable, deterministic application CLIs to completely sidestep "what do I need to say to you to make you do the thing??"I'm interested in how this spreads across enterprise flows, because the issue is always discovery and usability.How deep do you usually go with CLI composition and layering? Do you tend to find a flat list of commands and sub command help works most? Have you experimented with connecting CLIs Linux-pipe-style as if it was a dynamic application in the OS?

---

> **agentdev001** · 2026-09-17T18:44:21.000Z　
> "The agent holds the credential"Huh? It shouldn't. Am I misunderstanding, or is this referencing poor practices?"Using the same tool every time prevents this"What does this mean? I looked at the project, im not sure what this means.

---

> **chris_marino** · 2026-09-17T17:48:11.000Z　
> Yes. But any coding agent can do this in a matter of minutes. There is an example prompt and corresponding Skill.md in the repo.https://github.com/agent-cli-framework/aclif/blob/main/docs/...https://github.com/agent-cli-framework/aclif/blob/main/.clau...

---

> **pixl97** · 2026-09-17T18:19:30.000Z　
> Tell your providers to stop building workspaces with conflicting identifiers and namespaces.

---

> **chris_marino** · 2026-09-17T18:29:49.000Z　
> I thought I made it clear right up front. 'Why agents need their own CLI'What's not clear about that?

---

> **Cameri** · 2026-09-18T17:32:29.000Z　
> This is a legitimate question so I don't understand why it would get downvoted.
> The Printing Press _already exists_ (https://github.com/mvanhorn/cli-printing-press) and it's not limited to SaaS providers like Aclif seems to be.

---

> **chris_marino** · 2026-09-17T17:53:25.000Z　
> The objectives are to reduce/eliminate as much inference variability as possible. A side benefit is that inference costs collapse as well.It is used internally for what we call 'compiled workflow agents' where no inference is necessary. An agent composer determines the exact command at design time. That is part of a discovery loop that can introspect the service to construct the command.More here. https://www.promptone.ai/resources/downloads/

---

> **chris_marino** · 2026-09-17T18:27:37.000Z　
> The command structure is provider/topic/command. Taken literally from the oclif framework, with the provider simply being a topic namespace. Haven't needed to pipe anything since in our deployments, the agent makes a call to the gateway via a command API so a pipe wouldn't be possible between commands

---

> **chris_marino** · 2026-09-17T19:04:19.000Z　
> In many cases, the agent does hold the credential. When you authorize OpenClaw to read your gMail, OpenClaw has the credential. This is absolutely a poor practice, but common, nevertheless.As for using the 'same tool', what I meant was that you the agent doesn't have to pick the tool at all. There is just one: the aclif CLI. Not separate tools for Salesforce, Docusign, Workday, etc that the agent needs to learn (and possibly mess up). Just the one aclif tool. Same grammar for all external services. Less agent inference the better.Finally, alif CLIs support individual auth so a request can use SSO identities and fetch a token from a secrets value. The CLI holds the secret. If you deploy the CLI on a host or gateway, the agent never sees it.

---

> **chris_marino** · 2026-09-17T18:20:45.000Z　
> LOL.

---

> **sunir** · 2026-09-17T18:42:25.000Z　
> Here's a good set of questions for any write up:Who are we talking about? What's their role? (What agent? What is the job to be done?)What is the status quo? What's the problem with the status quo? What else has been tried? What's the consequence of not solving the problem? What more important problem do you need to work on that you're blocked because of this problem? What's the ideal solution? What's the current offer? Why would someone say no to any given solution? How have you addressed those problems?

---

> **agentdev001** · 2026-09-17T19:26:47.000Z　
> Some really broad assumptions here, and youre being unclear."When you authorize OpenClaw to read your gMail, OpenClaw has the credential."I can only assume you are implying that the execution environment accessible by the model via the harness here, had access to the credential. This is not even broadly true, as there are many single click solutions for deploying gateways that will allow operators to tls inspect and replace secrets in flight, outside of the agent execution environment.Sure, not doing that is poor practice- but your phrasing is unfair."the agent doesn't have to pick the tool at all. There is just one: the aclif CLI"Okay, so- if thats the only tool, then why are we even talking about credentials? Why are we talking about openclaw? The whole conversation regarding creds being in bad places is predicated on agents having native control over a sandbox- generally through shell. If your use case lets you bake whatever resource access is needed into a single tool- then many other security layers bubble up in value, being that you no longer need to authn/z arbitrary networked calls.Also, yea sure- there is "one tool", all you've done is abstracted the tools into arguments."Less agent inference the better."Show me the data, then. Show me how this performs better than the alternatives. This sounds like all you've done here is reinvent progressive disclosure?"The CLI holds the secret. If you deploy the CLI on a host or gateway, the agent never sees it."Okay, so- brokering, again. How are you solving authz then?

---

> **chris_marino** · 2026-09-17T20:04:43.000Z　
> My response was simplified because your question was basic. OpenClaw was one example that fit the pattern, not a claim that every deployment holds the credential in the sandbox. Injection proxies exist and I should have said so. As for showing the data for advantages, I'll refer you to Anthropic and Cloudflare's Code Modehttps://www.anthropic.com/engineering/code-execution-with-mc...
> https://blog.cloudflare.com/code-mode-mcp/We have our own, but will defer to 3rd party evidence.Reinventing progressive disclosure is definitely part of this, but that's only one element of the approach. To be clear, this is all based on what we use internally, deployed in a particular way within our platform. Will leave it up to others to determine how useful it may be for them.As for authz, that's what the rest of our system does and is beyond the scope of the aclif effort.

## 关联链接

- https://example.my.salesforce.com

## 导航

- 项目页：[[10-项目/aclif.ai_76c8d340]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
