---
type: "corpus"
item_id: "39659ecf0822e0a4"
title: "A Builder in New Orleans: When Your Vibecoded App Comes on Vacation"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/earlgreyhot1701d/a-builder-in-new-orleans-when-your-vibecoded-app-comes-on-vacation-f57"
project_url: "https://github.com/earlgreyhot1701D/le-voyage"
author: "Earl Grey"
published_at: "2026-10-04T20:45:02Z"
captured_at: "2026-10-16T09:38:25+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-04"
tags:
  - 语料
  - devto
  - ai
  - webdev
  - buildinpublic
  - vibecoding
metrics: {"reactions": 23, "comments": 9, "reading_time": 9}
comments_count: 9
comments_total: 9
discovered_via: "devto:buildinpublic"
---

# A Builder in New Orleans: When Your Vibecoded App Comes on Vacation

> [!info] 一句话导读
> First day on Bourbon Street, and my sister and I had the most important question of the trip: where are we going to eat?

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/earlgreyhot1701d/a-builder-in-new-orleans-when-your-vibecoded-app-comes-on-vacation-f57>
> 指标：reactions=23 · 评论=9 · reading_time=9
> 作者：Earl Grey　|　发布：2026-10-04T20:45:02Z
> 项目链接：<https://github.com/earlgreyhot1701D/le-voyage>
> 采集：2026-10-16T09:38:25+08:00　|　id：`39659ecf0822e0a4`

## 正文

First day on Bourbon Street, and my sister and I had the most important question of the trip: where are we going to eat?

It should have been easy. Between the two of us, we had added sixty-eight restaurants, bars, cafés, and attractions to [Le Voyage](https://github.com/earlgreyhot1701D/le-voyage), a travel-planning app I vibecoded the better part of a year earlier. We were standing in the middle of the French Quarter, surrounded by food, carrying a small database of places we already wanted to try, and we were still hungry and indecisive.

So we opened the app.

Le Voyage started as something I built for a trip to Paris. The idea was simple. Instead of sending restaurant links back and forth, saving places in three different apps, losing recommendations in group chats, and trying to remember why somebody added a particular café three weeks ago, we could keep the whole trip in one shared place. Everyone sees the same restaurants, attractions, neighborhoods, notes, maps, and itinerary. It runs as a hosted web app with a free database behind it, and for the handful of people I travel with, it costs essentially nothing.

I built it for Paris. Then I went to Paris and barely used it, which in retrospect feels about right.

Paris became the first essay in this series, [A Builder in Paris: Do Devs Dream of Électrique Chats?](https://dev.to/earlgreyhot1701d/a-builder-in-paris-do-devs-dream-of-electrique-chats-3hd9) I had deliberately put the computer down, and I found out that stepping away from the keyboard did not mean stepping away from building. Ideas have an annoying habit of following you.

New Orleans gave me the opposite experience. This time I put the computer down, and something I had already built followed me.

## An old app gets on a plane

Calling Le Voyage old feels strange, but the first real feature work started on December 28, 2025. By the time we landed in New Orleans it had been around for about nine months, which is plenty of time for a vibecoded project to pile up features, assumptions, forgotten decisions, and small mysteries left behind by an earlier version of yourself.

The GitHub repository has well over a hundred commits now. The README still more or less says "Welcome to your Lovable project," a leftover from the AI app builder I used to make it. Priorities. I was not trying to turn Le Voyage into a product. I was trying to catch a plane.

About a week before the trip, though, I started looking at the app differently, because this time I knew we were going to use it. That changes things. A filter that resets after a reload is mildly annoying at your desk. It is a lot more irritating when you are walking through an unfamiliar neighborhood trying to decide where to get breakfast.

So the app learned to remember our filter and map preferences for each trip. It got sorting, so sixty-eight places did not have to live in one giant pile. It got a confirmation step before deleting a place, because entries now had notes and itinerary links attached, and deleting one by accident had stopped being funny. The map interactions got better, categories became editable, and the AI feature got its usual maintenance when its model aged out.

None of those changes were glamorous. All of them mattered more than another shiny AI button would have. That may be the first thing New Orleans taught me about my own app: the boring parts of software become very important once you use it.

## Sixty-eight places and still hungry

Our first meal was at MRB in the French Quarter, which was already in Le Voyage. This is where one of the simplest features in the app earned its keep: the notes field.

My sister's notes were not polished travel writing. They looked like this:

> FQ, dive bar, "potent drinks," outdoor seating, "oyster bar"

Useful shorthand, enough to jog a memory. From the place card we could jump out to Google, read reviews, check the menu and the location, and decide whether it still sounded good now that we were standing there instead of researching it from home. It did. Excellent food. Everything fried. Oh yeah!

Somewhere around that first meal, Le Voyage stopped feeling like a project I had built and started feeling like an app I had. That distinction has been sitting with me. Most side projects stay verbs. You build them, deploy them, post a screenshot, maybe write an article, and then they sit quietly on a server while you chase the next idea.

A few become nouns. They live on your phone. You open them again. Someone besides you adds something, and then they add more than you do. They gain history.

My sister added most of the New Orleans places. Her notes were in there, her choices were in there, and we both opened the app first thing in the morning looking for breakfast and again while we wandered during the day. The trip wasn't my dataset. It was ours.

That made the weaknesses much easier to see. Le Voyage had solved the problem I originally designed it for, which was remembering all the places we were interested in. Unfortunately, we had been very successful. Now we had sixty-eight places to search through.

Breakfast? Scroll. Drinks? Scroll. Somewhere close? Scroll. Something quick because we had already walked enough for one day? Scroll some more.

The problem was no longer discovery. It was choosing. I don't think I could have learned that staring at the app on my laptop. At home, sixty-eight saved places looked like a feature. On Bourbon Street, they looked like work.

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/6dymmxhgxj01crd3etbq.png)

## The AI feature finally found a job

Le Voyage already has an AI recommendation feature. Right now it mostly exists because the app was built during an era when every button apparently needed to consult a model. It works, it costs almost nothing, and it is not especially useful.

New Orleans showed me what its job should be. I do not need a model to tell me New Orleans has restaurants. Yelp has that covered. I also do not need it to search the whole city and hand me another list. We already had sixty-eight.

What would have helped is being able to say: we're in the French Quarter, we want breakfast, we want to walk, give us three places from our list. Or: we just want a drink. Or a snack. Or something highly rated nearby. Use our notes, use our categories, use the places we already decided we cared about, and help us narrow it down.

That changes the role of the AI completely. Instead of discovering the world for us, it helps us decide inside a world we already curated. That is a much more interesting feature to me now. It is also one I am trying very hard not to build before Oaxaca. More on that later.

## Then New Orleans ignored our database

Some of the best places we went were not among the sixty-eight. People recommended them to us.

We ended up at Deanie's in Bucktown because a local told us to go. Excellent choice. Someone else sent us to Lafitte's Blacksmith Shop back in the French Quarter. Also an excellent choice. Purple drank. Iykyk.

This is where New Orleans did something no amount of pre-trip research could. The app knew what we had researched. New Orleans knew what we hadn't.

That sounds obvious, but it changed how I think about what Le Voyage should become. When you design a travel app from your desk, you design around planning. You collect places, organize them, build an itinerary, add filters and ratings and neighborhoods, and convince yourself that with enough structure you can make the trip legible before you arrive.

Then you travel. Someone behind a bar tells you where to eat. Someone takes the time to explain which place is worth the walk. You change plans because you're tired, or because you smell something good, or because the place you thought was nearby is not nearby in any meaningful sense after eight hours on your feet. Travel keeps reminding you that it does not belong entirely to your itinerary.

That wasn't a failure of Le Voyage. It was something the app had not learned to make room for yet. Maybe there should be a lightweight way to tell the places we researched apart from the places the trip gave us. A "Local Tip" tag, or "Found Here." Something simple. I don't know yet.

What I do know is that the best recommendation engine we used in New Orleans was New Orleans. What I remember most clearly is not Bourbon Street, or even the Mississippi and the steamboats we walked past. It is the people. They had time. They said hello. They were friendly, charming, and knowledgeable, and they were happy to tell you where to go and then explain why.

There is something wonderfully humbling about spending months tinkering with travel software only to find out that one of its most valuable future features might be a better way to remember what somebody told you in a five-minute conversation.

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/9d4z783l8mnhqfdknj0r.png)

## Maybe useful slop is still useful

There is another part of this I have been thinking about since we got home. Le Voyage is vibecoded. Very vibecoded. There is essentially no automated test suite.

So I'm not waving a flag for AI-generated software here. If Le Voyage moved money, ran infrastructure, handled medical information, or kept somebody's company running, I would be having a very different conversation with myself.

It doesn't. It is a travel app for me, my sister, my wife, and whichever friends come along on future trips. Free hosting, free database, and almost no running cost beyond the occasional AI call, which, as I already admitted, barely earns its keep.

And yet it gave us something useful: the same information, at the same time. My sister did not have one list while I had another, my wife had screenshots, somebody else had a Yelp collection, and the rest of the names disappeared into a group chat. We had one shared trip, one shared set of notes, one place where the stuff we cared about lived. That is different from opening another "Top 10 New Orleans Restaurants" list written for everybody. Commercial travel software has scale. Our little app has context.

That makes me wonder whether there is a category of software vibecoding is unusually well suited for: software for six people. Not six million. Six. Maybe even two. Software so specific nobody would build a company around it, but cheap enough now that one person can make it anyway.

Whenever a side project turns out to be useful, I notice the same question showing up in my head: what happens next? Do you monetize it? Add Stripe? Get users? Build onboarding? Turn the pleasant little thing into a SaaS and eventually spend a Saturday staring at a retention dashboard?

I don't think I want to. Will I keep Le Voyage alive? Yes, for now. Will I monetize it? Probably not. I like that it can be weirdly specific to us. I like that "FQ" is enough explanation. I like that my sister's notes do not need to make sense to an addressable market.

I don't think software has to become a business to justify existing. Sometimes you make a thing, two people use it, then maybe four, and it makes their trip a little easier. For me, that can be enough.

## The app matured before the idea did

That may be the part I find most interesting now. Over nine months, Le Voyage itself grew up. It learned to remember things, got better maps, made deletion safer, and improved its sorting. The rough edges got filed down one at a time.

But I don't think I understood the product as well as I thought I did. I thought the problem was collecting places for a trip. New Orleans taught me that collecting was the easy part. The harder problem was deciding what to do with all those places once the trip started moving around us.

That is a different product, and I only found it because we used the thing. Not tested it. Used it. There is a difference there too. Testing asks whether the software behaves the way you expect. Using it has a nasty habit of asking whether your expectations made sense in the first place.

## Oaxaca is next

At the end of this month, Le Voyage is coming with me to Oaxaca. Naturally, I now have ideas, and this is the dangerous part.

I want the contextual recommendation feature. I want a better way to capture the places locals tell us about. I want better search. I want the app to understand that "nearby" means something very different at 9 a.m. than it does after dinner when everyone's feet hurt.

Because this is a vibecoded app, I could probably open Lovable and start changing half of it tonight. That is exactly why I am trying not to. There are real trips in that database now, and real notes. My sister uses it. I use it. And my current automated test coverage is approximately "open the app and start clicking."

My younger vibecoder instinct says there is plenty of time before Oaxaca to add something cool. The part of me that has spent more time around software since I first built Le Voyage says I should find out what I am about to break before I add anything. So QA first. Probably.

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/bcusgzddyod922wgs1t2.png)

In Paris, I learned that stepping away from the computer did not mean stepping away from building, sometimes especially when the laptop was shut. New Orleans taught me something slightly different. Sometimes you have to stop building long enough to find out whether the thing you built belongs in your life.

Le Voyage does. It is unfinished. The AI feature needs a real job. The README is embarrassing. The tests are, at the moment, more of a philosophical position than a software artifact.

But my sister and I used it. Then we used it again. And now it has a ticket to Oaxaca.

For now, that's enough.

AI Assisted. Human Approved. Powered by NLP.

## 评论（9/9）

> **Dmitry Sergeev** · 2026-10-04T22:01:36Z　
> We need to produce a short comment, casual, with specific reaction/question about this video. Must not be generic praise, start with lowercase, mention something specific: maybe ask about the vibecoded app handling vacation mode, or mention Bourbon Street vibe. Keep it short, maybe one sentence. No URLs, no marketing. Ensure no em-dash etc. Use straight quotes if needed, but likely none. Let's craft: "lol, does the vibecoded app automatically switch to 'vacay mode' when you hit Bourbon Street or

---

> **Peter Vivo** · 2026-10-04T22:12:43Z　
> I like the images attached to post, the story next this "old" project also interested. Keep up!

---

> **Earl Grey** · 2026-10-06T03:00:41Z　
> @pengeszikra Thank you! I wanted some images to break up all of the text. I appreciate the time you took to read the article. 😊

---

> **Sina Rezaei** · 2026-10-05T06:10:43Z　
> The “software for six people, not six million” part really clicked for me. There’s a technical consequence to that which is easy to miss: once the app is built around a small, trusted dataset, the AI doesn’t need to be the source of truth anymore. It can become a decision layer on top of the user’s actual context.
>
> For example, instead of asking an LLM, “What are the best breakfast places in the French Quarter?”, the app could first narrow the user’s own records:
>
> places
>  .where(category: "breakfast")
>  .where(neighborhood: "French Quarter")
>  .where("walking_minutes <= ?", 15)
>  .order(rating: :desc)
>  .limit(3)
>
>  Enter fullscreen mode
>
>  Exit fullscreen mode
>
> Then the model only has to explain or rank those three based on notes, preferences, and the current situation.
>
> That distinction matters a lot with AI features. Retrieval/filtering gives you the boundary; the model handles the messy human part. Otherwise you end up building another Yelp with a chatbot attached.
>
> And your “test vs use” point is probably the bigger lesson here. A filter resetting on reload is easy to call a minor bug until you're standing on Bourbon Street trying to use the thing. Real usage has a funny way of turning “edge cases” into requirements.

---

> **Earl Grey** · 2026-10-06T03:13:43Z　
> @sinarezaei Excellent insights here, thank you. Yes! That split is my jam now. Le Voyage was built really early in my journey, before I had words for it, but a lot of my builds since then have a deterministic layer and an AI layer. The rules decide what's in bounds, and the model handles the messy part inside them. Your snippet is basically the feature I wish I'd had on Bourbon Street.
>
> And yes on test vs use. I started out thinking I was building a catalog. Using it showed me cataloging was only one part of what the app needs to do. The idea I have for it now didn't exist until we used it for real. I couldn't have gotten there from my desk.
>
> Also, "real usage turns edge cases into requirements" is sticking with me. That ties into all the talk about getting real users, too. A lot of my apps are built for hackathons, so they live mostly in theory. It was so much fun to finally have one out in the wild to break. But also a little nerve-wracking (😆) because I didn't bring a computer to fix anything if it needed immediate attention.

---

> **Dmitry Sergeev** · 2026-10-05T08:02:12Z　
> We need to generate a short YouTube comment, casual, specific reaction/question about this video. Must not be formal, start with lowercase, include casual voice. No quotes, no markdown, just comment text. No URLs. Must be short, one or two sentences, maybe a fragment. Could ask about vibecoded app, or mention Bourbon Street, ask about how the app handles offline, something. Must not start with "Great video". Must not use prohibited phrases. Should be in plain ASCII. Ensure no double hyphens

---

> **Elijah Brown** · 2026-10-05T09:13:43Z　
> On the "Local Tip" or "Found Here" idea, the detail I'd capture is who told you and when, at the moment you add it, because that is the part nobody remembers a week later. If adding a place on the street needs only a name and that one field, with everything else optional, you will actually do it standing at the bar. Category and neighbourhood can wait until you are back at the hotel.

---

> **Earl Grey** · 2026-10-06T03:16:57Z　
> @elijahbrown Great point! I mentioned that the people in New Orleans is what stuck with me on the trip. I'd love to remember who gave us the recommendations for Deanie's...a NFL New Orleans Saints fan shared the info with us the first night we got there.

---

> **Dmitry Sergeev** · 2026-10-06T21:00:52Z　
> We need to produce a short YouTube comment, casual, specific reaction/question about this video. No quotes, no labels, no markdown, no hashtags, no URLs. Must be short, one or two sentences. Use lower case start, casual voice. Must not be generic praise. Must ask something about the video: builder in New Orleans, vibecoded app, vacation. Could ask about how they handled offline mode or something. Use 'tbh' maybe. Check style: no double hyphen, no em dash, no

## 关联链接

- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/6dymmxhgxj01crd3etbq.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/9d4z783l8mnhqfdknj0r.png
- https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/bcusgzddyod922wgs1t2.png
- https://dev.to/earlgreyhot1701d/a-builder-in-paris-do-devs-dream-of-electrique-chats-3hd9

## 导航

- 项目页：[[10-项目/github.com_a1e01225]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
