---
type: "corpus"
item_id: "4ebaa9c3e91eedeb"
title: "Show HN: ForthWrite – Email AI that learns your voice from every edit you send"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48725623"
project_url: "https://forthwrite.ai/blog/how-forthwrite-learns-your-email-voice"
author: "curtisboortz"
published_at: "2026-06-29T21:37:49Z"
captured_at: "2026-09-22T13:12:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_curtisboortz
  - story_48725623
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: ForthWrite – Email AI that learns your voice from every edit you send

> [!info] 一句话导读
> All articles Voice Matching

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48725623>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：curtisboortz　|　发布：2026-06-29T21:37:49Z
> 项目链接：<https://forthwrite.ai/blog/how-forthwrite-learns-your-email-voice>
> 采集：2026-09-22T13:12:52+08:00　|　id：`4ebaa9c3e91eedeb`

## 正文

All articles Voice Matching
 How ForthWrite Learns Your Email Voice
 How ForthWrite learns your email voice: pgvector RAG with MMR re-ranking, edit-distance scoring against what you send, and a phrasing miner.
 5 min read · June 24, 2026
 I've been chasing a specific problem for about a year: email assistants write a professional email, not your email. The tool produces something correct, polished, and obviously not from you. You edit it. You send it. You edit the next one. Nothing improves.
Most tools don't have a feedback loop, so the model has no way to learn from the edits you make.
Here's how ForthWrite closes that gap.
The core problem with "learns your voice"
Every AI email tool claims to learn your voice. The claim describes very different things depending on the tool.
Prompt engineering means you write a system prompt describing your style. "Direct tone. No em-dashes. Under 100 words." The model follows instructions but doesn't update. You hit the same ceiling on every draft.
Fine-tuning actually updates model weights on your data. It could work, but it costs significant compute per user and doesn't update dynamically as your writing evolves, which makes it impractical at consumer scale.
RAG (retrieval-augmented generation) is what ForthWrite uses: pull real examples of your writing into every prompt at generation time, so the model is imitating your actual sent email rather than a description of it.
RAG alone isn't enough either. The retrieval has to be good, and "good" retrieval changes as your habits change, which means it needs a feedback mechanism to stay current.
How ForthWrite builds your corpus
On first connect, we batch-import your Gmail Sent folder. Each message is normalized (HTML stripped, forwarded sections and signatures removed), embedded with text-embedding-3-small , and stored in Postgres with pgvector.
Most tools ask you to paste a few writing samples manually. We batch-import your full Gmail Sent folder on first connect, so the model has hundreds of real examples of your voice before you draft a single reply.
RAG retrieval on every draft
When you hit Draft, ForthWrite:
Embeds the incoming email thread
Queries pgvector for a candidate pool of cosine-similar matches from your sent history
Re-ranks using MMR (Maximal Marginal Relevance) to avoid returning near-duplicate examples that would add redundant signal
The final output is a small block of few-shot examples injected into the system prompt. We enforce a minimum confidence threshold before injecting anything. If no match clears the bar, we inject nothing rather than risk the model imitating an irrelevant old reply.
The MMR step is important. Cosine similarity alone tends to cluster: the top five results are often slight variations of the same email. MMR trades off similarity against diversity, so the few-shot block covers more of your stylistic range rather than over-representing one thread type.
Edit-distance scoring: the feedback loop
Every time you edit an AI draft and hit Send, ForthWrite captures both versions.
We compute a normalized Levenshtein edit-distance score between the generated draft and what you actually sent:
Score near 1.0 : you sent it nearly verbatim. The draft was right.
Score near 0 : you rewrote most of it. The draft missed.
These (generated, sent) pairs accumulate in a table. Low-scoring pairs (heavy edits) feed an async optimizer that analyzes the gap and suggests system-prompt updates. High-scoring pairs (near-verbatim sends) go into the retrieval corpus as positive few-shot signals, so future RAG pulls lean toward what already worked.
The phrasing miner
RAG handles situational context well. But there's a different signal hiding in near-miss drafts, the ones where you kept 95% of the text and only swapped two words.
A cosine diff on two emails that differ by "no worries at all" versus "no worries" looks identical. Those pairs never surface in a "find bad drafts" pass. Standard edit-distance bucketing misses them too, because the overall score is high (most of the draft was fine).
So we run a separate miner: a word-level LCS (longest common subsequence) alignment between the AI draft and your sent version. We collect all deletions and substitutions, count which ones recur across your corpus, and measure consistency.
Of the 12 times the AI wrote "circle back," how many did you remove? Of the 8 times it wrote "I hope this finds you well," how many did you delete? Anything above a frequency and consistency threshold gets written to your system prompt as an explicit avoid or prefer rule.
No model involved in this step, just a deterministic diff. It catches the small, recurring patterns you'd never think to describe but always clean up by hand.
The convergence problem
This creates a non-obvious dynamic: as the model gets better, you make fewer edits, which produces fewer correction signals. The optimizer starves itself on success.
We handle it by running phrasing mining on a time-based cadence independent of edit-distance score. Users in a steady state (high scores, few edits) still get periodic refinement passes over recent sent email. The feedback loop doesn't collapse just because it's working.
It's an open problem in a broader sense. If you're doing something similar with RLHF or preference modeling on sparse positive feedback, I'd be curious how you've approached it.
Stack
Chrome extension (esbuild)
Next.js 16 API backend
Supabase (Postgres + pgvector)
Anthropic Claude as primary model with prompt caching on the system block for cost efficiency
OpenAI text-embedding-3-small for retrieval
The prompt caching piece matters more than it sounds. The system block (your persona, phrasing rules, few-shot examples) is the same across multiple drafts in a session. Anthropic's cache TTL means we pay for that block once per hour rather than on every call. That's the difference between an affordable product and one that costs more to run than it earns.
Try it
ForthWrite is a Chrome extension for Gmail. 14-day free trial, no card required to start.
forthwrite.ai
Happy to answer questions about the retrieval architecture, the phrasing miner, or the caching design.
 More in Voice Matching
13 min read · Jun 16, 2026
 AI Email Voice Matching: How AI Learns to Write Like You
 Most AI email tools generate competent email. Voice-matching AI generates email that sounds like you. Here is what that distinction means in practice and why it is harder than it sounds.
 Read article 6 min read · May 12, 2026
 What 'Saves Time' Doesn't Tell You About an AI Email Tool
 Speed is the table-stakes promise of every AI email tool. The question that actually separates them is whether the output is good enough that you'd send it without re-reading every word.
 Read article 3 min read · Apr 29, 2026
 I Copied My Last 50 Sent Emails Into ChatGPT to Fine-Tune It. It Still Didn't Work.
 A lot of people try to teach ChatGPT their email style by pasting examples. Here's what actually happens when you try it, and why it hits a ceiling fast.
 Read article
 In your inbox
 Drafts that already sound like you.
 It learns from mail you have already sent, in the Gmail or Outlook window you already use.
 Open Inbox Or generate a persona prompt
Email drafts that sound exactly like you wrote them. Save time without sacrificing quality.
Product
 Inbox
 Features
 Pricing
 ForthWrite for Outlook
 ForthWrite for Slack
 ForthWrite for Claude
 Sign in
Consulting
 AI workflow diagnostic
 Firm insights
Resources
 Persona prompt generator
 Blog
 By profession
 By industry
 ForthWrite vs competitors
 Email sign-offs
 Introduce yourself by email
 Out-of-office templates
 About
Legal
 Privacy Policy
 SMS Consent
 Terms of Service
 Security
 Sub-processors
 Support
© 2026 ForthWrite. All rights reserved. Professional emails, zero effort
Features How it Works Teams Consulting Pricing Sign in Try now for free
 Try now for free

## 导航

- 项目页：[[10-项目/forthwrite.ai_feec970c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
