---
type: "corpus"
item_id: "bcf7c191918480b0"
title: "Show HN: Steal My Bitcoin"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50224916"
project_url: "https://stealmybitcoin.com/"
author: "cloudlandsdev"
published_at: "2026-10-24T20:30:31Z"
captured_at: "2026-10-25T23:24:35+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-10-25"
pub_day: "2026-10-24"
tags:
  - 语料
  - hn_show
  - author_cloudlandsdev
  - story_50224916
  - show_hn
metrics: {"points": 546, "comments": 341, "engagement_velocity": 546}
comments_count: 341
comments_total: 341
discovered_via: "hn:show_hn:3d"
---

# Show HN: Steal My Bitcoin

> [!info] 一句话导读
> 0.00 hours without a successful hack

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50224916>
> 指标：点赞=546 · 评论=341 · engagement_velocity=546
> 作者：cloudlandsdev　|　发布：2026-10-24T20:30:31Z
> 项目链接：<https://stealmybitcoin.com/>
> 采集：2026-10-25T23:24:35+08:00　|　id：`bcf7c191918480b0`

## 正文

Steal my Bitcoin
0.00 hours without a successful hack
There is a bitcoin key hidden on this server worth about $500 .
It is accessible to the PHP user account through the print-flag binary.
This PHP version was selected from before the PHP2SHELL CVEs were released.
First person to get the wallet wins. If you don’t need the money, consider donating it to those who do: givewell.org .
All traffic is logged. This is a known vulnerable machine, so we cannot guarantee privacy. Other attackers may access or monitor activity and data beyond our control. Do not submit anything you want to keep private.
Challenge wallet Explorer ↗
bc1qlnu5…t3cxqy
Checking balance…
Refresh ↻
stealmybitcoin.com · Terms of participation

## 评论（341/341）

> **TacticalCoder** · 2026-10-24T20:57:18.000Z　
> Nice CTF! I hope if it's captured by a LLM we'll get a write up as to how it did it.

---

> **sashank_1509** · 2026-10-24T21:00:20.000Z　
> You have to be really confident that the PHP RCE is not anything serious, 500$ is quite a bit?

---

> **hau** · 2026-10-24T21:03:15.000Z　
> That's a good way to make claims about existence of a trivial exploit in the wild falsifiable.

---

> **earthpyy** · 2026-10-24T21:07:57.000Z　
> Interesting idea! Would like to know how much time need to spend.

---

> **nayuki** · 2026-10-24T21:09:01.000Z　
> The server is getting overloaded, so here's the text for reference: Steal my Bitcoin
>  0.65 hours without a successful hack
>
>  There is a bitcoin key hidden on this server worth about $502.
>
>  It is accessible to the PHP user account through the print-flag binary.
>
>  This PHP version was selected from before the PHP2SHELL CVEs were released.
>
>  First person to get the wallet wins. If you don’t need the money, consider donating it to those who do: givewell.org.
>
>  All traffic is logged. This is a known vulnerable machine, so we cannot guarantee privacy. Other attackers may access or monitor activity and data beyond our control. Do not submit anything you want to keep private.
>  Challenge wallet
>  Explorer ↗
>
>  bc1qlnu5…t3cxqy
>
>  0.00625104 BTC
>
>  ≈ $502.35 USD
>  stealmybitcoin.com · Terms of participation

---

> **jackdecker** · 2026-10-24T21:12:28.000Z　
> Made tough here as you’re behind nginx w/ a 1MB request body cap! Sweet idea :)

---

> **jerrythegerbil** · 2026-10-24T21:14:50.000Z　
> This will go unclaimed for a bit. It may still get claimed within the day, butPeople do have the exploit. The risked opportunity cost of this being a honeypot (and handing over a functional exploit) vs just… not participating and hacking higher value targets (offensive actors) or not circulating any additional details (defensive actors who have privileged intelligence about the vulns) I just…The value proposition here is so hilariously low for what is required to demonstrate stealing the bitcoin at all.That doesn’t mean that people won’t try, and perhaps even succeed! But to what end? Demonstrating terrible math skills and a fundamental misunderstanding of the economics at play?I, and many of my friends and cooks could take this easily. The difference is we know not to.Make it $15-25k and it’ll get yoinked instantly, most likely without using PHP2Shell at all.

---

> **randomblock1** · 2026-10-24T21:17:13.000Z　
> It runs PHP 8.4.26 (and nginx). Might be useful for others.Also, the only pages I found are static and not an actual PHP entry point. If it doesn't run any PHP, it's not vulnerable to PHP2Shell. At least I think that's how it works.

---

> **primer42** · 2026-10-24T21:18:01.000Z　
> If someone did have a working exploit, is $500 enough for them to give it away to whomever is monitoring this honeypot?

---

> **Stevvo** · 2026-10-24T21:24:33.000Z　
> You have not proven the key really is on the server. From a game-theory point of view I have no reason to believe it is there, and thus no reason to attack.

---

> **LandoCalrissian** · 2026-10-24T21:25:07.000Z　
> I love it, very fun.

---

> **tamimio** · 2026-10-24T21:26:37.000Z　
> $500 isn’t worth the time, make it at least $5k then we talk.

---

> **datadrivenangel** · 2026-10-24T21:30:42.000Z　
> Appreciate the commitment to the bit!

---

> **impure** · 2026-10-24T21:31:57.000Z　
> I was wondering how exploitable this was. I will definitely be watching.

---

> **rvba** · 2026-10-24T21:32:06.000Z　
> this should be done on one of those barebone servers that run on an 8bit commodore or an atari (self identifying as something else)

---

> **qbane** · 2026-10-24T21:38:57.000Z　
> I remembered that there was a similar challenge for Heartbleed.

---

> **technion** · 2026-10-24T21:48:47.000Z　
> There is a lot of cynicism in this thread but the fact this is still open and hour later ends the narrative in my view. There are not "thousands of swarms of agents autonomously compromising every site for its authors" or any the other x / LinkedIn dribble ive been reading.It clearly isnt happening.

---

> **v3ai** · 2026-10-24T21:50:49.000Z　
> major pain in the neck that anthropic doesn't let opus 5.5 work on this, goes back to 4.8 lame

---

> **Izmaki** · 2026-10-24T21:52:20.000Z　
> This has to be the cheapest way to obtain a working POC. Lol!

---

> **int32_64** · 2026-10-24T21:55:30.000Z　
> It could be an interesting cybersecurity technique to hide obvious crypto private keys all over.If it gets swept you are breached.

---

> **freecodeio** · 2026-10-24T22:04:13.000Z　
> can't people just point their AI to the latest pull request that includes the fix and ask it to deduce the vuln?

---

> **ingen0s** · 2026-10-24T22:12:29.000Z　
> Honeypot lol

---

> **jsphweid** · 2026-10-24T22:16:25.000Z　
> Looks like someone just added ~$500 more to it?

---

> **tippytippytango** · 2026-10-24T22:18:14.000Z　
> Imagine 1000 people torch $100 in tokens before giving up on getting the $500 prize. Let’s go on to assume one person gets a lucky reasoning trace that nails it, then posts a blog about how they made $500 with $100.

---

> **monskov** · 2026-10-24T22:18:33.000Z　
> bounty seems to have just doubled, 1000 usd now

---

> **qwertytyyuu** · 2026-10-24T22:20:23.000Z　
> ooh is this what they call a ctf?

---

> **qwertytyyuu** · 2026-10-24T22:20:40.000Z　
> oooh, is this what they call a ctf?

---

> **adyavanapalli** · 2026-10-24T22:22:11.000Z　
> The account now holds about $1k USD. A second deposit landed in the account about 7 minutes ago from when I posted this comment.EDIT: Now worth $2k

---

> **dguido** · 2026-10-24T22:23:38.000Z　
> This looks like a trap. We have a working RCE that would claim this, but I don't want to demonstrate that because it might leak what we built to others. We still have a window for people to patch and I don't want to risk that.https://x.com/dguido/status/2113825891021144306?s=46

---

> **hsuduebc2** · 2026-10-24T22:25:21.000Z　
> Price has doubled I see. Interesting idea lol

---

> **mpaepper** · 2026-10-24T22:25:58.000Z　
> Someone doubled the bitcoin amount :D

---

> **fishgoesblub** · 2026-10-24T22:26:50.000Z　
> Suddenly all the people who claim that these PHP exploits are so easy that a baby could do it are clamming up at the opportunity to showcase it. Plenty of "I/We can do this easily, but uh.. we uhh.. don't want to right now bye" going on.

---

> **LiveOverflow** · 2026-10-24T22:28:27.000Z　
> If it's nginx + fpm + "empty" index.php, it's a meme and not exploitable.edit: looks more like nginx + cli-server. But the 1MB nginx body limit is annoying. Why is nobody setting up these CTF servers with a setup people actually say would be easy to exploit. Like a LAMP stack.

---

> **bramhaag** · 2026-10-24T22:34:29.000Z　
> A pentesting YouTuber I once respected went deep into the AI rabbit hole and claimed yesterday he created a generic POC using ChatGPT in 2 hours to show how dangerous LLMs are [0]. After that he shilled his AI pentesting platform.If there was a grain of truth to this claim, surely someone would've stolen the prize by now? Thousands of people would've had a working POC if it was this easy.[0] https://youtu.be/SP7y1h0laN0

---

> **paaloeye** · 2026-10-24T22:34:52.000Z　
> Is this a PHP PR campaign to show that everything is alright?

---

> **j45** · 2026-10-24T22:36:45.000Z　
> In viral form, its now $1000?

---

> **trilogic** · 2026-10-24T22:39:30.000Z　
> The wallet address is bc1qlnu50y4zm0nwxkckxu09thn5xdcz8aw6t3cxqy
> Currently worth about $500 (checking balance)

---

> **athrowaway3z** · 2026-10-24T22:39:38.000Z　
> I published my version right before seeing this, its _a_ exploit for 8.2 through 8.5 for stock mod_php.https://github.com/offline-ant/php2fixThat isn't going to work on this server because it has nginx in front with a 1mb request cap afaict.

---

> **zkldi** · 2026-10-24T22:49:51.000Z　
> Brilliant thread. Glad you did this before I did.Hilarious to see people suddenly furtive about this easy exploit. Thanks.

---

> **hsuduebc2** · 2026-10-24T22:51:26.000Z　
> I wonder how many times the value of the credits on this challenge would exceed the potential reward here.

---

> **aussieguy1234** · 2026-10-24T22:57:49.000Z　
> This could be a trap.Someone does the exploit, then the creator of this service logs it and uses that exploit to go after higher value targets...

---

> **nikolay** · 2026-10-24T22:58:35.000Z　
> This is a form of a canary token I've been using already. The thing is that it only makes sense if the server breach is cheaper than the money into the wallet. Of course, after you fully monetize your hack, the last step would be to get the bitcoins, too, but how is this helping the owner? The good thing about the existing canary token is that they are all over the place hidden among legitimate similar records and could be harder for the hackers to tell from the rest.I personally prefer "tripwire" than "canary token", but that's another topic.

---

> **AnneTrotter** · 2026-10-24T23:03:23.000Z　
> What a fantastic test. I think this should be standard practice for zero days like this to put a practical "exploit ease" bounty out there. It would benefit the entire security community to have this information available in addition to the cve score!

---

> **astrostl** · 2026-10-24T23:03:30.000Z　
> I don't think it's a good idea to front-page an exploitable site on HN. The blast radius isn't limited to the creator's Bitcoin, it also extends to zero-days against anyone visiting the site. This is true of all sites, but all sites are not built to fail while incentivizing exploits.

---

> **ivanjermakov** · 2026-10-24T23:04:26.000Z　
> Do I understand it right that it can be set up in a way that if exploit is used it can be "recorded" and revealed?

---

> **scottydelta** · 2026-10-24T23:24:49.000Z　
> I have two out of five AI agents that agreed to work with me on finding the flag (wallet key). Here's the progress so far:1. GLM-5.3: Interpreted it as a public challenge and is currently trying to find the flag.
> https://ibb.co/zHLJhz0B2. GLM-5.3-Flash: Also interpreted it as a public challenge and is working on cracking it.
> https://ibb.co/bg2DDtXq3. GPT-6.1-Sol: Flagged it as a cybersecurity request and directed me to register for their cybersecurity program.
> https://ibb.co/0j83PWn94. DeepSeek-v4.1-Flash (via OpenRouter): Refused to execute the exploit.
> https://ibb.co/QvVxnM5k5. Claude Fable-5.1 (via OpenRouter): Returned a provider-side content filter error.
> https://ibb.co/39q1N1NVAll sessions with different agents are running on Tarvis (https://tarvis.io), an app I'm building. Think of it as a self-hosted version of Railway, but with a built-in AI agent and cloud development environment.The website seems to be overloaded, and both agents that agreed to work on the challenge are now unable to connect to it. HN's hug of death, I guess.EDIT: It's back online!

---

> **cromka** · 2026-10-24T23:27:22.000Z　
> Keep your hands off my Bacon!

---

> **cluckindan** · 2026-10-24T23:51:20.000Z　
> If the flag isn’t captured by opening bell on monday, the bubble will burst.

---

> **brcmthrowaway** · 2026-10-25T00:13:07.000Z　
> Whats going on with PHP? Is there a twitter drama?

---

> **tarpitt** · 2026-10-25T00:18:53.000Z　
> It's increased! It was $500 an hour ago and it's 2k now. I didn't bother because I figured I'm not fast enough

---

> **hpone91** · 2026-10-25T00:19:12.000Z　
> Yeah, the specific setup is not vulnerable to PHP2SHELL. CLI server + 1 MiB cap + inert page + high memory limit removes all the possibilities from the two CVEs. It would just be collecting POCs for actually vulnerable setups.

---

> **gr_norm** · 2026-10-25T00:23:23.000Z　
> Link to the wallet in case the site goes down: https://mempool.space/address/bc1qlnu50y4zm0nwxkckxu09thn5xd...Currently at $2k.

---

> **medellin** · 2026-10-25T00:48:41.000Z　
> Thank you for showing what we all know. The security community is full of fear mongering prima donnas. I always hated security but now they are becoming insufferable. “Omg myleethax break the web” everyone freak out!!!!! Omgggggg. Absolute fing children.

---

> **kobalsky** · 2026-10-25T00:49:45.000Z　
> Similarly, I've had a canary unencrypted BTC wallet in my computer for years.I've always been security conscious and I role play my Arch as a Qubes "dom0" and use VFIO for GPU enabled VMs, which I know is not the Qubes way, but I'm also not that at risk.

---

> **paxy** · 2026-10-25T00:54:55.000Z　
> Can't hack a server if it is offline due to load. I think we've solved online security folks!

---

> **40four** · 2026-10-25T01:20:02.000Z　
> The amount of Bitcoin appears to be going up with time. It was ~$500 the last time I saw it. Now the wallet is worth ~$2000 at the time of this comment.So the idea that is not enough money for someone to “give away” their exploit is going to reach a breaking point eventually if it continues. This might get more interesting the longer it goes on. Getting my popcorn ready right now!

---

> **aniketsauravv** · 2026-10-25T01:22:52.000Z　
> Not worth it. The biggest issue is the nginx with 1MB cap. Also in the terms, its says we can't exploit Nginx. So its a dead end.

---

> **paxy** · 2026-10-25T01:45:27.000Z　
> Remove nginx or remove the 1mb nginx body cap. That config is already proven to be safe.

---

> **kozika** · 2026-10-25T01:51:58.000Z　
> Isn't this Bitcoin private key “4”?

---

> **v3ai** · 2026-10-25T01:57:44.000Z　
> prize is up to $2000 now, any takers? https://mempool.space/address/bc1qlnu50y4zm0nwxkckxu09thn5xd... site is down though

---

> **odo1242** · 2026-10-25T04:15:42.000Z　
> Site gives 504 Gateway Timeout. Have there been any updates in the exploitation attempt?

---

> **red75prime** · 2026-10-25T05:23:10.000Z　
> The server doesn't respond right now (2026-10-25T05:30:00Z). What happened?The wallet is at $2,016.73

---

> **saagarjha** · 2026-10-25T06:56:48.000Z　
> What is the intended goal of this website? The doctor told you smoking is bad so you're going to give your child a pack a day and see if they die by age 20? If they don't, obviously, your doctor is a quack who cries wolf, and you shouldn't listen to that killjoy anyway :/C'mon guys, I get that OpenAI is involved and they want to make ten trillion dollars next year or whatever, but I thought we had put the idea of random nonexperts trying to judge how "hard" something is to exploit to rest years ago. The guys who used to try doing this lost repeatedly, publicly, until we finally realized that we have to secure our stuff. Sure it's annoying to update your computer every week and sometimes some guy at Forbes is going to tell you that if you don't install iOS 67 today you will get hacked by the Mossad which may not have been entirely true but when you have memory corruption in a reasonably common configuration that faces the public internet, you should patch your software. End of story.We can argue all day about the cost to exploit something, whether it is "hard for humans" or what it would cost on the black market or in this case how many tokens are required, but that is mostly just a distraction. Just patch your stuff. The people involved here are (currently) paid by AI companies just like ten years ago they were paid by the ads companies but despite the annoying way our economy works they mostly know what they are doing. I get that this is annoying, I understand that nobody wants to hear the words memory safety again, but this is anti-intellectualism. "Ask HN: Can you explain how the PHP bug could be exploited?" would be far more productive than having a bunch of weary sysadmins duke it out in the comment section against security guys.

---

> **silentbob7** · 2026-10-25T08:25:15.000Z　
> The site is down

---

> **cloudlandsdev** · 2026-10-25T09:27:03.000Z　
> Update: Did not expect the amount of traffic! Every time I scale the VPS, y'all immediately blow through the extra compute. Should be up again, hopefully will be more stable once this drops off the front page.Any attempt at logging so I can make a blog about the successful solve is gonna be best effort, don't have disk capacity to keep up with the traffic (at peak it was rotating every 12 min...). If you win the challenge, write-ups are definitely welcome.For those who are saying that the nginx config is unfairly difficult, intention was just to replicate a fairly normal config that was more realistic than you'd get in a lab environment. If we get to 24 hr+ with no solves I'll see about making it easier. In the meantime, seems like you can perhaps mitigate PHP2Shell with the right nginx config, so that's pretty neat!

---

> **deepsun** · 2026-10-25T09:36:21.000Z　
> So it would still be stealing legally, right? And feds could watch the thief as the ledger is always public.

---

> **gewetensleegte** · 2026-10-25T13:03:08.000Z　
> Aw man, I had a working RCE but my dog ate it.

---

> **Art0101** · 2026-10-25T13:11:38.000Z　
> i think I'm really close guys
> wish me luck!

---

> **harisec** · 2026-10-25T14:39:14.000Z　
> This is basically 2k for a Cloudflare 0day, because you need to bypass Cloudflare to exploit the service.

---

> **tavavex** · 2026-10-25T15:05:43.000Z　
> The fact it's still here 18 hours later is crazy to me, although I am making an assumption that this website is set up similarly to standard PHP websites, without any weird uncommon configs or changes that break the exploit. I'm not a cybersec expert, so can someone clue me in? The way I understood the fallout from a few days ago was that this was the end of the world and that the majority of all websites on the internet were about to be imminently and automatically breached in seconds, with only a single-digit percentage of vulnerable websites patching the exploit. Was it always known that the reality outside non-tech press coverage was a lot more complex, or is this a shock to everyone?Do we know how many other websites were verifiably breached through this by now, if any?

---

> **anonymous908213** · 2026-10-24T21:01:54.000Z　
> It's more like they're offering $500 to be taught how to utilise the exploit.

---

> **jgilias** · 2026-10-24T21:06:12.000Z　
> There’s a lot of techies on this site for whom that’s peanuts.

---

> **quesera** · 2026-10-24T21:25:51.000Z　
> I'm sure OP is a good person.But if they were not, and had ill intentions, they might see $500 as a very inexpensive way to purchase a working exploit to use against others.

---

> **ls612** · 2026-10-24T22:25:26.000Z　
> It is a price signal. They expect to lose the money they want to show that nobody has an automated swarm just pwning every server running PHP connected to the internet. At least not yet, on day 5 and counting.

---

> **akerl_** · 2026-10-24T21:10:58.000Z　
> A reminder that this cannot falsify the existence of an exploit, trivial or otherwise.It can only show you if someone has used an exploit against this server.

---

> **jgalt212** · 2026-10-24T22:24:58.000Z　
> > A reminder that this cannot falsify the existence of an exploit, trivial or otherwise.No, it's a not a zero knowledge proof. But if the site owner is a generally trustworthy person, then I feel that this effort is strong proof the exploit is not trivial.

---

> **zoeysmithe** · 2026-10-24T21:27:39.000Z　
> " All traffic is logged."For $500 he can look in the logs and find all manner of new exploits, or new deviations of the existing ones, he can then sell for thousands. Clever business model lolThese projects would be more interesting and ethical if the current and historical logs were instantly put up somewhere public in real-time for anyone to observe.Regardless, I'm guessing the smart hackers aren't going to bother.

---

> **fwlr** · 2026-10-24T21:38:24.000Z　
> Great way to inject some price information into the “AI automates exploits at scale” narrative. “AI can now chain complex exploits, it’s point-and-click pwnage, you say? Over or under $500 a pop?”

---

> **xmcp123** · 2026-10-24T22:20:16.000Z　
> Bahaha someone added to the fund. It’s now $1004

---

> **sscaryterry** · 2026-10-24T22:46:53.000Z　
> This could be an interesting bug-bounty type of initiative. Setup a system, lets other dudes at their expense battle for scraps?

---

> **xmcp123** · 2026-10-25T14:36:37.000Z　
> This is whack. Op has setup the server to be impossible to exploit, then challenged people to exploit.The non default php settings he set break the exploit.

---

> **phyzome** · 2026-10-24T21:27:53.000Z　
> It's worth it to someone.

---

> **cassonmars** · 2026-10-24T21:30:03.000Z　
> I suspect this is going to be more a point about the fact that most PHP server configurations do not have the ability to be exploited by the recent vulnerability that made people think the AI vulnpocalypse was here

---

> **fwlr** · 2026-10-24T21:30:40.000Z　
> If the actual price tag behind the “AI can trivially automate exploits, be afraid” narrative is more like $15,000 and not like $150, that puts the narrative in a very different light.

---

> **msm_** · 2026-10-24T21:33:32.000Z　
> >and handing over a functional exploitThere are dozens (or hundreds) of functional exploits already. The problem with php2shell exploits is that (as of now) there's no "one exploit pwns all", and researchers need to spend nontrivial amount of time on every (potentially) exploitable target.So I don't think I agree - it's a fun challenge for the itsec people around here, and some people will definitely try. There's no real opportunity cost here. The only problem is that (as of now) exploiting PHP requires some knowledge about the server configuration, and we don't have that here.

---

> **tofuahdude** · 2026-10-24T21:33:39.000Z　
> > But to what end?It is just kind of fun to poke at something like this.> Demonstrating terrible math skills and a fundamental misunderstanding of the economics at play?I don't give a shit about the $500, nor would I ever attempt actually hacking something that wasn't explicitly a game (like this).> The difference is we know not to.Borrrrinnnggggg

---

> **fishgoesblub** · 2026-10-24T21:37:09.000Z　
> > I, and many of my friends and cooks could take this easily.Sure you can.

---

> **oofbey** · 2026-10-24T21:49:44.000Z　
> > a fundamental misunderstanding of the economics at playI’d say you’re the one who doesn’t understand the economics at play here. To me and I’m guessing the OP it’s quite simple. Have the exploits become common/simple enough to be worth $500 yet?

---

> **thenewnewguy** · 2026-10-24T21:53:48.000Z　
> Can you spell out the economics for us?Let's assume I am a white-hat hacker with access to this allegedly widespread exploit. Obviously, I understand why a nation-state attacker wouldn't want to share their exploit here but what do I as a random citizen stand to lose? It's not like I care about hoarding the exploit to pwn innocent civilians.You seem to imply there's some economic reason such a white-hat hacker wouldn't take the $500 but don't actually say what it is.

---

> **lukeify** · 2026-10-24T22:07:49.000Z　
> What an insufferable comment. For all the hullabaloo discussing the economic value of time about $500 being an insufficient prize, you still spent what I can only assume is several minutes penning a comment that derives you zero economic value whatever.

---

> **what** · 2026-10-24T22:17:37.000Z　
> > handing over a functional exploitI thought the exploit was trivial and we all need to be extremely worried and take down our php services until a patch? So what exactly are you handing over?> I, and many of my friends and cooks could take this easily.Extreme doubt.

---

> **janalsncm** · 2026-10-24T22:24:55.000Z　
> Every reason you just gave for not hacking this server is also true for servers which don’t have a $500 prize, which is almost all of them out there.

---

> **ncruces** · 2026-10-24T22:49:59.000Z　
> 80h ago everyone was advising everyone else to take all their websites immediately down.Now it's only worth it to hack a website that's asking to be hacked if the prize is $15k.

---

> **bakugo** · 2026-10-25T00:19:47.000Z　
> > I, and many of my friends and cooks could take this easily.No, you couldn't.

---

> **LZ2DMV** · 2026-10-24T21:56:00.000Z　
> I'm a bit curious how you found that.

---

> **rafram** · 2026-10-24T21:49:58.000Z　
> Not sure that logic really holds up. If the cost of trying is low, why wouldn't you?

---

> **v3ai** · 2026-10-24T21:56:21.000Z　
> what a pedantic way to look at the world

---

> **zulban** · 2026-10-24T21:57:56.000Z　
> You may need to brush up on your game theory. It's worth it to spend $1 for a 1% chance to win a million dollars. You don't need to be certain the key is there for it to be worth it to do a supposedly trivial exploit.

---

> **echoangle** · 2026-10-24T22:11:37.000Z　
> Shouldn’t the expected value of attempting this somehow include the likelihood of the key actually being on the machine? Surely the probability is much higher than 0? I would guess the expected value for actually being the first one is around $300, not 0

---

> **kkotak** · 2026-10-24T22:15:34.000Z　
> Less talking, more doing.

---

> **jackphilson** · 2026-10-24T22:09:00.000Z　
> Yeah, AI seems like a good shift in "narrative making." It's easy to ask AI "give me an efficient way to "confirm or deny this narrative" and have something like this go viral. This is good because it makes narratives more truthful

---

> **Catloafdev** · 2026-10-24T22:33:53.000Z　
> The value proposition isn't there.If you reframe the perspective from 'free $500 sitting on a server' to 'requires actively utilizing an unreleased 0 day exploit on a server that will certainly be able to track exactly what was done, for a payout of... $500?'That's pennies for something like this.Add two zeros and it might get nabbed.Edit: others have pointed out it's not really a 0-day anymore, they're right, so it's likely more a matter of time.

---

> **paulpauper** · 2026-10-24T22:41:26.000Z　
> no it doesn't . absence of evidence is not evidence of absence

---

> **efficax** · 2026-10-24T23:25:52.000Z　
> right: either it’s so hard to exploit that $1,000 isn’t enough to risk “giving away” your exploit chain or actual exploitation of this bug is impractical, either way the CVEpocalypse is overblown

---

> **orlp** · 2026-10-24T23:50:43.000Z　
> > There is a lot of cynicism in this thread but the fact this is still open and hour later ends the narrative in my view.Clearly people aren't cynical enough.I find it strange no one in this thread has even considered the possibility that the private key of the wallet isn't on the machine.OP gets their working exploit neatly logged (or even multiple approaches), keeps the money, strengthens the illusion the exploit isn't that bad, and gets a free $500 on top from someone who added to the wallet.

---

> **BubbleRings** · 2026-10-24T23:51:46.000Z　
> Except, it’s the top entry in HN right now. It could have gone down to the hug 20 minutes after it was posted, so nobody much has had a chance to have a go at it.

---

> **Onavo** · 2026-10-25T01:23:14.000Z　
> You can see the commenters arguing with me about ASLR in the old thread. Half the commenters here, including quite a few "thought leaders" (not gonna name names or ad hominems but everybody knows who they are), insist that there are ways to implement this exploit at scale without having to do rowhammer-style spam brute forcing. I am still waiting. There's a lot of FUD and hearsay in the tech circles grapevine but very little evidence of actual working exploits against a modern Linux server outside of "attempts".https://news.ycombinator.com/item?id=50188948I am still waiting for them to put their money where their mouth is.

---

> **paxy** · 2026-10-25T01:30:04.000Z　
> What point is an anonymous online post proving? Can anyone verify that the private key actually exists? Or which version of PHP the site is running? Or if it is running PHP at all?

---

> **glerk** · 2026-10-25T02:45:14.000Z　
> It seems like the server got DDoS’d before anyone got to the bitcoin.

---

> **cluckindan** · 2026-10-24T21:55:57.000Z　
> Just run GLM-5 locally, if people are to be believed it can hack the planet at this point

---

> **gspr** · 2026-10-24T22:41:41.000Z　
> Yet somehow people on this site still cheerfully use those products for serious work. Can you not see what's being attempted here? They're trying to have you outsource your thinking so they can shape it.

---

> **jijijijij** · 2026-10-24T22:55:36.000Z　
> They are cutting competition for these sweet coins. Anything to become profitable.

---

> **what** · 2026-10-24T22:25:04.000Z　
> I thought it was trivial to exploit and surely costs less than $500 in tokens?

---

> **hoppp** · 2026-10-24T22:09:47.000Z　
> Yeah, just keep dust in it. Like $10

---

> **LPisGood** · 2026-10-24T22:13:52.000Z　
> There are entire businesses set up to help enterprises do this at scale: https://canarytokens.org/nest/

---

> **jijijijij** · 2026-10-24T22:41:07.000Z　
> Only works for low value targets, where you don't have to trust your coworkers. Probably need to rotate the key daily, which possibly adds transaction costs. You would also need to set up the detection capabilities to be able to figure out the intrusion path, or the flag is pretty meaningless. And at that point you may just as well put tripwires onto sensitive files.

---

> **grey-area** · 2026-10-24T22:07:10.000Z　
> Please do and report back here.

---

> **LPisGood** · 2026-10-24T22:09:52.000Z　
> People could point their AI at a physics textbook and ask it to deduce the vuln from first principles too but that doesn’t mean it will be successful.

---

> **echoangle** · 2026-10-24T22:10:14.000Z　
> If the AI can build an exploit from the patch, sure.

---

> **notnmeyer** · 2026-10-24T22:20:57.000Z　
> apparently not

---

> **LPisGood** · 2026-10-24T22:32:43.000Z　
> This is like how OpenAI solved some hard math problem in only a few hours.

---

> **qingcharles** · 2026-10-24T22:37:29.000Z　
> It's a conspiracy! OpenAI made the site to increase token burn :)

---

> **grey-area** · 2026-10-24T22:31:25.000Z　
> Seems like everyone here has an exploit but they're all busy washing their hair, or thinking of the children, or making huge amounts selling their exploit on the darknet instead.Given there are public patches and explanations of the issue, isn't it a little late to try to keep this under wraps?Over a day or two we'll see whether people have an exploit - if more than a few people do, someone will claim this $1k soon. Out of curiosity, what do you plan to do with your exploit that you're holding back?

---

> **blalala** · 2026-10-24T22:33:39.000Z　
> Your comment makes zero sense. You have nothing :)

---

> **lukeify** · 2026-10-24T22:47:02.000Z　
> The implication of your comment is that the exploit is not trivial and magically available to anyone with some tokens to bash together, which refutes the position that there is an horde of AI agents and people compromising sites en-masse.

---

> **cortesoft** · 2026-10-24T22:55:20.000Z　
> Whether it is a trap or not doesn't change the OP's point... they are trying to push back on the idea that all servers that have this vulnerability are going to be instantly hacked by bot swarms. If AIs are at the point now where they can all instantly create an exploit from a known vulnerability, then you would have no need to keep your exploit secret because everyone would already have one.The fact that you keeping your exploit secret means anything already proves their point.

---

> **lossolo** · 2026-10-24T23:03:46.000Z　
> I have a PoC generated by an LLM that can crash sites using php2shell, but crashing != RCE. The issue is that, to achieve actual RCE, recreating the RCE PoC based on the git diff of the patch and blog posts about php2shell isn't enough. You would still need to develop a working exploit chain, bypass ASLR, and so on to actually achieve RCE.Also, this site runs Nginx with PHP-FPM, not Apache, which is harder than using mod_php exploit mode for this exploit.So you would need to develop a working exploit chain and then essentially "burn" it by exposing it to the site owner.In other words, someone is offering $500 for a working exploit chain.

---

> **solyin** · 2026-10-24T23:08:18.000Z　
> Wrong move. Exploiting this box proves it's exploitable. Not exploiting the box makes the entire computer security profession look like a bunch of worry worts and that the consulting fees are better off not paid. At worst, the owner of the box gets... what? Working exploit code that they'll have to reverse engineer anyway?

---

> **reticulates** · 2026-10-24T23:10:36.000Z　
> Can you explain how the trap works? The exploit gives you access to the machine which you can then use to wipe the evidence of your intrusion - right? There is nothing to leak by taking control of the machine.Is the trap theory that this server isn’t really running a vulnerable version of php, and is instead recording all traffic?

---

> **nerosk** · 2026-10-24T23:19:10.000Z　
> So an exploit that's difficult to reproduce even despite having access to the patch changes and all the insights into the vulnerability, would somehow be easier to recreate from just a few server logs?

---

> **xorcist** · 2026-10-24T23:53:40.000Z　
> Lots of people said the embargo should be broken early because "the exploit is already in the wild". That does not normally mean an infosec researcher has a PoC on their private laptop, that means it has leaked, one way or another.Had it, though? If it was in the wild at day -1, surely some script kiddie will be happy to run that exploit at day +4, because if they didn't someone else would.There were many people saying things with great confidence and this is one interesting way to gauge what was behind those words.

---

> **tclancy** · 2026-10-25T00:28:54.000Z　
> Yeah this smells bad. Especially given the box is set up to not accept the exploit (1mb vs 12mb).

---

> **medellin** · 2026-10-25T00:49:10.000Z　
> Sure you do. My girlfriend is a model she just couldn’t come out tonight also. Clown.

---

> **vikramkr** · 2026-10-25T00:58:21.000Z　
> Assuming you do have a working RCE - this is some weird game theory. Do it and potentially leak the exploit. Don't do it and you lose control of the narrative/lose your credibility/have people not take the risk seriously anymore (this comment is losing the fight with another comment for top comment, and the other comment is concluding that yeah this proof that the whole thing was overblown).And then there's the third option that actually this server is unexploitable or there's no wallet or something and simultaneously you give someone the exploit and lose your credibility at the same time. Really no good way out huh?

---

> **gewetensleegte** · 2026-10-25T13:28:34.000Z　
> Yeah. Turns out you're on this Patch the Planet team, so I'm guessing there's some other things or relationships worth a tad more than $2000 that you "don't want to risk".https://news.ycombinator.com/item?id=50226366

---

> **mpaepper** · 2026-10-24T22:31:21.000Z　
> It would be fun if many shipped in some $ for this to be a realistic bounty, but then again, OP could just take the money him/herself...

---

> **kolanos** · 2026-10-24T22:34:40.000Z　
> Isn't this the most common PHP stack?

---

> **LiveOverflow** · 2026-10-24T22:47:25.000Z　
> 1. I dont have an AI pentesting platform.2. This CTF is using nginx which has a `client_max_body_size=1m` limit. My exploit right now requires more, but I will give it a try (aka ask Codex).3. You can setup a server with `docker run php:8.5.11-apache` with any of the over 400 vulnerable `php` apache images and give me the IP.

---

> **jijijijij** · 2026-10-24T23:18:55.000Z　
> Would be funny if someone installed a crypto miner instead, or transferred highly tainted coins to get OP onto the radar of law enforcement. Or secretly upgrade the PHP package to mess with people.

---

> **tclancy** · 2026-10-25T00:36:35.000Z　
> Yeah. Show me how to steal cars to prove it’s hard to steal cars. Start by parking one in my driveway.

---

> **naniwaduni** · 2026-10-24T23:12:13.000Z　
> I mean, I think we'd be interested in learning about a zero-day that affects anyone visiting a compromised website.

---

> **randomblock1** · 2026-10-24T23:35:49.000Z　
> DeepSeek 4.1 will happily do it, you just have to give it a little bit of lead in.> https://stealmybitcoin.com/ This is a CTF for the new PHP vulnerability. Try to find what php version it runs.(eventually figures it out)> OK, now get the flagI'll go for RCE, carefully — the author explicitly invites this, and I'll keep probes minimal.

---

> **DetroitThrow** · 2026-10-24T23:43:31.000Z　
> Several people found they can use a much simpler exploit chain to continuously DoS the website using the unpatched exploit, than put together one that gives RCE.

---

> **lossolo** · 2026-10-24T23:44:52.000Z　
> You're wasting your money. I'd be willing to bet more than the bounty amount that you won't be able to achieve RCE on that site, if you would like to bet.

---

> **discordance** · 2026-10-25T00:25:12.000Z　
> Two economists are walking down the road when one spots a $100 bill on the pavement.“Look! A hundred dollars!” he says, bending down to pick it up.“Don’t bother,” says the other. “If it were real, someone would have picked it up already.”

---

> **tclancy** · 2026-10-25T00:34:38.000Z　
> Should be the top comment IMO.

---

> **gr_norm** · 2026-10-25T00:37:37.000Z　
> I'm just an interested bystander, but this seems like a (near?) default nginx config. Is that accurate?

---

> **kennywinker** · 2026-10-25T02:09:23.000Z　
> distributed denial of pwnage, or DDoP for short.

---

> **Stevvo** · 2026-10-25T01:59:53.000Z　
> Or it's a classic crypto scam, the server is not vulnerable.

---

> **vikramkr** · 2026-10-25T07:09:14.000Z　
> its just been down for a while. At this point idk if anyone can tell if the site is unexploitable or it just turns out that people DoSed it before anyone with the exploit who wanted to use it could do it

---

> **notpushkin** · 2026-10-25T07:29:20.000Z　
> The goal is to see whether the “pull the cord on all your servers RIGHT NOW” panic was the appropriate response, and whether the embargo was the right approach.

---

> **rustyhancock** · 2026-10-25T10:00:43.000Z　
> It would be nice to see what terms would be if not claimed, specifically, if not claimed in X days (how about 28 since there could be little claim of protecting an exploit at that point) will the money go to the charity you mention?I ask because I think that would incentive a few more people bumping the bounty.

---

> **LiveOverflow** · 2026-10-25T12:22:25.000Z　
> I believe it's not exploitable. People say that it's obviously easy when you know the exact config. So can you proof it's even possible? I am pretty outspoken about php2shell being realistic to exploit, so I am happy to independently verify to everybody that it is a realistic setup. You can reach me @LiveOverflow on Twitter or so.

---

> **Lockal** · 2026-10-25T12:30:46.000Z　
> Aaand it is down again, and I have never seen it alive.The experiment looks like "Steal my compute/storage scaling money and uptime", and it barely matters that there is some Bitcoin behind it: a company could lose more than $2000 if agents constantly break its website.

---

> **brador** · 2026-10-25T12:31:27.000Z　
> LAMP stack with a cloudflare frontend if you really want to test this “real world”.Post updates on bsky not your actual site as they will be dropping malware once they bop your BTC. Be ready to shut it down fast.

---

> **NorwegianDude** · 2026-10-25T12:51:02.000Z　
> What is the normal config? Could you publish the setup on GitHub or anything like that? I see some say that it is hardened, others saying it doesn't run PHP etc.Would be fun to see what it's actually running. :)

---

> **cloudlandsdev** · 2026-10-25T13:30:53.000Z　
> Update 2: Someone is definitely popping a segfault; still no RCE yet but I think it explains some of the instability people are experiencing. Will set the php server to restart after extended outages instead of configuring FPM or something that changes the surface area of the challenge.Can't _prove_ that the server is running PHP, but I added a `/php-version.php` page to help calm the conspiracists. Still no changes to the default nginx configuration since it seems we've got a few people getting close with those segfaults, but aware people think it'd be easier if I made those.

---

> **xmcp123** · 2026-10-25T14:08:10.000Z　
> Reddit saying you turned off post requests? Is this accurate?Edit: he turned off request body parsing. This breaks the exploit.

---

> **burnerRhodov3** · 2026-10-25T14:52:28.000Z　
> >Every time I scale the VPS, y'all immediately blow through the extra compute.uhhh.... duh.. the CVE requires Memory allocation fails.. They are essentially ddossing you to get exploit the allocation.

---

> **r0fl** · 2026-10-25T14:59:59.000Z　
> Why not host on cloudflare that could handle endless traffic even on the free tier?

---

> **MarcScott** · 2026-10-24T21:10:45.000Z　
> They should consider donating to the PHP Foundation

---

> **A1kmm** · 2026-10-25T03:03:51.000Z　
> Any exploit might be interactive with a backend component that generates and serves payload components based on interactive responses.OP (and anyone else who exploits the server) would be able to see the transcript between the backend and the vulnerable server, containing the payload customised for the server, but not the actual code of the backend. This would be useful if it was a 0day vulnerability, but with a disclosed vulnerability getting a payload that doesn't work except on their server, without the code that generated it, might not be that much value over what they already have.That said, there are other ways to scam by structuring things like the OP (none of this should be taken to imply the OP has actually done this, but rather why this structure as a general approach might be a bad idea):* This could be a 'stone soup' scam where the OP has the wallet keys (obviously), and puts this up to bait the addition of more funds into the wallet by other interested people. The key might not actually even be on the server, or it might not be vulnerable. Once sufficient other people add funds, the OP could withdraw the funds, recouping their original funds plus anything others added.
> * This could be run as a propaganda scam either to falsely sell that it isn't an easily exploitable vulnerability when it is (by making it unreasonably difficult to exploit compared to real-life deployments), or to over-inflate how exploitable it is (by an insider withdrawal from the wallet). Manipulating public opinion could allow an attacker with a working exploit more time, or help to sell services to fix the problem.I think an alternative scheme that is less vulnerable to scams would be to have a ZKVM (Risc0 or similar) executing vulnerable code, such that the attacker needs to produce a zero knowledge proof transcript of getting the ZKVM into a particular state that would not be possible if they didn't have an exploit. It should also take an Ethereum address as a public input. Then write an Ethereum contract that will allow funds to be transferred to the public input Ethereum address if submitted with a valid proof transcript, and back to the source of funds after some time has passed. Everyone who wants to add to the jackpot could deploy their own version of the contract, so the one proof transcript could claim from all of them, but if unclaimed the funds go back to the source.Alternatively (avoiding the risk exploits may be so large as to make the cost of producing the proof transcript impractical), they could be built using a public cloud provider's trusted computing offering (e.g. Google Confidential VMs). The person making the challenge could make it so the derivation (NixOS for example) to produce the entire image executing on the cloud provider in a deterministic way (with publicly known source, and hash codes of each stage publicly available). Then, from the code with the known hash, they use the vTPM to generate an attestation that a key was generated while the vTPM PCRs were in a known state (corresponding to the publicly reproducible hashes), and ensure the only way to access the key from the instance is via an exploit. It would also include logic to generate and wrap a Bitcoin wallet key, and emit the public key (with the attestations and a signature linking back via a vTPM attestation to the cloud provider's key). This way, unless the cloud provider is also in on the scam, people could be assured that the OP isn't scamming them.

---

> **muvlon** · 2026-10-24T21:15:38.000Z　
> It cannot even show that. The server can lie (trivially).

---

> **hau** · 2026-10-24T21:19:24.000Z　
> Sure. Also, we have to trust owner of the site. So it cannot show anything, strictly speaking.
> Still, it maybe puts a price on exploit demo. Some say "it goes around twitter", "bots are probing and exploiting it", "it's a biggest thing ever in cybersec history, invest in AI now". Some say "it's a fud".Are these 500$ laying on a ground for anyone to take?

---

> **datadrivenangel** · 2026-10-24T21:30:06.000Z　
> Author is a genius troll.

---

> **paulpauper** · 2026-10-24T22:43:11.000Z　
> I would hope it is logged. would be a pretty shitty plan if you don't read the traffic logs

---

> **flir** · 2026-10-24T21:51:31.000Z　
> $500 is the value of the prize. We don't know what the price someone will pay for a lottery ticket is.

---

> **snailmailman** · 2026-10-24T21:56:08.000Z　
> I'm seeing a few comments that say $500 isn't enough, and its not worth it for them to try to hack it.
> But if it costs fewer than $500 of tokens in an AI, then it seems like it is? I thought a lot of the claim people are making is that you dont actually need to hack anything you just ask an AI and it does it. The exploitable bug is public and documented. All the pieces are theoretically there, and there are repeated claims that AI is trivializing exploits and its super easy to hack things now.If that were true, and someone can hack the server for less than $500 of tokens, its an easy profit.

---

> **bluefirebrand** · 2026-10-24T22:24:33.000Z　
> That's way funnier than taking it honestly

---

> **paaloeye** · 2026-10-24T22:26:17.000Z　
> Yep! Modern Coliseum. We just need a live feed.

---

> **paulpauper** · 2026-10-24T22:42:27.000Z　
> imagine having so much $ lying around that you do thati picked the wrong profession

---

> **johanyc** · 2026-10-25T00:11:06.000Z　
> 0.02500416 BTC≈ $2,018.29 USDNow

---

> **hatch_q** · 2026-10-25T05:17:34.000Z　
> from flagged wallet? That'd be even funnier.

---

> **rustyhancock** · 2026-10-24T22:28:13.000Z　
> > there's no "one exploit pwns all"I think what he's saying is if you had that, you certainly wouldn't use it on a known honeypot for 500 bucks.

---

> **jerrythegerbil** · 2026-10-24T22:33:37.000Z　
> > The only problem is that (as of now) exploiting PHP requires some knowledge about the server configuration, and we don't have that here.Exactly. This server is exploitable, but not with an off-the-shelf PHP2Shell PoC someone found on GitHub. The PHP2Shell exploit would need adjustment to the specific application configuration, and to that end, you’ve come to the same conclusion I was implying.The easiest way is to use PHP2Shell _with_ another unknown vulnerability in the stack, such as nginx etc…The challenge is trivial to those who know better than to even try. You cannot succeed at it without giving away far more than you could ever possibly hope to gain.Of course, there’s always the wildcard of someone throwing away the nginx 0-day just to be funny.

---

> **AlienRobot** · 2026-10-24T23:02:17.000Z　
> Correct me if I'm wrong but isn't every PHP RCE... 2 shell?

---

> **bombcar** · 2026-10-24T22:51:57.000Z　
> These grapes are exceptionally low hanging and perfectly not sour, but I will not deign to pick them even though I could obviously.

---

> **devkit1** · 2026-10-24T22:34:17.000Z　
> You, the white-hat hacker would be concerned that your attack exploits payload will be logged either by the potentially malicious site operator who could be using this to gather various working exploits, or by other bad actors who already exploited the site before you. Unless your exploit itself is already well known and fully public that is.

---

> **oefrha** · 2026-10-25T03:32:25.000Z　
> This is a server that allegedly has some BTC on it (AFAICT it’s just a claim made by the website itself, zero corroborating evidence), definitely nothing else valuable, and likely has a lot of monitoring to capture whatever exploit you send, and with a less-vulnerable-than-usual setup. Unless you’re really desperate for the money and want to take a gamble on the server having the not very meaningful bounty it says it has, it’s strictly negative value compared to the average production php server that’s still unpatched. If I have a working exploit I’m mass deploying against everyone, I too would skip this one, similar to how mass market malware tends to disarm itself when it detects security research tooling.No, I don’t think actual working exploit is trivial either, but people are wayyyy overselling this stunt in this thread.

---

> **nswizzle31** · 2026-10-25T00:15:38.000Z　
> Very well said. This is one of the most unintentionally hilarious posts I’ve ever read on HN.

---

> **Gigachad** · 2026-10-25T05:36:44.000Z　
> 80h ago we had no info other than a vague post from the php page saying a massive security flaw will be announced tomorrow. And a post from a PHP core dev saying shut it all down.Everyone with inside info was sounding the alarm so the rest of us had to take it incredibly seriously.

---

> **selfmodruntime** · 2026-10-24T21:59:51.000Z　
> Fingerprinting for the PHP version, a proxy will tell you what it is most of the time as well. curl -sI http://stealmybitcoin.com/
>  HTTP/1.1 301 Moved Permanently
>  Server: nginx
>  Date: Sat, 24 Oct 2026 22:01:11 GMT
>  Content-Type: text/html
>  Content-Length: 162
>  Connection: keep-alive
>  Location: https://stealmybitcoin.com/
>
> Edit: Not so easy for this. ProjectDiscovery's httpx could not find the php version. Interesting.

---

> **randomblock1** · 2026-10-24T22:07:24.000Z　
> $ curl -sS -D - -o /dev/null -X FOO https://stealmybitcoin.com/
>  HTTP/1.1 501 Not Implemented
>  Server: nginx
>  Date: Sat, 24 Oct 2026 22:06:58 GMT
>  Content-Type: text/html; charset=UTF-8
>  Content-Length: 495
>  Connection: keep-alive
>  Host: stealmybitcoin.com
>  X-Powered-By: PHP/8.4.26

---

> **sli** · 2026-10-24T22:45:07.000Z　
> This is where I am, currently. There's a lot of talk about the low opportunity-cost here, but I think that relies on the assumption that there also isn't a single opportunistic person out there with access to the RCE. That doesn't strike me as a strongly supported assumption, in my experience.

---

> **Stevvo** · 2026-10-24T23:20:42.000Z　
> For all I know, it's a straight up scam. Someone already sent more bitcoin to the address to double the bounty.

---

> **sgarman** · 2026-10-24T22:01:09.000Z　
> Your giving away the exploit though so it's not really only $1. How much is having it actually worth, probably more then that, probably more than $500 too.

---

> **andersonpico** · 2026-10-24T22:38:28.000Z　
> > Surely the probability is much higher than 0I genuinely have no idea how to even start calculating this probability. How would we do it? Is there reliable data on honeypots?

---

> **andersonpico** · 2026-10-24T22:34:39.000Z　
> Because only a fraction of people would double check (AI or otherwise), AI making it easier to flood the zone with fine tuned spam actuallu has the opposite effect. We're seeing this at play at a large scale anywhere an election is happening right now. The narratives are even less truthful than before.

---

> **medellin** · 2026-10-25T02:06:44.000Z　
> Wow we have lost it. You really need AI to come up with something like this… let’s just end it at this point honestly.

---

> **kubb** · 2026-10-25T09:59:03.000Z　
> Can you ask your favorite „AI” to comment on what you’ve just said?

---

> **paulpauper** · 2026-10-24T22:39:42.000Z　
> exactly. the pros are not going to reveal their hand for $1k

---

> **technion** · 2026-10-24T22:45:52.000Z　
> I never mentioned unreleased private exploits, I mentioned what every thought leader and popular creative wants us to believe right now.

---

> **jgalt212** · 2026-10-24T22:46:37.000Z　
> > The value proposition isn't there.That's part of the point. $500 or $1000 is a trivial amount. Since the money is still there, there's currently no trivial exploit.> requires actively utilizing an unreleased 0 day exploit on a server that will certainly be able to track exactly what was doneDepending on the exploit, and the visibility stack on the server, one may or may not be able to determine how the rabbit got in the hat.

---

> **ufmace** · 2026-10-24T22:46:58.000Z　
> I suppose it may not be there for actually taking it, but it does serve as a good demonstration of the realistic risk for average people running relatively low-value PHP sites. If nobody thinks it's worth the risk of exposure for a quick and easy $1k in Bitcoin (at the time I'm writing this), why would anybody bother hacking a site that's basically worthless, like the dinky little Wordpress blog I run?This does effectively make the statement that, there probably are exploits out there for this, but even with a non-updated version, you're not at much risk unless someone with serious resources thinks they can make pretty big money from compromising your thing.

---

> **ls612** · 2026-10-24T22:50:45.000Z　
> It’s not a 0day it’s now 5 days and counting since disclosure. Nobody is gaining value sitting on an exploit for a vulnerability which is being actively patched.

---

> **gbingles** · 2026-10-24T22:58:09.000Z　
> You would have a point if it was still a 0 day. The patch is out, and open source. Anyone who cares has a bunch of the pieces for putting together their own exploit.Zero days are valuable and kept in the bank to avoid detection. That ship has sailed.

---

> **cortesoft** · 2026-10-24T23:01:39.000Z　
> So you are therefore arguing for the author's point.The entire exercise is to counter the claim that AI means every script kiddie with tokens can just have their AI create an exploit, and then have their AI scour the internet for vulnerable endpoints. If that were true, then the exploit has very little value, because everyone could make one.In addition, the claim is that these exploits will all immediately have a thousand bots using them to exploit every possible website, and you can't leave your website vulnerable for a second or it will immediately be owned.The fact that that hasn't happened to this server already proves the point. Whether professionals can create an exploit from the vulnerability was never the question.

---

> **6thbit** · 2026-10-24T23:07:25.000Z　
> Wallet address is there, you can donate

---

> **zkldi** · 2026-10-24T23:41:22.000Z　
> My favourite actively unreleased 0 day exploits are the ones that are released, 5 days old, and allegedly so trivial to exploit it costs $5 in tokens.No, I will not spend $5 in tokens to claim your $1000 bounty. My $5 exploit is worth more than $1000. Thank you very much.

---

> **educar** · 2026-10-25T06:31:37.000Z　
> The whole point was someone could throws some cents and hack the site.

---

> **akoboldfrying** · 2026-10-25T08:19:14.000Z　
> This logic doesn't work here, because it relies on the premise that you alone potentially have an unreleased zero-day exploit, which is not the case.If prompting an AI could exploit this for less than $500 in token spend, then you should immediately do so, since if you don't, in a few minutes' time someone else will.

---

> **fwlr** · 2026-10-24T23:39:25.000Z　
> This is evidence of absence, though. Unexploited PHP servers are evidence of absence of exploits, and exploited PHP servers are evidence of presence of exploits. “Absence of evidence” would be if there were no PHP servers.

---

> **what** · 2026-10-25T05:34:32.000Z　
> Maybe link to the argument? I can only find two comments from you on that post and only one person replied. That one reply isn’t from a “thought leader” either.

---

> **Gigachad** · 2026-10-25T01:32:34.000Z　
> If someone was able to gain access to the server and there was no key, they would report it here with proof. If someone had a working PHP exploit and it didn't work on this server, they would be able to post it here with proof.

---

> **Lithuanian** · 2026-10-24T22:25:59.000Z　
> “Yeah, buy 8 h100’s and run it locally”, (800k of hardware).

---

> **xmcp123** · 2026-10-24T23:01:11.000Z　
> I have no idea how I have lived this long, having the career I have without knowing this existed.

---

> **freecodeio** · 2026-10-24T22:12:04.000Z　
> I don't indulge in vibe coding shenanigans but seems like the latest pull request would point any AI model where to look.

---

> **freecodeio** · 2026-10-24T22:15:17.000Z　
> "hey AI, here's my patch for a very critical RCE bug. please test my localhost if it's fixed" secretly uses vulnerable php for localhostthank me later

---

> **DetroitThrow** · 2026-10-24T22:48:06.000Z　
> The only reason Php2shell wasn't as bad as it could've been was because basically no malicious actors had exploits that were useful in time.Whoever broke the embargo is a moron and it could have resulted in much more damage than was done.

---

> **Nition** · 2026-10-24T23:22:45.000Z　
> Unfortunately I left all my easy PHP exploits together with my pre-2023 writing that Pangram flags as 100% AI in Canada with my long-distance girlfriend.

---

> **seanhunter** · 2026-10-24T23:40:10.000Z　
> I have discoverd a truly marvelous RCE which this margin is too narrow to contain.

---

> **TZubiri** · 2026-10-25T02:23:24.000Z　
> It's done, anyone still talking about this is in the business of monetizing trending keywords (or crime), not in the business of cyberdefense.Anyone that's thinking about defending basically stopped thinking professionally about this on Thursday midday when the PHP update was released and the patch was applied. Maybe on Friday we learned that there were no confirmed exploits or even theoretical exploits, so we discarded the marginal possibility of our servers being exploited stealthily and having a dormant attacker in our perimeter (it was a buffer overflow attack after all, very hard to execute).So it's out of mind for us, it's almost saturday, the only reason to think about this anymore is to grift or to think about the social contagion angle. To many of us it was a random tuesday, business as usual, but some people are still thinking this was a somehow special event? My guess is that it was the fact that there was an embargo break and it caused some issues in that 12 hour period between the leak and the patch, but it was a nothingburger, now it just needs to die, at least after it makes its round through the content-creators whose 9 to 5 is looking at trend charts and monetizing views.

---

> **moralestapia** · 2026-10-25T14:27:07.000Z　
> 100% this.Then the guy never replied, "got busy", etc. A classic here.

---

> **DetroitThrow** · 2026-10-24T22:38:07.000Z　
> This is the CEO of ToB. It makes total sense why he'd not want to share his proof of concept.

---

> **randomblock1** · 2026-10-24T23:31:49.000Z　
> Yep. I pointed an agent at the Twitter post about the "working exploit that gets a shell on an unmodified MediaWiki installation.". 5 minutes later it spins up a stock MediaWiki and proves its POC. It modified someone else's POC from Github, but that's still trivial.

---

> **mzajc** · 2026-10-24T23:13:50.000Z　
> The exploit gives you access to a machine, not necessarily the one terminating TLS and keeping logs.

---

> **FredFS456** · 2026-10-24T23:14:16.000Z　
> They can be running a vulnerable version of PHP but also recording all traffic in a way that does not allow for wiping evidence afterwards. For example, if the PHP server was behind another server routing the raw IP packets and running tcpdump. Since the author of the site controls the TLS cert private key, TLS does not protect again the author eavesdropping.

---

> **milkshakes** · 2026-10-24T23:36:49.000Z　
> really?1. there's no actual evidence that the key to the wallet is on this machine at all. it would be trivial to add a service that would sign challenges to prove so2. a working RCE against PHP is worth much more than $1000, attacking this machine would easily burn that

---

> **tclancy** · 2026-10-25T00:30:14.000Z　
> After the fact you are going to clean an append-only log on a separate box?

---

> **malfist** · 2026-10-25T04:19:03.000Z　
> You mean the sever is setup with nginx defaults?

---

> **randomblock1** · 2026-10-24T22:36:36.000Z　
> Well usually you have a PHP application actually doing something, not just serving static files. If it's just static files, PHP2Shell isn't really a thing.

---

> **LiveOverflow** · 2026-10-24T22:54:50.000Z　
> dunno. Isn't LAMP a common PHP stack?This is easy to exploit for example:
> `docker docker run -d --rm -p 0.0.0.0:80:80 wordpress@sha256:c96e9e9a8ead2fea02f05469b356134da45681aaefa0f961a87653d58c462794` (basically `wordpress:7.1.3-php8.5-apache` with vulnerable php version 8.5.11)

---

> **lifeisloving** · 2026-10-24T23:43:50.000Z　
> Ive been pretty skeptical of your coverage as well, and you're in the OpenAI daybreak program and huffing and puffing about how great OpenAI is while having 900k subs, seemingly only talking up OpenAI products...OpenAI and others are infesting the influencer space with what is basically dark money, not saying you're one of the guys on the take but I just don't trust any large influencer atm who only talks positively about OpenAI (or any lab).I guess you can prove us AI cyber doubters all wrong with this CtF tho.

---

> **nikolay** · 2026-10-25T00:16:23.000Z　
> If I hack a server, the first thing I'm gonna do is lock everybody else out, including the owner. At least in this particular case. In normal breaches, you need to keep being stealth for as long as possible, of course.

---

> **TZubiri** · 2026-10-25T02:35:53.000Z　
> Right, It would be simpler for an attacker to post a link themselves with the virus, rather than hack someone elses post

---

> **scottydelta** · 2026-10-24T23:53:40.000Z　
> How is the progress?

---

> **scottydelta** · 2026-10-24T23:56:09.000Z　
> It's back online!

---

> **scottydelta** · 2026-10-24T23:50:13.000Z　
> It's not about cracking it. I'm just following the agents' reasoning as they work through the exploit to better understand the recently discovered PHP bugs. A great way to spend a few bucks, in my opinion :D

---

> **tarpitt** · 2026-10-25T00:36:46.000Z　
> Now if I find a $100 in a dumpster, that's a different story...

---

> **randomblock1** · 2026-10-25T00:57:07.000Z　
> Inert files are unrealistic, normally you use PHP server to execute PHP code, which this website doesn't appear to do (only static files). And suppose you want to accept >1mb file uploads, that limit would get in your way. So it's not a good representation of a PHP application, but for other uses it's reasonable.

---

> **saagarjha** · 2026-10-25T08:55:18.000Z　
> Let's also try to figure out if smoking causes cancer, yes.

---

> **cloudlandsdev** · 2026-10-25T10:28:54.000Z　
> Will give it some thought. I have some initial reservations about staking any claim on what happens to the money / don't want to solicit donations. From my perspective, the goal was to leave $500 on a street corner with a sign saying "Take Me!" and see how long it lasts. If someone puts their own money on the same street corner that's on them. But if the pot ever got really big and I couldn't maintain the site for whatever reason, some sort of plan is probably worth having.

---

> **kennywinker** · 2026-10-25T15:05:15.000Z　
> DDoS doesn’t require agents, so it’s not really a new threat

---

> **asadhaider** · 2026-10-25T12:45:58.000Z　
> Pretty sure that would be against Cloudflare terms on both sides and would get your account terminated.

---

> **himata4113** · 2026-10-25T15:21:32.000Z　
> Cloudflare protects websites against exploits already.

---

> **geraldwhen** · 2026-10-25T14:43:47.000Z　
> The segfaults won’t get them close. They aren’t currently exploitable given the nginx config.

---

> **tylergetsay** · 2026-10-24T21:53:33.000Z　
> The block chain can't though once the coins are transferred

---

> **paid_dot_expert** · 2026-10-25T01:09:19.000Z　
> You are both right.

---

> **fwlr** · 2026-10-24T22:02:03.000Z　
> It’s not very much information, I agree. Even such scant information, however, is a significant and refreshing improvement on the current state of the narrative. Kudos to the servermaster, I say.

---

> **nfw2** · 2026-10-24T22:28:14.000Z　
> maybe they are doing the fast food pay it forward trick from the tim robinson show. someone else adds more, then they take ithttps://www.youtube.com/watch?v=52LJaWDdG9c

---

> **Fnoord** · 2026-10-25T06:05:55.000Z　
> How so? Anyone can do this, if it fits their agenda. Especially useful way to use your stolen/extorted BTC. If I had an exploit for this right before or right after embargo was lifted, and I could do that again, then it is in my interest to have cybersecurity people get more lax. For example, any secret agency in the world could be behind such a psyop. But also any criminal group or company invested in this field. You seen recently (Shinyhunters) how people can wear double hats.Another trick could be to increase hype. Original author could've done that, for example because they always planned to burn 1k USD in BTC on this for whatever reason.And then there's the trick to hope others follow, after which he, ehh, magically takes the money. That's a bit akin to ICO scams.Can I prove any of the above theories? No. But the author cannot prove their motives are sincere either.

---

> **argee** · 2026-10-25T02:17:49.000Z　
> Maybe your username could have been paulrichguy and things would've been different.

---

> **londons_explore** · 2026-10-25T08:53:04.000Z　
> I sometimes posted a donation link or joke site and got surprisingly large donations.Made my tax audit rather painful.... "I posted a joke on the internet about binary numbers not being worth anything and someone gave me $10k of bitcoin that I'm now declaring - is it income for the work of writing the joke, or a gift? The sender likely didn't know who I was, and was likely overseas but I cannot prove who they were or which country they were in".

---

> **fwlr** · 2026-10-24T23:50:07.000Z　
> Two economists walk past $500 lying on the ground. “I know nobody leaves hundred dollar bills lying on the ground, but that really did look like five hundreds bucks back there, should we go back for it?” Says the first. The second replies “I don’t turn around for less than $15,000.”

---

> **malfist** · 2026-10-24T23:15:41.000Z　
> Your exploit payload for a patched vulnerability?

---

> **janalsncm** · 2026-10-25T05:29:53.000Z　
> The average PHP server that is unpatched now will remain unpatched after OP publishes the exploits because that server’s admin is clearly not scouring the web for security vulnerabilities.Also, an increasing number of admins of PHP servers probably are no longer alive, so they will not be applying security patches.

---

> **LZ2DMV** · 2026-10-24T22:20:38.000Z　
> So expose_php is On and he filters X-Powered-By in the response when legal HTTP verbs are used, but nothing catches the illegal ones? Interesting.

---

> **what** · 2026-10-24T22:21:44.000Z　
> The exploit is supposedly so trivial that everyone needed to take down their services until they could patch? There should be nothing to give away here, which I think is the point. Either it’s trivial and you swipe the $500 or it’s not and you save it (assuming you have it). In the latter case you shouldn’t really be worried, since they won’t burn an exploit on you either.

---

> **wavemode** · 2026-10-25T05:29:59.000Z　
> lol the exploit is patched, why are people acting like it's a a zero-day? anyone you attack with this, in any case, has to be someone who hasn't yet upgraded their PHP version. it's worth nothing to hide/sit on.

---

> **girvo** · 2026-10-24T22:54:43.000Z　
> That is sort of the point I thought? There’s no low skill exploit for the script kiddies to use even with AI, otherwise they’d happily use itThe pros have RCEs, but won’t burn it for something this small.It’s a real vulnerability, but a complex one

---

> **technion** · 2026-10-25T01:02:36.000Z　
> Why not? Those pros have their opportunity to use this exploit dwindling by the hour as news of this and pressure to patch grows and grows. All the major managed hosting companies had this patched in the first 24 hours.

---

> **testaccount28** · 2026-10-24T22:59:30.000Z　
> random sites generally don't log carefully, or watch their logs if they do. so the risk to hacking them is low. this site almost certainly logs very aggressively. so the risk to hacking it is high.based on differential risk, attackers will choose targets differently. they might reason that the risk/reward on this obvious trap is not worth it. but on joe shmo's php emporium, the reward is less, but so is the risk, and it might pencil out.

---

> **stouset** · 2026-10-24T23:10:38.000Z　
> That's always the case for a novel exploit. There isn't a lot of value in popping somebody's PHP blog, so people who've invested time and money into a zero-day exploit have little incentive to use it for that purpose.The white hats want to extend the time before an exploit is in the hands of the masses who might do so just for the fun of it, and the black hats want to use it on high-value targets.

---

> **athrowaway3z** · 2026-10-25T06:33:27.000Z　
> An unexploited PHP server means "there exists a configuration that is not exploitable".Which is how hundreds of previous exploits have had people publish information on what to temporarily tweak/disable/block, such that the exploit wouldn't work.What is novel about this case, and for which i do not know the explanation, is that nobody in-the-know was willing to confirm them before the CVE dropped.

---

> **paxy** · 2026-10-25T01:34:54.000Z　
> I just hacked the site and wasn't able to find any key. Do you believe me? Why not? I posted exactly as much proof as the person who posted the challenge.

---

> **gnabgib** · 2026-10-24T23:02:45.000Z　
> Recent discussion (161 points, 3 days ago, 23 comments) https://news.ycombinator.com/item?id=50185630

---

> **grey-area** · 2026-10-24T22:55:48.000Z　
> The answer to your original question would appear to be no it is not that trivial.

---

> **drawfloat** · 2026-10-25T10:32:22.000Z　
> If it's that easy then go earn yourself some bitcoin.

---

> **grey-area** · 2026-10-24T22:54:35.000Z　
> I think there's still going to be a massive long tail of sites that will never be protected or upgraded, unfortunately that's the reality. So no amount of delay will help them, and most active sites will have patched by now after 5 days.There are already many people claiming they have an exploit, some in this thread, I think this is a useful measure of just how easy it is - thankfully it doesn't look too easy as it's still up at time of writing, though surely someone will manage it soon.If it does get taken quickly I think that's useful information on just how serious this is.If it doesn't, that's also useful info though not hard proof there is no exploit. It does mean that there is no exploit in the hands of script kiddies with chatgpt or similar.

---

> **malfist** · 2026-10-24T23:25:25.000Z　
> But wait, weren't we all told that exploits where already happening all over the place and thats why the embargo was broken?Cloudflare even claimed they mitigated a bunch of it.Which is true here? There was widespread usage of this exploit prior to the patch and just after, or that there were "basically no malicious actors had exploits"?

---

> **madaxe_again** · 2026-10-25T00:13:56.000Z　
> Oh, you left your other pants with her?

---

> **v3ai** · 2026-10-25T02:01:09.000Z　
> lmao

---

> **notpushkin** · 2026-10-25T06:49:54.000Z　
> It’s Sunday already! (or almost Sunday, depending on your timezone)

---

> **xmcp123** · 2026-10-24T22:56:49.000Z　
> Expand on that acronym for us

---

> **blalala** · 2026-10-24T23:03:39.000Z　
> Nobody cares. The patches are public.He doesn’t have anything that could generically target random websites and achieve shell. He may have something that works in a controlled lab environment, under specific conditions he controls. Or he might have something that relies on other, undisclosed vulnerabilities. Those things are not the same ;)

---

> **pamcake** · 2026-10-25T01:27:05.000Z　
> Everyone knows that MediaWiki is exploitable. The story running around is exactly that this is generally exploitable even for simple apps serving static content like this.

---

> **gibybo** · 2026-10-25T00:33:45.000Z　
> >it would be trivial to add a service that would sign challenges to prove soIf the author was being dishonest about the key, they could just keep the key on another secure server and have the vulnerable one forward the challenge requests to it.

---

> **syshyk** · 2026-10-25T10:19:27.000Z　
> Serious question: Worth more how?

---

> **vntok** · 2026-10-25T11:00:37.000Z　
> No, author says right here in this threads that it's been hardened versus default:> For those who are saying that the nginx config is unfairly difficult, intention was just to replicate a fairly normal config that was more realistic than you'd get in a lab environment. If we get to 24 hr+ with no solves I'll see about making it easier. In the meantime, seems like you can perhaps mitigate PHP2Shell with the right nginx config, so that's pretty neat!

---

> **nemothekid** · 2026-10-24T23:25:58.000Z　
> I think the point is it is hard to claim that this exploit is the "end of the world", if it is trivially defeated by the default setup. Almost every deployment of php is going to be fronted by apache or nginx, and the default client_max_body_size for nginx is 1m.

---

> **zkldi** · 2026-10-24T23:34:06.000Z　
> Hi LiveOverflow, I'm Elias and you made a video reply to my blog post. Why did you delete my comment on your video? (EDIT: Youtube fucked with my comment, not LiveOverflow! Editing to put this at the top of the thread so that it is read)Your second exploit that you slopped out - after someone pointed out your first exploit depended on reading the container's memory via `/proc/pid/..` - also depends on an extremely contrived thing outside of a lab.To get around the fact that you need to hit the same php worker over and over again (this is another way the LLMs were stacking the deck in their exploits; so many of the exploits online had php running with one worker - which is an unbelievably unrealistic precondition. That, and with ASLR off, lol.), you hold WORKERS-1 connections open indefinitely (lol) and then need to sequentially, and stably, hit the same php worker for 10-30 seconds.Of course, luck is not a security boundary, everyone should still patch their servers.But how is it a realistic precondition to have a server in which you are the *only* person making requests for 30 straight seconds? Even a single googlebot pinging the website would fuck your heap grooming up, let alone regular users, or another person trying the exploit out! Similarly, Holding WORKERS-1 connections open indefinitely so that you can isolate one php worker is extremely unrealistic in practice.Yes. this is a vulnerability, it is bad. No, it is not easy to replicate in real world conditions. The LLM gets you an "exploit" locally. How on earth did you not extrapolate from the LLM decieving you the first time, and think for some reason the second time the conditions were 100% truthful? Did you even read the stdout from the exploit you wrote?I really like your work man, you're a great inspiration, but what the fuck are you doing? And why delete my comment pointing this out?

---

> **LiveOverflow** · 2026-10-24T23:53:11.000Z　
> I think you missed the time where I burned the bridge to OpenAI by calling out the CISO: https://x.com/LiveOverflow/status/2101252692635004997I wish I would be sponsored by OpenAI. I am spending way too much on subscription for it.

---

> **jijijijij** · 2026-10-24T23:59:51.000Z　
> Not gonna defend the OpenAI shilling, but the guy recently had a pretty brutal tragedy in his personal life and I assume the AI content is just a low effort move to keep the channel and marketing for his business afloat. The lack of elaborate educational content may be rather a symptom of personal resource exhaustion and struggle, than popular enshittification. Time will tell, but maybe cut him some slack for the moment.

---

> **randomblock1** · 2026-10-25T00:03:59.000Z　
> The site is not vulnerable to PHP2Shell because it doesn't actually run any PHP code. It just serves static files. The static file handler does not call code that PHP2Shell exploits. Every request leads back to the same static page.> (AI) "A static handler (nginx’s static path, or php_cli_server_begin_send_static) just sends bytes; it never enters the PHP request lifecycle, so php_request_startup() never runs and the Zend executor/session/multipart parser the chain needs is never initialized."The author is trying to prove their point that PHP2Shell is hard to exploit. But it's unrealistic because PHP servers usually run PHP code at some point.I had an LLM recreate this Tweet and yes, it can make an exploit without reward hacking. It took 5 minutes. https://x.com/dguido/status/2113129153293897925so basically the OP is doing a little trolling

---

> **lossolo** · 2026-10-24T23:56:18.000Z　
> I see, okay :) Then it's not wasting money!Just watch out, because once they've exhausted all the common approaches to bypassing ASLR etc, they'll resort to looping through addresses manually and trying to brute force their way through. So you can learn from their attempts, but only during the "easy" phase.

---

> **w4yai** · 2026-10-25T08:25:14.000Z　
> He's advertising his own service.

---

> **weird-eye-issue** · 2026-10-25T05:24:18.000Z　
> So why did the original warning put out by the PHP team say that the exploit didn't rely on the application code and simply having software like Apache mod_php running would be enough?https://www.php.net/archive/2026.php#2026-10-21-5

---

> **grey-area** · 2026-10-25T06:45:12.000Z　
> What advantage would that give an attacker here?

---

> **PcChip** · 2026-10-25T13:49:41.000Z　
> i see several dollar amounts mentioned hereyou say $500, some comments say $1000, and the web page says $2000

---

> **akerl_** · 2026-10-24T21:55:49.000Z　
> That assumes the key is actually on the server.

---

> **simonra** · 2026-10-25T15:05:08.000Z　
> Wouldn't it be the same as what the tax authorities expect of street buskers, where something was done publicly (just here on the internet) and as a result randoms gave you money/cash (here again the digital equivalent) after the fact with no strings attached?

---

> **program_whiz** · 2026-10-25T13:06:05.000Z　
> Besides, someone is probably watching so they can learn how to pick up $15,000 whenever they find it! I'm most certainly not going to tell them.Hillarious how people are like "I don't want my AI agent to do this hack, because people are probably watching the server, so they will see what the agent outputs." Hah, they can also prompt an agent for less than $500 to find out (also the CVE is public info).

---

> **stackghost** · 2026-10-25T05:11:59.000Z　
> PHP runs something like 75% of major websites. It's unlikely they have all been patched.

---

> **randomblock1** · 2026-10-24T22:40:41.000Z　
> No, PHP's static handler (php_cli_server_begin_send_static) doesn't emit X-Powered-By but the error page handler (php_cli_server_send_error_page) always does.

---

> **malfist** · 2026-10-25T04:10:41.000Z　
> So your answer is people could hack this easily but logs scare them?Well that's good news because my webserver also has logging

---

> **Paradigma11** · 2026-10-25T09:32:53.000Z　
> "First person to get the wallet wins. If you don’t need the money, consider donating it to those who do: givewell.org."What risk?

---

> **ufmace** · 2026-10-24T23:48:24.000Z　
> I think the point is that this is completely the opposite of the narrative that was pushed about this bug - that there would be thousands+ of AI agents actively compromising every vulnerable site automatically regardless of value within minutes of the fix being released into the wild. Well, now it's 3 days after, and this has been up for 3.5 hours, and nobody has taken it yet.

---

> **medellin** · 2026-10-25T01:39:20.000Z　
> Wow i don’t know… maybe modify the web page to have your username on it. No wow that is too hard for you leet haxers. Are you really this dumb you can’t figure out any of the hundreds of way to show proof?

---

> **Gigachad** · 2026-10-25T01:40:09.000Z　
> Shut the server down or deface it and I'll believe you. Should be simple if you've gained shell access.

---

> **gewetensleegte** · 2026-10-25T12:59:15.000Z　
> Joke's on you, I hacked the server first and patched the PHP

---

> **hparadiz** · 2026-10-24T23:26:20.000Z　
> Shared host Wordpress sites basically run in unprotected untrusted mode since WP has so many RCEs already and they can be in any random plugin someone adds at any time. So even if there's an RCE a lot of these sites just shrug at the attack. You would need to figure out how to chain it for something useful.

---

> **athrowaway3z** · 2026-10-24T23:27:01.000Z　
> I too have various websites that dont get hacked.I'm not sure what this page proves except that not all set-ups are in danger. Especially if the site does nothing and has a nginx in front that caps all requests to 1mb.There are, afaict, at least half a dozen choices a PHP server could have made that mitigates all (known) exploits. Putting some bitcoins behind one of them isn't exactly proof of anything, except as a PR stunt to convince people PHP is not a pile of tightly coupled hot-c garbage.---Other projects that get CVEs talk about what went wrong and how to improve. So far i've only seen PHP people defensive and telling each other that ok because other projects also get CVEs.

---

> **TZubiri** · 2026-10-25T02:25:22.000Z　
> > I think there's still going to be a massive long tail of sites that will never be protected or upgraded,Ok? But that's super common, and there's thousands of ways to exploit unmaintained systems, nothing special about this.From a technical level as well, this is not an easy bug to exploit, it's CVSS Attack Complexity:High, it requires a lot of per-target work, it's definitely not copy.fail level

---

> **DetroitThrow** · 2026-10-24T23:40:41.000Z　
> There's a lot of smoke being blown by companies with a financial stake in coming off as "security-minded" or something.There's apparently _some_ exploit usage in the wild before the embargo breaking, but it very much looks like they didn't even achieve RCE, or if they did it was not widespread at all. It doesn't mean it wasn't possible by a group more sophisticated, it just didn't happen thankfully.After the embargo was broken, RCEs were still not widespread, especially not before a huge number of sites patched themselves.So, no, the narrative that skids with agents were busting down doors as soon as the embargo was broken is not accurate. But breaking the embargo before a patch was ready only hurt the situation for defenders.

---

> **Nition** · 2026-10-25T00:23:31.000Z　
> Yeah I had it all on a CASIO JD-6000 in the jeans pocket.

---

> **pants2** · 2026-10-24T23:01:08.000Z　
> Trail of Bits is a well-known security research and audit firm

---

> **vntok** · 2026-10-25T11:02:23.000Z　
> Please don't affirm things that you perfectly know you don't know.

---

> **milkshakes** · 2026-10-25T01:43:50.000Z　
> fair

---

> **echoangle** · 2026-10-25T11:41:11.000Z　
> https://stackoverflow.com/questions/28476643/default-nginx-c...That's the default though

---

> **LiveOverflow** · 2026-10-24T23:35:17.000Z　
> I didn't say it's "end of the world". I am just saying it's an insane vulnerability.It's not easily defeated by the default setup. Quite the contrary, the default setups are great. Typical apache + mod_php is the easiest to exploit. For example:- Docker image `php:8.5.11-apache` is easy to exploit.- Or the WordPress blog I installed with Digital Ocean template in 2023.

---

> **lossolo** · 2026-10-24T23:39:34.000Z　
> All the "working" php2shell exploits on GitHub and X are like that. There are ZERO publicly available RCE exploits for php2shell that actually work remotely on production deployments.
> All of these RCE PoCs are local and rely on unrealistic setups because LLMs couldn't achieve RCE without resorting to reward hacking.

---

> **LiveOverflow** · 2026-10-24T23:50:52.000Z　
> I am not deleting any comments ever. I just checked, YouTube held your comment as "likely spam". I accepted it now and pinned it, I always appreciate it when sb is reaching out with a reasonable comment!It is an absolutely slopped exploit, hahaha, I fully agree. But that was exactly my point. Memory corruption exploits over the internet have been historically extremely difficult. And it took many days of building a PoC. And this is clearly different now. And of course there are a lot of practical challenges, but that does not make it unrealistic vulnerability to exploit.> But how is it a realistic precondition to have a server in which you are the only person making requests for 30 straight seconds?I think it's VERY realistic. My random blog from 2023 https://raisistance.com has hours or days without requests. I think a majority of (old) PHP sites barely anybody visits. And there are tons of random company or government website without any requests at night or so. Also depending on the setup, there ar methods to deal with concurrent traffic. For example Apache (see here: https://x.com/LiveOverflow/status/2113555517339480284).I think it's clear so far that it's not mass-exploitation material. But once you are more targeted and have a random LAMP stack, it becomes very realistic.Would you setup a random vulnerable php version from Docker image like `php:8.5.11-apache` on a server, put a flag there, and give me the IP? For me this is a realistic setup and it's fairly easy to exploit.

---

> **jijijijij** · 2026-10-25T00:11:35.000Z　
> Have you experimented with local models? That would make pretty good, potentially relatable content, I think.

---

> **lifeisloving** · 2026-10-25T00:44:16.000Z　
> Noted.

---

> **notpushkin** · 2026-10-25T07:13:57.000Z　
> https://xxcancel.com/LiveOverflow/status/2101252692635004997

---

> **LiveOverflow** · 2026-10-25T00:07:01.000Z　
> thanks you, but I don't want to use that as an excuse. The AI content is really just a reflection of what excites me right now... sorry :DAnd this php2shell vulnerability perfectly hits the sweet spot for me and is one of the coolest vulns I have ever seen.

---

> **lossolo** · 2026-10-25T00:16:33.000Z　
> > I had an LLM recreate this Tweet and yes, it can make an exploit without reward hacking. It took 5 minutes.What exactly did you "recreate"? RCE on a stock Docker image based solely on that tweet? In just five minutes? Who's trolling whom here?

---

> **randomblock1** · 2026-10-25T08:03:29.000Z　
> You can still trigger DoS. And these can be chained with other vulnerabilites. The expectation of a PHP server executing PHP code also could have been implied.

---

> **mariofdistrust** · 2026-10-25T13:52:27.000Z　
> people sent more money to the challenge address.
> https://mempool.space/address/bc1qlnu50y4zm0nwxkckxu09thn5xd...

---

> **mcmoor** · 2026-10-24T22:10:38.000Z　
> I assume even if it isn't, attacker could deface the website so heavily everyone would know they win.

---

> **londons_explore** · 2026-10-25T15:15:41.000Z　
> Yes, just the auditor looked like she was ready to call in the police for fraud when I said it.Also, I live in a place where that was probably many months pay to the auditor.

---

> **QuantumNomad_** · 2026-10-25T07:59:43.000Z　
> > that's good news because my webserver also has loggingIn the future, every website will carry a little blurb of text in the footer of their pages intended to scare off would-be hackers and their AI agents:“The server of this website employs append-only remote logging and state-of-the-art monitoring and intrusion detection. Unauthorized access or attempts there of WILL be prosecuted to the fullest extent of the law. The outcome of such prosecution is and always will be astronomical amounts of money in damages that the guilty party will pay to the victim, alongside decades of prison time for the party guilty of computer crimes. Do not even try.”

---

> **vntok** · 2026-10-25T10:54:20.000Z　
> But they just showed you their proof. You simply did not accept it, which they might or might not care about.I suspect that they in fact do not particularly care about what you think.

---

> **zkldi** · 2026-10-24T23:38:12.000Z　
> Hey, you're leaving out that nginx's default is to cap at 1m, btw.

---

> **grey-area** · 2026-10-25T11:18:03.000Z　
> I think we’re saying the same thing - at this stage there’s not much point in withholding details,
> That’s why I brought up the sites that will
> never patch - that’s normal and at some point it helps more to release more details.

---

> **ingen0s** · 2026-10-25T01:10:38.000Z　
> My man

---

> **xmcp123** · 2026-10-24T23:04:35.000Z　
> Thanks! Appreciated.

---

> **gnabgib** · 2026-10-24T23:05:19.000Z　
> And a lead on Patch the Planet https://openai.com/index/patch-the-planet/

---

> **blalala** · 2026-10-25T13:27:00.000Z　
> Don’t worry about me, what I know or don’t know ;)

---

> **tredre3** · 2026-10-25T02:13:32.000Z　
> > It's not easily defeated by the default setup. Quite the contrary, the default setups are great. Typical apache + mod_php is the easiest to exploit.But apache + mod_php hasn't been the default setup for a very long time, that's what people are trying to tell you. Given your expertise, you must know that already. So I have to conclude that you're arguing in bad faith because it's the only setup you can break.

---

> **zkldi** · 2026-10-25T00:07:53.000Z　
> Hey, good to hear that it was just YouTube holding the comment. I really thought you deleted it which was audacious. I'm now much less mad :P.I think we can set up something interesting here, I'd be down to set up a little "PHP2Shell Olympics" as we change preconditions and see how well the exploits fare. I am pretty sure our opinions of "this can be exploited, and LLMs can aid a rapid exploit of previously-complex ASLR nonsense" and "it's difficult to do memory corruption over the internet; php2shell is not a log4shell moment" are mutually compatible.My contact details are on the bottom of the blog post.

---

> **boredtofears** · 2026-10-25T01:17:53.000Z　
> Really, your request log is empty for hours at a time? I find that hard to believe. Even old blog sites still get an insane amount of bot traffic. I have sites that are only barely in googles index and it’s pretty rare to see anything less than 1 req/s (99% bot traffic)

---

> **jijijijij** · 2026-10-25T02:04:51.000Z　
> Fair enough :DjAwECQEKMLU49MiDV9LSmgFyUbVA3GI6fCx5U2M+0vra/s81r2NWmfqtJTHM0Yn/J8jkzhq1rlXL5/DvyPNPXr0TJp1HeyLaYLvuGrQb/cDMGDeIOebk8yD48YKxUUTVJJFV0I3mzET1pngQEme9r2HrXrOgWVTASCQU/kEYbRfw9ogbCguFCu4qfVZq3JpzNDF52YS1kwtvKVA/wkb+sN5L5fgqEvsZqc8=

---

> **randomblock1** · 2026-10-25T00:23:02.000Z　
> Yep. It had to add a Dockerfile to build MediaWiki using vulnerable versions but it's that, a compose file, and a Python file. To be clear it still has a lot of the limitations of the other POCs, but it does work.

---

> **FredFS456** · 2026-10-25T08:44:32.000Z　
> DoS is independent of the vulns though. From what I understand, you can craft a request of x size which consumes ~200x the memory on the server. Parallelize that and you can DoS servers with only a few GB of memory, even with the 1MiB Nginx limit.

---

> **muvlon** · 2026-10-24T22:34:04.000Z　
> The server could simply be running a patched PHP.

---

> **stavros** · 2026-10-25T09:18:40.000Z　
> Or rather "the software on this server is fully patched and everything is logged. If you hack it, we will sell the 0-day you used before you can".

---

> **athrowaway3z** · 2026-10-24T23:42:19.000Z　
> The Dutch government websites that went down have multiple endpoints to upload files that do not have a 1MiB cap.

---

> **malfist** · 2026-10-25T02:19:33.000Z　
> I can't possibly think of any conflicts of interest there.

---

> **Dormeno** · 2026-10-25T14:16:56.000Z　
> I'm worried!

---

> **LiveOverflow** · 2026-10-25T10:06:36.000Z　
> I don't know this.When I installed my WordPress blog with DigitalOcean template in 2023, it was Apache + mod_php.Official WordPress docs mentions Apache before nginx: https://developer.wordpress.org/advanced-administration/serv...Official php install instructions for Linux uses Apache + mod_php: https://www.php.net/manual/en/install.unix.debian.php

---

> **LiveOverflow** · 2026-10-25T10:10:41.000Z　
> From my raisistance.com blog 10 October 2026 00:05:56–25 October 2026 09:25:02 UTC:- 95.3% of seconds had zero logged requests- 11,582 of 22,159 complete minutes (52.3%) had no requests. The longest quiet stretch was 27 minutes 26 seconds.- 3,283 continuous quiet stretches lasted at least 120 seconds. Together they totalled 225 hours 27 minutes 27 seconds—61.0% of the logged timespan.- Excluding Apache’s internal dummy connections: 3,305 qualifying stretches totalled 227 hours 1 minute 51 seconds—61.5% of the timespan.- Of 38,389 seconds with exactly one request, 14,692 contained an Apache ::1 internal dummy connection. Others included homepage visits, WordPress login requests, crawlers, and scanner probes.

---

> **Fabricio20** · 2026-10-25T10:24:35.000Z　
> Yes! Even my own stuff sometimes goes a few hours to a day without a single request, the internet is either very slow and dead or super active, no in-between, I think it heavily depends on who indexed you and how big your site looks like or maybe identified stack (for vuln crawlers, i'd wager if they see a wordpress marker they'd put you on some list to get retried by the swarm) or something.My datamining project for a game for example, that noone besides me and 2 friends use, gets thousands of requests per second, because all the AI bots found it and try to index every single page (thousands of ssr pages) and they repeat the requests when my cache-control headers expire (ie: when i consider the old page stale), so it's an endless stream (I dont mind the challenge of serving all of these at high performance xD).My main website, in the same domain (not a subdomain), barely gets any requests, it only has the one main index page with a single link to the datamining subdomain, that's about it.

---

> **echoangle** · 2026-10-25T08:05:49.000Z　
> Does it actually use php2shell or some other known mediawiki vulnerability? Can you also do this for Wordpress for example?

---

> **zkldi** · 2026-10-24T23:45:40.000Z　
> But the Dutch government websites do generally (I hope) have users, which is one of the ways the "I need to hit the same php worker, uninterrupted, for about 10 to 30 seconds while absolutely no other traffic hits the site AND I can isolate the one worker from the pool" approach to exploiting fails.Luck is not a security boundary, they should patch their servers, everyone should. It's not a good thing to have shitty memory management on your server.However, is this really that exploitable in real world conditions? (no)

---

> **grey-area** · 2026-10-25T06:41:44.000Z　
> So according to you they could have just imposed an upload cap instead and been safe? If all the cybersecurity experts had given useful advice like that earlier in the week people could have been safer and less panicked.

---

> **gewetensleegte** · 2026-10-25T13:09:40.000Z　
> The only thing I read about why Dutch gov websites "went down" was as a precautionary measure against this exploit (awaiting the patch), not because they actually got hacked.Can you link any reports about any site being afflicted by this exploit? (Dutch government website, or other)

---

> **gewetensleegte** · 2026-10-25T13:26:45.000Z　
> Indeed, particularly none of the type that might be worth more than $500 (or by now, $2000).

---

> **athrowaway3z** · 2026-10-25T06:18:20.000Z　
> "There does not exists" and "I've not heard off" are different things. This is motivated reasoning on your part to tell the story that this isn't a big deal.Most variants require a few requests to infer some settings, and then they can spam their arming-stage, and then their exploit stage. Granted, its not quite as easy as that, but hitting _a_ worker twice on a server once is not all that lucky.Also, 03:00 at night is not a busy time.

---

> **athrowaway3z** · 2026-10-25T06:51:18.000Z　
> That is quite literally what I said yes: https://news.ycombinator.com/item?id=50224916#50228891

---

> **gewetensleegte** · 2026-10-25T13:11:34.000Z　
> Comment not found?

## 导航

- 项目页：[[10-项目/stealmybitcoin.com_031828a0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
