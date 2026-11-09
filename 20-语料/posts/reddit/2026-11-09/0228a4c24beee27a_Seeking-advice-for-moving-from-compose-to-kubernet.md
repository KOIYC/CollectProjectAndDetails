---
type: "corpus"
item_id: "0228a4c24beee27a"
title: "Seeking advice for moving from compose to kubernetes"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xisbst/seeking_advice_for_moving_from_compose_to/"
author: "Dubmove"
published_at: "2026-10-30T02:39:25+08:00"
captured_at: "2026-11-09T09:41:26+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-09"
pub_day: "2026-10-30"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 15, "comments": 66, "upvote_ratio": 0.7586206896551724}
comments_count: 64
comments_total: 66
discovered_via: "reddit:14d+settle10"
---

# Seeking advice for moving from compose to kubernetes

> [!info] 一句话导读
> I think I am finally reaching the point where maintaining a growing docker compose file takes more time than the simplicity of it saved me in the beginning of m…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xisbst/seeking_advice_for_moving_from_compose_to/>
> 指标：得分=15 · 评论=66 · 赞踩比=0.7586206896551724
> 作者：Dubmove　|　发布：2026-10-30T02:39:25+08:00
> 项目链接：—
> 采集：2026-11-09T09:41:26+08:00　|　id：`0228a4c24beee27a`

## 正文

I think I am finally reaching the point where maintaining a growing docker compose file takes more time than the simplicity of it saved me in the beginning of my self-hosting journey. Migrating to Kubernetes should be the logical next step for me. However, I am a bit overwhelmed with all the advice and best practice guides I found online.

From what I've read k8s isn't really worth the overhead, and k3s would be the most popular alternative. But then there is also k0s which should be as good but it's barely used? Since I know nothing about running a Kubernetes cluster it is hard to decide on the best fit for me. Also I was not aware that these Kubernetes pods seem to run docker containers which is of course good for me on the one hand as migration should be easy then but that does raise the question for me then what are helm charts then for. I thought they are to a Kubernetes cluster what a docker-image is to a docker runtime, but according to the docs they are more like a config file for dependency resolution? And then there is also the question whether it would make sense to install Kubernetes directly on my host machine or whether I run it in a docker container. Since I don't really know what I am doing here, setting it all up in a nice deposable container sounds like a great idea, but that would defeat my goal of moving on from a docker setup. Also there is the choice between directly running rancher/k3s or running k3d...

I am also a bit unsure on how I should actually approach local experiments on my laptop. Online, some people suggested microk8s, other suggested minikube, chatgpt also mentioned kind.

So if anyone has some opinion on which approach I should try I would be happy to listen! What I basically want is whatever helps me spending as little time as necessary on maintaining the cluster itself while ideally also being lightway. I don't have a problem with spending extra time on setting everything up if that means everything will just run once it runs. One of the big features is replication but I am honestly more interested in saving time on maintaining the infrastructure. So maybe my main concern isn't that much the Kubernetes runtime but instead adding the right sidecars/plugins/etc, but if that is the case then I especially don't even know what I am looking for. Thanks in advance.

## 评论（64/66）

> **asimovs-auditor**（1 分） · 2026-10-30T02:39:35+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **Dubmove**（1 分） · 2026-10-30T02:41:11+08:00　
> No AI - I mentioned Chatgpt in it as I asked it for advice before I came here but the post itself has been written by me.

---

> **clintkev251**（14 分） · 2026-10-30T02:46:25+08:00　
> Kubernetes is a container orchestrator. Those containers are derived from the same container images that you use to run your docker containers now, and orchestrated as part of a pod, which can contain one or more containers and is the smallest unit of work in k8s.
>
> Helm is effectively a tempting tool that can make it easier to deploy groups of dependent resources consistently. It is in no way required (and I wouldn’t recommend starting with it) but it can make some more complex stacks easier to work with.
>
> Personally, my favorite way to run Kubernetes is through Talos

---

> **RevolutionaryElk7446**（2 分） · 2026-10-30T02:50:34+08:00　
> I run K8S RKE2, but really it's definitely more overhead than compose but allows for easier automation to be created to drive it.
>
> If you can setup the automation, it does become easier than compose, but getting there is a different story if you haven't done Kubernetes administration before. I'd recommend running some small dev k8s systems alongside your docker stuff if you can.

---

> **No_Kangaroo_3618**（3 分） · 2026-10-30T02:53:37+08:00　
> I’m not running Kubernetes in my home lab, but having used it at work, I would look into GitOps, which may make it easier to manage everything and deploy apps and updates, regardless of sticking with Docker or going to Kubernetes. This really is where you’ll spend much less time on the host and more time just pushing config updates. Look at Komodo for Docker or ArgoCD for Kubernetes. You won’t believe how much time you’ll save and how much less tinkering you’ll do.
>
> A lightweight version of Kubernetes is called k3s, it’s pretty easy to deploy and will work for 1 node or many.
>
> I will say that Kubernetes has a huge learning curve, so definitely expect to spend lots of time up front setting things up. Learning to debug it properly can also be a challenge, so don’t be afraid to ask an LLM.

---

> **Dubmove**（0 分） · 2026-10-30T02:54:27+08:00　
> And Talos itself I would want to run in a docker container for example?

---

> **clintkev251**（5 分） · 2026-10-30T02:56:23+08:00　
> No, Talos is an OS. I’m talking about for a full-fledged environment, not for local desktop experimentation

---

> **Kimcha87**（2 分） · 2026-10-30T02:57:50+08:00　
> I’ve been going through the same process.
>
> First of all, I think it’s totally worth it and very satisfying. But it is a lot of new stuff to learn.
>
> I can’t recommend k3s. It has some kind of issues with metric scraping that causes high IO load and other people seem to have the same issue.
>
> I am using Kubernetes in the cloud right now. So I don’t have a recommendation for bare metal. Talos is probably what I’m going to try next in my homelab.
>
> What I strongly recommend is using gitops with fluxcd. That’s the most important thing that makes the switch worthwhile if you don’t need high availability.
>
> I also recommend to set up linting of the manifests early on. You can use flate to render fluxcd kustomizations and helm charts into plain Kubernetes manifests and then run polaris, kube-linter and deadvalues against them. This helps to ensure your agents are following best practices.
>
> Next, I recommend setting up renovate to automatically create PRs whenever apps have updates available. Have CI and an agent run your linters against these PRs to evaluate the update risk and then merge. Your cluster will then install the update and if something goes wrong you will get notifications (if you have monitoring set up).
>
> With all the vulns being discovered nowadays, this will make it much easier to keep it all updated.
>
> Edit:
> You may also be interested in this comment where I shared some more tips:
>
> https://www.reddit.com/r/selfhosted/s/4fIn9WuaXA

---

> **Angelsomething**（2 分） · 2026-10-30T03:01:52+08:00　
> have you considered a docker manager like  or dockge? personally, my whole homelab is IAC running off my local git instance. I use k8s at work and i can’t ever imagining bringing that complexity at home. also from what you said, it’s unclear what hardware you have? k8s needs 3 masters and 2 workers so 5 hosts; k3s should be fine with 1 master and 2 worker host. if you’re running everything from your laptop, you don’t need kubernetes at all, but learn to work off of your git files.

---

> **StewedAngelSkins**（1 分） · 2026-10-30T03:02:12+08:00　
> k3s is convenient because it comes with certain things preconfigured that you'd have to dp yourself with kubelet. i would recommend it.
>
> helm charts are sort of comparable to docker compose files in the sense that they template out the configuration of the networking and volumes and such in addition to the containers. remember kubernetes has stuff like automatically configured proxies and dns and load balancing and such. this is all configured with a ton of individual yaml files, but a helm chart provides a kind of "meta-config" to tie it together. you will probably want something like argocd to manage this config and handle deploying it from a git repo. you can do it manually but it's less convenient.

---

> **cookingmonster**（98 分） · 2026-10-30T03:03:55+08:00　
> If maintaining compose files is where you draw the line then Kubernetes is _not_ the next logical step. You'll have more files to maintain, just in a different format.

---

> **mbecks**（53 分） · 2026-10-30T03:11:52+08:00　
> Op is basically saying “I’m tired of how hot this sauna is, so I’m considering getting in an oven instead, what’s the best way to climb into the oven?” It makes no sense haha

---

> **GenerouslyFrothy**（1 分） · 2026-10-30T03:12:56+08:00　
> If you're already eyeing k3s and just want something that runs itself once it's set up, Talos is a pretty good call. cuts out all the OS-level cruft, no SSH, no package manager to babysit. the api-driven design feels weird at first but it's refreshing once you stop fighting it. only downside is you really gotta commit to the "machine as an appliance" mindset, can't just pop in and apt-get something like you're used to

---

> **Only-Stable3973**（1 分） · 2026-10-30T03:15:54+08:00　
> I'm using k3s I am running it in vert-manager to play with and you can set it up using master and just one worker or two if you want I used ai to help with the setup, it's a good way to learn. I already have treefik installed so I disabled traefik and route it through my existing traefik proxy and use the config.yml to add the routes...works great.

---

> **techw1z**（7 分） · 2026-10-30T03:18:24+08:00　
> your first paragraph makes it sound like you put all your containers and services into a single compose file?
>
> if that's the case, the logical next step would be to move to split them up.
>
> the next step after that would be to move to portainer stacks and move all compose files to something like gitea and practice CI/CD.
>
> then add a second portainer node.
>
> if there is still something you cant do after that, only then look into kubernetes.
>
> k0s only makes sense if you want to familiarize yourself with kubernetes tooling without actually running a proper kubernetes env, otherwise its kinda stupid since the main point of it is having multiple nodes.
>
> also note that many k8s tools can be substituted by portainer + ansible

---

> **sakebi42**（1 分） · 2026-10-30T03:23:24+08:00　
> Just use Talos

---

> **gscjj**（6 分） · 2026-10-30T03:31:45+08:00　
> Significantly more files but GitOps makes it more manageable

---

> **coderstephen**（102 分） · 2026-10-30T03:35:13+08:00　
> I run Kubernetes at home. Maybe I can help.
>
> > I think I am finally reaching the point where maintaining a growing docker compose file takes more time than the simplicity of it saved me in the beginning of my self-hosting journey. Migrating to Kubernetes should be the logical next step for me.
>
> Config management is the #1 selling point of Kubernetes for me, so I get it. I like that basically my entire homelab can be a bunch of organized, individual YAML files in a Git repo that I can apply to my cluster (or, a brand-new cluster if the old one is beyond repair). Boom, entire homelab deployed.
>
> Docker Compose gives you _some_ of that, but Kubernetes goes way further on just about everything.
>
> > However, I am a bit overwhelmed with all the advice and best practice guides I found online.
>
> Kubernetes is the most popular container orchestration tool in the world, so yeah there's an overwhelming number of articles out there. And a lot of them don't have the small homelabber in mind primarily so it can be confusing
>
> > From what I've read k8s isn't really worth the overhead, and k3s would be the most popular alternative.
>
> Terminology:
>
> - _k8s_ is just an abbreviation for _Kubernetes_
> - _k3s_ is a specific distribution of k8s
>
> See, the Kubernetes project is slightly weird, in that it isn't one specific program like Docker is. Rather, its a collection of small individual programs that they expect _you_ to assemble yourself. Which most people don't really want to do, so usually you pick a _distribution_ of k8s that does that for you. I guess its kinda like Linux distributions in a way. You could take Linux kernel and a bunch of tools and build your operating system, but most people just choose a distribution where people did that for you.
>
> So k3s is a pretty popular distribution of k8s in the homelab, because it packages things into a single binary that is basically just as easy to run as Docker. It is missing a couple of fancy features that k8s is capable of, but you probably don't care about those.
>
> > But then there is also k0s which should be as good but it's barely used?
>
> k0s is another distribution of k8s. I don't recall it ever picking up a ton of steam. k3s is kinda the favored popular one so I might stick with that.
>
> > Also I was not aware that these Kubernetes pods seem to run docker containers which is of course good for me on the one hand as migration should be easy then
>
> Yep, k8s is just a different way of running containers than Docker. If you squint, k8s a kind of like a competitor to Docker.
>
> Technically k8s doesn't actually use Docker by default (although it can, see the [supported container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)) but all of them are fully or nearly-fully feature-for-feature the same as Docker in terms of containers. I guess you could say it is similar to the Docker/Podman comparison.
>
> > but that does raise the question for me then what are helm charts then for.
>
> OK, so Helm is something a little different that doesn't really have an equivalent in Docker. You know how with Docker Compose, you can download people's Compose files provided by an app developer instead of writing your own? Sometimes you want to do this because an app actually requires several containers running together to work, or the config is just kinda complicated and you don't want to deal with it?
>
> Well Helm is basically a _package manager_ for shared configuration files. People can bundle up one or more config files that are needed for running an application, and then publish them as a _Helm chart_. Then you as the consumer can just say "install this Helm chart" and instead of copy-pasting configs, it will pull the latest configs published by the developer and run them.
>
> > And then there is also the question whether it would make sense to install Kubernetes directly on my host machine or whether I run it in a docker container.
>
> Please don't do that, you'll just run into issues later. Don't run containers inside of containers...
>
> >  I am also a bit unsure on how I should actually approach local experiments on my laptop. Online, some people suggested microk8s, other suggested minikube, chatgpt also mentioned kind.
>
> Virtual machine is the safest bet to just try it out. But I would actually just install k3s directly onto your machine. Its pretty small and self-contained, and it doesn't touch anything else on your system unless you ask it to.
>
> Don't use microk8s, I've had bad experiences with it. (It is also another distribution of k8s if you did not know.)
>
> ---
>
> > So if anyone has some opinion on which approach I should try I would be happy to listen!
>
> If you want to just dip your toes into k8s, I would install k3s and play around with it before deciding what to do next or committing to anything.
>
> If you decide to move everything to k8s, you can stick with k3s. Or you might try [Talos Linux](https://www.siderolabs.com/talos-linux) which is what I use. It is also another distribution of k8s, but what makes it different is it is _also_ a Linux distribution! Its great if you want to go 100% k8s. But I would say k3s is slightly easier to set up and requires much less commitment.

---

> **miramichier_d**（-2 分） · 2026-10-30T03:37:09+08:00　
> I wouldn't touch Kubernetes unless there was big money at stake for whatever I intend to run on it. It's complete overkill for just about any homelab environment.

---

> **clintkev251**（6 分） · 2026-10-30T03:39:10+08:00　
> If you're already running a ton of services across multiple hosts, Kubernetes can actually reduce complexity if you know what you're doing, but it's not for everyone.

---

> **chevdor**（0 分） · 2026-10-30T03:40:57+08:00　
> Take your machine(s) install Talos. Done.

---

> **coderstephen**（12 分） · 2026-10-30T03:43:41+08:00　
> That's important, if you don't like a bunch of config files, then you'll hate Kubernetes. The number of lines of YAML you have will triple going from Docker Compose to Kubernetes.
>
> _But..._ arguably your config files will be a little easier to read, more explicit in what they are doing, and also more things that you used to just "assume" about the machine are now codified in your config files directly.

---

> **miramichier_d**（3 分） · 2026-10-30T03:48:02+08:00　
> I kind of disagree. Kubernetes represents a net increase in complexity. There's complexity of installation, complexity of configuration, complexity of observability, and complexity of potential problems. Not saying that no one should use it, and the right person can use it quite effectively, but it's not correct to say that it specifically reduces complexity. The question in using Kubernetes is whether that complexity is worth what it delivers or not.

---

> **AdInner239**（1 分） · 2026-10-30T03:50:30+08:00　
> AI makes running an Kubernetes gitops system really trivial. Yes you burn a bit more resources on idle. But once its running its more or less bulletproof

---

> **clintkev251**（5 分） · 2026-10-30T03:51:47+08:00　
> The initial configuration complexity is high, but that's a trade-off for lowering ongoing maintenance complexity. (and I'd say those first two issues, complexity of installation and complexity of configuration, can be really easily mitigated by using things like Talos or k3s)

---

> **Luolong**（-1 分） · 2026-10-30T04:20:01+08:00　
> Underrated comment.
> Come on guys, vote it up!

---

> **sshwifty**（8 分） · 2026-10-30T04:27:54+08:00　
> *does it though?*

---

> **Luolong**（2 分） · 2026-10-30T04:33:21+08:00　
> I liked the [coderstephen’s](https://www.reddit.com/r/selfhosted/s/XH8SI4jXKN) comment but I would like to add one more recommendation.
>
> Once you’ve familiarised yourself with k8s concepts, you would want to keep the entirety of your configuration in a Git Repo.
>
> This way, if you ever need to nuke your server and rebuild it from scratch, you could simply apply the entire config from the repo and be back running in a matter of minutes.
>
> Taking that one step further, make k8s pull latest changes from your Git repo and apply them automatically as it detects a change. This is called GitOps.
>
> I personally like FluxCD for its relative simplicity.
> ArgoCD is another popular option and it has a nice dashboard, so many people like that.

---

> **DistractionHere**（2 分） · 2026-10-30T04:58:45+08:00　
> I would look into TechnoTim's content surrounding Kubernetes to get your toes wet. Rancher running as a Docker Compose stack with some VMs or bare metal hosts for nodes would be a good place to start.

---

> **Dubmove**（1 分） · 2026-10-30T05:31:04+08:00　
> I don't have a problem with "too" config files. What I have a problem with is that atm I have like 35 containers across 4 different compose files wherein 1/3 have either some kind of manual entrypoint because their standard entrypoint is not configurable enough with env vars alone (most commonly the service wouldn't read secrets from files which means I have to monkeypatch that behavior if I want to actually have version control for my hit files) or I have a custom Dockerfile and staying on the latest version becomes too much of a hassle. In addition, I got interested in a sandboxing project that could work with docker containers but would be much more idiomatic with kubernetes.

---

> **Dubmove**（5 分） · 2026-10-30T05:55:27+08:00　
> Thank you so much for this comment. You took the time to address every single point and I appreciate that 🙏
>
> There is one question I have though: Another comment also mentioned Talos. During my research I came across that name but didn't really look into it beyond acknowledging that it's a custom Linux distro specifically designed for running a kubernetes cluster. I asked that redditor whether running Talos in a container would be a good idea and he just told me not to do that. You also begged to not run containers inside other containers.
>
> I understand that every container is an additional layer of abstraction but considering how docker actually maps kernel space capabilities I would consider it an almost zero-cost abstraction for any practical purposes assuming I'd use the standard runc runtime. So my question is whether the advice against a dockerized Talos just boils down to an unnecessary containerization layer is "a bit icky" or whether I am overlooking something important? Because at least for now I'd happily trade a clean reproducible environment against a few extra dozens of megabytes in overhead and a few milliseconds in speed.

---

> **Myzzreal**（2 分） · 2026-10-30T06:20:02+08:00　
> I use k8s and I love it but there is a ton of stuff to learn if you're new to this. My repo is public, maybe it will help: [https://github.com/rskupnik/ether/tree/master](https://github.com/rskupnik/ether/tree/master)

---

> **GolemancerVekk**（13 分） · 2026-10-30T06:23:47+08:00　
> I don't think Kubernetes will help with badly made images...

---

> **coderstephen**（6 分） · 2026-10-30T06:28:17+08:00　
> > I asked that redditor whether running Talos in a container would be a good idea and he just told me not to do that.
>
> It's not that you _shouldn't_ do that, you _can't_ do that. You can't run Windows 11 in a container, for example. Just not possible.
>
> > I understand that every container is an additional layer of abstraction but considering how docker actually maps kernel space capabilities I would consider it an almost zero-cost abstraction for any practical purposes assuming I'd use the standard runc runtime.
>
> The issue is permissions. Containers restrict what processes inside the container are allowed to do. But _running a container_ itself requires certain permissions to even do that. You can work around this somewhat but it can get messy.
>
> Docker, for example, usually requires root to run. But its usually a bad idea to allow a container to run as root. But if you were running Docker inside another Docker container, you'd _have_ to do that, because the Docker engine requires root. And sometimes you don't even notice that certain features of Docker still don't work because the outer Docker is taking away a `PCAP` that the inner Docker needs just for certain operations, etc.
>
> It's just really messy in my opinion, and likely to lead to weird behaviors down the road that are really hard to diagnose.
>
> > So my question is whether the advice against a dockerized Talos just boils down to an unnecessary containerization layer is "a bit icky" or whether I am overlooking something important? Because at least for now I'd happily trade a clean reproducible environment against a few extra dozens of megabytes in overhead and a few milliseconds in speed.
>
> Going back to Talos its because Talos is an operating system that tightly integrates the kernel and other features. So it can't be run in a container.

---

> **coderstephen**（1 分） · 2026-10-30T06:31:07+08:00　
> I mean sometimes it can using `init` containers.

---

> **Celestial_User**（3 分） · 2026-10-30T06:41:11+08:00　
> You can do init containers with docker too

---

> **jfugginrod**（2 分） · 2026-10-30T09:28:31+08:00　
> I have no idea how my kubernetes server runs, but it does work

---

> **Bright_Mobile_7400**（1 分） · 2026-10-30T09:43:34+08:00　
> It simplified my setup drastically on my side.
> It required a ""significant"" amount of work to get there, but it definitely much simpler to manage once that setup is done.
>
> But still agrees with you. I think the ball is somewhere in the middle. It makes the setup simpler once it works, but getting there is not a simple step.

---

> **sagacious123**（3 分） · 2026-10-30T12:04:27+08:00　
> Don't pick a distro yet. Run Kubernetes locally in Docker with k3d or kind to learn the objects: Deployments, Services, Ingress. Helm charts are not like Docker images; they are packages of Kubernetes manifests with templating, so you deploy a chart, not a container. For self-hosting, k3s on a host is fine for a single node and easier than k0s; k0s is solid but has a smaller community. Once you understand how your compose services map to Deployments and Services, migrating is mostly writing charts.
>
> Practice that migration on SnowOps Labs (free, open source: [https://github.com/sagar2395/snowopslabs](https://github.com/sagar2395/snowopslabs)). It sets up a real cluster locally with `labctl init`, then run `labctl scenario up gitops-cicd` to deploy apps with Helm and GitOps, and `labctl incident inject service-selector-broken` to debug a broken Service. It runs on your laptop.
>
> Disclosure: I'm part of the team behind it.

---

> **Red-And-White-Smurf**（4 分） · 2026-10-30T13:34:24+08:00　
> It sounds like you have all your Docker services in one big Docker compose file. If that's the case, you should look into splitting the different related services into seperate folders with their own Docker compose file. That will make it much more simple to maintain.

---

> **snekk420**（3 分） · 2026-10-30T13:43:25+08:00　
> Just want to comment om microk8s, if you happen to run Ubuntu server i think its a valid choice, i have been running it for years in my cluster. It also have ”plugins” you can just install such as gpu, rbac, traefik, portainer support etc.
>
> I have had some issues with app armor and microk8s once but that is pretty much it. It works well
>
> So it has been very easy to setup gpu passthrough to my containers. They even share the gpu. Its not locked to one container

---

> **Expensive-Sock-7876**（1 分） · 2026-10-30T13:49:29+08:00　
> Prepare for a world of pain

---

> **AdUnfair9248**（1 分） · 2026-10-30T13:59:49+08:00　
> Do. Not. Fuck. With. Kubernetes.

---

> **neoKushan**（11 分） · 2026-10-30T18:27:33+08:00　
> If your reason for switching to k8s (or k3s) is you think it'll be simpler and easier than docker, you're going to have a bad time.
>
> Don't do it for that reason alone. There's things you can do (like splitting your compose files out) to make docker far easier to manage, kubernetes is a whole other barrel of complexity.

---

> **Dubmove**（1 分） · 2026-10-30T18:36:08+08:00　
> Yeah Docker-in-docker shenanigans are annoying. I already have learned that lesson the hard way. That's actually part of the reason why I want to move on from my current setup because one of my services needs to spawn sandboxes and I experimented with docker proxies and other solutions + running my sandbox containers with gvisor instead of runc. It kinda gets the job done but leads to new problems because since these new containers aren't defined in my compose files, compose can't see them and I'd have to handle the lifetime more or less manually. Theoretically it's all doable in a perfectly safe way with custom runtimes, docker proxies and daemons but it would mean adding a lot of complexity and moving parts which would come out of the box with Kubernetes.
>
> >Going back to Talos its because Talos is an operating system that tightly integrates the kernel and other features. So it can't be run in a container.
>
> Unless we are talking about different thngs here, there is an official image by Sidero Labs: [https://github.com/siderolabs/talos/pkgs/container/talos](https://github.com/siderolabs/talos/pkgs/container/talos)

---

> **Dubmove**（0 分） · 2026-10-30T18:44:25+08:00　
> These images aren't badly made per se. It's just that sometimes upstream wouldn't release a latest-tag and versions are always pinned. Or they packaged a service with default build options but I would like to change some of these.
>
> Also some service wouldn't come with Oauth-support and I wrote a custom oauth2-proxy image for them so my reverse proxy would send the user first to my Oauth2 provider

---

> **Dubmove**（1 分） · 2026-10-30T18:57:18+08:00　
> >your first paragraph makes it sound like you put all your containers and services into a single compose file?
> if that's the case, the logical next step would be to move to split them up.
>
> I already did split them up.
>
> >he next step after that would be to move to portainer stacks and move all compose files to something like gitea and practice CI/CD.
> then add a second portainer node.
>
> I don't know it but with news like that I declne: [https://linuxnews.de/portainer-3-0-community-edition-bleibt-bei-version-2-x/](https://linuxnews.de/portainer-3-0-community-edition-bleibt-bei-version-2-x/)
>
> >k0s only makes sense if you want to familiarize yourself with kubernetes tooling without actually running a proper kubernetes env, otherwise its kinda stupid since the main point of it is having multiple nodes.
>
> Can you explain that point? Isn't K0s a minimal but fully functional Kubernetes runtime?

---

> **Dubmove**（1 分） · 2026-10-30T19:10:32+08:00　
> Many valuable recommendations, thank I will check them out.
>
> Regarding the high IO load of k3s, are you basically talking about etcd? I think I came across mentionings like that in the docs when I researched k3s: [https://docs.k3s.io/datastore/ha-embedded](https://docs.k3s.io/datastore/ha-embedded) \- I saw it being mentioned but assumed it's less of a problem if I only have 1 replicate and a fast ssd.

---

> **Dubmove**（1 分） · 2026-10-30T19:16:03+08:00　
> Thanks, I'll check it out.

---

> **Dubmove**（2 分） · 2026-10-30T19:22:13+08:00　
> That's an awesome project!

---

> **Dubmove**（4 分） · 2026-10-30T19:22:58+08:00　
> I will fuck with Kubernetes.

---

> **Kimcha87**（1 分） · 2026-10-30T22:10:57+08:00　
> No, I don’t think that is the issue. I’m using it on a super fast NVME ssd and I only have one node. In that configuration I think it’s using SQLite.
>
> I tried to look but haven’t been able to find some of the GitHub issues showing the same.
>
> My problem was that once I installed a metric scraper, the cluster started reading from the ssd at like 1gb/s constantly. Which led to my ssd overheating and throttling, which led to the Kubernetes api server dying.
>
> I think due to the thermal constraints of my ssd the issue is more severe and pronounced.
>
> But either way, I don’t think there be a constant stream of such large reads there.
>
> Anyways, the beauty is you can still try k3s and see if it’s fine for you. As long as you practice gitops and use something like velero for backups, you can just restore the whole cluster on another distribution.
>
> However, the value of k3s is pretty limited in this setting. You get a bit lower ram and cpu usage because you don’t use etcd and a few pre-installed infrastructure pieces like traefik.
>
> But if you do gitops, you would probably still want to install them yourselves to easily customize their settings.
>
> And it’s really easy to add those services.
>
> So, I don’t think there is much value of using k3s over something like k0s or talos.
>
> For talos there is a trade off. You can’t ssh into the node to poke around when you have issues or if you want to use host mounts. I think you also need to give an entire ssd to talos and can’t just partition it.
>
> But you can solve this by using proxmox and then spin up a VM for talos.

---

> **techw1z**（1 分） · 2026-10-30T22:57:53+08:00　
> portainer offers a free business edition license for up to 3 nodes
>
> most homelabbers use this and use the business edition of portainer
>
> community edition is limited anyway and makes proper CI/CD hard
>
> there are also alternatives like podman but portainer is just better and learning portainer also improves job prospects.
>
> k3s is also full functional but IMO its just not proper kubernetes.
>
> if you scale kubernetes to many nodes I guess it makes sense for it to have more overhead than docker, but running kubernetes on a single host will keep the same overhead making it incredibly inefficient. the only thing worse than k0s in terms of efficiency would be openstack on a single node.
>
> IMO, k3s and k0s are just for testing and learning but shouldn't be used to run your entire homelab.

---

> **coderstephen**（1 分） · 2026-10-30T23:52:35+08:00　
> Huh, I guess they provide a container version now... TIL. But its not going to be the same thing as the full OS most likely.

---

> **coderstephen**（1 分） · 2026-10-30T23:56:45+08:00　
> You do you, but my 2 cents on microk8s is
>
> - its tied to snap, which, eww
> - its tied to Canonical, which, eww
> - I've had multiple occurrences where upgrading microk8s corrupted etcd, and that was just on a single node
> - certain things like node ports worked weird and in a not-very-standard way last time I used it which was annoying to deal with
> - I had multiple times where the OCI image cleanup didn't work and it filled up the disk with old image tags

---

> **Hostman_com**（1 分） · 2026-10-31T00:33:58+08:00　
> If the main goal is less maintenance, try splitting that big Compose file into smaller stacks before committing to Kubernetes. That may solve some of the pain without adding a cluster to look after.
>
> If you still want to explore Kubernetes, take one app through deployment, an update and a rollback in a local test cluster. Getting it running once won’t tell you much about the ongoing upkeep.

---

> **asinglenoob**（1 分） · 2026-10-31T03:37:45+08:00　
> I just finished shutting down the last of my Proxmox nodes and running everything in k3s. My journey went something like this: started with Docker on NAS but wanted more power so moved to Proxmox on mini PC. Ran a few VMs and LXC container instances there for a while. Then decided using Portainer was too much GUI work and too difficult to reproduce results so I moved to running a k3s VM. Ended up adding more Proxmox hosts running k3s VMs to get multiple nodes and eventually HA k3s.
>
> The initial climb on learning and breaking stuff is real. But I can now go from wanting to try a new service and having a full deployment complete with valid certs and DNS in like 5 minutes for an existing chart / container image. There’s an additive effect where the more you put in the cluster the more benefit you see. For instance, need to shut a node down for maintenance? All those workloads transition automatically (assuming overhead in hardware etc.). You can have basically zero downtime homelab changes.
>
> I finally moved over Home Assistant which I was least confident in because it really required a dedicated NIC and IP but after that I migrated (live) from a multi node Proxmox setup to just k3s running on Debian. Entire infrastructure is now in gitops and I’m dealing with less complexity and mess than when I was running Docker compose and Portainer stuff. But the major caveat there is it took over a year for the entire transition. And I use k8s at work so had some existing experience.
>
> I would start with gitops if you want to go down this path and manage the entire cluster through that. I would use k3s, it’s well supported and I’ve not had any issues with it. I would use Longhorn for storage. Do it in a VM first till you get comfortable, if you run multiple nodes (I think this only makes sense in that scenario) you can get HA up and running and move over to just k3s on Linux nodes in the future to reduce the layers when you are confident in it. Many Linux distros work fine for node OS, I use Debian mainly because it’s simple and stable out of the box.

---

> **812046**（1 分） · 2026-10-31T04:28:33+08:00　
> before you jump in, how many services are you actually running and is this a single machine? because if its like 15-20 containers on one box, splitting your compose into multiple files with shared networks might solve the maintenance pain without the kubernetes learning curve

---

> **AdUnfair9248**（1 分） · 2026-10-31T09:11:20+08:00　
> Fine, but you'd better wear TWO condoms.

---

> **Subject_Bat2225**（1 分） · 2026-10-31T21:14:18+08:00　
> Exactly, Kubernetes would probably add even more maintenance here. It solves different problems than just wanting fewer config files

---

> **beje_ro**（2 分） · 2026-10-31T23:17:50+08:00　
> You can try to reorganize this. This is how I also started and grew, and grew. Now I am moving to a 1 config file per service which should kake everything more manageable.
>
> I also consider moving these files to a git repository and then just setup an agent to follow the updates and to bump ke whenever an update or an action is necessary.

---

> **rightiousnoob**（1 分） · 2026-11-01T21:27:27+08:00　
> As others have mentioned, it sounds like maybe all you need is to isolate compose files.
> I have a compose for each app I'm running and that each gets its own subfolder.
> The parent level then contains a 'master' compose that just does a bunch of includes. This allows me to keep things isolated, while still being able to manage them all from the root folder context.
>
>  Something like this:
>
> ```
> ---
> Include:
>   - path: ./diun/compose.yaml
>     project_directort: ./diun
>     env_file:
>       - .env
>       - ./diun/.env
> ```

---

> **No_Cattle_9565**（4 分） · 2026-11-01T22:24:56+08:00　
> Nothing in kubernetes changes that

---

> **Current-Secretary-52**（1 分） · 2026-11-05T03:44:08+08:00　
> A few of your questions have short answers, so taking them in order.
>
> Helm charts. Your pods run container images, same images you use in compose. A Helm chart is a templated bundle of the Kubernetes YAML that runs an app (Deployment, Service, volumes, ingress), plus a values file for the parts you change. Closer to a compose file with variables than to an image. You can skip Helm entirely at first and write plain YAML for your own apps.
>
> Host or container. Install it on the host. Running Kubernetes inside Docker is great for throwaway tests, and that's what kind and k3d are for, but for the thing you self-host you want it on the machine directly, otherwise you keep both layers to maintain.
>
> Laptop experiments. Use kind or k3d, break things, delete the cluster, start again in a minute. Don't experiment on the box that runs your services.
>
> Which distribution. For a single home server, any of the lightweight single-binary ones you listed is fine, and the differences matter less than you'd think. Pick the one whose docs you find easiest to read, because that's what you'll be using at 11pm when something breaks.
>
> Storage decides how much maintenance you sign up for, more than the runtime does. On one node, local path volumes behave like your compose bind mounts and are easy to back up. Replicated storage across nodes is where the time goes. If you don't need replication yet, stay on one node for a while.
>
> Honest take: if compose works and the file is only long, splitting it into one compose project per service gets you a lot of the tidiness with none of the new moving parts. Move to Kubernetes if you want to learn it, and that's a perfectly good reason.

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
