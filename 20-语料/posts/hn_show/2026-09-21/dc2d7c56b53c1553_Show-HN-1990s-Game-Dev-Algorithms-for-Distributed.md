---
type: "corpus"
item_id: "dc2d7c56b53c1553"
title: "Show HN: 1990s Game Dev Algorithms for Distributed Systems"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47953717"
project_url: "https://docs.merca.earth/blog/1990s-game-dev-algorithms-distributed-systems"
author: "cremer"
published_at: "2026-04-29T19:59:12Z"
captured_at: "2026-09-21T02:52:33+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_cremer
  - story_47953717
  - show_hn
metrics: {"points": 12, "comments": 0, "engagement_velocity": 12}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: 1990s Game Dev Algorithms for Distributed Systems

> [!info] 一句话导读
> Skip to main content

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47953717>
> 指标：点赞=12 · 评论=0 · engagement_velocity=12
> 作者：cremer　|　发布：2026-04-29T19:59:12Z
> 项目链接：<https://docs.merca.earth/blog/1990s-game-dev-algorithms-distributed-systems>
> 采集：2026-09-21T02:52:33+08:00　|　id：`dc2d7c56b53c1553`

## 正文

Skip to main content
Basics Guide Economics Protocol Reference
 Blog Explore Map
Updates
 2026
 Floats Don't Agree With Themselves
 Paint First, Claim Later
 1990s Game Dev Algorithms for Distributed Systems
 merca.earth Is Live: What Works Today
 Contestability Is the Point: Why 'Always for Sale' Makes Claims Meaningful
1990s Game Dev Algorithms for Distributed Systems
 April 29, 2026 · 9 min read
 Gerardus Cremer
 Engineer
Imagine a global map simulation, a distributed land registry, or a radio frequency allocator. They all share one unbreakable rule: two people cannot own the exact same space. Polygons must not overlap.
Traditional GIS solved this decades ago. But doing it on-chain —inside a strictly consensus-driven network without external servers—has long been considered impossible. Compute limits were simply too strict.
I wrote Mercator , an open-source spatial indexing library for Sui. It lets you register polygons of any shape directly in a smart contract, mathematically guaranteeing zero overlap.
Registering a 4-vertex polygon in Mercator costs about $0.0065. Registering twenty polygons costs exactly the same. The system scales logarithmically, not linearly. To achieve this, I didn't invent anything new. I just borrowed algorithms from 1990s game engines: the Separating Axis Theorem (SAT) for collision detection, and the Morton Z-curve for indexing.
Why are these classic tools only becoming smart contract primitives now? The answer lies in data model architecture. This code simply will not run on EVM, Solana, or Aptos. Here is why.
Wait, Why Do This On-Chain at All? ​
The obvious question: why not just use Postgres and PostGIS?
If you trust a central authority to arbitrate boundaries, you absolutely should. A centralized database will always be faster. But if you are building a system that requires trustless ownership—like a decentralized frequency allocator, an autonomous world, or a censorship-resistant registry—the spatial guarantee must share the same security model as the ledger.
If your ownership record is on-chain, but your collision detection runs on a central server, the server administrator is the actual owner of the network. They can arbitrarily approve overlapping claims, destroying the asset's value.
Bringing the index on-chain also unlocks atomic composability. A third-party smart contract can dictate: "Execute this complex financial trade only if this exact 50-vertex polygon is successfully registered without overlapping existing claims." If the spatial check fails, the entire transaction rolls back. You cannot do that if the spatial state lives outside the virtual machine.
The Double-Claim Problem ​
When math gets too heavy, smart contracts usually offload it to external servers (oracles). This works for many tasks, but for spatial rights, it destroys atomicity.
Here is the state vulnerability:
Alice sends a transaction: "Register Polygon A."
The contract asks the oracle: "Is this space clear?"
While the oracle computes (an async delay of several blocks), Bob sends a transaction: "Register Polygon B," which overlaps A.
The oracle replies to Alice: "Clear." It then replies to Bob: "Clear" (Alice's polygon isn't saved in global state yet).
Result: Both Alice and Bob get rights to the exact same territory.
This is an inevitable flaw of asynchronous architecture. "Fast" oracles don't exist: a time gap of even a fraction of a second leaves a window for a race condition.
The only fix is to check for collisions and save the result in the exact same transaction , entirely on-chain. The geometry must be calculated inside the network's virtual machine.
The 1990s Classics: AABB, Quadtrees, and SAT ​
I ported three classic physics engine algorithms to the Move language. Together, they form a fast pipeline: filter out the noise for pennies, leaving heavy math only for actual collisions.
AABB (Axis-Aligned Bounding Box). The rough filter. We bound each polygon in a simple rectangle. If the rectangles don't intersect, the polygons don't either. This costs just four simple comparisons and eliminates 90%+ of candidates.
Quadtree with Morton Z-curve (1966). Map space is recursively divided into four quadrants. To store this tree in a flat hash table, I use a Morton curve: interleaving the bits of x and y coordinates into a single 64-bit integer. The magic here is that Mercator stores a polygon in exactly one cell —at the depth where it fits entirely inside one square. Insertion and deletion are O(1), regardless of the plot's size.
SAT (Separating Axis Theorem, 1996). The heavy artillery. Two convex polygons do not intersect if and only if you can draw a straight line between them. The algorithm checks axes perpendicular to the polygon edges. As soon as it finds a gap, it stops (early exit).
Crucial detail: All arithmetic in Mercator is integer-based. The Move VM does not support floating-point numbers. While painful for game physics, this is a salvation for distributed consensus. We get strictly deterministic results across all nodes. The on-chain math and the client-side math match bit-for-bit.
The Pipeline ​
The innovation isn't the algorithms themselves; it's the pipeline. A new registration passes through four filters:
Topology: Polygons must be convex, closed, and not pathologically stretched. Invalid shapes abort immediately.
The "Home" Cell: The algorithm calculates the AABB, traverses the quadtree, and finds the smallest cell that fully contains it. It computes the Morton key here—this is the polygon's address.
Broadphase: To avoid scanning the entire tree, a bitmask ( occupied_depths ) tracks which tree levels actually contain registered plots. The search skips empty space entirely.
Narrowphase: Finally, for the tiny handful of remaining candidates, SAT is deployed. The first detected overlap aborts the transaction.
For 99% of registrations, step 4 never executes. The AABB and quadtree filter out irrelevant plots instantly, saving compute resources.
Why This Breaks on EVM, Solana, and Aptos ​
If oracles are out, why not just write a quadtree in Solidity or Rust? Because every major platform kills this idea in its own way:
EVM (Ethereum): Transactions execute sequentially, and compute is extremely expensive. Running SAT on EVM hits gas limits immediately. ZK-proofs (proving SAT off-chain) take 5–30 seconds to generate—killing interactivity.
Solana: Two fatal blockers. First, Solana requires a static list of all memory cells (accounts) you will read before execution. But a quadtree traversal path is only known during execution. Static lists and dynamic trees are incompatible. Second, Solana has a hard limit of 1.4M CU per transaction. SAT for two 16-vertex polygons takes ~4.5M CU. You cannot optimize that away.
Aptos: Aptos uses Move, so you could store the tree in a table. The problem is concurrency. Block-STM executes transactions optimistically but rolls them back on memory conflicts. If Alice and Bob register plots on opposite ends of the map, Aptos still flags a conflict because they are writing to the same global registry table. Parallel registrations degrade into a slow sequential queue.
The root problem: none of these platforms support dynamic runtime access to independent objects without state conflicts.
Sui Architecture: Dynamic Objects ​
Sui solves this at the object model level. There are no "accounts with tables." Every quadtree node is a separate, independent object.
When a transaction calculates a Morton key, it accesses the required object on the fly—just like a program working with pointers in RAM. Parallelism follows automatically: plots in different quadrants touch different objects. Nodes process them in parallel with zero locks.
The collision check and database write happen in one transaction. Finality takes less than a second. Attackers have no time gap to exploit.
Gas Economics ​
Tests ran on the Sui Testnet. The minimum compute cost for any transaction on the platform is floored at 1,000,000 MIST.
Vertices Cost (MIST) In USD (at $0.93/SUI)
 4 7,045,496 ~$0.0065
 8 7,531,896 ~$0.0070
 16 8,504,696 ~$0.0079
 32 11,120,296 ~$0.0103
 64 20,481,496 ~$0.0190
Up to 16 vertices, the algorithm runs so fast it simply hits the platform's minimum compute threshold. Costs only rise for complex shapes (32–64 vertices) because SAT scales quadratically. The bulk of the total cost (about 6–7 million MIST) is actually storage, not math.
Fun fact: Register 20 square plots in different locations sequentially, and each transaction costs exactly 7,045,496 MIST. The tree does not degrade as it fills. A million objects on the other side of the continent won't slow down your transaction.
As a bonus, deleting a polygon triggers a storage rebate, refunding part of the gas. The net cost of a "register and delete" cycle is about $0.0019.
Engineering Constraints ​
This is not a silver bullet. The architecture dictates strict limits:
Convex Decomposition: SAT only works with convex polygons. The protocol supports complex plots (e.g., L-shapes), but registers them as arrays of convex parts. The client-side application must decompose complex polygons before sending the transaction.
DOS Limits: To prevent compute spam, the contract hardcodes strict limits: maximum 64 polygons per tree cell. Registering a 65th plot in an overcrowded square aborts with ECellOccupancyExceeded .
No Privacy: The spatial index is public. If you need to prove non-intersection while hiding coordinates, this approach fails. You would need ZK-proofs, inheriting all their speed compromises.
Flat Coordinate System: The library was built for Web Mercator, meaning the "earth" is flat. This works perfectly for city-sized plots, but projection distortions will break area calculations for polygons the size of Greenland. You can fork the library and use any other 2D coordinate grid (like game boards).
Source Code & Links ​
Mercator is open-source. Use it as an out-of-the-box spatial registry, or extract the standalone geometry modules ( polygon , sat , aabb ) to use independently of the quadtree.
GitHub: mercaearth/mercator
WASM Client: exact-poly — decomposes complex shapes into convex parts in the browser. It uses the exact same integer math as the smart contract, guaranteeing bit-for-bit identical results.
Live Demo (Mainnet): merca.earth — a spatial cadastre built on top of Mercator.
Questions, bug reports, and PRs are welcome in the repository.
Tags: technical
 sui-ecosystem
 mercator
Newer post
 Paint First, Claim Later
 Older post
 merca.earth Is Live: What Works Today
 Wait, Why Do This On-Chain at All?
 The Double-Claim Problem
 The 1990s Classics: AABB, Quadtrees, and SAT
 The Pipeline
 Why This Breaks on EVM, Solana, and Aptos
 Sui Architecture: Dynamic Objects
 Gas Economics
 Engineering Constraints
 Source Code & Links
Documentation
 Getting Started
 Key Concepts
 FAQ
Community
 Telegram
 X (Twitter)
More
 Blog
 App

## 导航

- 项目页：[[10-项目/docs.merca.earth_9fd2aa79]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
