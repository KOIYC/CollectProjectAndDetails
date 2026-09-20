---
type: "corpus"
item_id: "76552ae059eb817d"
title: "Show HN: Pollen – distributed WASM runtime, no control plane, single binary"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47961935"
project_url: "https://github.com/sambigeara/pollen"
author: "sambigeara"
published_at: "2026-04-30T13:15:04Z"
captured_at: "2026-09-21T01:41:05+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_sambigeara
  - story_47961935
  - show_hn
metrics: {"points": 137, "comments": 65, "engagement_velocity": 137}
comments_count: 65
comments_total: 65
discovered_via: "hn:show_hn:174d"
---

# Show HN: Pollen – distributed WASM runtime, no control plane, single binary

> [!info] 一句话导读
> Show HN: Pollen – distributed WASM runtime, no control plane, single binary

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47961935>
> 指标：点赞=137 · 评论=65 · engagement_velocity=137
> 作者：sambigeara　|　发布：2026-04-30T13:15:04Z
> 项目链接：<https://github.com/sambigeara/pollen>
> 采集：2026-09-21T01:41:05+08:00　|　id：`76552ae059eb817d`

## 正文

Show HN: Pollen – distributed WASM runtime, no control plane, single binary

## 评论（65/65）

> **sambigeara** · 2026-04-30T13:15:43.000Z　
> Hi everyone, I'm Sam. I started Pollen as an experiment last summer, got carried away, and have landed here.It's a single Go binary. Install it on every machine you want in the cluster and they self-organise. Topology is derived deterministically from gossiped state, so workloads land where there's capacity, replicas migrate toward demand, and survivors rehost from failed nodes. The mesh is built on ed25519 identity with signed properties; any TCP or UDP service you pin gets mTLS. Connections punch direct between peers where possible, otherwise they relay through mutually accessible nodes.I built it because I'm fascinated by local-first, convergent systems, and because I wanted to see if said systems could be applied to flip the traditional workload orchestration patterns on their head. I also _despise_ the operational complexity of modern systems and the thousands of bolted-on tools they demand. So I've attempted to make Pollen's ergonomics a primary concern (two-ish commands to a cluster, etc).It serves busy, live, globally distributed clusters (per the demo), but it's very early days, so don't be surprised by any rough edges!Very happy to answer anything in the thread!Cheers.Docs: https://docs.pln.sh

---

> **kaoD** · 2026-05-02T13:45:21.000Z　
> I know the individual words in the description but I'm a bit confused about what this is.What would I use Pollen for?I'm not sure I understand the "seed" metaphor.

---

> **monster_truck** · 2026-05-02T13:49:56.000Z　
> This is neat, what does the actual throughput look like though?Have been hacking on a wasm+webtransport stack for distributed simulation workers and found the ceiling on one connection/worker per machine pretty quick. Had to pin adapters/workers to cores to get the latency I was expecting, then needed to use dedicated tx/rx adapters to eliminate jitter. Some bullshit about interrupt scheduling

---

> **sambigeara** · 2026-05-02T13:54:31.000Z　
> No idea why this post has picked up traction 2 days later, I’m out and about right now but will endeavour to respond thoughtfully when I’m back at my keyboard later on!

---

> **dbalatero** · 2026-05-02T13:56:08.000Z　
> I suspect you have something cool, but I think if you told a clearer example story that solves a real-world problem on the homepage it might alleviate some questions I'm seeing (and also having) in the thread here!

---

> **jitl** · 2026-05-02T13:56:56.000Z　
> Wow, this is super cool. It almost feels like a DIY pocket-Cloudflare. I’m curious how a WASM binary gets mapped to HTTP endpoints that take JSON, how much of that is Pollen vs Extism? Are the routes encoded in the WASM binary somehow?

---

> **hsaliak** · 2026-05-02T14:03:38.000Z　
> Using CRDT gossip to inform scaling is a clever idea. You are on to something there. Perhaps extract it as a core library/concept from the runtime? I feel that would be generally useful!

---

> **docheinestages** · 2026-05-02T15:35:18.000Z　
> Even after looking at the homepage and the GitHub README, I don't really understand how this could help.

---

> **esafak** · 2026-05-02T15:57:21.000Z　
> Did you have any applications in mind when you were designing this? Any weakness in precedents that you wanted to rectify? Are you familiar with Lunatic (https://lunatic.solutions/), and wasmCloud (https://wasmcloud.com/) ?

---

> **evacchi** · 2026-05-02T17:06:32.000Z　
> I am a simple man, I see wazero, I upvote :)(I am one of the maintaners, interesting work!)

---

> **m_ramdhan** · 2026-05-02T18:24:20.000Z　
> Really neat project. The idea of a fully decentralized leaderless WASM runtime is bold. My main question is around failure modes -- how does it handle network segmentation or split-brain scenarios? Does the gossip protocol deal with this gracefully, or is there an eventual consistency aspect that workloads need to be aware of?

---

> **omginternets** · 2026-05-03T00:25:29.000Z　
> Oh wow, this hits close to home. Hope it’s not bad form to plug an adjacent project on your post — felt too aligned not to, and it seems like we've converged on quite similar ideas! I’ve been working on Wetware [0], which has significant overlap on the substrate (P2P WASM, content-addressed, single binary, no control plane).Different design center, though. Wetware is aimed at people building multi-tool agent products who’ve hit Simon Willison’s lethal trifecta [1], so the design pressure goes elsewhere: cells are fully async WASM/WASI procs (cheap to suspend, parallel by default); inter-cell calls go over object-capability RPC (Cap’n Proto); and there’s a tiny Clojure-inspired Lisp (“Glia”) that doubles as an LLM-facing or human-facing shell. It’s pure by default w/ content-addressable, immutable data structures planned, and an algebraic effect system gating every impure operation exists today. An agent (human or otherwise) can list, attenuate, and invoke just the caps it’s been granted, and you can see at a glance which fragment of code can actually touch the world.The cap-vs-ACL bit seems to be the main point of divergence, AFAICT. Pollen’s grant docs show capabilities as cert-baked properties the callee inspects in user code (closer to attribute-based access control than to invocation-time cap tokens, and a clean fit for trusted-cluster ops like delegating admin or roles -- very sensible and def don't want to knock it!). Wetware leans the other way on the spectrum: caps are unforgeable references to specific methods (Cap’n Proto), the runtime enforces that nobody can call a method they don’t hold, and attenuation happens by grafting a strict subset of those references to a child cell with per-method granularity. So tool-calls-tool composes naturally, and the worst case of pulling a sketchy MCP server off GitHub becomes “the call fails,” not “depends whether the seed wrote its property check correctly.”It's a les polished compared to what Sam has shipped, but moving fast, and this post has jolted me into sharing a bit before I had planned! Sam, would love to compare notes if you're open to it. And I'd also love to talk to anyone who’s shipped a multi-tool agent and gotten bitten : pwned in eval, legal blocking a third-party integration, can’t audit every MCP server you depend on. We’re in the first 100 conversations.Either way, congrats on shipping — the 10-node demo is super slick, and “pure Go, no CGO” is IMO a major win :)[0] https://github.com/wetware/ww
> [1] https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/

---

> **ivere27** · 2026-05-03T03:09:54.000Z　
> nice project. can I use it like a microservice?
> in a small company, and installing Pollen in all computers.
> then, running a business logic in there? instead of 'centeral servers'?
> good to have WASM sandboxing everywhere."Use idle company machines as a decentralized, sandboxed microservice cluster"

---

> **samantp** · 2026-05-03T05:27:53.000Z　
> This is so nice. Encouraging to see such persistent serious efforts in the local-first, control-resistant tech space, even knowing it is a long uphill climb. Hope all the fragmented efforts help move toward something really formidable one day.

---

> **drzaiusx11** · 2026-05-03T16:59:35.000Z　
> This looks fantastic, however it's not clear (to me), which WASM feature sets are supported? p1, p2, simd, garbage collection, tail calls, etc. Might be good to include in a table on the readme itself as different features will expose which compute loads can be used in this distributed runtime system.

---

> **mitchsayre** · 2026-05-06T14:57:56.000Z　
> This is really cool. Do you have any plans to make a version that runs on Android or iOS eventually?

---

> **yencabulator** · 2026-05-11T19:48:50.000Z　
> I'm a little confused about a "zero-trust mesh" where I actually do need to trust the honesty of the nodes performing my computation. I'd suggest less buzzwords and more concrete examples.

---

> **anilgulecha** · 2026-04-30T16:47:48.000Z　
> Interesting project.In a potential modern cloud, having a globally named primitives (computer, store, messaging) can unlock very wider applications. Have you come across any such?

---

> **Levitating** · 2026-05-02T13:43:17.000Z　
> You have some workload demos which all definitely try out but could you paint us an example use-case of the technology?What are the workloads in the runtime capable of?

---

> **digdugdirk** · 2026-05-02T13:46:34.000Z　
> From someone who definitely doesn't fully understand what you made, this looks really cool!I'm seeing some functionality that seems like it could replace some personal services I currently host via my tailscale network. Am I understanding this correctly? If so, do you have a feel for what the performance implications would be?

---

> **r3trohack3r** · 2026-05-02T14:39:22.000Z　
> This is incredible.We’re building an AWS analogue catalogue of services (Databases, Compute, Auth, etc.) for distributed systems.Want a job do Pollen-like dev full time?william.blankenship@webai.comEither way, would be great to compare notes!

---

> **convolvatron** · 2026-05-02T17:34:31.000Z　
> this is a great direction - self organizing service meshes that don't require a infinite tower of manually configured turtles to rest upon. state management is really going to be an intersting and I encourage you to post back here with your thoughts. strong consistency kind of gets you back to turtle-land pretty quickly, and free-for-all eventual turns out not be a good foundation. the sane middle ground seems to be monotonic eventual consistency, which I think is what CRDTs get you.I wish more projects were conceived this way, instead of assuming that there is a kuberenetes cluster another database or two, and some message queues to lash it all together.

---

> **al_james** · 2026-05-02T17:46:09.000Z　
> This is very interesting! I agree about the operational complexity of many systems, cough Kubernetes.For most systems, state storage is the toughest problem, have you considered adding some form of storage layer over the top or would you recommend another solution that allows all the workloads to share state?

---

> **chris-corby** · 2026-05-03T13:00:02.000Z　
> Fascinating project – do you think there is a use case where a cluster could host web assets or a full static site? I wonder if it could act like a personal CDN in that way...

---

> **sambigeara** · 2026-05-02T14:02:37.000Z　
> Well, that’s a good question. I think the best answer for now is “we’ll see”?I use it in place of Tailscale for some homelab applications. I’ve started to deploy other experiments on a “prod” cluster. The demo I showed shows how Pollen responds to a multi-step pipeline type application; two WASM seeds and a single egress communicating over the provided RPC mechanism (`pln://seed…` etc) whilst handling routing, back pressure and the like.Right now, the workloads need to be stateless. I’m coming up with a story for state at the moment, which’ll likely start as some WAL-like convergent structure with thin (KV store etc) abstractions layered over it. Probably not dissimilar from the pattern underpinning the current CRDT gossip state.

---

> **sambigeara** · 2026-05-02T17:05:27.000Z　
> Failed to mention in my other reply: a "seed" because I envisioned, perhaps too poetically, "seeding" some generic computational unit into the cluster only for it to organically spread to other nodes in the cluster... sort of like pollen? Maybe.

---

> **sambigeara** · 2026-05-02T14:39:11.000Z　
> It’s a really interesting question.The real challenge is gating and reserving “slots” for downstream calls. If seed A on one node calls seed B on another, as it stands, Pollen holds that seed A instance up and waiting (with the memory overhead etc) until the response finds its way back across the cluster.You can probably imagine how latencies then start impacting this (espesh when a node in USW is generating traffic that needs to ultimately land on my laptop in the UK), not to mention all of the contention from other nodes elsewhere generating load too.In the demo, I see about 2500rps land on my laptop with 4k-5k generated across 4-5 nodes globally, but this is a multi hop scenario. If a call is only invoking a single, light WASM function, I see much higher throughout.The project is in its infancy, no doubt I’ll have lots of fun figuring out how to optimise as it progresses!In the first scenario above, memory seems to be the ceiling, in the latter, CPU.(Edit: these numbers are really quite meaningless but I wanted to give something tangible)

---

> **greyface-** · 2026-05-02T13:59:51.000Z　
> A moderator added it to the second-chance pool: https://news.ycombinator.com/item?id=26998309

---

> **sambigeara** · 2026-05-02T14:58:42.000Z　
> Yes, definitely.

---

> **onlyrealcuzzo** · 2026-05-02T17:48:15.000Z　
> Second -> this seems like something that might be cool.But as someone who's probably as close to your target audience as you can get -> it's not clear to me what exactly this does, and when I would need it.That may mean I'm not in your target audience, but then I suspect that audience is very small.My critique:> Pollen is a self-organising mesh and WASM runtime written in pure Go. Workloads are "seeded" into the cluster and organically scale and follow load. There is no central coordinator; decisions are made deterministically, locally, using a gossiped CRDT runtime state as their source of truth. Same view of the world; same workload placement and routing.Sentence one is fine. It could probably be less mumbo-jumbo-y.Sentence 2 should be paragraph 2.Your actual sentence 2 should be along the lines of: what is a self-organizing mesh, and when is it useful (IMO).I also would suggest not using CRDT right away. I think you might have a lot of people that might be interested in this, but don't know exactly what that is or why it's useful.

---

> **sambigeara** · 2026-05-02T16:52:13.000Z　
> Ha, thanks! The routing is all Pollen. You reach the workloads through the gRPC control API (exposed on a socket on the host) via a `pln call seed_name function_name payload` or with a more traditional gRPC client. But once they're in, it routes them to a keyed WASM instance of that given seed on whatever node happens to be hosting it at that moment.

---

> **sambigeara** · 2026-05-02T14:08:05.000Z　
> Thanks! That’s certainly crossed my mind!

---

> **sambigeara** · 2026-05-02T17:52:56.000Z　
> Fair comment that I'm hearing in a lot of places. I'll work on trying to land some concrete examples.

---

> **sambigeara** · 2026-05-02T17:18:09.000Z　
> Honestly, not really. It started as an experiment in local-first, convergent state (I have a historical fascination of this: https://news.ycombinator.com/item?id=27606604, https://news.ycombinator.com/item?id=42444856) and then continued to grow.I do absolutely despise the complexity of administering modern distributed systems, hence my attempt to make Pollen as ergonomic and (as much as I hate to use this term) batteries-included as possible.I've not come across either of those projects, oddly. I have a tendency to avoid looking for similar projects during the development of my own, lest I get despondent and run out of steam. Both sound cool, though. I'd say WASM was a natural workload "type" that fit nicely into what I was trying to achieve with Pollen, rather than a driving factor, if you know what I mean.

---

> **sambigeara** · 2026-05-02T17:36:28.000Z　
> Well, I have a lot to thank you for. The single binary, heterogeneous story would have fallen flat on it's face if it wasn't for the brill work you lot are doing, so, thanks!

---

> **sambigeara** · 2026-05-02T18:35:59.000Z　
> So, the moment a partition occurs, nodes within their resultant partitions then view the remaining peers as the full view of the world. There is _no_ concept of a split brain scenario.ANY decision around network topography or workload placement is a deterministic calculation run by all nodes individually. If all nodes see the same sub-set of peers representing their entire "cluster", they'll all naturally converge on the same view of what the cluster should look like. If the calculated output determines that Node A should claim Seed B, and it doesn't have it, it requests it from a peer who has it.As soon as the partition recovers, nodes see the additional nodes re-enter the candidate set, which is then added in to future routing and placement decisions.The main tradeoff to understand here is that you're at mercy of the random (best attempt redundant) placement of a seed. If the entire cluster has, say, 2 replicas stored on any given nodes, if a resultant partition doesn't happen to have either of those two nodes, then the seed will be unavailable until the partition recovers. You can work around this with "smart" initial placements (one near, one close, for example) but you're still at the mercy of random partition events. An additional factor is of course getting very unlucky with dropped gossip events, which would also impact the rate of convergence across the cluster.

---

> **sambigeara** · 2026-05-03T07:17:33.000Z　
> Wow! This is seriously cool. And certainly not bad form, there is a level of convergence here and it's always interesting to see what else is being built out in the ecosystem.I'd agree that Pollen's current cap-enforcement story is limited, I'm not sure what direction I'll be heading in for that, but I was erring on the side of "bring your own enforcement" as a design pattern (ultimately, people deploy their own decision engines as first class seeds in the cluster). Naturally, the enforcement is weaker than the (fascinating) pattern you've landed on--seriously cool.> and there’s a tiny Clojure-inspired Lisp (“Glia”) that doubles as an LLM-facing or human-facing shell.This is a _lovely_ abstraction. How does it work? Does the LLM emit Glia directly or is there a translation layer between natural language and the interpreter..?> It's a les polished compared to what Sam has shipped, but moving fast, and this post has jolted me into sharing a bit before I had planned!I'm _far_ from polished. I suspect you're underselling your own position here, looks like you have something very compelling. And apologies for the jolt! Certainly happy to compare notes--I (think) I've added my email to my profile.

---

> **sambigeara** · 2026-05-03T06:20:09.000Z　
> Hypothetically, yes! If your workloads are bounded and can compile to WASM, break them into logical units which would benefit from individual scalability, and `pln seed` them into the cluster. Ingress can be from any node. Any workload that doesn't suit the WASM seeds can be `pln serve`d on dedicated hosts.You could also establish a dev cluster (/environment) where all devs run a local instance. You can iterate on services quickly, expose ngrok-like capabilities by exposing a local dev instance of a server with `pln serve 8080 test_server` for your colleagues to consume with `pln connect test_server`, etc, etc.A more whacky idea I've not been able to get out of my head which might become possible as the access story solidifies: imagine a customer could access a controlled subset of your companies offering by having a delegated node, running in their own infrastructure, that ultimately you can delegate and revoke at any given time.

---

> **sambigeara** · 2026-05-03T06:12:44.000Z　
> Thank you. Me too!

---

> **sambigeara** · 2026-05-04T08:36:13.000Z　
> Thanks! It's just Wazero's default config[1] right now, so it implements (and is constrained to) those capabilities--WASI p1 is supported, WASI p2 isn't (Wazero yet to implement). Yes to SIMD, no to GC and tail calls (I think), etc. Full capabilities can be inferred from digging around in the code linked below.Good suggestion on listing capabilities, will add a note.[1]https://github.com/wazero/wazero/blob/2bbd517b7633bf6a126305...

---

> **sambigeara** · 2026-05-06T15:40:09.000Z　
> Thanks. Definitely crossed my mind, but it's in the "distant future" bucket, for now at least.

---

> **sambigeara** · 2026-04-30T16:59:38.000Z　
> To clarify, are you asking if I’ve considered incorporating those concepts into the project?If so, I have loose ideas around how I might introduce shared state, it’s an interesting problem that’ll require a lot of thought. Early days yet, though.

---

> **sambigeara** · 2026-05-02T16:41:01.000Z　
> OK bear with me on this, it'll probably be a idle thought-stream because I don't have a concrete answer right now.My intention is for Pollen to become a "generic blob of computational capability" into which you idly `pln seed` a workload and do not have to worry about ANY aspects of managing locality, scale, redundancy etc. You seed a workload onto any node, and you call it from any (other?) node. If you want to add more computational power to the cluster, you fire up Pollen on another machine and `pln invite` -> `pln join`.Every node also has it's own ed25519 cert. The root key pair (the "don't lose this or you're in trouble" key pair) is used to delegate admin certs to other nodes. I'm also working on a mechanism which allows you to bake any arbitrary properties into a cert (as it stands, these are lifted into the WASM guest code for, say, in-application authz purposes). I have more ideas about how this can be extended in the future.The root authority can invalidate a participating peer's cert at any point, currently just via a `pln deny` command which is eagerly gossiped around the cluster so other nodes stop talking to the denied node, too. I think this offers some opportunities for some fairly novel applications. Perhaps, in the future, you'll provision a node with a certain level or capability or authority to run on some external infrastructure. It'll have all of the (allowed) capabilities of your cluster, but will act like it's local to the external system. Plus, you can revoke it's access or re-set it's capabilities at any point; `pln grant` eagerly applies across the cluster, too.The workloads, at the moment, are just anything you can compile to WASM via the Extism PDK. Stateless, for now, but with a view to add shared state and persistence in the near future!Sorry this was rambly, hopefully it offered something useful.

---

> **sambigeara** · 2026-05-02T15:58:28.000Z　
> Thanks! I think the classic answer: "it depends" applies here. It currently only supports stateless workloads (for now, see below), so if you have nice, isolated, functional workloads, the WASM seeds could be a good fit!My original intention was that the WASM seeds would be the primary workload entity in the system, because it fits nicely with the whole local-first, self-balancing ethos (and WASM modules are blobs that can be gossiped around readily as nodes claim them). That said, you can also register generic TCP/UDP servers on a host (`pln seed 8090 some_service`), which are callable from nodes and seeds (via `pln://service/`).On statelessness, as I've alluded to elsewhere in the thread, I'm looking at how (convergent) state can be introduced into the system and exposed to seeds, so this would ultimately add another layer of capabilities to the WASM functionality.On performance: again, it'll depend. I noted elsewhere in the thread the distributed implications of chaining multiple seeds in a call flow. You're not _just_ dealing with CPU, WASM boundary-hopping or even traditional IO ceilings, there's also a component of synchronising gates in proxying nodes (as seed A calling seed B needs to reserve the WASM instance locally until seed B responds, which has knock on memory implications, etc). Its a fun problem, no doubt the story will get better in the coming months. For a local, simple invocation, depending on the nature of your workload, I would expect the standard WASM overheads to apply (there's only a thin layer between the API and the underlying Wazero runtime). For a lot of applications, this should be neglible.Also a note on placement, if you run, say, 10 nodes globally, `pln seed` will, by default, only place two replicas into the cluster. However, as load is introduced, the seeds will propogate towards it, so a node that's acting as an ingress for `pln call` will generally claim the workload to benefit locality/latency.

---

> **sambigeara** · 2026-05-02T15:59:43.000Z　
> Feel free to message here or privately if you wanted to discuss your actual use-case, would be keen to understand how people might try to use it!

---

> **sambigeara** · 2026-05-02T17:18:48.000Z　
> Thank you!

---

> **sambigeara** · 2026-05-02T17:49:17.000Z　
> Thank you! I suspect there'll be a fair few dragons to uncover (memory constrained nodes and partial views, disk storage, startup/shutdown patterns, etc etc), if it's worthy of a write-up then I shall certainly post it here.

---

> **sambigeara** · 2026-05-02T18:37:47.000Z　
> Oo good question. I'd prefer to keep external storage solutions as an exercise for the reader. I've touched on this in other comments, but I am looking to introduce state to the cluster internally, but for more sophisticated storage solutions, I'll probably avoid steering the project towards any one solution, at least for now.

---

> **debarshri** · 2026-05-02T21:09:13.000Z　
> I agree with operational complexity of kubernetes. That is the reason why we started writing single binary rust based kubernetes compliant platform [1]. Think of it like a minimal kubernetes rewritten in rust. Basically, you can deploy with kubectl.I like wasm idea here. I'm probably going to add wasm as runtime for this project.[1] https://github.com/debarshibasak/superkube

---

> **sambigeara** · 2026-05-03T14:13:07.000Z　
> Yes! I host pln.sh (and subdomains) as assets on my prod cluster. I have a couple of nodes hosted in EU/US, but do rely on a Cloudflare and a couple of A records to land traffic on them.

---

> **kaoD** · 2026-05-02T14:05:19.000Z　
> Let's see if I got this right: so it's something like a private Yggdrasil Network (minus the IPv6 overlay?) meets self-distributing WASM-powered serverless functions? Plus some built-in functions for proxying/serving.

---

> **sambigeara** · 2026-05-02T15:45:05.000Z　
> Ah! Makes sense.

---

> **DaiPlusPlus** · 2026-05-02T19:23:03.000Z　
> > but don't know exactly what that is or why it's useful.I hate to say it, but the only applications I can think of can be best categorized as illegitimate, likely clandestine, distributed computing tasks.

---

> **ivere27** · 2026-05-03T09:45:33.000Z　
> good to hear that. there are plenty of idle cpus in a company. then, we can use it safely in sandboxing wasm.

---

> **mitchsayre** · 2026-05-06T18:02:38.000Z　
> Do you think Pollen is applicable to distributed AI inference? I think it could work for realtlime Voice Agents running directly on mobile hardware.There are speech-to-speech LLMs that are big and do pure audio in audio out. But you can also make voice agents that use multiple smaller models cascadded. ASR for transcription, LLM for response text, TTS for speech, interrupt detection. If you try to load ASR, LLM, and TTS models that actually do a good job onto the same mobile device all at once, you can't get it to be realtime. But if you run them in a distributed setup, where each device has only one model loaded and streams its output to the next task device, you might achieve realtime performance while using stronger models for each task.Does this sound possible, or am I misunderstanding how Pollen works?

---

> **imcritic** · 2026-05-03T03:21:03.000Z　
> Splitting a big task (like anything ML-related) into a set of smaller ones and distribute them across the "fleet" of workers. Then reap the results, stitching it back into a single artifact at the end. This could be commercially viable. This could even become a p2p platform/market where some people basically buy computation while the others offer their hardware for temporary rent to earn a few bucks. You become the coordinator that just connects the demand with the supply and become rich from just commissions alone.

---

> **imcritic** · 2026-05-03T03:11:48.000Z　
> That's an interesting project, don't give up!P.s.: it's a shame that a rust lib for containers has a hardcoded path to sock file. That's weird.

---

> **sambigeara** · 2026-05-03T06:12:11.000Z　
> This is a cool idea!

---

> **sambigeara** · 2026-05-02T16:13:12.000Z　
> Ha, at a hand-wavey level, yes? Like you say, there's no IPv6 overlay, each node just exposes it's own primary UDP port which talks Pollen's mesh protocol. It uses a single QUIC transport, one QUIC connection per peer, and a combination of streams and datagrams for different bits serving both the control/data layers.I'd say "WASM-powered serverless functions" is a reasonable analogy, if your serverless functions maintained a minimal number of live replicas at any one point Also, of course, you're tied to the physical ceiling of the explicit hosts that are underpinning your cluster (N machines which are not dynamic like, say, lambdas are when they auto-provision to match demand).And yeah, you can also `pln serve` arbitrary services which are then exposed to the cluster, but it's worth mentioning that these will of course not benefit from the inherent, organic autoscaling and locality mechanisms that come with the WASM blobs. I only added it in as a feature so I could retire my (basic) Tailscale usage.Also, you can `pln seed` arbitrary blobs which can be `pln fetch`ed from other nodes. You can also `pln seed ./public my-site` a static webpage which you can reach from any node with `curl -H "Host: my-site" http://<node-addr>:8080/` (8080 being a configurable port).

---

> **onlyrealcuzzo** · 2026-05-02T19:54:48.000Z　
> I'm unaware of a better solution for local-first / offline-first software syncing (which IMO should be more common)!They're also great for collaborative text editing or if you're building a distributed database (not many people, but I'm in an adjacent field).At MASSIVE scale (inherently not many people), they're also good for things people take for granted, like counting (and other things people don't take for granted).Again, it's not clear to me exactly where and why Pollen helps in any of these scenarios.

---

> **sambigeara** · 2026-05-07T10:16:38.000Z　
> From a conceptual, workload-deployment perspective, I'd say yes--this is largely what I'm trying to achieve with Pollen. In fact I'd go so far as to say that it would be the recommended way of deploying workloads. Pollen's placement model responds better to single functions per seed rather than a single module with multiple, disparate functions, because you'd get a natural balancing of compute; heavy functions scale more aggressively, light functions less so.The wonder if the limiting factor would be _which_ models can actually be compiled into a reasonably sized WASM module (I'm not familiar with this right now--are you aware of efforts in this space?). If there are genuinely effective WASM models that fit into a reasonable sized modules, then it would fit nicely.All this with the previously acknowledged limitation that it's not yet on mobile (but perhaps a number of edge Pollen nodes could act as ingresses into the cluster in the interim).I'm super interested to hear how you might employ it though, if you did start experimenting. I'd be interested to learn where it's useful and where it falls short. Please feel free to hit me up on Github or by email (in my profile)!

---

> **sambigeara** · 2026-05-03T06:23:24.000Z　
> Absolutely! What's _really_ cool is that if you have disjoint computational steps that don't necessarily scale together linearly, you could split them into separately deployed `pln seeds` and let the cluster organically balance the compute as the different usage patterns occur. And yes, "p2p compute on demand" is certainly an intriguing idea.

---

> **kaoD** · 2026-05-03T00:23:01.000Z　
> And what's the public API/stdlib/bindings inside the WASM workers?I've been thinking a lot about this today and I think you might have a hidden gem here. Where can I reach you to talk more about this?Feel free to drop an email (address in my profile)

---

> **mitchsayre** · 2026-05-07T15:05:00.000Z　
> Just emailed you but I'll reply here as well in case anyone comes across this thread and finds it useful later.-TTS: I am actively working on this at Wfloat and just released a 30M param model with 20 voices, emotion, and intensity control that supports running on even legacy 2017 phones.
> -ASR: I think this is relatively in a good spot, the current ones small enough to fit on-device just mess up more at transcribing
> -LLM: For sure the main bottleneck. I know a bunch of people are working on this one. The problem with LLMs is just that they have to be so big to actually know how to do anything.

---

> **sambigeara** · 2026-05-03T07:26:26.000Z　
> Ha, thanks! I'll ping you an email.> And what's the public API/stdlib/bindings inside the WASM workers?Wazero (via Extism) carries the load here. As it stands, the runtime lifts three basic host functions into guest code which enable the RPC-like behaviour, injection of caller-context and basic logging[1], which are in turn referenced in the guest code like in the example[2].In the reverse direction, guest code exposes it's public APIs via build directives[3], which are handled by the runtime code[4].Figured that concrete examples might be more helpful here (I hope the formatting works).[1] https://github.com/Sambigeara/pollen/blob/567e85d5f1407932dd...
> [2] https://github.com/Sambigeara/pollen/blob/567e85d5f1407932dd...
> [3] https://github.com/Sambigeara/pollen/blob/567e85d5f1407932dd...
> [4] https://github.com/Sambigeara/pollen/blob/567e85d5f1407932dd...

## 导航

- 项目页：[[10-项目/github.com_ca43e137]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
