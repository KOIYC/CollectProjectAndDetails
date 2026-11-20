---
type: "corpus"
item_id: "bdb5a35f8f900a5f"
title: "Show HN: I rebuilt evilgrade to test where a leaked CA still works"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50560557"
project_url: "https://faradaysec.com/evilgrade-2026-225-modules-meet-a-leaked-emudhra-ca"
author: "famato"
published_at: "2026-11-19T14:26:56Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_famato
  - story_50560557
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: I rebuilt evilgrade to test where a leaked CA still works

> [!info] 一句话导读
> Overview Unified offensive security platform.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50560557>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：famato　|　发布：2026-11-19T14:26:56Z
> 项目链接：<https://faradaysec.com/evilgrade-2026-225-modules-meet-a-leaked-emudhra-ca>
> 采集：2026-11-20T09:45:52+08:00　|　id：`bdb5a35f8f900a5f`

## 正文

Skip to content
Spanish
Platform
Overview Unified offensive security platform.
Capabilities Offensive operations made simple.
Vulnerability Management Continuous scanning and tracking.
Penetration Testing Reporting Automate and centralize pentests.
Application Security / DevSecOps Integrate security into development.
Integrations Connect tools, automate workflows.
Client Portal Access SaaS or on-prem Faraday environments.
Services
Faraday All-in-One Unified offensive security platform.
Faraday Enrichment Train. Simulate. Evolve your offensive capabilities.
Faraday Ops Automate detection, response, and continuous validation.
Faraday CART Reverse, exploit, and understand complex software systems.
Faraday Labs Discover, analyze, and disclose real-world vulnerabilities.
Red Team Services Offensive operations made simple.
Research Lab Advancing offensive security research.
FaradAI AI pentesting for real risk.
Pricing
Company
About Us Driving innovation in offensive security.
Partner Program Collaborate, grow, and secure together.
Cybersecurity Events Connecting experts, sharing knowledge.
Careers Join our team and shape the future of security.
Resources
Blog Insights and updates from our security team.
How to Get Started Set up, connect tools, and start testing.
Documentation Full technical docs and API references.
E-books Downloadable security guides and practical resources.
Media Hub All Faraday channels in one place.
Webinars Learn from experts. Watch live or on demand.
Atrás
Platform
Overview Unified offensive security platform.
 Capabilities Offensive operations made simple.
Vulnerability Management Continuous scanning and tracking.
 Penetration Testing Reporting Automate and centralize pentests.
 Application Security / DevSecOps Integrate security into development.
Integrations Connect tools, automate workflows.
 Client Portal Access SaaS or on-prem Faraday environments.
Services
Faraday All-in-One Unified offensive security platform.
Faraday Enrichment Train. Simulate. Evolve your offensive capabilities.
 Faraday Ops Automate detection, response, and continuous validation.
 Faraday CART Reverse, exploit, and understand complex software systems.
 Faraday Labs Discover, analyze, and disclose real-world vulnerabilities.
Red Team Services Offensive operations made simple.
 Research Lab Advancing offensive security research.
 FaradAI AI pentesting for real risk.
Pricing
 Company
About Us Driving innovation in offensive security.
 Partner Program Collaborate, grow, and secure together.
 Cybersecurity Events Connecting experts, sharing knowledge.
 Careers Join our team and shape the future of security.
Resources
Blog Insights and updates from our security team.
 How to Get Started Set up, connect tools, and start testing.
 Documentation Full technical docs and API references.
 E-books Downloadable security guides and practical resources.
 Media Hub All Faraday channels in one place.
 Webinars Learn from experts. Watch live or on demand.
Get in touch
Offensive Security Open Source Pentesting
evilgrade 2026: 225 Modules Meet a Leaked eMudhra CA
November 15, 2026
A research log, told in the order it happened. We started by pulling on the October 2026 eMudhra CA compromise — and following where it actually reached, versus where everyone assumed it reached, is what sent us back to rebuild evilgrade . The honest headline up front: as a real-world attack this is narrow — it needs an on-path position, a client whose trust store still trusts the cross-signing root, and an install channel with no second signature, and macOS had closed most of it before we finished. The value wasn’t a big exploit. It was drawing the exact line between where a TLS-only attack works and where it doesn’t — and the updated tool is the thing that came out of drawing it.
It started with a leaked CA
In October 2026, two eMudhra intermediate CAs were found with recoverable private keys. The interesting one for us was EM DV TLS CA - G3C — not because it was obscure, but because of what it cross-chains to : the public AAA Certificate Services root (Sectigo/Comodo lineage), a root that has sat in trust stores for years.
The naive way to think about a leaked CA is “attacker plants a cert.” But that’s not the threat worth studying — if you can plant a root in someone’s store, it’s already over. What made this one worth a second look is that nothing needs to be planted . You present a leaf signed by the real, leaked EM DV TLS CA - G3C intermediate, it cross-chains up to AAA, and it validates against any client that still trusts AAA and hasn’t applied the eMudhra distrust — with nothing touched on the victim . No --cert , no flag, no planted root. That’s the line between “theoretical, with preconditions” and “default-exploitable on a concrete slice of clients.”
So the question we actually wanted to answer was: which clients, doing which everyday thing, fall to that leaf? That’s where the research went.
How far does it actually reach?
Here’s the honest answer, stated before any of the fun details, because an earlier draft of this post overstated it:
It needs an active on-path or DNS position — not a lab /etc/hosts edit, a real MITM. That’s already a high bar.
It only works against clients whose trust store still contains AAA Certificate Services and hasn’t applied the eMudhra distrust . Browsers were protected the day after the leak; macOS command-line tools were fully fixed on Nov 9 (timeline below).
It only works on install/update channels with no second integrity layer below TLS — and a lot of the ecosystem has one.
So the surviving real-world surface is a slice: unpatched machines, some Linux clients, and tools shipping their own stale root bundle. Small. We wrote it up anyway, precisely because mapping a small attack honestly is more useful than inflating it.
And measuring that slice surfaced the finding that actually mattered: in 2026 the weak link usually isn’t the auto-updater evilgrade was born to attack — it’s the TLS trust decision an installer makes the first time you pull software down. pip install , git clone , curl | sh . So we pointed the research at the install channel and wrote down, truthfully, which idioms are exploitable by default and which aren’t.
What worked, and what didn’t
We built the attack as real modules rather than slideware, and each one documents the mechanism and who is actually vulnerable. The scoping is the finding.
What worked:
pip install . PyPI dropped PGP signatures for sdists in 2023, so sdist integrity is now TLS plus trust-on-first-use, and setup.py runs at build time. A bare pip install evilpkg with DNS pointed at pypi.org is enough. Vulnerable: pip whose certifi bundle still carries AAA — stock macOS /usr/bin/python3 , plenty of distro/corporate Pythons. Not: a pip whose certifi already removed AAA. This depends on the client’s bundle age, not on anything the attacker picks.
curl | sh . The most common install idiom on earth, with zero integrity below TLS. We built the payload as a faithful two-stage preinstaller : stage 1 (ours) runs, then stage 2 pulls the genuine installer from the real CDN (which we don’t intercept), so the victim ends up with a working tool and notices nothing. In the published demo, stage 2 just runs --version — proof it fetched the real binary without shipping a weaponized flow.
git clone + pip install . . We serve a real source tree over dumb-HTTP with a reverse shell prepended to setup.py . Nothing runs on clone; it triggers on the habitual next step. Vulnerable: git on the OpenSSL backend (Homebrew, Linux, or forced via http.sslBackend=openssl ).
What didn’t — the useful half:
Homebrew. Homebrew’s ca-certificates had already removed AAA; its own curl / openssl reject the leaf. We’d written a homebrew_update module, then deleted it — it implied an exploitability that didn’t exist by default.
Apple Secure Transport. macOS blocked the eMudhra intermediates for framework-based validation on 2026-10-19 , so Apple’s /usr/bin/git (Secure Transport) rejects the MITM. The git vector only works on the OpenSSL backend.
Second-signature channels. apt / yum (GPG), Go modules (GOSUMDB), signed Terraform providers (GPG + lockfile) don’t fall to TLS alone — there’s a second signature to forge.
That’s the whole finding, in one sentence: a TLS-only attack is default-exploitable only where there’s no second signature and the store still trusts the root — curl | sh , pip (post-2023), git clone +build — and not where the ecosystem moved the trust store (Homebrew, Apple) or kept an independent signature (apt/yum, Go). Both halves are the result.
The whole surface, tool by tool
Two things decide each row. Premise A is the attacker’s side: an on-path position presenting the leaked-but-still-trusted eMudhra chain, so TLS validates with nothing touched on the client. Layer B is the defender’s side: a content signature on the artifact itself, independent of TLS. Where Layer B is missing, premise A alone is enough for code execution; where it exists, the attacker would also have to forge that signature, and the attack is blocked.
Tool Content signature (Layer B)? Honest RCE under premise A?
 pip (PyPI) ❌ None — PyPI dropped PGP signatures in 2023 ✅ Yes — the cleanest
 npm install ❌ Not verified on install by default; postinstall runs ✅ Yes
 gem / composer / helm ❌ Optional, off by default ✅ Yes
 curl | bash (rustup, nvm, get.docker.com, Homebrew installer…) ❌ TLS only, by design ✅ Yes — the purest
 apt / yum / dnf ✅ GPG by default ❌ Blocked
 go modules ✅ GOSUMDB ❌ Blocked
 Terraform providers ✅ GPG + lockfile ❌ Blocked
The pattern is the point: the green column on the left is the red column on the right. A second signature is the whole difference between an install channel that trusts whoever holds the cert and one that doesn’t.
Here’s the cleanest row — pip — running end to end in the rebuilt console. Select the eMudhra cert, start the MITM, and a victim’s ordinary pip install executes code at build time, with nothing touched on their machine:
Note the payload: a neutral touch /tmp/OWNED . The modules ship pointed at a harmless marker, not a weaponized flow — the point is to prove the trust decision, not to arm it.
The macOS window, and why it’s largely closed
Being exact here, because the timeline is the whole story of how narrow this stayed:
Oct 18 — the eMudhra intermediates are revoked (recoverable private keys).
Oct 19 — Apple blocks them for Safari, Mail, and anything on its security frameworks. Browsers safe without a macOS update.
Oct 26 — macOS 27.2 did not fix the command-line path, and reverted manual /etc/ssl/cert.pem edits some admins had applied.
Nov 9 — macOS 27.2.1 (and 26.7.3 , 15.8.3 ) closed it. Per Apple’s advisory: “Starting in macOS 27.2.1, these command-line tools stop accepting these certificates.” It also removed five root CAs from /etc/ssl/cert.pem — including AAA Certificate Services , the cross-sign our chain relied on. On a patched Mac, that path is simply gone.
So the macOS system-tool window was open for about three weeks and is shut. What remains after the patch is narrow but real: tools that ship their own root list (Apple is explicit — “Some apps and tools include their own list of root CA certificates and don’t use Apple’s block or /etc/ssl/cert.pem… contact the developer” ), which is exactly pip / certifi with an older bundle; plus any unpatched fleet and Linux clients whose distro ca-certificates still ships AAA.
Credit where it’s due
We surfaced the install-channel angle while rebuilding evilgrade, not before it, and we’re not claiming the CA discovery. Others flagged the macOS gap publicly first: International Cyber Digest (@IntCyberDigest) warned that git , curl and python3 on macOS still trusted the compromised certs after Apple was told, and Corey Quinn (@QuinnyPig) noted the 27.2 update “ROLLED BACK the eMudhra cert removal from /etc/ssl/.” Two independent voices landing on the same facts is what told us it was worth measuring carefully rather than loudly.
The release: evilgrade 2026
The research kept returning one verdict — the weak link had moved from the auto-updater to the install channel — and the tool needed to move with it. That’s what the rebuild is. It lived on a branch ( feature/modern-update-modules , 11 commits) and it’s mostly unglamorous engineering, which is the point: it’s the plumbing that makes the finding above reproducible.
Recursive module loader ( main.pm ): modules used to live flat; they now load from subdirectories ( modules/linux/ , modules/macos/ , modules/package_managers/ ), so coverage grows as install systems ship new footguns.
Selectable SSL cert ( set sslcert  ): choose the cert/key pair per demo ( certs/emudhra_mitm , certs/selfsigned , certs/emudhra_authorized ) instead of a hardcoded cert — so a demo can switch between a self-signed cert that should trip alarms and a chain that, against an un-distrusted store, doesn’t.
Static-dir request type in the webserver ( webserver.pm ): serves a tree of static files, which let us serve a dumb-HTTP git repo with no git backend.
Robustness fixes in the demo runners: poll the bind instead of a fixed sleep , and a fix for a Perl ABI mismatch ( env -u to keep the shell’s PERL5LIB from breaking the system interpreter under sudo ).
And the headline the rebuild earns:
225 implemented modules , 275+ documented CVEs (2018–2026) , across 18 categories — OS updaters, browsers, enterprise apps, dev tools, IoT/firmware, security/VPN, package managers (npm, PyPI, Maven, Cargo, RubyGems…), and AI/ML (Hugging Face, PyTorch, TensorFlow).
A recursive loader and an automated generator, so the catalog keeps pace.
A selectable SSL cert per module, so you can demonstrate the difference between a cert that trips alarms and a chain that doesn’t.
Use it the way it’s meant to be used — authorized only: pentests with permission, bug bounty, research, disclosure.
A short history
evilgrade isn’t new. Francisco Amato released it as ISR-evilgrade in July 2008 — the Full Disclosure post was titled “Using DNS cache poisoning to exploit poor update implementations.” The premise: software checked for updates over channels that trusted whatever answered, so redirecting a victim’s DNS turned “check for updates” into “install this.” Dan Kaminsky’s DNS flaw made that redirect trivial at internet scale, and he referenced evilgrade in his Black Hat USA 2008 talk; HD Moore’s reaction was a Metasploit post titled “Evilgrade Will Destroy Us All,” and Brian Krebs wrote it up for the Washington Post after interviewing Amato.
Version 2.0 followed in October 2010 (63 modules, DEF CON 18 ); written in Perl and open source, it moved under Faraday Security Research. The 2026 rebuild keeps the idea and moves the target — from the auto-updater to the install channel, and from a planted CA to a real leaked one. Eighteen years on, the premise hasn’t changed: software still trusts whoever holds the cert.
If you want to harden against this class (modest, not urgent)
The attack is small, but the structural weakness — install channels that make a single TLS trust decision — is worth a second opinion that doesn’t rest on one CA:
Patch macOS (27.2.1 / 26.7.3 / 15.8.3). A macOS update can replace cert.pem , so don’t restore a pre-update backup over it.
Check your certifi / pip bundles. Fixing the system store doesn’t fix a Python whose bundled roots still carry AAA. Pin or refresh certifi , prefer wheels, use a hash-pinned lockfile.
Treat curl | sh as structurally fragile. Where you can’t avoid it, pin the host’s cert/pubkey, or fetch-verify-then-run against an independent checksum instead of piping to a shell.
Prefer channels with a second signature — GPG-signed repos, Go’s checksum DB, signed artifacts. They’re the ones that didn’t fall here.
Want to see where your install and update tooling makes a one-CA trust decision — and prove which side of the line it’s on? Faraday · evilgrade on GitHub →
Sources: Apple — About the compromised eMudhra intermediate CAs (HT149555) · 9to5Mac — Today’s macOS updates fix the eMudhra gap · MacRumors — macOS 27.2.1 fixes the eMudhra flaw in command-line tools · Mozilla Bugzilla 2083449
Continue Reading
The latest handpicked blog articles
Check all articles
Argentina Tightens Telecom Cybersecurity: Is Certifying Suppliers Enough?
Argentina strengthens telecom cybersecurity with Disposition 7/2026, introducing new supply chain security requirements. Explore what changes, who is affected, and why supplier certification alone isn't enough to secure critical infrastructure.
November 19, 2026
Read article
evilgrade 2026: 225 Modules Meet a Leaked eMudhra CA
A research log, told in the order it happened. We started by pulling on the October 2026 eMudhra CA compromise — and following where it actually reached, versus where everyone
November 15, 2026
Read article
Faraday en UCEMA: compartiendo perspectivas sobre los desafíos de la ciberseguridad
Participamos de un encuentro del Posgrado en Gestión Estratégica de la Ciberseguridad de la Universidad del CEMA, donde Marcos Carabajal, CRO de Faraday, compartió una mirada sobre los desafíos actuales
November 2, 2026
Read article
Stay Informed, Subscribe to Our Newsletter
Enter your email and never miss timely alerts and security guidance from the experts at Faraday.
Thank you for Signing Up
Por favor corrija los campos marcados a continuación.
1,true,6,Contact Email,2 1,false,1,First Name,2 1,false,1,Last Name,2
Website - Suscripcion Newsletter
Faraday provides a smarter way for Large Enterprises, MSSPs, and Application Security Teams to get more from their existing security ecosystem.
Headquarters
3310 Mary St Suite 501
Miami, FL 33133, USA
+1 904 715 4284
Research Lab & Dev
Bolivar 238 2° Floor
Buenos Aires, C1066AAF
Argentina
+54 11 4331 0469
Solutions
Products
Services
Pricing
Company
Resources
Open Source
Community
First Scan
EmploLeaks
Doggie
© 2025 Faraday Security. All rights reserved.
Terms and Conditions | Privacy Policy
Faraday provides a smarter way for Large Enterprises, MSSPs, and Application Security Teams to get more from their existing security ecosystem.
Headquarters
3310 Mary St Suite 501
Miami, FL 33133, USA
+19047154284
Av. Córdoba 883 12° Floor
Buenos Aires, C1054AAH
Argentina
+5491155781884
Santiago, Chile
+56958182424
Platform
Overview
Vulnerability Management
Penetration Testing Reporting
Application Security/DevSecOps
Faraday Community
Client Portal
Services
Faraday All in One
Red Team Services
Research Lab
Company
About Us
Partner Program
Cybersecurity Events
Resources
Blog
Documentation
E-books
Trust Center
Support
Webinars
Website developed by
Cookies Settings
To provide the best experiences, we use technologies like cookies to store and/or access device information. Consenting to these technologies will allow us to process data such as browsing behavior or unique IDs on this site. Not consenting or withdrawing consent, may adversely affect certain features and functions.
Functional
Functional
Always active
The technical storage or access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network.
Preferences
Preferences
The technical storage or access is necessary for the legitimate purpose of storing preferences that are not requested by the subscriber or user.
Statistics
Statistics
The technical storage or access that is used exclusively for statistical purposes.
 The technical storage or access that is used exclusively for anonymous statistical purposes. Without a subpoena, voluntary compliance on the part of your Internet Service Provider, or additional records from a third party, information stored or retrieved for this purpose alone cannot usually be used to identify you.
Marketing
Marketing
The technical storage or access is required to create user profiles to send advertising, or to track the user on a website or across several websites for similar marketing purposes.
Manage options
Manage services
Manage {vendor_count} vendors
Read more about these purposes
Accept all
 Decline all
 Manage cookies
 Save preferences
 Manage cookies
{title}
{title}
{title}
Manage consent
Spanish

## 评论（1/1）

> **tucketi** · 2026-11-19T19:17:57.000Z　
> .

## 导航

- 项目页：[[10-项目/faradaysec.com_283f9cef]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
