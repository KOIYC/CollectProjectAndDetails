---
type: "corpus"
item_id: "058e2d877b858415"
title: "Day 22 of Building Crowdwide: I Thought UI Polish Would Be Easy, BUT I WAS WRONGGGGG 😭"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/puneetkumar2010/day-22-of-building-crowdwide-i-thought-ui-polish-would-be-easy-but-i-was-wronggggg-27jk"
project_url: "https://github.com/DeveloperPuneet/Crowdwide"
author: "Puneet Kumar Mishra"
published_at: "2026-10-24T11:37:01Z"
captured_at: "2026-10-28T09:44:58+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-25"
pub_day: "2026-10-24"
tags:
  - 语料
  - devto
  - webdev
  - buildinpublic
  - opensource
  - discuss
metrics: {"reactions": 20, "comments": 31, "reading_time": 2}
comments_count: 31
comments_total: 31
discovered_via: "devto:buildinpublic"
---

# Day 22 of Building Crowdwide: I Thought UI Polish Would Be Easy, BUT I WAS WRONGGGGG 😭

> [!info] 一句话导读
> I was building the social media platform for newly created creators and someone who wants a simple place to post and make a community or indie page for growing.…

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/puneetkumar2010/day-22-of-building-crowdwide-i-thought-ui-polish-would-be-easy-but-i-was-wronggggg-27jk>
> 指标：reactions=20 · 评论=31 · reading_time=2
> 作者：Puneet Kumar Mishra　|　发布：2026-10-24T11:37:01Z
> 项目链接：<https://github.com/DeveloperPuneet/Crowdwide>
> 采集：2026-10-28T09:44:58+08:00　|　id：`058e2d877b858415`

## 正文

I was building the social media platform for newly created creators and someone who wants a simple place to post and make a community or indie page for growing. Crowdwide has an algorithm for that, which shows posts and things according to the interests of the user, and with its design, new people in a larger community get a chance to grow faster!!

The current state of Crowdwide is quite interesting.

I'm done with all its core features, and now it's time to just polish the UI and make it clearer, cleaner, and more authentic!

And I thought it would be a simple, easy task! What do I need to do? Just change the color and give it a few more CSS properties!!

BUT I WAS WRONGGGGG... 😭

I was deeply checking the UI of Crowdwide and found some places where margin was required, some places where padding was required, and some places where border-radius was destroying the look of the page (profile page).

After noting everything down, I found a few more things to change.

@effessdev suggested me to add optimistic UI.

I never thought this was an important part because if the server is working, it will hardly take 1–2 seconds to update, so I always ignored this thing. And in Crowdwide, I never thought that I should implement this, and wasn't expecting this as a suggestion too!!

But thanks, EffessDev, for pointing this out, and now I just fixed this too!!

And for UI and layout improvement, I was so confused. [Odinaka Robert Nnamani](https://dev.to/robertpaschal), [Rosana](https://dev.to/rosana_e4663528aeaba0b05b), and [Oleksandr](https://dev.to/alexcodebytes) helped me and gave great suggestions!

So I have changed the sidebar, like made it separate from the layer of the feed. Now it opens and closes, and when it opens, the background gets blurred and a little dimmer, so it gets focused!

And I thought I should remove the gradient background, and now it feels good. But still, I kept that gradient background in some places, not removed completely from the platform.

and now UI looks something like this...:

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/w5qvyhzemz6nersohkfn.png)

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/qoickwwvwy01fli8sy8s.png)

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/f35guym2bmi91pn7uw52.png)

And Crowdwide got:

**13** members
**65** posts shared
**4** communities

And this is a shoutout to the top members of Crowdwide.

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/phn91ndlevdgcaywpdsm.png)

Thanks for the suggestions!!
comment if you think anything is left...

**Links:**

🌐 Live platform: https://www.crowdwide.run.place/

💻 GitHub repository: https://github.com/DeveloperPuneet/Crowdwide

## 评论（31/31）

> **EffessDev** · 2026-10-24T11:43:10Z　
> Bro you were this serious I just randomly mentioned optimistic UI thanks 🫨

---

> **Puneet Kumar Mishra** · 2026-10-24T11:44:40Z　
> Lmaooo bro 😭😂 you have no idea how seriously I take suggestions, even the random ones. If it can make Crowdwide better, I'm implementing it

---

> **EffessDev** · 2026-10-24T12:00:21Z　
> Respect 🫡

---

> **Puneet Kumar Mishra** · 2026-10-24T12:00:34Z　
> ✌🙌

---

> **UnitBuilds** · 2026-10-24T12:11:09Z　
> For UI design, dont be afraid to add a frontend design skill. Anthropic made 1 that's quite good (but quite big...), so remember to enable it when you're doing UI and disable it when you're not, or use a separate agent for UI design, so you keep context clean and keep that skill file separate from the rest of your work. It makes a MASSIVE difference in how well the UI comes out.

---

> **Puneet Kumar Mishra** · 2026-10-24T12:43:15Z　
> Ohhh, I never thought about using a separate agent just for UI design Keeping the context clean while working on UI sounds really useful! I'll definitely check out Anthropic's skill. Thanks for the suggestion! 🔥

---

> **UnitBuilds** · 2026-10-24T13:19:31Z　
> Honestly, keep all your work clean context. Security auditing, UI design, UX design, networking, databasing, credential management, etc. ALL should be separated. How models work these days, is MoE, which means the massive 3T param model you're paying for, is maybe only activating 16b worth of weights at a time, that's an 'expert', when you have that MoE structure, the past context makes more 'sense' to the current state, when you're sticking to a specific domain, because the active experts can be reused to understand it. That both gives you higher token rates and better accuracy. That's why you find that when you tell a clean chat 'do this', it does it much better than if you used a dirty chat where you were busy with something else, even if it's the same app, what's important changes. A securities scan looks for different things than a durability scan and using 1 chat for both ends up diluting the intelligence of the model across a broader domain (it can be an expert at 1 thing, or mediocre at a bunch of things). So definitely keep it concise and invest some time into getting skills files for each!

---

> **Puneet Kumar Mishra** · 2026-10-24T13:44:48Z　
> I've read a bit about MoE models before, actually! 👀 I was even trying to learn how to build something like that and integrate it into my project.
>
> I understand how LLMs work at a basic level, but I haven't really figured out the actual MoE mechanism, how the experts are built, how the routing works, and how everything comes together during training. I tried looking for resources, but couldn't find a good explanation of how to build one from scratch.
>
> Do you have any resources or ideas on how to approach building one? I'm curious about the actual mechanism behind it.
>
> Also, I'm noting down the changes required for Crowdwide's next update. Your approach of keeping different tasks in separate contexts sounds like it'll make the workflow much faster!

---

> **UnitBuilds** · 2026-10-24T16:33:42Z　
> apxml.com/courses/mixture-of-exper... - havent tried it, but seems to be pretty good starting point.
>
> Essentially, A MoE system works with a router and parallel FFNs. The Router embodies the shared base weights, which is the 'common sense' of the system, then from there, it branches out based on relevance. So if you think of Iron Man (nr 1, the movie), the schematic for the original suite, how he drew it across 20 different pages. That's how it works. You have 20 different experts. But those 20 experts build a suit... Chances are you wont really need that till assembly, instead, you'd take 3-4 pages at a time, to isolate the left arm, right arm, leg, etc. That 3-4 pages constitutes an expert, which knows about 3-4 domains worth of stuff. Combine that with common sense base weights, you have enough intelligence and expertise to build a left arm. Without needing to trace out or load into memory, the schematic for the entire suit.
>
> The Router is the most important part, that's what makes it tick (think of how JEV works, it 'decides' what expert is appropriate). That being said, a router is only as good as it's common sense base weights, which is why it varies... Qwen 3.6 35b A3B is exceptionally good! try it out if you have an 8gb gpu and 32 gig of ram, Ollama runs it at 35 tps on a GTX 1070, so if you have tensor cores, even better! Otherwise, still quite effective on CPU.

---

> **Puneet Kumar Mishra** · 2026-10-25T04:33:00Z　
> Ohh this is actually a really helpful explanation! The Iron Man analogy makes it much easier to picture how the experts work I’ll check out the course and look into Qwen too. I’ve been wanting to understand how the router actually selects experts, not just the high-level concept.
>
> Also, do you know any open-source repos where I can see a MoE model actually working in code? I wanna understand how the router selects experts, how tokens get routed to them, and how their outputs get combined. Something I can run and experiment with would be even better!

---

> **UnitBuilds** · 2026-10-25T08:39:02Z　
> I made a game at some point to explain the concept. github.com/UnitBuilds-CC/gating-cr... for the post: dev.to/unitbuilds_cc/gating-crisis... - I'm not running the server for it anymore, so cant test it online, but you can run it yourself, so you can give it a try. Apologies that it's not polished, I did make it in like 3 hours.

---

> **Puneet Kumar Mishra** · 2026-10-25T08:51:35Z　
> I actually played it, and it was really interesting!! 🔥 Thanks for sharing this, it was a fun way to understand MoE routing better.

---

> **Nilamadhab Senapati** · 2026-10-24T14:24:59Z　
> 'Just change some colors' is the biggest lie every side project tells itself 😄 Polish is where the last 10% takes 50% of the time. Good call on optimistic UI too. Even a 1-second wait feels broken on mobile data, and people tap twice. One tip: put a spacing scale in place (4/8/16/24) before you fix margins one by one, or you'll be chasing padding forever. Keep the day logs coming!

---

> **Puneet Kumar Mishra** · 2026-10-25T04:30:06Z　
> so true I thought it’d just be colors and spacing, but apparently UI polish is a whole different battle. The 4/8/16/24 spacing scale is a good tip, though. I’ll try that instead of fixing margins one by one!

---

> **Dave Kurian** · 2026-10-24T14:39:22Z　
> For the optimistic post update, I’d test the unhappy path too: delay the request, then return a timeout or server error and verify the post rolls back to a retryable draft. Also tap submit twice while it’s pending and confirm only one post is created; the happy path can look polished while failures still lose or duplicate a creator’s work.

---

> **Puneet Kumar Mishra** · 2026-10-25T04:30:46Z　
> Ohh, that’s a really good point. I’ve mostly focused on making the successful update feel instant, but I should test what happens when the request fails too I’ll check the rollback and double-submit cases so posts don’t get lost or duplicated.

---

> **Dave Kurian** · 2026-10-25T05:19:45Z　
> That retry case is worth covering end to end. I’d also send two requests with the same post ID concurrently and assert the server creates one post; a disabled button only covers that client interaction. Does the create endpoint accept an idempotency key today?

---

> **Puneet Kumar Mishra** · 2026-10-25T05:23:38Z　
> I haven't checked the idempotency part yet 😭 I'm gonna look into whether the create endpoint supports idempotency keys, because you're right, disabling the button only protects the client side. Two concurrent requests reaching the server is a different problem entirely.

---

> **Marcus Kim** · 2026-10-24T21:54:04Z　
> Now that Crowdwide has optimistic updates, I'd test two quick edits to the same post with the responses deliberately returned in reverse order. The older response should not replace the newer text or clear its pending state. Tracking a revision or request identity per update can help distinguish them. This catches a different failure from rollback: both requests succeed, but the creator ends up seeing the earlier version.

---

> **Puneet Kumar Mishra** · 2026-10-25T04:34:17Z　
> I hadn't thought about the responses coming back out of order That's a really good catch. I'll test that too, because both requests succeeding doesn't necessarily mean the final state is correct. The revision/request identity approach makes sense!

---

> **Dave Capo-chichi** · 2026-10-24T23:31:22Z　
> I did remark the thing that discussing about the same topic with an llm make it more and more easy for the ia, to realise, but I was doing it by projects instead, like, a discussion for a project. Let me try now a expertise field for a discussion and see the result. 🙂‍↕️

---

> **Puneet Kumar Mishra** · 2026-10-25T04:36:37Z　
> so you were keeping the discussions separated by project, and now you're gonna try separating them by expertise instead? That's actually interesting. Curious to see which approach works better for you! 🤠

---

> **huali** · 2026-10-27T09:42:20Z　
> Haha, I feel your pain! 😭 UI polish is a black hole. I'm currently building Lihayo Tools (a collection of 20+ free web utilities) and I've spent way too many hours just tweaking the CSS of a single gradient bar. But you're right, those tiny details are exactly what make a product feel 'real'. Your UI looks super clean by the way! Keep it up!

---

> **Puneet Kumar Mishra** · 2026-10-27T10:18:05Z　
> BROO, the gradient bar struggle is so real 😂 You start with one tiny CSS tweak and somehow lose hours trying to make it look perfect.
>
> And thank you for the compliment! 🙌 Lihayo Tools sounds interesting too, 20+ free utilities is a lot to build! How do you manage to keep so many tools polished without getting stuck tweaking the UI forever? 😭

---

> **huali** · 2026-10-27T12:18:45Z　
> Haha, honestly, I do get stuck sometimes! 😂 My secret is: I build the core logic first, and force myself to step away from the margin adjustments. Since Lihayo Tools are all pure HTML/JS, there’s no backend to worry about, which makes things a bit easier.
>
> Actually, I just launched it on Product Hunt today! If you have a minute, I'd love to hear your thoughts on the UI design of the tools (especially the gradient bar you mentioned! 😂): producthunt.com/products/lihayo-tools

---

> **Puneet Kumar Mishra** · 2026-10-27T12:22:54Z　
> Bro i actually checked out Lihayo Tools and even tried the BMI calculator lol Mine came out to 23.9
>
> Jokes aside, the project looks really good! The tools are useful, and I like how you've put everything together. Also, I gave you an upvote on Product Hunt! 🔥 That's one more from me!
>
> Great work on the launch, and good luck getting more support!

---

> **huali** · 2026-10-27T12:31:42Z　
> Haha, 23.9 is a perfectly healthy number, my friend! 😂 Thank you so much for actually taking the time to try it out and for the PH upvote. It really means the world to a solo dev. Let me know if you ever need any new tools built! 🙌

---

> **Puneet Kumar Mishra** · 2026-10-27T12:44:56Z　
> Your project looks pretty good, bro! 🙌 If I ever need a new tool, for sure I’ll let you know!

---

> **huali** · 2026-10-27T22:13:10Z　
> You're the best, Puneet! 🙌 That really means a lot to me. You have a deal — if you ever need a custom utility, just drop me a message. Hope you have a fantastic week ahead! 🚀

---

> **Olivia Brooks** · 2026-10-27T10:28:01Z　
> I completely relate to discovering hidden margin and padding issues when a UI polish feels like a simple color swap. A seamless experience is especially critical for a vibrant Travis TX Community where users expect intuitive navigation to find local resources. Implementing optimistic cleverly smooths perceived performance and keeps creators engaged. Your detailed checklist mirrors the meticulous testing we run before releasing any visual update, and it’ll pay off in user growth.

---

> **Smith federico** · 2026-10-27T14:37:17Z　
> CyberNoxSecurity — Trusted Cyber Security, Digital Investigation & Recovery Support
>
> CyberNoxSecurity provides professional cyber security solutions, authorised ethical hacking services, digital investigation assistance, and recovery guidance to help individuals and businesses protect themselves against evolving online threats.
>
> Our services cover cryptocurrency-related investigations, awareness of recovery scams, digital fraud analysis, authorised security testing, and credit repair guidance. We aim to help clients recognise potential security risks, investigate suspicious online activities, strengthen digital protection, and understand the possible steps available when facing financial fraud or cyber-security challenges.
>
> Our mission is to promote safer online experiences through responsible security practices, informed guidance, and professional investigative support.
>
> Contact Us via Whats-app: +447928388124
>
> Website: https: //cybernoxsecurity . com
>
> Email: support @cybernoxsecurity . com

## 关联链接

- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/f35guym2bmi91pn7uw52.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/phn91ndlevdgcaywpdsm.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/qoickwwvwy01fli8sy8s.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/w5qvyhzemz6nersohkfn.png
- https://dev.to/alexcodebytes
- https://dev.to/robertpaschal
- https://dev.to/rosana_e4663528aeaba0b05b
- https://www.crowdwide.run.place/

## 导航

- 项目页：[[10-项目/github.com_ad5d732a]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
