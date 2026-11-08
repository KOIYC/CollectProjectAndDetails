---
type: "corpus"
item_id: "bed8aecc7be429cb"
title: "How do you collect user feedback if telemetry is not possible?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/buildinpublic/comments/1xi3as7/how_do_you_collect_user_feedback_if_telemetry_is/"
project_url: "https://otlfrosta.com/"
author: "FetaFowa"
published_at: "2026-10-29T06:56:15+08:00"
captured_at: "2026-11-08T12:52:11+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-08"
pub_day: "2026-10-29"
tags:
  - 语料
  - reddit
  - r/buildinpublic
metrics: {"score": 3, "comments": 21, "upvote_ratio": 1}
comments_count: 20
comments_total: 21
discovered_via: "reddit:14d+settle10"
---

# How do you collect user feedback if telemetry is not possible?

> [!info] 一句话导读
> I've been working on a [side project](http://otlfrosta.com/) that helps people save their AI conversations, and I've accumulated a handful of users. Because it'…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/buildinpublic/comments/1xi3as7/how_do_you_collect_user_feedback_if_telemetry_is/>
> 指标：得分=3 · 评论=21 · 赞踩比=1
> 作者：FetaFowa　|　发布：2026-10-29T06:56:15+08:00
> 项目链接：<https://otlfrosta.com/>
> 采集：2026-11-08T12:52:11+08:00　|　id：`bed8aecc7be429cb`

## 正文

I've been working on a [side project](http://otlfrosta.com/) that helps people save their AI conversations, and I've accumulated a handful of users. Because it's a super privacy-sensitive use case, I promised not to collect any data, including telemetry. That makes it really hard to gather meaningful user feedback. I tried including a feedback form, but people rarely use it, other than occasionally leaving an 'it's not working' comment. Any advice?

[](https://www.reddit.com/submit/?source_id=t3_1xi2kep&composer_entry=crosspost_prompt)

## 评论（20/21）

> **investigatormaker**（2 分） · 2026-10-29T07:02:52+08:00　
> With no telemetry allowed, make feedback something users choose to hand you. Those "it's not working" notes are the clue: add a button that builds a local diagnostic snippet (version, browser, which AI site failed), shows the user exactly what's in it, and lets them paste it into the form themselves. Then replace the open form with one question at a natural moment, like after someone's tenth saved conversation: what almost made you stop using it? A short changelog that invites replies also reaches people who never open forms.
>
> I make ThreadFox. We find relevant Reddit conversations and post for your business. We'll post 3 replies free first, no card; then the $79 Pilot covers seven days and up to 50 posts and replies. No automatic renewal. [https://threadfox.vip/p/e80zr/managed](https://threadfox.vip/p/e80zr/managed)
>
> Which AI tools does it save conversations from right now?

---

> **kai_mercer19**（2 分） · 2026-10-29T07:05:45+08:00　
> One option that keeps the no-telemetry promise: make the "it's not working" note carry its own context. A report button that opens a prefilled, plain-text summary (app version, browser or OS, what step failed) which the user can read in full and then copy or send, so nothing leaves without them seeing it. You can also say on the page exactly what it contains, which for a privacy product is a selling point. And since people leave "it's not working" more than anything, a short list of the three most common fixes shown right next to that button may cut those down.

---

> **FetaFowa**（1 分） · 2026-10-29T07:06:00+08:00　
> Thanks for the response. I just realized I should setup a discord server for feedback collection. Setting up rn!

---

> **FetaFowa**（1 分） · 2026-10-29T07:07:15+08:00　
> I was debating should I ask user to include diagnostic information in bug report. I guess I should have that functionality ready and let user to make the decision.

---

> **Optimal_Diet_2324**（2 分） · 2026-10-29T07:08:55+08:00　
> That constraint is annoying but honestly the right call for a product that stores people's AI chats. An "it's not working" comment is worth more than silence, go back to those people and ask what exactly broke, one question, no form. With a handful of users you can just email each one personally, telemetry wouldnt tell you more than a five minute reply does.

---

> **FetaFowa**（1 分） · 2026-10-29T07:11:21+08:00　
> lol, I'm wondering if this is bot response. But thanks for your advice, I'll think about how to let ppl upload diagnostic when reporting bugs.
>
> right now it allow user to save conversation from Gemini (which I use the most), and the beta build has extended to ChatGPT/Claude/Grok, but I'm hesitating to release it cause I haven't tested them thoroughly.

---

> **FetaFowa**（1 分） · 2026-10-29T07:14:13+08:00　
> The problem is, I'm currenlty using [tally.so](http://tally.so), it allows me to easily set up a feedback form. But contact info is optional, and for most (98%) of response ppl didn't leave any contact. The product itself don't require any account/login so I really have no idea who and how manyu people are using it.

---

> **codectl**（2 分） · 2026-10-29T07:19:30+08:00　
> Couldn't you capture entirely anonymous telemetry for this product such as export/sync failures without capturing any of the contents of the page? i.e. you have a bunch of static query selectors that can/will fail if the chat markup changes which could be one failure point. So raising an invariant if certain expected elements aren't found seems like a reasonable piece of telemetry. I suppose a daily e2e test would be a better approach for this in particular but you get the idea that you can capture some data. I suppose for a browser extension, allowing external calls kinda breaks the privacy contract.

---

> **FetaFowa**（1 分） · 2026-10-29T07:22:59+08:00　
> anonymous telemetry sounds reasonable, but I'm not sure if that'll break "no telemetry" promise. But I'm thinking of asking user to include diagnostic data when bug reporting. Thanks for the advice!

---

> **QuanTradin**（2 分） · 2026-10-29T07:39:14+08:00　
> the people who leave 'it's not working' are the feedback. reply to each one personally, within the hour if you can, and ask one question: what were you trying to do when it broke. no form ever got me as much as five of those conversations, and nothing leaves the user's machine.

---

> **FetaFowa**（1 分） · 2026-10-29T07:42:42+08:00　
> Thanks for responding! However, my problem is that I'm using [Tally.so](http://Tally.so), which allows anonymous feedback, and 98% of the responses I got were without contact info. I wish there's more direct way of contacting my users

---

> **QuanTradin**（2 分） · 2026-10-29T08:10:34+08:00　
> make the contact field the follow-up, not the gate: "want to hear when this is fixed? leave an email". people who just hit a wall will give it for a fix they want, not for your sake. and the 2% who did leave one, reply to them today, those are your interviews.

---

> **Ok_Gur_9033**（2 分） · 2026-10-29T08:42:25+08:00　
> What moved this for me more than the form design was asking one specific question instead of inviting feedback in general.
>
> I went back through my own comments from October. Of the 51 that ended in a direct question, 27 got a reply. Of the 13 with no question at the end, 6 did. Same writing, same places, roughly double the response rate from there being one answerable thing at the end.
>
> So I would drop the form and send one line by hand: what were you doing when it stopped working. With a handful of users that is an afternoon. How many of the people who left an "it's not working" note did you write back to?

---

> **FetaFowa**（1 分） · 2026-10-29T08:54:38+08:00　
> Thanks for the advice! The short answer is zero—people didn't leave any contact info when submitting feedback, so I had no way to write back to them. That's actually why I'm feeling stuck.

---

> **Ok_Gur_9033**（2 分） · 2026-10-29T09:03:52+08:00　
> Then the thing to fix is not the telemetry, it is that the form has no return address. An optional "email if you want a reply" field is still the user handing you something on purpose, which is the same promise you are already keeping.
>
> The other half is giving them somewhere to talk that they control. A public issues page, or a thread they can post in, means the conversation starts on their side and you never hold anything. People who care enough to write "it's not working" will usually take a reply route when one exists.
>
> Does the form live inside the app, or on a page they have to go and find?

---

> **FetaFowa**（2 分） · 2026-10-29T09:17:15+08:00　
> I use [tally.so](http://tally.so) to create a free feedback form, It's located on the main page (it's a chrome extension). I also made it exit survey when people uninstall the extension. I guess I should distinguish the feedback response with uninstall response.

---

> **codesbyshivam**（1 分） · 2026-10-29T14:20:53+08:00　
> A feedback form on its own almost never gets used. What works better is asking at the moment people have something to say. Put a one question prompt in the app after someone has used it a few times, like "what almost made you stop using this?", and make it easy to skip. With only a handful of users you can also just message them and ask for a quick call. Talking to five people beats any dashboard. When someone writes "it's not working", reply fast and ask what they were trying to do. Those are your best leads. You could also add an opt in "send debug info" button that shows exactly what gets sent before they hit send. That way you keep your promise and still get details when something breaks.

---

> **Competitive_Tune_590**（1 分） · 2026-10-29T16:15:26+08:00　
> tough spot, privacy-first products make feedback loops a real pain. have you tried reaching out to people in the wild who are already asking for a fix for this problem? a quick landing page with a waitlist or a 'tell me what you'd pay' button can give you signal without touching your users' data. i run a service that does exactly this kind of validation outreach, ghostlaunch.so, might be worth a look if you want to test demand beyond your current handful.

---

> **After-Base-8368**（1 分） · 2026-10-31T07:40:21+08:00　
> Since 98% leave no contact details, would a couple of follow-up questions before they submit solve the problem? For a failed save, you could ask which AI site and what happened after clicking Save, without collecting the conversation itself.

---

> **Ok_Gur_9033**（1 分） · 2026-10-31T16:18:41+08:00　
> A Tally form works for the people already engaged enough to go find it. The risk is it only catches your happy users, since the ones bouncing never open the feedback page.
>
> What moved the needle for me was one inline question at the exact moment something failed or felt slow, instead of a form they navigate to. Same idea as the telemetry point: one answerable question where they already are beats a form they have to go to.

## 关联链接

- http://otlfrosta.com/
- https://www.reddit.com/submit/?source_id=t3_1xi2kep&composer_entry=crosspost_prompt

## 导航

- 项目页：[[10-项目/otlfrosta.com_c7ee927e]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
