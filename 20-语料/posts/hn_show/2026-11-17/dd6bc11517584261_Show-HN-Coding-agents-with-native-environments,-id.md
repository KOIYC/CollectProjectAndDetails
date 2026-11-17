---
type: "corpus"
item_id: "dd6bc11517584261"
title: "Show HN: Coding agents with native environments, identity and access"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50526516"
project_url: "https://kosem.ai/blog/coding-agents-workstation-moment"
author: "yevpats"
published_at: "2026-11-17T02:11:01Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-17"
tags:
  - 语料
  - hn_show
  - author_yevpats
  - story_50526516
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Coding agents with native environments, identity and access

> [!info] 一句话导读
> kosem Blog Join the waitlist

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50526516>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：yevpats　|　发布：2026-11-17T02:11:01Z
> 项目链接：<https://kosem.ai/blog/coding-agents-workstation-moment>
> 采集：2026-11-17T11:09:12+08:00　|　id：`dd6bc11517584261`

## 正文

kosem Blog Join the waitlist
On this page
 Why today's coding agents break
 Security
 Performance and productivity
 What kosem is and how it works
 Environment
 Identity and access
 Models
 People and projects
 Audit
 Get started with kosem agents
 Blog
 Introducing kosem. Coding agents with native environments, identity and access
 E Evgeniy Pats Nov 16, 2026 · 7 min read
 Coding agents are reliving the mainframe and minicomputer era. Anyone who was there, or read about it in a history class, knows the setup: people reached a central computer through terminals to get their work done. One big job slowed everyone down, and even once each person had a user of their own, everyone still shared one operating system.
Now the developer's laptop is the mainframe, and the agents are the people at its terminals, all sharing one operating system and the developer's identity and access, while the developer supervises them through a terminal emulator.
Today we're introducing kosem: coding agents with native environments, identity and access. Each agent gets an environment of its own, an identity of its own, and only the access you grant it, instead of the developer's laptop and keys. kosem is in private beta, and we're opening it to more teams as we roll it out. Join the waitlist , and read on for what's inside and how we built it.
acme / checkout / Agents
 Find why checkout returns 502s Done
 Maya Checkout's API has returned 502s since this morning's deploy. Find out why, fix it and open a pull request.
 I'll clone checkout, read the errors since the deploy and find what it changed.
 Started its environment from acme/checkout-dev · Small · 1 vCPU
 Issued github/acme · acme/checkout · read · 60 min, granted without asking
 $ git clone https://github.com/acme/checkout 4.1s
 $ git log --oneline -2 0.1s a41c9e2 payments: share one HTTP client (#1427)
7d03b18 checkout: retry idempotent writes (#1425)
 The 502s are in CloudWatch. Reading them takes aws/prod-logs , which needs your approval.
 Can I use aws/prod-logs for one command? Maya approved · this command · one log group
 Issued aws/prod-logs · one log group · this command · source identity agent:ags_01m9…r7tx
 $ aws logs filter-log-events --log-group-name /prod/checkout-api --filter-pattern 502 1,284 events upstream payments: context deadline exceeded (Client.Timeout 2s)
 The credential expired as the command ended
 a41c9e2 gave payments the fraud check's HTTP client, with its 2s timeout, and payments takes up to 6s. I'll give it its own client back.
 internal/payments/client.go +3 −1 func NewClient(cfg Config) *Client { - return &Client{http: shared.HTTP} // 2s, the fraud check's + return &Client{http: &http.Client{ + Timeout: 10 * time.Second, + }} }
 The integration tests build the whole service, which crawls on 1 vCPU. I'm moving to Large for the build.
 Restarted at Large · 4 vCPUs · 16 GiB, on the same disk, within your limit
 $ make test-integration 212 passed · 3m 08s
 Back to Small · 1 vCPU, as the build is done
 Issued github/acme · acme/checkout · contents and pull requests: write · 60 min
 $ gh pr create --fill #1432
 #1432 Give payments its own HTTP client lint build integration
 Opened #1432, which restores payments' 10s timeout. It's yours to review.
 Idle, so its environment stopped. Its disk is kept for 7 days
Reply to the agent… best
agent:ags_01m9…r7tx Maya
 Environment
 Image acme/checkout-dev
 Now Stopped · idle
 1 2 4 8
 vCPUs · limit Large , 4 vCPUs Its size over the task
 Disk · 20 GiB kept for 7 days
 Access
 github/acme granted Token · write · 60 min
 aws/prod-logs prompt Expired with the command
Go idle 0:47 / 0:47
One task in kosem, from the first message to the pull request.
 Why today's coding agents break
Today's coding agents run on the developer's laptop, as the developer, and that breaks in two ways. The biggest is security. Then come performance and productivity.
Security
An agent needs what a developer needs to get work done: private code and secrets, text from strangers in issues, docs and dependencies, and a way to push and call out. That's Simon Willison's lethal trifecta, [1] and it can't be designed away, since the work needs all three. Any text the agent reads can carry a prompt injection, so it needs defense in depth. On a laptop, only the first layer is there:
The model. System prompts and training teach it to follow the developer rather than what it reads, and models keep getting better at it. Anthropic says that isn't enough: prompt injection is "far from a solved problem." [2]
Least privilege. An injection that gets through should reach only what the task needs. On a laptop, the agent runs as the developer, so one injection reaches everything: their GitHub and cloud credentials, their SSH keys and every repo on their disk.
Audit. Afterwards, the team needs to see what the agent read and ran, what to roll back and what to rotate, and to trace each commit and cloud call back to it. On a laptop, every action is logged as the developer, and the transcript sits in their home directory, where the agent can rewrite it and Claude Code deletes it after 30 days by default. [3]
The patches on top mostly add friction. Approval prompts aren't a security boundary, [4] and Anthropic says they lead to "approval fatigue." [5] OS sandboxes share the laptop's kernel, the docs say not to rely on them "to stop a malicious command," [6] and they break tools like docker . [7] So everyone ends up running --dangerously-skip-permissions , which is a little unfair to the flag: without it, the agent was almost as dangerous.
Performance and productivity
The second set of problems is the mainframe's. Every agent on a laptop shares one machine, and each agent a developer adds makes it worse:
They step on each other's toes. Agents on one laptop share its ports, its Docker daemon, its databases and often its working tree. One switches branches under another, one's tests take the port another's dev server needs, and one's migration resets the database another is testing against. Git worktrees separate the files, not the rest.
They compete for the same cores. One agent's ten-minute build takes every core, and the other agents, and the developer's own editor, wait on it. A laptop can't grow for the build and shrink back while the agent reads code.
They stop when the laptop does. A task that runs for hours needs a machine that stays up for hours. Close the lid, or lose the Wi-Fi on a train, and the agent stops mid-task, so the developer keeps the laptop open and babysits a row of terminal tabs.
Their work is one developer's alone. The transcript, the branch and the half-done work live on one laptop. A teammate can't see how a fix was verified, steer an agent while its developer is out, or pick up the task where it stopped.
Both sets of problems have one cause: the agent borrows the developer's machine and identity. So the line belongs in two places. Around the machine: the agent gets an environment of its own, with its own kernel and nothing of the developer's in it, so it can run freely. And at its edge, where it reaches the outside world: its own identity, only the credentials its task needs, and a record of everything it did with them. Two developers don't share a laptop or a login, and two agents doing different tasks shouldn't either.
What kosem is and how it works
In kosem, each agent gets three things of its own: an environment, an identity with only the access its task needs, and models through one gateway. Around the agents, the team gets IAM for its people and an audit trail of everything. How we built environments, access and audit will each get a post of its own.
kosem Your team
 M Maya Starts and steers the agent
 D David Approves what's on prompt
 Sets the permission set, the size limit and the budget once signs in IAM for people M Maya Agents User on project checkout
 D David Secret Accessor on secret aws/prod-logs
 S Sam Agent Viewer on agent ags_…r7tx
 Roles on the organization, its projects and single resources, such as one secret. Agents hold none. who can start, read and steer it Agent
 agent:ags_01m9…r7tx Directed by Maya
 Its own identity No keys of its own Transcript kept in kosem calls models LLM Gateway Model best This agent $3.18 Project $412 of $2,000 Keys stay in kosem, never in the agent's environment on your accounts Model providers
 Anthropic
 OpenAI
 Google Gemini
 Your own server
 runs its commands in asks for access Environments A fleet of microVMs, one for each agent, each from its team's image Running Stopped Running Running This agent's microVM Large · 4 vCPUs · building Disk kept while idle Credential broker
Its own kernel, root and Docker Resized within the team's limit asks · issues IAM for agents The team's permission set granted github/acme prompt aws/prod-logs · David approves denied Everything else
 The task's lease GitHub · acme/checkout · 60 min AWS · one log group · one command Minted when a command asks the broker, narrowed to it. Ends with the task.
 mints, narrowed Integrations
 GitHub App installation token, scoped to repos Audit log · hashed_token
 AWS AssumeRole with a session policy CloudTrail · accessKeyId
 Google Cloud Short-lived access token Cloud Audit Logs
 records every credential Audit 09:41 Maya started agent:ags_…r7tx
 09:42 agent:ags_…r7tx was issued github/acme hashed_token 3f9a…c1
 09:43 David approved aws/prod-logs · one command
 09:43 agent:ags_…r7tx was issued aws/prod-logs accessKeyId ASIA…7Q2M
 joined on the ID
kosem's building blocks, around one agent.
 Environment
Each agent gets an environment of its own: a microVM with its own kernel, adjustable CPU and memory, a persistent disk, and any Docker image from your registry, so it starts with the team's languages, databases and tools. The agent is root and runs Docker inside it, and nothing of the developer's is there, so it doesn't have to ask before each command.
The agent picks its environment's CPU and memory and changes them as the workload does, within the team's limits: small to read code, large for the build. Each step gets what it needs and no more, so less goes to waste. When the agent goes idle, waiting on someone's answer, its environment stops but its disk persists, so it resumes where it left off in seconds. It keeps working with the laptop's lid closed, and agents no longer share one laptop.
Identity and access
Every agent is a principal of its own, agent:ags_… , and starts with no access at all. The team grants it secrets, and nobody can grant more than they hold: granting a secret to an agent takes access to it.
For GitHub, AWS and Google Cloud, kosem mints short-lived credentials when a command asks for them, narrowed to the request, so no long-lived key enters the environment. Static secrets are the exception, for services that can't mint short-lived tokens yet.
The team marks each secret granted, prompt or denied: the agent uses what's granted without asking, asks a teammate before it uses what's on prompt, and says when something is denied instead of working around it. When the task ends, its access ends with it.
Models
Agents call models through one gateway: every model the team turned on, on the team's own accounts at Anthropic, OpenAI and Google Gemini, or any compatible server. Provider keys never reach an agent or a person.
The organization decides which projects can use which models, and sets spend limits for itself and for each project. Usage is broken down by project, model and agent, so spend ties back to the work it paid for.
People and projects
People get permissions of their own, separate from the agents'. One organization holds your people and your projects, and you shape it the way your teams work: a project for each team or service, and groups for the people who work together.
Roles decide who can do what, at the level you choose: the whole organization, one project, or a single agent or secret, for a person or a whole group. They're granular, so you can split who views, starts and steers a project's agents, who can use which secrets, and who can grant them to agents. Billing, members, policies and the audit log have roles of their own, so nobody needs to be an admin of everything.
Agents are shared with their project by default, so a teammate can read a run, answer the agent's question or pick the task up where it stopped. An agent can be private too, shared only with the people you choose.
Audit
kosem keeps a record of everything, where the agent can't change it. The transcript, every message, command and result, lives in kosem, where the team can read it and the agent can't rewrite it. Every action is logged too: creating an agent, granting a secret, changing a role and reading a transcript.
Every credential is recorded under the agent's name, with GitHub's hashed_token or CloudTrail's accessKeyId , to join with the provider's own logs. In AWS, the agent's name is each session's source identity, so CloudTrail shows which agent made each call.
Get started with kosem agents
Register for the private beta on the waitlist , and we'll email you when your team's access is ready.
Your first agent starts with an environment of its own and nothing else. Give it a task and grant it what the task needs. Then follow its work from your laptop or your phone, and steer it together with your team.
kosem is in private beta. Its agent asks for a key when it needs one, and gives it back.
 Join the waitlist Notes
 Simon Willison, The lethal trifecta for AI agents , June 2025. ↩
 Anthropic, Mitigating the risk of prompt injections in browser use , November 2025. ↩
 Claude Code's docs: cleanupPeriodDays . ↩
 Claude Code's docs: Configure permissions and Choose a permission mode . ↩
 Anthropic, Beyond permission prompts: making Claude Code more secure and autonomous , October 2025. ↩
 Claude Code's docs: Configure the sandboxed Bash tool , and its security limitations . ↩
 Claude Code's docs: docker commands fail . ↩
kosem Blog hello@kosem.ai Privacy policy Terms of service © 2026 Kosem AI

## 关联链接

- https://github.com/acme/checkout

## 导航

- 项目页：[[10-项目/kosem.ai_11f5e85b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
