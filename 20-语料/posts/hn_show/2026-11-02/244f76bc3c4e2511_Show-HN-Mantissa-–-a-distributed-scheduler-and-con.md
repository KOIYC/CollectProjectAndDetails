---
type: "corpus"
item_id: "244f76bc3c4e2511"
title: "Show HN: Mantissa – a distributed scheduler and container orchestrator"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50326366"
project_url: "https://github.com/MantissaLabs/mantissa"
author: "abronan"
published_at: "2026-11-01T15:07:58Z"
captured_at: "2026-11-02T09:37:22+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-02"
pub_day: "2026-11-01"
tags:
  - 语料
  - hn_show
  - author_abronan
  - story_50326366
  - show_hn
metrics: {"points": 2, "comments": 3, "engagement_velocity": 2}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:3d"
---

# Show HN: Mantissa – a distributed scheduler and container orchestrator

> [!info] 一句话导读
> MantissaLabs/mantissa

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50326366>
> 指标：点赞=2 · 评论=3 · engagement_velocity=2
> 作者：abronan　|　发布：2026-11-01T15:07:58Z
> 项目链接：<https://github.com/MantissaLabs/mantissa>
> 采集：2026-11-02T09:37:22+08:00　|　id：`244f76bc3c4e2511`

## 正文

# MantissaLabs/mantissa

Distributed Workload Scheduling and Cluster Management

- Stars: 16
- Forks: 0
- Watchers: 16
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://mantissa.io
- Default branch: master
- Created: 2021-01-05T22:13:22Z

## Languages

- Cap'n Proto
- Rust
- Shell

## Topics

- containers
- crdt
- ebpf
- scheduler

## Top Contributors

- abronan (1203 contributions)

---

## README

---

Mantissa is a distributed orchestration system that grows with you and your workloads.
Every node participates equally in scheduling, state replication, and cluster membership.
No control-plane masters, and no federation layer required at scale. The focus of Mantissa
is convergence and auto-stabilization.

Built in Rust with Cap'n Proto RPC, CRDT replication, Merkle Search Trees over Redb, and
an eBPF driven data path, Mantissa targets low-latency scheduling and fault-tolerant
operation across small and large fleets of nodes alike.

## Why Mantissa?

Traditional workload orchestration systems often rely on a centralized control plane, which
could become a bottleneck and hard to maintain as the cluster grows. Mantissa explores an alternative
approach that leverages distributed scheduling with optimistic concurrency. It is similar to the
Omega scheduler in the
approach, but with the shared state being replicated via CRDTs.

The goal is to reduce the operational overhead and complexity, simplifying upgrades and maintenance
as well as aiming for a highly available and fault-tolerant system. This could be useful to scale
infrastructures and deploy a large number of AI agents for example.

## Status

**Experimental**. Do not use in production (_yet_).

Take this as a research-focused system, pushing the scalability limits of a completely distributed
control plane.

See the docs/limits.md for more details on the ongoing challenges and limitations.

## Highlights

- Fully distributed scheduling with resource reservation (no primary scheduler).
- Designed to scale to large fleets of nodes without a federation layer.
- Various workload types with their own lifecycles: _services_ (tasks), _jobs_ and _agents_.
- Batch placement, opt-in gang admission, and dependency-aware rollout for multi-task services.
- GPU-aware scheduling with device-level reservations (NVIDIA).
- eBPF-accelerated overlay networking for low-latency service discovery and routing.
- Durable state via CRDT + Merkle Search Tree (backed by Redb) for fault tolerance and convergence.
- Support for cluster split/merge operations (creating cluster views).
- Cluster dataplane encryption using Noise, vxlan traffic encrypted via wireguard.

## Local cluster experimentation (Dev Cluster)

1. Provision a local multi-VM cluster with Lima:

Install lima, clone the mantissa repository and navigate to the project directory, then:

```bash
./setup-dev-cluster.sh -n 3 -r $(pwd)
```

2. Open a shell into each VM with the repo as the working directory:

```bash
limactl shell --workdir /mantissa mantissa-1
```

Then build once on one of the VMs:

```bash
cargo build
```

3. Start the first node and grab its join token:

```bash
sudo mantissa init
mantissa token show
```

`mantissa init` prompts for the local master-key envelope passphrase when run
interactively. Non-interactive deployments should provide it through
`--master-key-passphrase-file` or `--master-key-passphrase-fd`.
Use `mantissa init --detach` to run the local daemon in the background; it
still prompts when attached to a terminal. Inspect it with `mantissa status`,
stream daemon logs with `mantissa logs -f`, and stop it with
`mantissa shutdown`.

4. Join a second node (replace ` ` and ` `):

```bash
sudo mantissa init
mantissa join --anchor <vm1-ip>:6578 --join-token <TOKEN>
```

5. Submit commands on the cluster (_from any node_) and try out the examples:

```bash
mantissa nodes list
mantissa services run examples/service_discovery_demo.ron
mantissa networks list
mantissa services list
mantissa tasks list
mantissa tasks logs <id-task>
```

6. Play around and bring nodes up/down (_see the rebalanced tasks, and the network/attachments healing_)

---

- See docs/quickstart.md for the full local and multi-VM workflow.

## Contributing

See CONTRIBUTING.md.

## 评论（3/3）

> **abronan** · 2026-11-01T15:10:15.000Z　
> Hello HN,I’m Alexandre, I have worked on Docker Swarm and the integration with distributed key value stores (etcd/consul/zookeeper), but also on Docker Swarmkit and the Raft distributed datastore, with the integration of etcd's Raft library.Last July, I open sourced Mantissa (https://mantissa.io): a fully distributed scheduler and container orchestrator. I did this quietly to keep working on patches and stability. It is still at an experimental stage and will probably stay that way for a while, but could be tested to get a "look and feel" of the project.Mantissa is using CRDTs[1] and Merkle Search Trees[2] for its data replication strategy (via anti-entropy/gossip). It is a bit of a departure from existing systems that are relying on strong consistency/linearizability (like Kubernetes, Swarm and Nomad): Mantissa focuses on fast convergence and self-stabilization instead. This comes with plenty of benefits (no quorum and Primary/Follower setup, simplified deployment and upgrades, etc.) but also trade-offs (increased storage size, no resource overcommit, temporary divergences in or outside of partition events, etc.) that would be too long to list and detail here.Mantissa is a particular fit for small clusters, home labs, agent orchestration but could also be used in larger settings (I’d be comfortable to say up to a hundred nodes per cluster view/shard, but I’m making no claims for higher than this, since I don’t yet have access to hardware that would allow me to test and make such a claim). At the core was the idea that it should be trivial to interconnect machines together and create a transparent overlay on top of the operating system, regardless of the scale.It is sort of a spiritual successor to Docker Swarmkit: going even further with simplification and reducing the deployment and maintenance burden. You'll see that it retains some of its design elements (with the node join flow) while taking inspiration from other systems like Google Omega[3].Why building Mantissa while Kubernetes and other systems exist? I think it is worthwhile to experiment with new approaches and see how it may impact existing systems. Improving on the UX/DX of schedulers and orchestrators has been a long obsession of mine and Mantissa is a long story, with its initial codebase and architecture being 10 years old. The scope is incredibly large however and working on this alone is quite difficult even with the help of LLMs. AI is a double-edged sword, and I could write a full article around my frustrations with building complex distributed systems with LLMs (they have a hard time “reasoning” correctly about systems relying on convergence for example).I’m having a lot of fun building this however and I hope this could be useful to some of you, despite its current limitations and experimental status. Feedback is also welcome to help steer the project in a direction where it could be the most useful/impactful to you.Cheers.Github: https://github.com/MantissaLabs/mantissa[1] https://www.lip6.fr/Marc.Shapiro/papers/RR-7687.pdf
> [2] https://inria.hal.science/hal-02303490/file/paper%20%281%29....
> [3] https://research.google/pubs/omega-flexible-scalable-schedul...

---

> **verdverm** · 2026-11-01T15:49:48.000Z　
> I would think eventual consistency would be a big problem for orchestration. I am not seeing how it makes sense, too many edge cases that would make it even harder to reason about fleets, versions, load balancing, and the like - and then make sure what you want is actually what the system has.I recall a google paper with a tl;dr like "distributed data; central control"

---

> **abronan** · 2026-11-01T17:04:00.000Z　
> It’s a fair concern, and Mantissa is really just moving the complexity around.One detail is that it relies on Strong Eventual Consistency, which is a slightly stronger model than Eventual Consistency. Replicas that have observed the same updates are guaranteed to converge to the same end state, regardless of the order in which those updates have been received.That said, convergence alone doesn’t guarantee scheduling correctness. This is why it separates convergence from scheduling coordination. The CRDTs and MSTs provide the replicated state, and the scheduling protocol handles placement decisions and conflicting operations (with atomic slot reservation that is node local). There is a reconciliation loop (owned by a single node that is picked for the service/workload to deploy) that is then responsible for bringing the cluster back to its desired state if it potentially made a wrong call.And it comes with trade-offs as mentioned in my post. You accept temporary divergences rather than requiring global agreement before every operation. This may or may not be acceptable for certain workloads. This removes the need for a quorum-based and centralized control plane, but it also means that certain invariants and guarantees have to be enforced at the scheduling and workload layer rather than by the datastore itself.Strong consistency is also not a silver bullet to handle distributed systems. It is relatively hard to get it right and not serve stale values because of the presence of bugs in the protocol or state corruption. It could also bring the availability down and prevent from scheduling any more tasks due to a loss of quorum (which is by design and acceptable in most cases).Mantissa is just making a different trade-off and accepting a different set of problems to solve: favoring availability and accepting that the desired state could shift temporarily on partition and network blips. If your cluster has good connectivity, then it should be a rare event, for which you should have prepared with some replicas that could handle being moved around. Again, it is not for everybody, and will probably remain a niche tool for users who want a simplified cluster deployment/updates to schedule mostly stateless tasks (even though stateful tasks are supported).One remaining comment: replicated volumes do use a Raft quorum per volume. There are things that couldn't accept anything weaker than strong consistency, and volumes are one of them. So we are using strong eventual consistency for most of the state replication, but fallback to Raft for things that truly require strong consistency.

## 关联链接

- https://mantissa.io

## 导航

- 项目页：[[10-项目/github.com_5e6f434a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
