---
type: "corpus"
item_id: "3520d39dceb602ed"
title: "Do you not patch your docker images against CVEs?"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1x6x5c0/do_you_not_patch_your_docker_images_against_cves/"
author: "thepenguinboy"
published_at: "2026-10-16T04:47:26+08:00"
captured_at: "2026-10-26T09:43:54+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-10-26"
pub_day: "2026-10-16"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Need Help
metrics: {"score": 108, "comments": 92, "upvote_ratio": 0.8648648648648649}
comments_count: 91
comments_total: 92
discovered_via: "reddit:14d+settle10"
---

# Do you not patch your docker images against CVEs?

> [!info] 一句话导读
> Started using a Docker Manager (Arcane) with built-in vulnerability scanning (using Trivy) which is also able to automatically patch docker images (using Copace…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1x6x5c0/do_you_not_patch_your_docker_images_against_cves/>
> 指标：得分=108 · 评论=92 · 赞踩比=0.8648648648648649
> 作者：thepenguinboy　|　发布：2026-10-16T04:47:26+08:00
> 项目链接：—
> 采集：2026-10-26T09:43:54+08:00　|　id：`3520d39dceb602ed`

## 正文

Started using a Docker Manager (Arcane) with built-in vulnerability scanning (using Trivy) which is also able to automatically patch docker images (using Copacetic/Copa). I'm frankly astounded at the number of vulnerabilities it found in just the small handful of containers I'm running. The worst offenders are Immich, with 745 vulnerabilities spread across 4 containers, and Nginx Proxy Manager with a staggering 1,420 vulnerabilities.

I tried patching a couple non-essential containers (iSponsorBlock and Scrutiny) just to familiarize myself with the process in case I broke anything. It's manageable, albeit a little cumbersome. But I'm scared to try patching system critical things like NPM and Immich, for fear of breaking things.

I'm just surprised that this isn't talked about more. Are people just out here raw-dogging their docker images and that's normal? Or is this a non-issue and I'm worrying about nothing?

## 评论（91/92）

> **asimovs-auditor**（1 分） · 2026-10-16T04:47:35+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **thepenguinboy**（4 分） · 2026-10-16T04:47:52+08:00　
> No AI used in this post.

---

> **SammyDavidJuniorJr**（17 分） · 2026-10-16T04:53:06+08:00　
> Depends on the attack vectors.
>
> There are often other ways to mitigate.

---

> **Informal-Detail6034**（8 分） · 2026-10-16T04:58:41+08:00　
> Most people are absolutely raw-dogging it and just hoping for the best

---

> **thepenguinboy**（-7 分） · 2026-10-16T05:00:18+08:00　
> Care to expand on that? I don't know much about security. Currently I don't have everything exposed and only access everything local or through Tailscale for that reason, but ultimately I'd like to open things up. I have a few friends and family who would like to use the services I'm hosting, but I'm terrified of exposing my server to the open internet.

---

> **thepenguinboy**（-2 分） · 2026-10-16T05:02:53+08:00　
> Seems unwise, but idk how much of a risk that actually is?

---

> **ethansky**（1 分） · 2026-10-16T05:05:37+08:00　
> Bot ^

---

> **BeautifulBlueNight**（3 分） · 2026-10-16T05:07:49+08:00　
> And that is exactly the reason why I switched of the threat detection in Dockhand.
>
> It gives a huge number of warnings. OK, great. What now? I got anxiety of it.
>
> I have no ports opened, all exposure is through Tailscale. I keep my containers updated, and I'm pretty much the only user, besides my wife who just uses Vaultwarden to access shared passwords.
>
> There's other things to have anxiety about in out hobby (which I tend to get easily anyway).

---

> **Gvarph006**（19 分） · 2026-10-16T05:09:02+08:00　
> For example, if a database has a known vulnerability where it's data can be read without authorization, is it really an issue if it can only be reached from the one service using it and can't be accessed from the internet?

---

> **Bemteb**（176 分） · 2026-10-16T05:09:25+08:00　
> Did you look into the vulnerabilities found? Many of them are very specific and might not apply for these containers. I'd guess by not having them reachable with a public URL you could already ignore quite a few.
>
> Apart from that, yes, many users (me included) use docker images similar to .exe files on windows: Download them from somewhere, run them, enjoy the software.

---

> **Bemteb**（5 分） · 2026-10-16T05:11:39+08:00　
> Don't simply expose them all. Have a single entry point (VPN, reverse proxy, etc.) that you can monitor and secure.

---

> **thepenguinboy**（-7 分） · 2026-10-16T05:12:21+08:00　
> Surely you don't do that kind of per-vulnerability analysis on hundreds of CVEs?

---

> **Thutex**（5 分） · 2026-10-16T05:13:42+08:00　
> i think that if the host machine is safe (as in, for example, only accessible by you because it's behind a firewall that allows only you, and you expose as little as possible (say only the web port of immich) and do so behind some layer of defense (say cloudflare or pangolin), and you keep the container updated.... then the risk will be relatively small (because: an attacker would have to be able to get to your immich instance, then find a vulnerability in immich which gives access to the container, and then have a vulnerability to break out of the container)
>
> impossible? not at all
> likely? i don't think so unless you're a big target, or there's a vulnerability that can be automated that happens to be able to access your instance.
>
> for example, my immich container is not patched for vulnerabilities (as it's often a ridiculous amount of work and every day brings new things to patch), but:
>
> \- it is accessible only through pangolin (no other publicly accessible route)
> \- and pangolin is limited to a few countries, with the basic crowdsec+fail2ban+waf stuff in place
>
> now, if the attacker were to gain access to the machine \*running\* pangolin, we're ofcourse talking about a very different kind of breach, but pangolin is only available to me (for ssh) and only through cloudflare for http/https,
> which is an additional layer of filtering.
>
> so, in order to get into a vulnerability of the immich container, in my case:
>
> \- an attacker would have to go through cloudflare, bypass the security on the pangolin container, get into immich with a vulnerability, and then exploit whatever vulnerability there is in the container....
> so i'm not all that worried about a vulnerability inside the container directly.
>
> just:
> \- try to make sure your instance is as secure as possible
> \- update it regularly
> \- and keep access to the host restricted
>
> bonus points for doing some additional isolation to prevent problems when container containment is breached,
> or for making important folders read-only with an overlay so ransomware (if it hits the container) won't damage too much (this, i'm not -yet- doing enough myself)

---

> **thepenguinboy**（-63 分） · 2026-10-16T05:13:58+08:00　
> There's a few thousand vulnerabilities it found, all told. Should I be looking into each of them individually? That's crazy work.

---

> **Gvarph006**（19 分） · 2026-10-16T05:15:31+08:00　
> You don't usually get hundreds of NEW high severity updates with each update.
>
> Usually you can mostly disregard stuff below severity 6, and you get used to reading the summaries

---

> **Cheeze_It**（4 分） · 2026-10-16T05:17:08+08:00　
> My docker containers don't talk to the internet natively so.......raw dogging is ok.

---

> **Bemteb**（90 分） · 2026-10-16T05:20:29+08:00　
> So why do you assume the developers of these tools, who oftentimes develop them for free in their free time, want to do it?
>
> Also many vulnerabilities are of the form "you have library A installed. There is a bug in library A that when you call function f more than 10.000 times in one second, you gain admin rights" or something similar. This is only relevant if attackers can access your machine (as non-root maybe) or the software you expose gives an option to call f very, very fast. But A is only installed because we need function g from it, which has nothing to do with f. And g is only used for daily backups, a user can't access it at all.
>
> Just an example, to illustrate that there is a big difference between a theoretical vulnerability existing on your system and your system actually being compromised or vulnerable.

---

> **camh-**（35 分） · 2026-10-16T05:21:01+08:00　
> It is likely that most of the vulnerabilities listed are false positives and not actually exploitable. These scanners are typically very coarse and just flag if a container image contains a version of a program with a CVE, even if that program is not used. For instance, a container image uses a base image that has a common set of CLI tools. One of them has a vulnerability but it is not used at all by the derived container and not accessible in any way. It cannot be exploited.
>
> https://www.chainguard.dev/unchained/stemming-the-tide-of-false-positive-vulnerabilities goes into more details - this is not an endorsement of chainguard - I've never heard of them before now - but I searched for relevant blog posts and this describes the problem in enough but not too much detail.
>
> Another worthwhile post is https://dev.to/oleg_sydorov/the-subtleties-of-vulnerability-scanning-in-go-projects-26fm - this is more from a development perspective related to code in your binary vs programs in your container image, but it's the same problem.

---

> **stevecrox0914**（4 分） · 2026-10-16T05:25:42+08:00　
> Tdlr; It represents a large attack area, but typically relies on a successful attack to a regularly patched area to exploit.
>
> A lot of people use distribution based docker images, these install all the tools you need for a server or desktop install. Almost all the CVE's will be related to these tools.
>
> However...
>
> To exploit one of these tools an attacker has to find a way to execute code within the docker container.
>
> Something like Immich exposes a https server and rest endpoint. A CVE on the those endpoints is a concern because they can chain an attack, but that exploit is needed first.
>
> So as an end user a CVE in nestjs would concern me, but one on coreutils doesn't.
>
> You also have the fact a lot of CVE's are overrated. A lot of them rely on multiple components being wildly misconfigured to create a root attack. Its .. possible but literally no one has that configuration
>
> Lastly this is why Alpine is a popular base image, with Alpine you get the kernel and every thing is packaged seperately. It means only the things your application needs are installed.
>
> Alas a lot of people also struggle with this level of packaging so default to ubuntu/red hat base images

---

> **Jolicristo**（3 分） · 2026-10-16T05:27:34+08:00　
> most of those are completely unreachable false alarms. just put everything behind a vpn and dont stress.

---

> **Zanish**（85 分） · 2026-10-16T05:29:37+08:00　
> I work in cybersec and specifically with docker and kubernetes. All cves are not created equally.
>
> You said you found thousands but what's the severity? What packages are they in? What's the reliability of the findings? Are they reachable?
>
> Nowadays especially with NVD being flooded with bogus ai scanned vulns it's important to review the details of security findings before making decisions based on them.

---

> **thepenguinboy**（1 分） · 2026-10-16T05:32:10+08:00　
> Thanks for the links, I'll definitely give those a read.

---

> **cloudcity**（17 分） · 2026-10-16T05:32:21+08:00　
> It's ok not to lock your bedroom door if the house doesn't have a front door. (use Tailscale/Twingate)

---

> **thepenguinboy**（2 分） · 2026-10-16T05:32:29+08:00　
> This is helpful, thank you.

---

> **thepenguinboy**（0 分） · 2026-10-16T05:35:42+08:00　
> I think part of the problem is that, as someone who just dabbles in this and is by no means a programmer or security expert (I'm a paper pusher at my day job, not a network admin), I don't have the skill set to make any of those determinations, much less interpret what they mean for me. It seems... scary and ineffable.

---

> **thepenguinboy**（4 分） · 2026-10-16T05:36:22+08:00　
> This is probably the most succinct and clear way to say what everyone else here is saying. Thank you.

---

> **garbage_dev**（3 分） · 2026-10-16T05:38:01+08:00　
> Most of those numbers are OS packages baked into the base image that the app never loads. An old libtiff in a Debian base shows up as dozens of CVEs even if nothing touches it. What matters is what's reachable. Keep Immich on the latest release, put admin stuff like NPM's port 81 behind Tailscale or a firewall rule, and only sweat CVEs in whatever is actually facing the internet. Copa patching Immich is more likely to break it than to save you.

---

> **Zanish**（13 分） · 2026-10-16T05:38:57+08:00　
> So think of it this way. You asked a scanner that isn't configured to give you all the possible issues with an image. You can't validate if they are legit or not.
>
> Do you think an app as big as immich would just allow tons of vulns to sit in their images?
>
> The most likely answer here is false positives from an untuned scanner. No issue if you want to learn but not something you should be freaking out about imo. Unless you want to post actual details and have that convo.

---

> **KookyInformation7841**（27 分） · 2026-10-16T05:38:58+08:00　
> Work in a similar line, Linux/Container security. You’re spot on.
>
> I’m pretty sure if OP filtered out CVEs with no available fix, or CVEs with an EPSS score of 0.05 or higher, there’s maybe a handful of patches required.
>
> Linux foundation becoming a CNA and assigning a CVE for every kernel bug was a mistake.

---

> **Oujii**（1 分） · 2026-10-16T05:40:25+08:00　
> ?

---

> **koollman**（2 分） · 2026-10-16T05:47:54+08:00　
> The number of usable vulnerabilities is different from the number of cve on some files included in a container image. Your tool report the second kind

---

> **kernald31**（59 分） · 2026-10-16T05:53:24+08:00　
> Welcome to the world of security, where most things are noise, but ignoring the wrong thing can be a big mistake. And that's also the answer to your initial question.

---

> **Mrbucket101**（1 分） · 2026-10-16T05:59:28+08:00　
> I’m the maintainer behind [renamarr](https://github.com/hollanbm/renamarr), and security is very important to me. So is my sanity, this is how I, and most of the industry, solve the problem — By outsourcing the work lol
>
> Use a pre-hardened image as your base, dhi.io is currently free. Then use a multistage build, compile your app in the first stage, then copy into the final runtime image, only the artifacts needed for your app to function. [Example](https://github.com/hollanbm/renamarr/blob/main/Dockerfile)
>
> I also go a little further and ensure that the image doesn’t start as root, and that the container has a read-only root filesystem. I’m still working on dropping nearly the unused capabilities.

---

> **Playful-League3414**（9 分） · 2026-10-16T06:03:33+08:00　
> Or Netbird if you want a non-US option

---

> **KookyInformation7841**（7 分） · 2026-10-16T06:08:03+08:00　
> If it’s something you’re interested in learning more about, the Risk Based Prioritization guide on GitHub offers plenty of good information: https://riskbasedprioritization.github.io/introduction/Introduction/
>
> If it’s something you don’t: use images based on things like Docker Hardened Images/chainguard etc and patch early patch often

---

> **Ezedon001**（1 分） · 2026-10-16T06:15:16+08:00　
> One distinction worth keeping: a real vulnerable package that isn't reachable in your setup isn't the same thing as a false-positive detection. Trivy inventories known vulnerabilities in components; the total by itself doesn't tell you which ones an attacker can actually use. Its docs explain the package/advisory matching: [https://trivy.dev/docs/latest/scanner/vulnerability/](https://trivy.dev/docs/latest/scanner/vulnerability/)
>
> For the fear-of-breaking-Immich part, I'd tackle recoverability alongside patching: follow the project's backup instructions, test a restore on a separate instance, then test the supported image update there before changing the main instance. Keeping the old image alone isn't a rollback plan if an update migrates the database.
>
> For prioritization, pick one finding in a service you expose and check the affected package/version, exploit prerequisites, available fix, and the project's advisory. That gives you something concrete to act on or ask about here. A VPN reduces exposure, but it doesn't make vulnerabilities disappear. No need to choose between blindly patching thousands of findings and dismissing all of them.

---

> **gscjj**（-15 分） · 2026-10-16T06:17:54+08:00　
> This is why I keep saying the auto update images blindly to be “secure” isn’t worth it.
>
> If you don’t need a feature added or a security issue isn’t exploitable or isn’t severe, leave it be.

---

> **fernandops**（2 分） · 2026-10-16T06:21:20+08:00　
> For the fear of breaking Immich or NPM, test the patched image against a copy of the data first. Write down what you’ll check: login, photo upload, existing photos, and proxy routes. Keep the original image and a backup from before the change. If the test changes the database, rolling back the image alone may not undo it.

---

> **kayson**（2 分） · 2026-10-16T06:28:03+08:00　
> I think part of the problem is visibility. Devs just don't set up reporting or scanning so they don't know. I actually maintain Scrutiny and only just recently set up automatic scanning. Most of the CVEs are fixed in the nightly builds now, and a new release should come soon. The big remaining issue is the frontend uses a very outdated build system because of the skin we use. Updating it is a huge task, and given the low risk, it's just not a high priority.

---

> **ComputeEngines**（1 分） · 2026-10-16T06:29:48+08:00　
> tailscale does seem to be the go to nowadays, spinning up your own private VPN tunnel used to be the way

---

> **Zanish**（9 分） · 2026-10-16T06:45:18+08:00　
> No this is the wrong message completely. 9/10 times cves are solved by an update that changes almost no functionality. Updating often is a good way to keep secure as they may patch vulns you aren't aware of because of disclosure agreements.

---

> **gscjj**（-6 分） · 2026-10-16T06:58:38+08:00　
> Right I’m talking about blindly updating to say you’ve updated, like all the auto-updating scrips/software.
>
> Most CVEs don’t require urgent action and you have time to evaluate your risk

---

> **SwizzleTizzle**（2 分） · 2026-10-16T07:02:55+08:00　
> I've had to deal with this at work and it's massive PITA.
>
> For example, the scanner might identify some CVE in a perl library that exists in the base image and it blocks deployment, despite our application never using perl and there is no way for it to be executed.
>
> We're slowly moving to distroless containers.
>
> I don't care for my home stuff, the only things exposed to the web are served over https and the reverse proxy drops connections that don't present the right hostname in SNI.
> The hostnames are not available in public cert transparency logs.

---

> **AirshipCommand**（3 分） · 2026-10-16T07:04:11+08:00　
> Most of those counts are noise. Trivy reports every CVE in every OS package in the image, including ones with no fix available and ones in libraries the app never loads. Run it with --ignore-unfixed --severity HIGH,CRITICAL and the list usually gets much shorter. Also, Copa only patches OS packages, not the app's own dependencies (Node, Go, Python libs), so a patched image can still carry the same app-level CVEs. For things like Immich and NPM, pulling upstream releases regularly and keeping the admin UIs off the public internet does more than patching images locally, and you avoid running a build nobody else has tested.

---

> **lukistellar**（5 分） · 2026-10-16T07:56:45+08:00　
> May I ask how do you work with managers who doesn't get this? I am currently getting spammed with unfiltered vul reports from M365 Defender, which goes way beyond my resources. I am not sure if they use any AI tools for the scanning, but all the communication comes clearly from an LLM.

---

> **FlexTeam26_Agents**（1 分） · 2026-10-16T08:08:55+08:00　
> raw counts are noise. triage by what the container can actually reach - exposed ports, whether the vulnerable binary runs at all - and patch that first. 1400 findings is a queue, not a crisis.

---

> **Zanish**（7 分） · 2026-10-16T08:23:50+08:00　
> I mean we have a really robust update and risk acceptance process. You get your sla and then if you can't fix it past that the app owner can accept the risk and they get to talk to compliance about why they are ok with it. Education on reachability and risk + paperwork is how big security operations stay above water.

---

> **lukistellar**（1 分） · 2026-10-16T08:38:09+08:00　
> Unfortunately we don't do processes at all, as well as there are no standards. We rather get randomly pieces of information tossed, mostly screenshots from the Security Center without any guidelines, filtering or information besides the raw output of the vulnerability scanner inside of this plattform.
>
> What really concerns me is the circumstance that it's all about the output of such tools nowadays, while real weak points in our infra totally are getting ignored, like proper subnet isolation or reviewing and fixing of decade old rulesets on edge firewalls.

---

> **Noisyss**（1 分） · 2026-10-16T08:43:32+08:00　
> I'm on the latest img group, dunno it will update whenever it needs a update, 3 years no issue so far, just migrate to a vps becouse of costs.

---

> **FerWasTaken**（2 分） · 2026-10-16T10:50:43+08:00　
> None of my things are exposed to the internet, they are accessed over a VPN, so most security vulnerabilities don't really matter to me.

---

> **thatboyonabike**（0 分） · 2026-10-16T10:55:03+08:00　
> This is a bot.

---

> **ILoveAppSec**（2 分） · 2026-10-16T11:22:52+08:00　
> Isolation genuinely lowers exposure, so for a locked-down immich box that reasoning mostly holds. It breaks down when a scanner or an upstream dependency forces a specific CVE, and the only patched tag also drags in a base-image jump you did not ask for. In that case it is worth checking whether the fix alone can be backported onto the image version you already run, so you clear it without the upgrade.

---

> **masiha97**（1 分） · 2026-10-16T11:26:02+08:00　
> The distroless angle is the one that actually moved the needle for me. Most of those scary counts are OS packages the app never touches. Switching base images cut my reported CVEs by like 90% without me patching a single thing myself.

---

> **JohnnyBeeGaming**（1 分） · 2026-10-16T12:03:07+08:00　
> I wouldn't really consider having docker images with possible vulnerabilities really raw-dogging it.
>
> If nothing is open to the web maybe stability is more important than having the latest patch. A lot of those images probably have vulnerabilities because they have older versions of some library or package that may or may not break things if upgraded.
>
> I typically just stick to upgrading the docker image every so often when there is an official stable release.

---

> **yawkat**（47 分） · 2026-10-16T12:15:35+08:00　
> > Many of them are very specific and might not apply for these containers. I'd guess by not having them reachable with a public URL you could already ignore quite a few.
>
> This is actually two separate reasons why a CVE might not matter.
>
> * just because library X has a CVE, and an application uses library X, doesn't mean the application is exposed to the CVE. The majority of library CVEs depend on the application using the library in a particular way.
> * Keeping the network endpoint private protects against almost all remaining CVEs.
>
> In my homelab I also try to defend against application vulns by reducing exposure (reverse proxies with TLS, OIDC gates that don't rely on app auth) and by reducing potential impact (noexec for writable dirs, virtualization, firewalling)

---

> **smstnitc**（2 分） · 2026-10-16T12:21:12+08:00　
> I raw dog it with my wife... My docker images don't get to participate.

---

> **incyashraj_redd**（1 分） · 2026-10-16T12:23:03+08:00　
> one thing I'd mention: VEX. it's a statement from the people who make the image saying "this CVE is in there but our code never reaches it". trivy can pull those from the public VEX Hub:
>
> `trivy image --vex repo` [`ghcr.io/immich-app/immich-server:release`](http://ghcr.io/immich-app/immich-server:release)
>
> and anything the maintainer marked not affected drops out. how much it removes depends on whether the project publishes VEX at all, and plenty of self-hosted projects don't yet. but when they do it's the maintainer's call, not you guessing about reachability.
>
> second, if a project ships an SBOM with its release, scan that instead of the image: `trivy sbom thing.cdx.json`. that shows what's in their app separately from the base image. a lot of those 745 tend to be base image packages, which is the part copa can patch. the app part you can't fix yourself anyway, it needs a release from them.
>
> the ones worth losing sleep over are the ones reachable from outside. something only on your tailnet can wait for the next upstream release.

---

> **maquis_00**（1 分） · 2026-10-16T14:44:25+08:00　
> I try to keep my containers updated to mitigate the risk, but... All containers for me run in rootless podman, and aside from my website and VPN, none are accessible from outside my local network....

---

> **Mrhiddenlotus**（8 分） · 2026-10-16T14:44:47+08:00　
> If it makes you feel better, your reaction is relatable to anyone who just started vulnerability scanning for the first time. Everything is scary and red.

---

> **Bemteb**（7 分） · 2026-10-16T15:15:31+08:00　
> > way beyond my resources
>
> I would try that angle. Show that reports have drastically increased but your team size has not. Offer multiple suggestions:
>
> - Reports should be better prepared. Work out a form the reporter needs to fill out, including information like affected systems, severity, etc.
>
> - Instead of solving every report when it comes in, do triage. Quickly review them and sort them into "needs fix asap", "fix in next release" and "lol, don't care"
>
> - Outsource the actual fixing, you only identify and report
>
> - Strongly push back on bogus reports, push for trainings on how to report
>
> Managers work best if you tell them "Here is a problem, I've prepared a few solutions, let's discuss."
>
> And even if no solution is found, you have the meeting notes to point out that you warned early. Btw, write and distribute meeting notes.

---

> **agendiau**（1 分） · 2026-10-16T15:17:29+08:00　
> Where I work we have vulnerability scanning running on everything. It creates a lot of noise and makes management feel safe. Many of the warnings don't really take into account how the app is being used, the network setting or if the affected library is even loaded at run time.
>
> I'm not saying that vulnerability scanning doesn't catch real issues but boy it creates a lot of useless work as well. It needs to be weighed up appropriately rather than just blindly actioned.

---

> **valerian1**（1 分） · 2026-10-16T16:00:15+08:00　
> I do at work. My NAS is not exposed to the Internet.

---

> **Quiet-Wafereater**（1 分） · 2026-10-16T17:34:48+08:00　
> Most people just keep images updated from upstream, as maintainers rebuild with patched base images. Pulling new versions regularly fixes the majority of CVEs without self-patching. Patching with Copa creates images that drift from upstream, which can complicate future updates and support. Self-patching makes sense mainly for critical CVEs the maintainer hasn’t addressed.

---

> **brutchev**（1 分） · 2026-10-16T18:28:39+08:00　
> How can you tell so fast?

---

> **AnomalyNexus**（4 分） · 2026-10-16T18:51:16+08:00　
> 0% of my docker stuff is on the internet, so pretty relaxed about it

---

> **tj_moore**（2 分） · 2026-10-16T18:53:03+08:00　
> Seen managers turn on automated scans in corporate dev repos that pick up 1000s of "vulnerabilities" from dependencies and automatically raise hundreds of PRs with "fixes" that don't consider how many dependency updates have breaking changes.
>
> Massive workload to go through the PRs and it's raising more than you can address.
>
> But the vast majority can be non-issues for the product as it doesn't touch any of the risks. Many can even be fixed by removing or replacing unnecessary dependencies, or by writing the code yourself rather than depending on something that depends on 100s of other unnecessary packages to do a very simple job.

---

> **gemengelage**（7 分） · 2026-10-16T19:07:24+08:00　
> > Did you look into the vulnerabilities found? Many of them are very specific and might not apply for these containers.
>
> Yeah, for example I recently looked into a CVE that only applies to Windows and wondered why I even bothered to begin with.

---

> **RedVelocity_**（4 分） · 2026-10-16T19:22:14+08:00　
> most of don't expose services to the internet

---

> **A_cold_dish**（1 分） · 2026-10-16T20:06:14+08:00　
> Many moons ago I worked for a cloud services provider in their SOC working on FedRAMP, one of the things we’d do is recasting CVSS scores, you very quickly learn that security is best done in layers. So how I’ve designed my homelab is around exposure, what’s the realistic exposure of my service, one way I’ve done that is all of my services are only on my VPN overlay, except the critical ones that must exist outside it.
>
> I now work for a vendor doing secrets management and often times our customers put in a ticket “your image has CVEs” and we have to comply because they’re paying us lots of money and we can’t explain the above without sounding condescending 😆 though it is in our best practices docs, well mostly.
>
> If you have management that won’t see the light give them a little layers of the onion security 101 explanation of why this isn’t as big of a deal as they think it is, or you’ll discover it is actually a huge deal and that medium is a problem because x, y, z.

---

> **Ill_Leader_7104**（1 分） · 2026-10-16T20:07:02+08:00　
> are those 1400 vulns actually in the app layer or in the base OS packages? most scanners flag everything in the image including stuff that's never loaded into memory. worth filtering by severity and actual reachability before panicking

---

> **binarypower**（2 分） · 2026-10-16T22:36:46+08:00　
> watchtower and host updates nightly

---

> **Open-Adhesiveness-86**（2 分） · 2026-10-16T23:41:13+08:00　
> worth knowing what copa actually does before you trust the counts: it only rewrites OS packages from the scan report, so apk/apt/rpm stuff. immich's number is mostly npm deps and the bundled ffmpeg/cuda libs, which copa can't touch, so patching barely moves it. and your patched tag disappears the next time compose pulls, which is why nobody bothers.

---

> **GeologistPutrid2657**（2 分） · 2026-10-17T00:43:39+08:00　
> everything for me auto-patches and i never look at a changelog.

---

> **binary_flame**（1 分） · 2026-10-17T00:48:05+08:00　
> There's also some developers that don't know about docker best practices, such as separating the build and deployment layers, using a minimal/distroless image for the final layer, only copying the dependencies you need. That helps cut down a lot, since images like nodejs tend to have a lot of vulnerabilities

---

> **Jonjolt**（1 分） · 2026-10-17T02:02:23+08:00　
> Every time snakeyaml is imported into a java project the warnings fly, but no one uses the unsafe deserializer its a joke.

---

> **Anusien**（1 分） · 2026-10-17T02:18:08+08:00　
> Another example I've seen: you can use React Router in either Declarative Mode, Framework Mode, or Data Mode. Take [CVE-2026-42211](https://app.opencve.io/cve/CVE-2026-42211):
>
> >React Router is a router for React. In versions 7.0.0 through 7.14.1, when using Framework Mode, a combination of steps could potentially allow unauthorized remote code execution (RCE) through external requests. This attack requires the application code to have an existing prototype pollution vulnerability, which can then be leveraged in a 2-step attack where the second step triggers unauthorized RCE on the remote server. This does not impact applications using Declarative Mode (\`<BrowserRouter>\`) or Data Mode (\`createBrowserRouter/<RouterProvider>\`). This is patched in version 7.14.2.
>
> The CVE scanner will flag a vulnerability if you're using React Router version 7.0.0 through 7.14.1, but it doesn't scan your codebase to see if you're using Framework Mode.

---

> **Anusien**（1 分） · 2026-10-17T02:20:46+08:00　
> Something else to consider: most projects out there probably use semantic versioning, so it should be safe to upgrade a patch version. But what if they don't use semver, or there isn't another patch version that mitigates this vulnerability? It's not always safe to blindly upgrade versions of dependencies. And sometimes the problem will manifest by just breaking when you try to run the thing.
>
> This is the problem maintainers have. Are they going to try to fully test their software every time any of their dependencies releases a new version? And what if it's a dependency (and therefore CVE) they only get transitively?

---

> **SuperBelgian**（3 分） · 2026-10-17T04:34:12+08:00　
> You are correct the application itself might not be vulnerable because it is only affected if a library is used in a specific way.
>
> However, that doesn't mean the CVE doesn't matter.
> The vulnerable library is still present on your system and it could be misused by other, completely unrelated software, like a trojan horse.
>
> Compromises are almost never because of a single big vulnerability is present on the system, but because an entire chain of "small" vulnerabilities can be misused towards a full compromise. Unfortunately, AI is getting really good at finding such paths.

---

> **yawkat**（2 分） · 2026-10-17T04:40:53+08:00　
> That is almost never a realistic option. If you can induce an application to load and call into arbitrary libraries you have bigger problems.

---

> **Delicious-Director43**（1 分） · 2026-10-17T05:41:10+08:00　
> I agree with this response because it is the most well informed and reasonable. Many containers/apps are always going to rely or have many dependencies that can become out of date or contain potential CVE’s but your actual attack surface depends on a lot of other things including your network configuration, firewalls, access rules, etc…

---

> **coderstephen**（1 分） · 2026-10-17T07:08:45+08:00　
> No. I'm not in the business of maintaining my own Docker images. I rely on the developers of the app(s) to maintain their Docker images. They might do a good job, or they might do a bad job. If they do a really bad job, I just wouldn't use the app, rather than maintaining my own image.

---

> **coderstephen**（6 分） · 2026-10-17T07:12:02+08:00　
> I work in tech, and we talk about CVEs a lot lately, and I concur. Most CVEs are irrelevant. And there indeed are many thousands being filed constantly; it is basically impossible to have zero CVEs. You could spend hundreds of hours of work just to have 0 CVEs for about 1 hour before a new one pops up on your latest build.
>
> Most CVEs are not exploitable unless the attacker already has access to your environment, in which case you are screwed anyway for other reasons.

---

> **laffer1**（1 分） · 2026-10-17T10:36:21+08:00　
> I give you cve 2026 99999
>
> The host needs to keep the kernel patched

---

> **Thutex**（1 分） · 2026-10-17T16:12:31+08:00　
> yes, but then we are talking, again, about \*the host\* not the container.
> and that lis literally part of the "host machine is safe" idea (though i do notice i did not explicitly mention keeping the host updated (i come from a time you did not need to expliclty say things that were obvious, but here we are in a time that states to not put your pets in the microwave, so.... maybe that time has long gone)

---

> **Thutex**（0 分） · 2026-10-17T16:15:58+08:00　
> how would an unrelated application get access to the library inside a container with only a specific application running inside it?
> we're talking about containerized applications here, not stuff running freely on the host, so this vector seems extremely unlikely.
> (it would be much more likely that the container pipeline is compromised and you get a malicious image altogether)

---

> **laffer1**（1 分） · 2026-10-18T04:21:54+08:00　
> I just assume people won't at this point.  I see it a lot at work.  the peops folks don't patch the k8s hosts but like twice a year.  We get yelled at about CVEs in container images but the hosts are the most vulnerable thing in our scanner tool.
>
> I got yelled at for patching this week because there was a regression in netty.  The netty folks refuse to fix the issue.  So they made me rollback to a vulnerable version. Good times.

---

> **tresero**（1 分） · 2026-10-18T08:02:32+08:00　
> If you are looking for something that just runs on cron, I wrote this for me and a non-profit I volunteer for, it works fine, a couple of quirks, but, it's open source and you can modify it if you want.
>
> [https://github.com/tresero/docker-scanner](https://github.com/tresero/docker-scanner)
>
> Oh, and I'm a 35+ year sysadmin/programmer, and yes, I used claude to do grunt work. Take it for what it is.

---

> **Long-Librarian-997**（1 分） · 2026-10-18T20:57:08+08:00　
> Why are you using both clouflare and pangolin?

---

> **Thutex**（1 分） · 2026-10-18T23:56:20+08:00　
> added benefits, mostly:
>
> 1. the ability to use the cloudflare protections
> 2. the fact that my dns is in cloudflare, and this way i can just use their proxied dns instead of using the pangolin host ip in dns
> 3. due to 2, the ability to use the ddos/blackholing in case it would ever be needed
>
> that + then you can rely on the cloudflare ip-headers, which basically do the check on the real user ip for you (which, unlike the regular x-forwarded that is usually used, can't be spoofed, as cloudflare uses the IP of the actual tcp connection instead of the header information to set their header)
>
> also, the usual "why not" :) (it's not like adding cloudflare as the first part of the puzzle creates a bottleneck, so there's really no reason not to, if you're open to using cloudflare)
>
> and finally: it also allows me to up and move the pangolin host in it's entirety to a new machine, with a different ip, keeping everything intact, by just changing the proxied IP in cloudflare,
> which is something i have done before (i.e: copy the entire compose stack with it's configs over to a new machine, let it come up, and with only the change of 1 setting in CF, which does not need to do dns propagation, you're up and running again)

---

> **ice456cream**（1 分） · 2026-10-19T05:26:02+08:00　
> Specifically reverse proxies with *m*tls, which means the connecting client has to prove who it is to the server before exposing any application attack surface

---

> **iEliteTester**（1 分） · 2026-10-19T16:25:05+08:00　
> Preach, 30 cves a day, A DAY

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
