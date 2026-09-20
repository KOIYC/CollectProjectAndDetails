---
type: "corpus"
item_id: "8ef7753e10c2bd6a"
title: "Show HN: Pizza Bot – An inbox for AI agents that work in the background"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49713894"
project_url: "https://github.com/pizza-bot-app/pizza-bot"
author: "jd_"
published_at: "2026-09-15T15:20:26Z"
captured_at: "2026-09-20T09:38:26+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_jd_
  - story_49713894
  - show_hn
metrics: {"points": 60, "comments": 37, "engagement_velocity": 60}
comments_count: 37
comments_total: 37
discovered_via: "hn:show_hn:90d"
---

# Show HN: Pizza Bot – An inbox for AI agents that work in the background

> [!info] 一句话导读
> Hi HN - long-time lurker (since 2012!), first time poster.Pizza Bot is a self-hosted desktop app for Mac, Windows, and Linux that runs AI agents in the backgrou…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49713894>
> 指标：点赞=60 · 评论=37 · engagement_velocity=60
> 作者：jd_　|　发布：2026-09-15T15:20:26Z
> 项目链接：<https://github.com/pizza-bot-app/pizza-bot>
> 采集：2026-09-20T09:38:26+08:00　|　id：`8ef7753e10c2bd6a`

## 正文

Hi HN - long-time lurker (since 2012!), first time poster.Pizza Bot is a self-hosted desktop app for Mac, Windows, and Linux that runs AI agents in the background and exposes them through an email-like UI. Finished work shows up in Unread, and anything waiting on your approval shows up in Action. It's Apache 2.0-licensed, there's no signup and no telemetry, and you bring your own model provider: Anthropic, Amazon Bedrock, Google Gemini, OpenAI, OpenRouter, or a local model through Ollama. There are builds on the releases page, or you can run it from source.Pizza Bot started as an internal passion project I worked on with a small team at Amazon.The whole thing came out of my frustration at having to manually log CRM activities through a browser form. I built a simple REST API called "JoeBot" that connected to my authenticated browser session over CDP and filled out the form for me using Playwright. Then I hacked up a quick Obsidian plugin so I could trigger it from my local notes (no AI and no MCP servers involved).This caught on quickly. My fellow AWS Solutions Architect Igor Fil joined up with me, and we rebranded the project as "Pizza Bot," named after Amazon's two-pizza teams. We started seeing what other automations we could build. We found a GraphQL API we could query and hacked up some "recipes" to pull data out of the CRM to help with meeting prep. That worked great, and it was right around the time MCP servers seemed to be taking off, so we decided to expose Pizza Bot as an MCP server instead, so it would be available to AI tools through natural language.This was a decent solution for technical users, but the Account Managers who live inside our CRM system wanted something too. We decided to rebuild Pizza Bot as an Electron desktop app modeled after an email inbox, so it would be familiar to non-technical users and would run on both Mac and Windows. We also bundled internal MCP servers as OCI images and hosted them in Amazon ECR as an "addon marketplace" so users could install them with one click without having to set up Amazon developer tooling.The project took off organically and expanded outside of AWS into the wider Amazon organization globally. More than 2,000 people ended up using it for meeting prep, email drafting, Slack summaries, CRM logging, prioritizing their day, and web research.Once apps like Claude Cowork and Amazon's own Quick Desktop came out, we realized the real growth opportunity was outside of Amazon. Rather than try to rip out the Amazon-specific integrations, we rebuilt Pizza Bot once more as an open source project. We leaned on coding agents heavily, which is the only reason a team our size could pull off a full rewrite. I'm pleased to say it's finally public, and we're hoping to bring in community members and see where it goes. We'd like to do for knowledge workers what Claude Code and Codex have done for programmers.A couple of things to know up front. Most of what made Pizza Bot useful on day one inside Amazon came from that internal catalog of skills and MCP servers for Amazon's own systems, and none of it could come out with the app. So it ships thinner than the version those 2,000 people used, and building that catalog back up for tools other people actually use is where we need the most help. It's also a community project and not an AWS service, so there's no support or SLA behind it. The Windows and Linux builds aren't signed yet either.On the technical side, Pizza Bot is a server and a client. The desktop app bundles both, or you can point a client at a remote backend; personally, I self-host the server on my home network and reach it from my phone over Tailscale. The server owns the thread lifecycle and checkpoints state with DeepAgents and LangGraph, and clients rehydrate from it as needed, so you can disconnect mid-run and pick the thread back up from another client. Approval pauses outlive the session that created them and collect in an Action filter, so you can answer an hour later from a different device. The agent you talk to has a sandboxed QuickJS interpreter that can reach your filesystem only if you grant it a folder, but its main job is to delegate. Each subagent is a 1:1 mapping of a Skill, and an Activity bar shows that subagent and the tool calls it's making as it works. Memory is opt-in and stored as plain markdown files on your machine. Every tool call is explicit, including looking up a memory - we err on the side of transparency to reduce surprises. Tools come from MCP servers, and skills are ordinary SKILL.md files with a per-tool approval policy, so existing skills that don't require a code interpreter should still work.What I'd most like to hear about is where the app itself gets in your way, the kind of problem you can't fix by writing a skill or an MCP server. I'm around today to answer questions!

## 评论（37/37）

> **taylorhou** · 2026-09-15T22:21:03.000Z　
> congrats on the public launch! it's been clear to me for a while now that agents will need their own ways to communicate and an asynchronous inbox/task system is a necessity already. will point my agents at the repo to see how we can leverage

---

> **esafak** · 2026-09-15T23:06:46.000Z　
> I have a more basic question; I am trying to understand its purpose.How does this compare with connecting your agent to your ticket tracker? Linear can dispatch the agents: https://linear.app/agents https://linear.app/docs/coding-sessionsIf it is about local work, how does it compare with simply having your agent monitor a directory for ticket files?

---

> **scottydelta** · 2026-09-15T23:32:33.000Z　
> Why does it have to be a desktop app vs a self hostable web app?That way it can truly run asynchronously, even with the computer switched off.

---

> **boplicity** · 2026-09-15T23:59:14.000Z　
> This looks great. I've been playing around with GrokBot, and like a lot of what it does, but would much, much prefer an open source project to manage various asynchronous tasks.What I like about GrokBot is the combination of freeform agent discussions, scheduled jobs, agent-to-agent communication, per-agent memory, and the fact that they all get a sandboxed instance with a browser. It's very well implemented. I think they have a very similar vision to yours.

---

> **aaronax** · 2026-09-16T00:05:24.000Z　
> Why not use real email?

---

> **sgc** · 2026-09-16T00:28:40.000Z　
> Do you have a list of a few mcp servers or other tools you would add to help with the pizza-bot specific workflow? For example, how would you enforce structured output, should that be an mcp server, a plugin, already in the box?

---

> **zdyn5** · 2026-09-16T02:00:59.000Z　
> Nice work! Can you comment on how this differentiates from Paperclip?

---

> **htrp** · 2026-09-16T02:50:45.000Z　
> why not an actual inbox? set up a gmail and have the agent email you?

---

> **nucleardog** · 2026-09-16T03:25:38.000Z　
> Got it installed, been playing with it for a bit.Had a bit of jankiness during setup as I fought with llama.cpp bugs. There are a few issues around models reported by the provider changing, refreshing as they change, had a few instances of "New Chat" showing one model then hitting llama.cpp with another, etc. Sorry, been traveling for a bit and didn't have the energy to properly recreate and put together a real bug report. Just a heads up that the onboarding there is a bit rough, though anyone running their own local models is probably more than able to get it figured out.I'm really liking it. I wish I had something more substantial to say than "it's easy and clean" but... it's easy and clean. And as far as "AI tooling" goes, the setup was an absolute breeze even with the issues. The fact that I can just install a single app and go rather than spending hours and hours on setup, configuration, etc makes me way more likely to use this going forward... it's a lot easier to rely on a tool when I know it will be quick to fix if it breaks.One note and one feature request, if you want 'em:Though now that I understand the concepts better it's obvious, it _wasn't_ immediately obvious why the MCP server I added wasn't working. Tools are called via "tasks", and "tasks" are defined based on the skills. I had to create a skill. I'm sure it's somewhere in the documentation but I (and most people) don't read that kind of stuff, so would be good to surface somewhere obvious in the UI maybe?And I would absolutely _love_ if you could override the provider and model per task. I run a small model locally as it's good enough for most of what I want to do (and cheap! and private!), but it would be great if I could define a "write-code" skill that was run via Claude instead or something so I could delegate tasks that aren't really suitable for a tiny local model out to something more capable.Anyway... Cool tool. Hope to see it continue to grow and evolve! Thank you for releasing this!

---

> **jd_** · 2026-09-16T03:51:41.000Z　
> Author here - thanks so much for the great questions! Our post on the AWS Open Source blog has more screenshots and an architecture diagram if you want to give it a skim: https://aws.amazon.com/blogs/opensource/introducing-pizza-bo...

---

> **je42** · 2026-09-16T04:57:31.000Z　
> How would you compare PizzaBot to Herdr?

---

> **aadyachinubhai** · 2026-09-16T06:27:14.000Z　
> cool idea, how helpful is this in practice?

---

> **digi59404** · 2026-09-16T06:40:00.000Z　
> Was watching a video from GitLab, posted 7 months ago about something similar.You might find it interesting. https://youtu.be/TRpQW-TFTfw

---

> **nzjrs** · 2026-09-16T07:33:01.000Z　
> Why bother depending on DeepAgents and LangChain etc. My professional impression is such Middleware no longer brings anything if you primarily maintain the codebase with coding tools.

---

> **weee322** · 2026-09-16T07:51:06.000Z　
> Ideal for https://github.com/giannisanni/pulsar/
> or kimi 3 on CPUprobably 30s for one token is too long for normal people but for agents it is ok

---

> **BSOhealth** · 2026-09-19T17:39:05.000Z　
> I added a quick setup option for Pizza Bot + AudioReality, so you can have your Pizza Bot inbox turned into a quick audio update via podcast feed: https://www.audioreality.ai/docs/agents/pizza-bot

---

> **jd_** · 2026-09-15T22:32:06.000Z　
> Thanks! I was pleasantly surprised with how naturally a lot of email idioms seemed to align here. In retrospect, it makes sense if you think of human-to-agent communication as another form of asynchronous communication.

---

> **jd_** · 2026-09-15T23:25:10.000Z　
> Thanks for the question!Think of Pizza Bot as the "harness"/interface your agents actually run in. You'd still hook up Linear via their MCP server (https://linear.app/docs/mcp) for "what needs doing." Pizza Bot is what handles the run itself (scheduling the interaction, routing tool-call approvals to you, and holding conversation/agent state).The part that's actually different from "agent in a terminal" or "agent posting to Slack" is that it's built for having a bunch of these running at once. Instead of N terminal tabs or N ticket comment threads to figure out which agent is stuck waiting on you, they land in one inbox — jump between threads, see which ones are paused on an approval or a question, answer, and move on.Let me know if that helps to clarify things!

---

> **jd_** · 2026-09-15T23:43:12.000Z　
> It’s both! The Releases page indeed links to the Electron app so it’s easy to get started, but you can also run just the backend and web app separately. I have it running in a Docker container on my home network that I connect to from my phone using Tailscale. Check out the docs here: https://github.com/pizza-bot-app/pizza-bot/blob/main/docs/ST...

---

> **jd_** · 2026-09-16T00:16:11.000Z　
> Thanks for the feedback! I’ll give GrokBot a closer look. We’re focused on being open source and decoupled from any particular model provider, but it’s great to see a lot of capable tools popping up in this space.We do ship a QuickJS code interpreter, but otherwise, sandboxing is something we deferred until after launch to make sure we have time to get it right. LangGraph / DeepAgents, which we’re built on, already have the right hooks in place, though. :)

---

> **jd_** · 2026-09-16T00:22:14.000Z　
> You mean giving each agent its own real email address? Startups like AgentMail are certainly doing that!In our case, we wanted to borrow the UX of email (to be intuitive to knowledge workers) but not necessarily the implementation.Was there a particular workflow you had in mind here?

---

> **jd_** · 2026-09-16T00:35:32.000Z　
> There are so many! Personally, I’ve been able to get remarkably far with the built-in filesystem tools (courtesy of DeepAgents) paired with a web search MCP (Kagi is great!). Were there any particular workflows you had in mind?

---

> **jd_** · 2026-09-16T02:24:21.000Z　
> Thanks! I'm not overly familiar with Paperclip, but from the website, it looks to provide orchestration over a fleet of existing agent harnesses, whereas with Pizza Bot, we run the execution loops for each agent ourselves (built on LangGraph / DeepAgents). We also stick to a "thread" model (similar to email), whereas Paperclip seems to work on a task-based model.It's an interesting alternate UX framing, for sure. It's possible there are scenarios where a different abstraction makes more sense, but I'm personally curious to see how far we can extend the email idiom!

---

> **jd_** · 2026-09-16T03:05:11.000Z　
> @aaronax had a similar thought!In our case, we wanted to borrow the UX of email (to be intuitive to knowledge workers) but not necessarily the implementation.Full control of your data was a design principle from the beginning, including being able to run fully offline with local models, so we didn’t want to add a dependency on email.With that said, you can certainly hook up an MCP server and have the agents read and send emails (with human-in-the-loop approval) on your behalf.

---

> **jd_** · 2026-09-16T03:37:34.000Z　
> Thanks so much for the feedback! The README arguably needs a diagram that shows the orchestrator-subagent delegation pattern and how they map to Skills, since you’re right - it’s not intuitive without reading the docs, and it’s somewhat unique from other agent harnesses I’ve seen.The internal-only predecessor actually did let you specify the individual model for the subagent calls. DeepAgents supports this, so it shouldn’t be a big lift. I’ll add an issue on GitHub. Thanks for the request!

---

> **jd_** · 2026-09-16T05:13:48.000Z　
> Thanks for the question! Similar to another user’s comment about Paperclip, Herdr looks to provide a layer on top of existing agent harnesses, whereas with Pizza Bot, we run the execution loops for each agent ourselves (built on LangGraph / DeepAgents). This gives us control over checkpointing, human-in-the-loop, etc., and the only “dependency” is your model provider.I’ve been describing Pizza Bot as an “inbox” because it captures the UX, but this does seem to cause confusion and undercuts the fact that Pizza Bot actually is an agent harness itself, not just an orchestrator of agents hosted elsewhere.Let me know if that makes sense!

---

> **jd_** · 2026-09-16T06:43:52.000Z　
> Thanks! I think it depends on how well Pizza Bot aligns with your mental model. Despite living in Claude Code for many things, I find the email-like UX we built for Pizza Bot matches my intuition for how I want to interact with agents beyond a simple chat interaction, including concepts like pinning, folders, filters, actionable threads, etc.The bigger proof point for me was the adoption we saw from less technical folks at Amazon. Most of them immediately “got it.”

---

> **jd_** · 2026-09-16T06:52:10.000Z　
> Oh neat - thank you for sharing! I hadn’t seen this before, but we were definitely inspired by a post LangChain made about “ambient agents”: https://www.langchain.com/blog/introducing-ambient-agentsIt seemed fitting to build Pizza Bot on top of LangChain’s tech, given the inspiration. :)

---

> **jd_** · 2026-09-16T13:53:18.000Z　
> Thanks for the question!I could maybe see that being the case for LangChain, specifically, if you’re just thinking about abstracting the LLM provider’s APIs. But here, we’re specifically using LangGraph to handle checkpointing and state management. This is a much more difficult challenge to get right in a sufficiently complex application like Pizza Bot.Case in point: for the internal-only version, we wrote this ourselves. It works for the most part, but there are subtle edge cases and bugs that we’ve had to tackle like a game of whack-a-mole.For the open source release, we looked at a few frameworks and deliberately settled on LangGraph (and DeepAgents). I’ve never been so happy to throw away code. :)In our experience so far, it’s been rock solid. Most of the issues/bugs we’ve had have come from streaming to the frontend, so a simple Cmd-R / Ctrl-R will get you back up and running without having to worry about your data being lost.

---

> **jd_** · 2026-09-16T13:56:05.000Z　
> Totally agree! I’ve got scheduled agents that run (a little slowly) overnight using Qwen 3.8 27B that are ready for me by the morning. :)

---

> **taylorhou** · 2026-09-16T01:13:38.000Z　
> yep. as someone who is inbox zero and treats my inbox(es) as task management, it all makes sense to me!

---

> **sgc** · 2026-09-16T04:13:39.000Z　
> I need to be able to enforce structured output easily (json, and xml if possible). That would be my number one slightly less than typical requirement.Other than that, I like to insert agents into deterministic workflows, so some way to easily have deterministic steps (calling a script rather than delegating to an agent, but determined by the workflow rather than the agent). However this second one is likely out of scope for a while, since it is the inverse of the typical agent workflow. I could probably work this out clunkily by polling the cli from an external master script, but it would be cool to have it all inside the box.

---

> **jd_** · 2026-09-19T00:51:21.000Z　
> Quick update that I added issues for both the README update and overriding the model that a skill's subagent will use:- https://github.com/pizza-bot-app/pizza-bot/issues/99- https://github.com/pizza-bot-app/pizza-bot/issues/100Thanks again!

---

> **jd_** · 2026-09-16T02:33:12.000Z　
> Love it. Maybe "inbox zero" for agents would have been a better tagline! :)

---

> **jd_** · 2026-09-16T04:27:10.000Z　
> Ah, this may actually work out of the box if you tell Pizza Bot to use its `task` tool to dynamically launch a subagent (which maps 1:1 with a Skill), and provide it with a `responseSchema`. I’ll test this when I’m back at a computer and report back!

---

> **jd_** · 2026-09-19T00:38:18.000Z　
> Quick update. This doesn't work out of the box, but I've created an issue to enable this here: https://github.com/pizza-bot-app/pizza-bot/issues/98

---

> **sgc** · 2026-09-19T19:38:25.000Z　
> Thank you, I will keep my eye on it.

## 导航

- 项目页：[[10-项目/github.com_0ce48682]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
