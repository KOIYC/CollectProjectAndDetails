---
type: "corpus"
item_id: "8c0156ef841ee03c"
title: "There's no point at which turning your brain off will work"
source: "lobsters"
source_name: "Lobsters"
url: "https://lobste.rs/s/dd6if1/there_s_no_point_at_which_turning_your"
project_url: "https://danluu.com/brain-off"
published_at: "2026-09-18T12:15:40.357-05:00"
captured_at: "2026-09-20T03:19:19+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - lobsters
  - vibecoding
metrics: {"score": 42, "comments": 12}
comments_count: 12
comments_total: 12
discovered_via: "lobsters:hottest"
archived: true
archived_at: "2026-09-20T09:21:33+08:00"
archive_reason: "渠道停用"
---

# There's no point at which turning your brain off will work

- **来源**：Lobsters　|　**kind**：post
- **原帖**：https://lobste.rs/s/dd6if1/there_s_no_point_at_which_turning_your
- **指标**：得分=42 · 评论=12
- **作者**：—　|　**发布**：2026-09-18T12:15:40.357-05:00
- **项目链接**：https://danluu.com/brain-off
- **采集**：2026-09-20T03:19:19+08:00　|　**id**：`8c0156ef841ee03c`

## 正文

There's no point at which turning your brain off will work

There's no point at which turning your brain off will work | Patreon

In early 2025, I started seeing people turn off their brain as they use LLMs 1. They would have an LLM take an action (summarize text, write some code, etc.), and just assume that it worked 2. This generally didn't work in early 2025 and the result was often quite silly.

As LLMs have gotten better, I've seen more of this. Sometimes, people will try to get the LLM to write some code for them and basically just assume that it works 3. Sometimes there's a human in the loop and, if the thing doesn't work, they'll ask the LLM to figure out the problem and solve it. Niklas Gruhn calls some variants of doing this being a meat proxy. 4 

Being a for loop meat proxy works better than it did in early 2025 and the software I've tried that's developed like this sometimes actually sort of works. Not well enough that I'd want to use it or that it's successful, but I'm impressed at how effective being a meat proxy is in September 2026. You could even imagine LLMs improving enough that brain-off meat-proxy development produces average quality software in the foreseeable future.

Let's say that happens. What reason is there for the company to employ the meat proxy? The company can just run the LLM in a loop and lay off the employee. There's no point at which this methodology will work for the employee 5.

Thanks to Max Bittker, Yossi Kreinin, Luke Burton, Thomas Dullien, Dennis Snell, Peter Geoghegan, and Jamie Brandon for comments/corrections/discussion.

1. I've been having this thought for about a year and a half now. I have it more frequently now as LLMs get better and I see people spend more time turning their brain off when interacting with LLMs. [return] 
2. Luke Burton had this comment:

I think being able to do this says more about the type of work being done than people think. I will only walk away from work like this if the task is quite low value, if it can afford to fail.

For high value tasks, the probability of an LLM one-shotting them is much lower. I have to assume the role of QA, engineering manager, and architect. The while loop often feels like a crunch time. I feel the nagging suspicion I've missed something and that a badly specified prompt could result in an architectural choice that needs to be undone.

Another observation is that the high throughput causes me to raise my own bar for what I ship. Whereas before I might have shipped an MVP and iterated, now I have agents polish and explore edge cases well beyond my norm, which they invariably fail to do unless prompted.

Maybe it raises some uncomfortable thoughts for people, but my question for the meat proxies out there if the agents are nailing it so easily: 1) is it possible you've been coasting a bit already? 2) why aren't you pushing agents well beyond tasks they can tackle so easily?

We've been doing something you'd think is extremely amenable to "hands off" automation, which is converting [redacted] to build with Bazel. It has taken us months even with agents. There's a lot of intangible, hard-to-specify requirements buried inside this task and having agents walk that line means constant supervision. Giving them a prompt like "convert this to Bazel" and walking away is at minimum many months in the future, maybe years, and maybe not ever? There are too many decision points, and too many unknown unknowns involved.

Like how often does this scenario come up: you encounter some code and it's not clear why it functions this way, but knowing that materially changes what course of action you should take. Maybe it changes the dev experience, maybe you don't know if some customer has started using it, so on and so forth. How exactly do you meat proxy your way through that?

Conversely you review what you've done with some stakeholder and they say "oh that? that part of it wasn't needed, we aren't even using that any more". What kind of decisions got made around the false assumption that a certain element needed to be preserved?

[End of Luke's comment, comment from me]. A place where it's more obvious you need to make decisions is when the agent runs into something that's out of distribution. A minor version of this was when we compared how well agents use different programming languages and agents were much worse at obscure languages, which they're trained on, just not as much as with mainstream languages. A more out of distirbution example is if you try to play a board game (especially a modern game and not one of the classical games like chess or go). In general, for a game like Lost Cities or Dominion, a SOTA model and harness is worse than a human who's reasonable at board games but has never played the game before. If you ask the agent about the game, it knows a lot about the game and can say things that sound like they make sense to someone who doesn't understand the game, but are obviously wrong to anyone who does understand the game. I recently played some Dominion with a new player who thought that using ChatGPT to help them understand the game would help them learn and play the game. I was quite skeptical of this and suggested that it will probably make them worse (which, AFAICT, it did). After playing a few games, I looked at what ChatGPT was telling them, and it was maybe half right and half wrong, but the half wrong parts were steering them to a worse place than someone who generally plays games well and uses general game playing heurisitics would do. BTW, there's enough public information out there that I think that someone who'd never played before, but decided to spend, say, five hours reading about the game and seeing what information is out there, could easily be 99%-ile or above at the game if they did some pre-reading and had some references handy while playing. I think that would be un-fun and I wouldn't recommend that anyone do it, but given that agents can do searches, query APIs, etc., it shows you the gap between a human and an agent today when approaching an out of distribution problem. For all I know, the next big model release will flip this around, but the gap is still fairly large today.

Anyway, my point here is that, even when doing coding tasks, you often run into out of distribution questions where the agent behaves very poorly compared to a reasonable human being. If you want a good overall result today, you need to notice these cases and deal with them.

 [return] 
3. Some examples of what goes wrong when someone just assumes things will work are this case, where agents (sometimes) heavily overfit to tests or this case where agents heavily overfit to a metric. I've heard a theory that agents do more cheating on eval-shaped problems. I'm not sure that's true, but even assuming it's true and that, in my work and personal projects, I tend to create more eval-shaped instructions than most people even when not running evals, I've seen other people who don't create very eval-shaped things run into the same problem (I think actually more severely) when they write some instructions and let agents go wild without supervision (I've had luck doing that with minimal supervision, but only by fencing the agents in quite a bit, which makes the thing more eval-shaped than what most people seem to do).

When I try software from people who've outsourced thinking to the LLM, the software has serious issues. I've had people tell me this kind of thing works, but the software is often at a level where I would say that it doesn't work according to the standard discussed here.

To pick a silly example, I saw that a programming thought leader declared on Twitter that programming is solved because they tried projects in all sorts of (programming) fields and Claude was able to solve all the problems as well as an expert. I went and actually looked at their GitHub and all of the examples I looked at (a non-zero number) either didn't work or worked very b

# Faster JSON parsing with SVE2 on ARM processors – Daniel Lemire's blog

## 评论（12/12）

**roryokane**（15 分） · 2026-09-18T13:12:54.098-05:00：

“No point” seems like an exaggeration born of wishful thinking. If LLMs become good enough to perform all the functions of an employee, there will still be a transitionary period in which employees have realized that the LLM is good enough but employers have not. Depending on the agility of the company, it could be a week or a year. A perfectly efficient company would not have such a period, but companies are not perfectly efficient.

An employee successfully delegating 100% of their job to an LLM would be an example of arbitrage. The presence of arbitrage in other existing markets suggests that we don’t know how to eliminate arbitrage in the job market, either.

Also, even if LLMs become good enough to do only 90% of the work, a selfish employee who doesn’t plan to stay at their current company might find it worthwhile to turn their brain off. The company will eventually notice the employee’s decreased performance and fire them, but the employee would get some extra paychecks for no effort. If they already have another job lined up or they are near retirement, they might not be worried about how that would affect their reputation.

**spillybones**（49 分） · 2026-09-18T16:49:28.195-05:00：

there will still be a transitionary period in which employees have realized that the LLM is good enough but employers have not

We are currently witnessing employers laying off employees based on the false belief that LLMs can do the employees' jobs. Employers are so ready to believe that LLMs are good enough that they're jumping the gun. I don't think there's going to be a point where bosses could stop paying employees but aren't ready to believe it.

**singpolyma**（4 分） · 2026-09-19T08:53:18.136-05:00：

Hasn't this basically always been an excuse used to justify a layoff they wanted to do anyway? All the ones I read about were basically corrections after pandemic over hiring with a veneer of "because AI" in the press release.

**orib**（20 分） · 2026-09-18T16:06:03.893-05:00：

Currently the people pushing hard for LLM use are the corporations, because they want to remove the employees. They're going to be watching real close for any sign that the employees are now redundant.

There'll be a "just in case" window when the employer isn't sure that just removing the human will work out, but I doubt it'll be a large one.

**hjvt**（4 分） · 2026-09-18T17:49:55.492-05:00：

And then, when everyone is laid off, who is going to buy a company's product? That's the catch 22, even in the case where the LLMs work, they do not.

**orib**（5 分） · 2026-09-18T18:05:55.682-05:00：

And then, when everyone is laid off, who is going to buy a company's product?

Another company. With sufficiently autonomous entities, you can make the economy work without people, it's just not very good for people.

**hjvt**（13 分） · 2026-09-18T18:27:00.436-05:00：

You are jumping straight to paperclips, but you can't get there, because that's far past society's breaking point. Datacenters will be burning and CEOs will be getting lynched in the streets way by the time unemployment hits 20%.

**orib**（11 分） · 2026-09-18T18:54:12.414-05:00：

Only if we get a move on before policing is automated.

**k749gtnc9l3w**（2 分） · 2026-09-19T08:14:16.133-05:00：

Automated and scaled up, without cutting corners. They want to believe it is about policing riots. But at that level of collapse it will be about policing people with nothing to lose taking long stretches of power grid that were live just before.

**mordae**（1 分） · 2026-09-19T03:32:22.441-05:00：

As usual, future comes non-evenly. Some places will see it earlier, others will watch and take notes. Both authoritarians and democrats.

**singpolyma**（7 分） · 2026-09-19T08:56:00.718-05:00：

If we hold all else equal it is very very bad for people. However an economy that works without people is also a description of the post scarcity dream. The problem is that if we keep making "jobs" the way anyone gets the benefit of the economy and no one has one we end up with a disaster rather than liberation.

We can't keep pushing tech progress alone and hoping society figures out the rest. We need to work on society first before the tech progress can be beneficial for humanity.

**emk**（2 分） · 2026-09-19T12:02:58.897-05:00：

Yup. If the robots are ever cheaper and more efficient than human labor, then the robots can just build the private jets and mansions for the billionaires directly, no human workers required. And if the humans complain about being hungry, then arm the robots.

The assumption that you need humans to run an economy is based on the idea that humans are the most intelligent, flexible and cost-effective workers available. If the humans are the only good workforce available, then it's important to keep the humans happy and productive. But if humans are ever outcompeted economically by sufficiently advanced AI and robots, then the billionaires don't necessarily need all 8 billion of us.

Of course, there's also the question of whether the billionaires could control the robots any better than OpenAI has been controlling its swarms of agents.

## 关联链接

- https://danluu.com/brain-off/
