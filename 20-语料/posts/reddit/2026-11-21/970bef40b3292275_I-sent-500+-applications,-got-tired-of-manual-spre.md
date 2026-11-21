---
type: "corpus"
item_id: "970bef40b3292275"
title: "I sent 500+ applications, got tired of manual spreadsheets and a broken system. So I built my own job-hunt CRM."
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/microsaas/comments/1xsyk59/i_sent_500_applications_got_tired_of_manual/"
author: "ayodelep"
published_at: "2026-11-11T05:01:01+08:00"
captured_at: "2026-11-21T14:46:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-11"
tags:
  - 语料
  - reddit
  - r/microsaas
metrics: {"score": 6, "comments": 19, "upvote_ratio": 0.875}
comments_count: 18
comments_total: 19
discovered_via: "reddit:14d+settle10"
---

# I sent 500+ applications, got tired of manual spreadsheets and a broken system. So I built my own job-hunt CRM.

> [!info] 一句话导读
> Like a lot of grads and job seekers, I've felt the brutal beating of the modern job market. Since August of 2025, I’ve sent out over 530 applications across tec…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/microsaas/comments/1xsyk59/i_sent_500_applications_got_tired_of_manual/>
> 指标：得分=6 · 评论=19 · 赞踩比=0.875
> 作者：ayodelep　|　发布：2026-11-11T05:01:01+08:00
> 项目链接：—
> 采集：2026-11-21T14:46:36+08:00　|　id：`970bef40b3292275`

## 正文

Like a lot of grads and job seekers, I've felt the brutal beating of the modern job market. Since August of 2025, I’ve sent out over 530 applications across tech and commercial roles, only to be hit with endless "we're sorry, but we've decided to move on to other candidates" emails. It felt like I was smashing my head against a brick wall over and over again and asking for more.

Things finally clicked for me when I saw a post on LinkedIn that prompted me to try a new approach. Instead of just blindly applying on portals, I started reaching out directly to hiring managers and decision-makers at the companies I was applying to.

I started tracking every single application manually, logging target companies, finding decision-makers using Hunter io and LinkedIn. I wrote down the details of every contact and the date I reached out in my notes app.

I started getting more interviews and even reached several final rounds. I even had a final offer lined up, only for the company to tell me they were no longer expanding into the UK and Europe.

Managing dozens of companies, custom outreach drafts, and strict follow-up bumps in a standard spreadsheet and notes app got messy fast. Leads started to slip through the cracks, and honestly, the whole process was fucking exhausting.

I searched for something that would automate the pain and couldn’t find one, so I said fuck it, let me build it myself. I spent the last few weeks building **CareerCommand** to help me manage and automate the job application process.

**The Tech Stack:**

* **Coding:** Claude Code for core development
* **Prototyping:** Gemini for mockups and prompt engineering
* **Database & Auth:** Supabase + Google OAuth for one-tap signup
* **Payments:** Stripe Checkout
* **Emails:** Resend for automated outreach triggers
* **Hosting:** Vercel

**What It Handles:**

* **Pipeline Tracking:** Keeping all your targets, roles, and stages in one clean view.
* **Smart Follow-Up Scheduling:** Setting business-day reminders so contacts never slip through the cracks.
* **Direct Outreach Generator:** Drafting stage-appropriate, tailored messages that don't sound like a robotic resume dump.
* **UK Visa Sponsor Badging:** Automatically cross-referencing official Home Office registers for those of us navigating visa sponsorship.

Happy to answer any questions!

## 评论（18/19）

> **ayodelep**（1 分） · 2026-11-11T05:01:44+08:00　
> I'm opening up 50 early Pro user slots at 50% off forever with code **FOUNDER50**. Link: [https://careercommand.app](https://careercommand.app/)
>
> Let me know if you try it out, I am open to feedback and always happy to make improvements to the product.

---

> **Patient_Celery_2406**（2 分） · 2026-11-11T05:56:09+08:00　
> You couldn't find anything that tracks applications? Teal, Huntr, Simplify all do roughly this. What's the specific thing none of them had, because "I couldn't find one" usually means I didn't look past page one.

---

> **ayodelep**（1 分） · 2026-11-11T06:07:18+08:00　
> I know they exist, but most of the existing ones felt heavy or lacked specific features I need for my job search. For example, automated UK visa sponsor checking and outreach drafting. I built it for myself and figured others might find it useful as well.

---

> **lawrence_builds**（2 分） · 2026-11-11T06:15:51+08:00　
> For the visa badge, show when the register was last checked and distinguish 'licensed sponsor' from 'sponsoring this role'. A company can be on the register without offering sponsorship for a particular vacancy, so a single green tick could send people down the wrong path.

---

> **ayodelep**（1 分） · 2026-11-11T06:51:44+08:00　
> Thanks for the callout! You're completely right, currently it just checks whether the company is a licensed sponsor on the register, not the individual role criteria. I'll look into adding role-level verification as well so people don't get sent down the wrong path. Really appreciate the input!

---

> **alankffman**（2 分） · 2026-11-11T06:53:33+08:00　
> How are you handling replies to the Resend emails? Having a reply cancel the next follow-up would be a useful safeguard against nudging someone who has already answered.

---

> **nian2326076**（2 分） · 2026-11-11T08:03:18+08:00　
> If you're finding it tough to manage your applications, consider using [LandOffer](https://landoffer.ai/) to streamline your job search. It lets you filter roles by various criteria and set up job alerts, which can help you stay organized while focusing on your outreach efforts. This approach may improve your chances of getting noticed by decision-makers.

---

> **drakatmm**（2 分） · 2026-11-11T08:05:37+08:00　
> Job seekers are the worst subscription customers I've had, they cancel the week they get hired and that's the product working, I'd charge once for three months of access or sell seats to university career offices who get a fresh batch of grads every year

---

> **jfbode**（2 分） · 2026-11-11T08:36:14+08:00　
> For automated follow-ups, make sure a reply or rejection cancels anything queued for that contact. If you're sending through Resend without reading incoming replies, a scheduled bump could go out after someone has already answered. An approval queue with a “heard back” button is a safer starting point than unattended sending, especially when a mistimed email could hurt an application.

---

> **ayodelep**（1 分） · 2026-11-11T08:45:03+08:00　
> That's a good point, but because CareerCommand opens drafts directly in your own mail client rather than sending from a server,  replies go straight to your personal inbox, and it doesn't see the thread.
>
> Right now, follow-ups pause when you hit a manual toggle, the stop following up button.  Automatically catching replies would mean either wiring up inbound domain MX records/webhooks or full Gmail OAuth API integration, which is  doable, but for now keeping it manual is a nice clean boundary that protects user privacy and my wallet.
>
> Appreciate the thoughts!

---

> **ayodelep**（1 分） · 2026-11-11T08:52:43+08:00　
> This is sick! Does it let you filter listings for international applications like the UK, or is it localised to a specific country?

---

> **ayodelep**（1 分） · 2026-11-11T08:57:01+08:00　
> That's a brilliant idea, exactly why I am going to pitch to my alma mater and get them to help me market it. I'm even thinking of a special discount code for users who sign up using our email domain

---

> **ayodelep**（1 分） · 2026-11-11T08:58:09+08:00　
> What was your product?

---

> **Brufacee**（1 分） · 2026-11-11T09:03:40+08:00　
> The UK sponsor check gives you a much more specific first audience than all job seekers. I would show that workflow in the launch demo, from finding a suitable company to saving the next follow-up, rather than opening on the CRM dashboard.

---

> **LudolphsDiddie22**（1 分） · 2026-11-11T09:06:06+08:00　
> the UK visa sponsor cross-referencing is probably the only niche piece here since standard trackers rarely pull from official government registers

---

> **ayodelep**（2 分） · 2026-11-11T09:08:52+08:00　
> That's a fair point.
>
> Right now, the app is intentionally designed not to blast emails autonomously, it just generates the outreach drafts so you personally handle what is actually sent. Follow-ups only queue if you explicitly set them.
>
> Because of this architecture, CareerCommand doesn’t read or monitor your emails. Stopping a sequence currently relies on pressing 'Stop Following Up' button.
>
> Appreciate the insight!

---

> **Assantra_Manes**（1 分） · 2026-11-11T11:49:09+08:00　
> are the resend follow up bumps sent automatically or do you still have to fire them off by hand

---

> **Strong_Teaching8548**（1 分） · 2026-11-12T23:19:33+08:00　
> I went through something similar, just chasing backlinks for my own site instead of jobs
>
> one thing that bit me, I was tracking contacts across different records and sent the same follow up to one person 10 days in a row
>
> now I match everything by email before any reminder goes out
>
> I'd check before you lean on that follow up scheduler too much

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
