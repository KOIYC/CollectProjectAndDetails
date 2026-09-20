---
type: "corpus"
item_id: "be69d1c920579bcd"
title: "Saving another 100TB of RAM"
source: "hn_front"
source_name: "HN 首页（非 Show HN）"
url: "https://news.ycombinator.com/item?id=49758580"
project_url: "https://blog.cloudflare.com/saving-100-tb-of-ram-with-math"
author: "f311a"
published_at: "2026-09-18T18:51:46Z"
captured_at: "2026-09-20T03:41:55+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - hn_front
  - author_f311a
  - story_49758580
  - front_page
metrics: {"points": 439, "comments": 98, "engagement_velocity": 439}
comments_count: 86
comments_total: 86
discovered_via: "hn:front_page:2d"
archived: true
archived_at: "2026-09-20T09:16:59+08:00"
archive_reason: "排除:无主题词"
---

# Saving another 100TB of RAM

- **来源**：HN 首页（非 Show HN）　|　**kind**：post
- **原帖**：https://news.ycombinator.com/item?id=49758580
- **指标**：点赞=439 · 评论=98 · engagement_velocity=439
- **作者**：f311a　|　**发布**：2026-09-18T18:51:46Z
- **项目链接**：https://blog.cloudflare.com/saving-100-tb-of-ram-with-math
- **采集**：2026-09-20T03:41:55+08:00　|　**id**：`be69d1c920579bcd`

## 正文

Published: 2026-09-18

Saving another 100TB of RAM with math (and Rust) | Cloudflare Blog

September 18, 2026

# Saving another 100TB of RAM with math (and Rust)

Kevin Guthrie

Mariia Iurchenko

Zaidoon Abd Al Hadi

 and 

Ivan Babrou

Cloudflare operates at a scale so big that even after working here for years, it doesn’t seem real. We have thousands of servers all over the world with petabytes of RAM and millions of CPU cores, and all of it is pushed to the max. As vast as those resources feel, they are still finite, and when you need every service to run on every node, it doesn’t leave room for wasted space.

At this scale, small improvements are greatly magnified, so even 1%-at-a-time improvements are worth celebrating. And some tweaks add up to a lot more: in this post, we’ll look at how small changes to a single algorithm reduced the memory footprint of one of our Pingora-based services significantly. That allowed us to reclaim more than 100TB of RAM globally, on top of the 100TB of memory the DNS team was able to shed last month.

## Waste not

Maintaining equitable resource sharing between teams is not easy, especially in large organizations. One of the ways Cloudflare ensures the balance is kept is through the tireless efforts of the wonderful Performance team. 

This story starts with a ticket filed by Ivan who found: Excessive memory usage from pingora-ketama in Pingora Backend Router. The finding was that our internal load-balancing service, Pingora Backend Router (yes, PBR), was using significantly more memory than expected — specifically in structures associated with pingora-ketama, which is our open-source library for handling consistent hashing.

In order to talk about how we addressed this seeming overuse of memory, we need to talk about what consistent hashing even is, why we are using it in PBR, and how it became so memory hungry. Along the way, we’ll learn some Rust and even a little math.

## Consistent hashing

Consistent hashing is a widely used method for distributing tasks across multiple servers in a way that does not require large changes when servers are added or removed. Internally we use it to route cacheable requests to servers by URL. This allows us to keep only one copy of a file stored per data center and gives a stable way to find the location of each file. We have mentioned this system before, but let’s take the time to walk through how and why this algorithm is used and how it works.

The key concept of consistent hashing is that while hash functions can accept any kind of input, their output is limited to a single unsigned integer (32, 64, or 128-bit integers depending on which hash function). This allows us to relate tasks and servers to each other in a consistent way. Most discussions of consistent hashing have you think of that output space as a continuous, circular ring that wraps around from its max value to zero. This depiction makes for some nice visualizations, but it can also make the simple concept of integer ranges seem more complicated than it needs to be. For our discussion, we’ll represent the 32-bit output of our hash function as a number line.

Now, let’s say we have a set of servers, A, B, & C, and a set of tasks t-z. We can map each onto the number line based on the hash of their representative values, so something like IP addresses for servers and cache keys for tasks.

Assigning tasks to servers is now just a matter of finding the first server to the left of each task. We can represent this visually by coloring in the region of hashes that will be associated with each server. Notice that the range covered by server C wraps around to the beginning, hence the idea that hashes exist in a ring.

And that’s it. At a base level, consistent hashing is this simple — but it doesn’t take long to see that there is room for improvement. Notice that the range covered by server A in our example is significantly larger than that of either B or C. This is a problem because the fraction of the requests a server handles is going to be proportional to the size of its range on the number line. Ideally we would like to guarantee each server will have an equal size, but because hashes are essentially random numbers, we have to talk about the size of the regions in terms of statistics. 😨

## Math and consequences

First: don’t panic. I promise I'm not about to lie to you and that we will stay safely within the bounds of a day-one probability lesson. When we talk about statistical distributions, there are two big factors that help us quantify uncertainty in helpful ways: expected value and standard deviation. In (over-)simplified terms, expected value gives us a point where measurements based on a distribution will be centered, and standard deviation tells how close to that central point most measurements are likely to be.

For consistent hashing, we can calculate these factors for the fractional size of the range associated with one of N servers. (Details on where this formula comes from later).

$$m \begin{align*} \text{Exp} &= \frac{1}{N} \\ \text{SD} &= \frac{1}{N}\sqrt{\frac{N-1}{N+1}} \end{align*} m$$

In terms of concrete numbers, let’s say we have 100 servers. The formulas above give: 

$$m \text{Exp}=1/100 = 1\% \\ \text{SD}= \frac{1}{100}\sqrt{\frac{100-1}{100+1}} \approx 0.99\% m$$

That tells us that we can expect that the range each server handles will be centered around 0.99% of the total and most of the lengths to fall within 1% of what's expected. This sounds good until we realize that that’s 0.99% of the total length. We need to scale the standard deviation by the expected value to see how big the error is as a fraction of the target size. This value is called the coefficient of variation. 

$$m \text{CV} = \frac{\text{SD}}{\text{Exp}} = \sqrt{\frac{N-1}{N+1}} m$$

At $m N=100, \text{CV} \approx 99\% m$ — meaning some servers will likely be working 99% harder than they should be (handling twice as many requests) while others could be doing practically nothing! Now that we have a way to predict how evenly loaded servers will be using consistent hashing, we can start working on improvements.

## What if we add hashes?

The simplicity of consistent hashing is a double-edged sword. It’s easy to understand and implement because everything is turned into easily-relatable hashes on the same numberline, but any improvements to the system will also need to be relatable to that numberline. That means the solution to any consistent hashing problem can only be more hashes. It’s less like a golden hammer (a tool with which all problems look like nails) and more like a golden nail in that it turns all tools into hammers.

To solve the problem of imbalanced workloads, we can add multiple hashes to represent each server instead of just one. We’ll get to the math behind this momentarily, but it should make some intuitive sense that while each individual range has a large standard deviation, adding a bunch together should make their total size even out. If we take our three-server example from the above diagrams and add two more hashes at random for each server, we see that it helps even out each server’s workload. 

This is an admittedly contrived example. The random nature of the system means there’s no guarantee how much improvement you will get from adding 2 additional hashes per server, but it should make some intuitive sense that combining more of these hash segments together produces a more even distribution. Each segment in the sum has a chance of balancing another. Maybe one is too short; maybe one is too long. This is essentially what the law of large numbers tells us should happen… The obvious problem is it only works for large numbers. In NGINX, the baseline number of hashes per server is hardcoded to 160, and Pingora uses the same value as the default. I’ll spare you the math for now, but if we go back to our 100-server example, if we use 160 points per server instead of just one, the coefficient of variation (which we can

## 评论（86/86）

**agosta** · 2026-09-18T20:48:29.000Z：

Bang up article! As someone who doesn't get to do enough (almost any) calculus in my daily programming assignments, I thoroughly enjoyed reading about Kevin's dive into that derivation (linked in the supplemental article). All the people being negative here can swallow raisins

**proc0** · 2026-09-18T20:49:29.000Z：

The only Rust section is the one on storage improvements about the struct that stores the hash, but do they really need that many hashes that 2 bytes makes that big of a difference? Article doesn't expand, but I guess it's a hash for every task on every computer, so maybe yes.

**ricardobeat** · 2026-09-18T20:52:05.000Z：

These optimizations are impressive, but it gets me thinking: at what point does a company become a collection of impenetrable siloes, where nothing really does what you expect? Maybe know with AI this is less of an issue as exploring a codebase is also much faster.

**dr_dshiv** · 2026-09-18T21:37:14.000Z：

Cloudflare is truly amazing, they have made so much possible for my main side-project at a price and performance that I can’t really take credit for (http://sourcelibrary.org), I don’t care if their text was written with AI, I just wish I could get my own AI to sing so well about hashing… but wait.. today I noticed Claude trying to use hashing when a timestamp would honestly do, and now I’m really doubting myself, hmm…

**kingleopold** · 2026-09-18T21:54:35.000Z：

anyone remember 100tb hosting company?

**sroussey** · 2026-09-18T22:11:19.000Z：

Someone really needed a few hundred TB to waste on inference and went looking under the rugs…

**parallax_error** · 2026-09-18T22:23:38.000Z：

I definitely enjoyed this writing style more than a lot of the recent cf blog posts. Cool article!

**swe_dima** · 2026-09-18T22:53:05.000Z：

does this mean RAM prices can go down now? Please?

**Fordec** · 2026-09-19T00:17:07.000Z：

This sort of thing makes me thing that we're about to enter an era where software development is going to be where most of the jobs fallout will be. You can't one-shot vibe code your way to this. But for proper Software Engineering, those jobs are safe where more and more problems are going to actually need solving by creatively using math because all the problems individuals deliver are just going to be larger. People are just mourning the loss of the low hanging fruit.

**zer0x4d** · 2026-09-19T00:19:18.000Z：

Incredibly happy to see this series of CF articles. I was always so proud of devs back in the days where RAM and processing were scarce and who had to get creative to fit even the most basic stuff in the budget. It seemed to me that after RAM and processing became abundant, most gave up on optimization and focused on shipping instead which meant now that even with several cores, a basic notepad or music player failed to work. In a way, RAM becoming more expensive has ushered in a new era of forced optimizations, which I'm really happy for

**variety8675** · 2026-09-19T01:22:47.000Z：

It’s nice to see Cloudflare is letting humans write the blog posts again after all the fallout from their LLM slop blogs

**jiggawatts** · 2026-09-19T03:09:19.000Z：

I'm surprised to see no mention of hierarchical rendezvous hashing in either the article or the comments here.It is purpose-designed for exactly this type of proxy/cache load-balancing scenario!

**vlovich123** · 2026-09-19T03:21:08.000Z：

I would get rid of consistent hashing and ketama for a better system which works save an additional 600TiB.You use the first N bits of your key hash to pick the server partition so it’s a reasonable number (eg 128 servers per partition). Then use high quality precomputed hashes (first 64 bits of sha256) for the server name as N in H(K + N). Use wymum from wyhash as the H so that you do o(n) integer multiplications while retaining a result that’s still a good hash statistically.Now you’re using a tournament hash, the small N means O(N) vs O(N log N) doesn’t matter, and also this O(N) is also going to be much less CPU than computing 160 hashes per key as they do now, so much less latency added per request.

**sfink** · 2026-09-19T04:40:58.000Z：

Um.I read the article thinking it would make for a great brain puzzle, but I quickly decided there's something wrong with the question setup because the initial solution didn't make sense. I assumed it was just missing a constraint that would be revealed later, but I'm still not seeing it -- the article just kept patching up the flaws in the wrong solution, the one that is more complicated than the straightforward one.I'm probably still missing something obvious? It's probably something to do with "...in a way that does not require large changes when servers are added or removed."But let's start with the problem as initially posed: you have an infinite stream of tasks and you need to deterministically assign them to N servers. (Perhaps you have to shard the collections of servers, so not every load balancer knows about all of them? But no, that would break the solution in the article.) Ok, then hash the task request (I assume that you hash it, the article doesn't explicitly say, but that's how you'd get determinism) and take that hash mod N, that's your server index.Why hash the servers too? If you roll 6 dice, and then another one to choose which die to use, you're not getting any more randomness. You're matching up two sides, the tasks on one side and the servers on the other; no need to randomize both.Ooh, but that's not a perfect distribution? Ok, if the hash value is large enough to be in the at most N-1 slop values at the top of UINT_MAX, then roll again (compute another hash). But CF is happy with 8% unevenness, there should be no problem with this 0.1% or whatever.Also, how do they find the nearest server hash to a task hash? Surely it's not a log(n) binary search through sorted server hashes, I hope?Weights break this scheme. Now each server has some number of tickets. So you compute hash % T (where T=total tickets) and have to figure out what server that is. There's probably a more clever way, but you could make a big array of (2-byte!) server indexes, one per ticket, and just fill them in and look up at index hash % T.That's 2 bytes per ticket, which feels uncomfortably wasteful if weights can be large. That's where things get more complicated for me: since the tasks are hashed, it doesn't matter what order a server's indexes come in relative to other servers', so sort them by descending weight. [I'm starting to suspect I'm making a fool of myself here by missing something obvious with the whole setup...] Now you can make an array of indexes for servers with the highest weight, then the next lower, then the next. Record the number of servers of each weight. Then you can take the hash % T and figure out which array it's in, then divide by the weight to give the index within that array.To reduce the number of per-weight arrays, you can restrict the weights allowed. If you restrict weights to be powers of two, you can eliminate a division by using a shift. If you really want more flexible weights, you can allow servers to be in more than one of the arrays. Let the arrays be powers of two, and then add an entry to each array corresponding to 1 bits in the binary representation of the weights. That increases the total memory usage of the arrays, so you could somewhat restrict the allowed weights by rounding to the nearest number with, say, 2 or 3 "on" bits at most. With at most 2 bits, that means weights are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, .... The error really isn't bad.And this should all be easily doable without any branches, I'm pretty sure. As long as you statically cap the max weight.Anyway, that's just plowing through with the straightforward approach, and I still think I'm probably missing something major here. I imagine with large numbers of servers, some go down, so fast deletions are probably important. You can get by a little while by marking dead servers and if you "roll" one, just roll again. (Yes, deterministically, assuming other load balancers agree that the server is down.) But when more than some number of servers go down, you'd want to kick off a background task to rebuild a new set of tables -- so that's a factor 2 in size usage to have them both in memory during the rebuild.Adding is trickier, you'd probably want to do a 2-level structure where first you use the hash to decide whether it's in the old set that the table is built for or the set of servers that hasn't been incorporated yet (you'd collect these over time, and empty them out on the next table rebuild.) It's a little weird, because the load balancers' outputs would only agree when the added and deleted sets agreed, but I don't see how to do better than that. (I think you could set up some kind of synchronization scheme so that the old sets would agree, which would make them usually agree on which of the old set of machines gets it.)Somebody, feel free to tell me I'm being stupid! I'm sure there's a constraint that I'm missing, given that my understanding of the initial problem doesn't require any memory at all except for the servers' info.(Or if not, I'll let you know where I'd like to receive shipment of 1% of the memory I've saved...)

**schobi** · 2026-09-19T07:26:53.000Z：

I can imagine the other internal teams looking at this.. "100 TB gets you attention? Hold my beer.. we will try that as well!"

**videocompressde** · 2026-09-19T09:17:42.000Z：

I've hit the same thing at smaller scale — once you know the real cardinality, shaving a few bytes per entry beats the clever stuff that never got profiled.

**MisterMunchkin** · 2026-09-19T09:44:28.000Z：

I like that they have a performance team that actually tries to improve their products over time.I also really appreciate the fact that this is human-written and not just AI slop. It’s refreshing to actually read English instead of Claudelish.

**goodpoint** · 2026-09-19T09:48:41.000Z：

TLDR: the existing implementation was poorly designed. They packed 2 integers better and saved memory.

**cloudengineer94** · 2026-09-19T11:24:09.000Z：

Every single optimization stories I read such as these make me super happy

**christina97** · 2026-09-19T14:51:24.000Z：

I’m not sure why folks are finding this so revolutionary. There are teams of scientists at big techs with PhDs working on all kinds of optimization across compute fleets. This seems cute but its exposition of math is more along the lines of “look at how cool I am that I could do a bit of calculus”, and that makes me question the technical depth at CF.I found the motivation pretty lackluster: nowhere does it actually explain why you use consistent hashing (dividing the item space naively/regularly would actually cause much more than 1/n items to move, which is unintuitive) and how you actually use it.That said, it got me to spend a few minutes studying this and got me to understand the key bit I was missing.

**Sevii** · 2026-09-19T15:47:04.000Z：

It's crazy to realize 100TB of RAM isn't that much anymore. 10TB server racks are already in production. Before long we'll have 100TB racks serving one instance of an LLM.

**nopurpose** · 2026-09-19T16:13:51.000Z：

Do I understand correctly, that they spent memory storing largish N hash values per server, so that request hash determines which server to send request to using closest higher value of all server hashes?That in effect boils down to consistently selecting server S with probability P, where P is function of weight and total number of servers?Surely there must be better way to select server with a given probability without storing a massive lookup table of hashes? Randevouz hashing of some sorts

**varispeed** · 2026-09-19T18:59:27.000Z：

Stop hoarding RAM. Are they going to offload it through ebay? Unlikely.

**terabyteoff** · 2026-09-18T21:13:16.000Z：

Thanks! Maybe dial it back or people are going to think I paid you

**agosta** · 2026-09-18T20:52:55.000Z：

That's exactly his point/the area of cost saving - that they didn't actually need as many hashes as they had started with. The trick was in finding out how many hashes they could cull without degrading load balance.

**simonjgreen** · 2026-09-18T21:26:18.000Z：

My intuition around larger companies is they are already impenetrable silos, and AI makes it worse

**BobbyTables2** · 2026-09-18T21:30:05.000Z：

I feel like any company whose products have RESTful interfaces are already there…One wants to turn on an indicator on a remote device. A simple Boolean value. But we need networking, TLS, authentication plugins, certificate validation, distributed logging, containers, orchestration, HTTP client/server, interprocess communication, daemon dependency management, …Sure, one can say each of these layers and abstractions has an important and justifiable purpose. But one can also step back and start wondering - what the hell are we really doing???At some level, it seems like each layer of abstraction has to manage others, only simply because they exist.Imagine the simplicity of 1800s telegraph signaling - no software!Too often we build systems with Fortune-50 style hierarchies when a 5-person team could do the whole job.

**nikanj** · 2026-09-18T22:08:55.000Z：

And at what point does a company start to care about performance? 100TB of RAM is expensive as hell, but getting products to market faster was worth the cost

**mitxela** · 2026-09-18T23:26:02.000Z：

Actually, AI creates spaghetti faster than any human ever could before.

**sb057** · 2026-09-19T04:26:49.000Z：

>at what point does a company become a collection of impenetrable siloes, where nothing really does what you expect?Around the year 2015.

**procaryote** · 2026-09-19T06:38:28.000Z：

The trick is to keep the silos losely coupled and small enough that you can understand it reasonably quickly. A component like the one in the article is pretty good like that. It just routes traffic according to weights. It doesn't care what the weights represent. It doesn't care where the servers are. It doesn't care what the traffic isThe team that owns it needs to understand it. Everyone else can just use it.

**davidbarker** · 2026-09-18T21:43:35.000Z：

This is pleasant coincidence. Really like your site and it's queued to send in my newsletter in the morning! Just happened to see your comment here while I was reading. Great work.

**ChoosesBarbecue** · 2026-09-18T22:31:34.000Z：

> I don’t care if their text was written with AI, I just wish I could get my own AI to sing so well about hashing… but wait.. today I noticed Claude trying to use hashing when a timestamp would honestly do, and now I’m really doubting myself, hmm…Tried out the first 1000 words in Pangram, and it seemed happy it was human written. Not surprised either, it has been some of the better writing I've seen out of Cloudflare recently.

**mitxela** · 2026-09-18T23:25:22.000Z：

What does Cloudflare make possible for your project?

**why_only_15** · 2026-09-18T22:19:40.000Z：

CPU DRAM can't really be used for inference efficiently -- inference mostly wants memory bandwidth, not memory capacity, and GPU DRAM has >10x more bandwidth. The fabs can switch between them but you can't switch after the fact.

**killingtime74** · 2026-09-19T00:33:31.000Z：

I think you're speaking like a software engineer, which is understandable, and not like a historian or economist. There's no reason to believe math based jobs would survive. The models regularly do well on math problems. You can auto-research loop ways to optimize memory usage for any particular program.

**jfengel** · 2026-09-19T00:48:42.000Z：

I don't remember those days with a ton of fondness. Yes, the challenge was fun, but I really wanted to ship it and get my product in the hands of customers. Now I can spend more time thinking about what they want and less time about what the computer wants.

**necovek** · 2026-09-19T07:02:29.000Z：

While it's nice to see this focus, while they highlight absolute figures, we are still talking about 1% improvement. For most other software systems, nothing worth putting effort in for.

**huijzer** · 2026-09-19T09:28:18.000Z：

> In a way, RAM becoming more expensive has ushered in a new era of forced optimizations, which I'm really happy forIsn't this mainly Cloudflare's scale though? That's literally also what's in the introduction written as the reason why they are doing the optimization

**colechristensen** · 2026-09-19T17:41:18.000Z：

During the Moore's Law years you didn't have to optimize much, if you did a significant release yearly computer hardware grew faster than your optimization problems.

**MakersF** · 2026-09-19T07:43:33.000Z：

I think they do only a hash per request. The 160*weight hashes were done per server (per feature set), to partition the hash space.
Per request you do a single hash and then a lower_bound on a sorted map to find the serving server (again, on the ring appropriate for the features required by the request, so likely a hash map lookup first)

**procaryote** · 2026-09-19T06:51:46.000Z：

You hash the servers because then adding or removing a server doesn't directly affect other servers position on the ring; adding a server just takes some load from som servers.This is useful because you want stickiness, so requests for the same key mostly go to the same server.Sorting servers by weight means that removing or adding a server will shift a lot of traffic from the servers it used to go to. A flapping server early in the list will break stickiness for the whole set of servers.The simplicity of stable hashing means you don't have to think about new sets, old sets, table rebuilds, synchronisation schemes etc, and that's useful because every such extra step adds bugs and corner cases

**varispeed** · 2026-09-19T19:00:18.000Z：

Who cares if you can buy all the RAM available. To hell with small business and working class who now cannot afford it.

**QuaternionsBhop** · 2026-09-19T19:00:31.000Z：

Plus it's limited to 65k entries. Perhaps a btree where parent nodes sum the weights of child nodes would work well. Using the input hash scaled by total weight, a binary search lookup would compute the partial sums for comparison on the fly. Adding/removing a node would only update the ~8 parents when the btree order is 4. Eytzinger layout and struct-of-arrays could be used to improve cache locality during lookup. This does mean an add/remove could drastically change the overall mapping, perhaps that's why consistent hashing is used instead.

**pixl97** · 2026-09-18T21:57:11.000Z：

Build a system as simple as possible but no simpler.An 1800s telegraph system doesnt work in the modem world, there is far too much communication and the system would just collapse into molten slag.All those things you've listed are because we live in an adversarial world and I'd steal all your money off the telegraph wire if you tried it.

**sroussey** · 2026-09-18T22:10:07.000Z：

Having worked in hardware for a moment, everything we do in software is like this. Even C.

**jeffrallen** · 2026-09-18T22:13:12.000Z：

There are a whole series of blog posts from the Fishworks guys explaining why it could possibly be so hard to turn on one LED.But Oracle probably deleted then so you'll have to find them on archive.org.

**MisterMunchkin** · 2026-09-19T09:51:32.000Z：

Cloudflare is unusual in that their product is performance and their costs are primarily hardware and networking. You see similar performance initiatives from companies like AWS who also need to maximise their hardware usage.Whereas for somewhere like Burger King, the costs are all rent and staff, so they wouldn’t care how much RAM their website uses. But you would see similar optimisation in their supply chains for their ingredients, and their rotas to reduce staffing.

**GroksBarnacles** · 2026-09-19T02:19:18.000Z：

Do you feel like this is a very meaningful comment? Will someone go "mm yes, actually it's spaghetti, I didn't think of that.."Are you trying to succinctly say AL'S spaghetti code outweighs the benefits of what it produces quickly?If you're not saying it outweighs it, what are you saying?

**adrianN** · 2026-09-19T02:42:57.000Z：

The steelman argumentation is probably that spaghetti doesn't matter to LLMs and no humans will read that code anyway.

**anigbrowl** · 2026-09-19T03:24:09.000Z：

I mean you can just pause and refactor regularly. I tend to use every ~4th session as an opportunity to refactor, adjust interfaces, break overly large modules into smaller ones and suchlike.

**dr_dshiv** · 2026-09-19T13:50:30.000Z：

Oh super — I appreciate that!

**terabyteoff** · 2026-09-18T22:35:11.000Z：

An AI would have known that saying, “Hi, mom” in a professional post was a bad idea.

**hiddencost** · 2026-09-19T17:38:24.000Z：

Please stop using this stuff. It's snake oil.

**sroussey** · 2026-09-18T22:32:17.000Z：

Those machines with GPUs still need RAM of their own, and they generally want large caches to avoid SSD penalties. You even see this spill out in the form of costs for KV cache in <1min, 5m, 1hr rates etc.

**halJordan** · 2026-09-18T23:19:02.000Z：

The majority of inference actually does happen in cpu.

**Fordec** · 2026-09-19T01:20:42.000Z：

The point isn't that "doing math" is safe. Auto-research solves one target variable in one system, doing it at scale where say one developer is SME for the agentically manged 200 microservices down the line, heh I mean you certainly can, but good luck with that token cost of auto-research when that problem space is O(microservice^2). I point at that example yesterday of that optimized database memory with the comments pointing out that the specific problem fit in memory, over optimized and didn't generalize. The problem isn't the work, but the rework. A historian should know that new solutions to problems doesn't lead to "no problems ever again" but only problems with barriers that the new solution doesn't solve.

**switchbak** · 2026-09-19T01:51:43.000Z：

Yes, I remember those too. The costs of manual memory management were real and were not low.But costs on the cloud are real too, especially now. I’ve been living in JVM land for a very long time, but now it’s especially clear how important lean services are. Especially now that the bar for writing lean code is so much lower: let the borrow checker figure it out, etc.I just spent a couple days wringing out more performance/memory efficiency for our services. Nice gains to be sure, but it’s still so immensely wasteful compared to something well written running native. If it was my money, I’d be going native for sure.

**appreciatorBus** · 2026-09-19T02:30:35.000Z：

Different people are different.Some of us find production and optimization more interesting than marketing and distribution.

**rstat1** · 2026-09-19T02:37:03.000Z：

And its this obsession with shipping things as fast as possible quality be dammed that got us basic weather apps that eat a gigabyte+ of RAM.

**suriyaG** · 2026-09-19T03:05:02.000Z：

incredible way to put it!!

**anigbrowl** · 2026-09-19T03:19:51.000Z：

(Cat reading newspaper)
I should build a database out of pointers

**sdevonoes** · 2026-09-19T10:59:46.000Z：

I wish I could care more about what the computer wants (because it’s fun). I couldn’t care less what the product demands.

**1vuio0pswjnm7** · 2026-09-19T17:08:34.000Z：

"Now I can spend more time thinking about what they want and less time about what the computer wants."What if they want memory efficiency

**robotresearcher** · 2026-09-19T19:02:14.000Z：

Customers often want to pay less, and shareholders often want lower capital costs. A tasteful optimization is a win-win. The opportunity cost should be traded off against new features of course, but tasteful optimization is a good thing for customers.

**sfink** · 2026-09-19T11:43:00.000Z：

Ah, right. The joys of being a fool in public.The part I missed is that the load balancers don't have a consistent view of the set of servers. There is no magical synchronization scheme that creates that consistent view. You want load balancers with slightly different ideas of what servers are available to mostly make the same choices for the servers they do agree on.Doh! I should have been able to infer that from the original solution.

**HPsquared** · 2026-09-19T08:18:31.000Z：

Kind of like analogue TV. Sure it worked and was simple, but consumed some prime spectral real estate.

**datadrivenangel** · 2026-09-19T02:02:57.000Z：

like this one? https://eschrock.dtrace.org/2008/07/

**AdamN** · 2026-09-19T09:37:46.000Z：

Great - now you've trained the next set of AI to put things like "Hi, mom" into their text as a tell that they're human ...

**adrianN** · 2026-09-19T02:45:52.000Z：

The argument is probably that LLMs can find those optimizations cheaper than a human expert. Since LLM cost at fixed capability seems to be going down you either expect humans to be completely replaced or human wages to be lowered by LLMs.

**locknitpicker** · 2026-09-19T09:54:09.000Z：

> But costs on the cloud are real too, especially now. I’ve been living in JVM land for a very long time, but now it’s especially clear how important lean services are. Especially now that the bar for writing lean code is so much lower: let the borrow checker figure it out, etc.I don't think even Cloudflare bothers with this waste of time. If they did, they would certainly not have built their global infrastructure on JavaScript running on V8. They'd have done what Google and old-time Facebook did and built their whole infrastructure on low-level system languages, and hiring the world's leading minds on the subject to milk the last drop of performance from their hardware.Even Google stopped to look at the problem and came up with Go. Not V8.

**CookieCrisp** · 2026-09-19T03:22:30.000Z：

And yet the world still turned

**locknitpicker** · 2026-09-19T09:42:49.000Z：

> And its this obsession with shipping things as fast as possible quality be dammed (...)You seem confused. Allocating more memory than optimal levels is not a measure of quality. Similarly, a web page is not suddenly lower quality if an image asset is 50kb instead of 25kb. And how much complexity and engineering effort and bugs are you willing to tolerate to halve your memory allocations?You are conflating quality with mindless minimization, not even knowing or caring that are the tradeoffs. The blog post you're commenting on starts by presenting the case for celebrating small improvements, even 1% improvements at a time. A similar 1% improvement in a mobile app is at like 1MB. Do you ever notice it? How many hours of engineering effort are you hoping to spend on this nonsense? And you prefer to spend it on this or in actually fixing a bug or implementing a feature?This puerile conflation of minimization with quality suggests your personal notion of quality has no bearing on what quality actually is.

**robotresearcher** · 2026-09-19T19:35:13.000Z：

Not foolish. The constraint of no-need-for-globally-consistent-state is so important and rules out so many approaches that it was well worth stating in the article.Indeed the statistical model described in the article does not model the distribution over server hash allocations you'd get if you allow them to be inconsistent across load balancer hosts, so the model implies a single global source of truth that they probably don't have in practice.

**Fordec** · 2026-09-19T06:28:20.000Z：

I expect average human wages for programming to get lower and the overall percentage of the developer to move lower wage countries and this probably means away from the US and US salary expectations. Meat proxies and agentic CRUD will be off-shored to low wage Asian or even African countries with AI handling language barriers. Why wouldn't they be? Why pay six figures for a meat proxy? Product Builders should weather the storm the most, but they'll be the high end skilled PMs/engineers that of the overall industry but probably won't break 10% of total global headcount. In a world where knowing the domain will be the key driver of differentiation, as building averages out and knowing the customer and how to market to them becomes the differentiator, being closer to the target market will fragment competition from four global winners with over 10k employees in a space to 100 niche/regionally tailored winners with maybe 500 employees a piece. Not to mention if you thought GDPR was a pain, wait until AI laws that vary by country to country get added in.I also expect as AI becomes more cost sensitive once the quality plateaus (there's only so many ways to get an answer to 100% right), the data centers are going to chase where the cheap power is, and this long term is likely to be in high-solar locations. So lower latitudes. Doesn't rule out places like Texas of course, but places like India, Mexico, Brazil, Israel or Saudi Arabia will have home field advantages.

**OoooooooO** · 2026-09-19T12:45:09.000Z：

Google came up with Go because:> The key point here is our programmers are Googlers, they’re not researchers. They’re typically, fairly young, fresh out of school, probably learned Java, maybe learned C or C++, probably learned Python. They’re not capable of understanding a brilliant language but we want to use them to build good software. So, the language that we give them has to be easy for them to understand and easy to adopt.From Rob Pike

**solarengineer** · 2026-09-19T03:36:56.000Z：

The world turned millenia ago and will turn millenia later.The problem statement is of applications using up expensive RAM. Incidentally, expensive RAM is just one of the problems we face in the computing space. Forced obsolescence is another, when running hardware needs to be replaced because software is built for only newer CPUs.

**altmanaltman** · 2026-09-19T05:59:16.000Z：

Thankfully the world's turning is not decided by big tech

**latexr** · 2026-09-19T08:55:37.000Z：

That statement can be used to justify anything, to the point it is utterly useless.— Humanity has been on the decline. People are hateful towards each other, striking their fellow man and poisoning the environment. Despots eventually launched nukes which killed everyone but the cockroaches.— And yet the world still turned.

**ffsm8** · 2026-09-19T10:31:31.000Z：

> And how much complexity and engineering effort and bugs are you willing to tolerate to halve your memory allocations?You seem to be confused about this relationship. It's usually exactly the opposite.The wasteful applications are generally not well reasoned about and half assed implementations. That's why they're guzzling resourcesThere is ofc a middle ground, because targeting eg incredibly resource constrained embedded systems will naturally increase complexity, but that's something entirely different to the scenario this discussion was about up to this point.

**anonzzzies** · 2026-09-19T07:06:29.000Z：

> because software is built for only newer CPUs.You are right, but it reads (to me, could be just me) you mean newer specs which used to be true when I shipped software in the 70-90s; you mean faster machines / more memory right? Like installing a new version of software or OS and suddenly all memory is used, system is swapping and you did not ask for that but some obscure feature you didn't need needed to be shipped fast.

**locknitpicker** · 2026-09-19T09:48:37.000Z：

> The problem statement is of applications using up expensive RAM. Incidentally, expensive RAM is just one of the problems we face in the computing space.You need to stop and think about the problem. Nowadays RAM is expensive because many people now want to max out their computers with RAM to run LLMs and AI coding assistants. Today's software is still the same software that ran perfectly well half a dozen years ago. Cloudflare happens to operate a large global computer infrastructure, and it's scale is such that 1% gains are lauded as fantastic cost savers. But that's the bean counter's perspective, pointing out that they saved a bean.

**dns_snek** · 2026-09-19T08:21:37.000Z：

Probably not for the lack of trying.

**BSDobelix** · 2026-09-19T13:33:45.000Z：

Exactly, that`s why i refuse to call 99.9% of "software engineers" engineers. Imagine you optimize a aircraft turbine 1%....man you get to drink a pool of champagne with the highest ceo's and aircraft carriers try to buy that turbine as fast as possible.But with software and a install base of some millions 1% optimization is seen as wasteful, its like software slop is acceptable since forever because hardware gets faster, and electricity is "green" anyway.

**jpc0** · 2026-09-19T11:02:28.000Z：

> Today's software is still the same software that ran perfectly well half a dozen years ago.This statement is quite honestly not true at all. Just take the two largest OS from 6 years ago and compare resource usage between them and you will find you are incorrect, never mind the software running on it.

**Capricorn2481** · 2026-09-19T17:05:12.000Z：

> Nowadays RAM is expensive because many people now want to max out their computers with RAM to run LLMs and AI coding assistants.Source? I imagine the amount of people trying to run local LLMs is miniscule. RAM is expensive because a handful of companies have spent billions buying all of the compute.

## 关联链接

- https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/
