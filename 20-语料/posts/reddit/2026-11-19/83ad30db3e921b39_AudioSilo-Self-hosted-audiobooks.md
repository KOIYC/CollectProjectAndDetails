---
type: "corpus"
item_id: "83ad30db3e921b39"
title: "AudioSilo - Self hosted audiobooks"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/selfhosted/comments/1xr8g7s/audiosilo_self_hosted_audiobooks/"
project_url: "https://fanart.tv/"
author: "ls_kode"
published_at: "2026-11-09T04:36:44+08:00"
captured_at: "2026-11-19T09:44:40+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-19"
pub_day: "2026-11-09"
tags:
  - 语料
  - reddit
  - r/selfhosted
  - Product Announcement
metrics: {"score": 175, "comments": 124, "upvote_ratio": 0.8326996197718631}
comments_count: 123
comments_total: 124
discovered_via: "reddit:14d+settle10"
---

# AudioSilo - Self hosted audiobooks

> [!info] 一句话导读
> \*Edit\* The mods told me to remove any links to a github repository that is less than 3 months old (I thought it was just the [ls.io](http://ls.io) docker imag…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/selfhosted/comments/1xr8g7s/audiosilo_self_hosted_audiobooks/>
> 指标：得分=175 · 评论=124 · 赞踩比=0.8326996197718631
> 作者：ls_kode　|　发布：2026-11-09T04:36:44+08:00
> 项目链接：<https://fanart.tv/>
> 采集：2026-11-19T09:44:40+08:00　|　id：`83ad30db3e921b39`

## 正文

\*Edit\* The mods told me to remove any links to a github repository that is less than 3 months old (I thought it was just the [ls.io](http://ls.io) docker image, but it was also the bridge repository), so if you have seen this flash up a couple of times before disappearing, that is why, sorry.

[v2.6.0](https://audiosilo.app/blog/server-2-6/) was released yesterday, and it's at a stage now where a lot of the features I wanted in are there.

A bit about me first, I've been a software developer for 20 years, I'm a member of [linuxserver.io](http://linuxserver.io/) and the developer of the [Heimdall Application Dashboard](https://github.com/linuxserver/Heimdall), which is 8 years old at this point, has over 9k stars on github and 589M docker pulls. I'm also the developer of [fanart.tv](http://fanart.tv/) which is 16 years old and [used by lots of mediacentres](https://fanart.tv/get-an-api-key/#casestudies) such as Plex, Emby, Jellyfin, Kodi etc.

Both of those projects were made for other people though. I wanted to build something I had a passion for, and that was where this project was born 5 years ago, there are still reddit posts from around then, and the old repository for it is now archived here: [https://github.com/KodeStar/audiosilo-old](https://github.com/KodeStar/audiosilo-old)

About 5 months ago, I decided to see what I could accomplish with assistance from Claude, this isn't a vide coded project, but it would not have been possible to get so much done in the relatively short amount of time without the help, so if that turns you off, I completely understand but please just ignore this post rather than turning your firehose of vitriol on me 🤣

# How does it compare to the competition?

A question I get a lot is how does it compare to AudioBookShelf, so I have a post here [https://audiosilo.app/blog/audiosilo-vs-the-competition/](https://audiosilo.app/blog/audiosilo-vs-the-competition/) comparing it with ABS, Grimmory and BookOrbit, but as I'm the AudioSilo dev, take those claims with a pinch of salt and do your own tests (I tried to keep it as fair as possible).

The short version is AudioSilo is faster than the others and uses less resources, but lacks some of the feature the others have, in particular OIDC (It's on the roadmap) and 3rd party integrations (though there is an api and [developer docs](https://docs.audiosilo.app/developers)), as it's just not as mature yet. But at this point it also has an incredible amount of features, it has the server, a web player, apps for ios, android, apple watches (wear os is planned for the next release), carplay, android auto, audible integration (automatic or manual backups from audible to your server), upcoming releases, readalong (this is new and not well tested yet, hopefully improvements will come in 2.7.0), a community metadata database, character list, recaps and much more.

# What you need to get started:

The only thing you need for 90% of the functionality is to run the [audiosilo-server](https://github.com/KodeStar/audiosilo-server) component, you can just run the docker container, either [our one](https://docs.audiosilo.app/users/getting-started/quickstart-docker), or the [linuxserver.io](http://linuxserver.io) version (it's also available on Unraid). The server component is designed to be readonly, have no default passwords, credentials are generated on first run or by you on a one-time setup page, access by invite and login attempts are rate limited. This is because the server component is the most likely part to be internet facing so I've tried to make it as safe as reasonably possible. It has the web version baked into it.

There is also an audiosilo-bridge component, this is designed to \*not\* be internet facing. It has write access, and the bridge calls the server, the server never calls the bridge. Every 30 seconds or so the bridge sends a heartbeat to the server and asks if there are any jobs for it. The bridge is used for the audible integration, podcasts, character sheet and recap generation, github integration (for sending recaps and characters to the meta repository as well as metadata fixes) and read-along alignment. There are lots of other bits that happen as well, so [read more details here](https://docs.audiosilo.app/users/getting-started/running-a-bridge) but this is a completely optional part.

Another pillar of the project in the community metadata database at [https://meta.audiosilo.app](https://meta.audiosilo.app/) this is what is used for fixing metadata and providing character sheets and recaps, everything is stored on github so that the data is always freely accessible and not stored away in some black box noone can see. Storing it on github has some downsides, the main one being having to store the data in packs (I'm looking at alternative options), which makes it less convenient to contribute to than I'd like, but it does mean I don't have to store any account details, but you can file fixes from the site, or by creating a github issue. The meta site also allows you to watch series for new books without using AudioSilo at all.

# Is it bug free?

Of course it's not, when has any software been? There are going to be issues, a lot of them I'm aware of and are planned for upcoming releases [https://github.com/users/KodeStar/projects/1/](https://github.com/users/KodeStar/projects/1/) but I've also been using this everyday for the last 4-5 months (the initial version was mostly a rewrite of the old version so I had something running pretty quickly) and making it better with every release.

There is probably twice as much time, if not more, devoted to testing than adding the feature in the first place.

# Do I plan to charge for this?

No, as stated on this page [https://audiosilo.app/pricing/](https://audiosilo.app/pricing/) everything is free, there is no paid tier, no features behind a paywall, no accounts, no ads, no telemetry. Everything is either AGPLv3 or CC0-1.0 (the community meta database), to the extent that the metadata database is stored on github, so anyone can see and use the data.

Everyday we see multiple vibe coded apps released with the sole purpose to create a quick buck, I wanted to instead use AI to help me create something special that I could use every day myself, and also share with the world for free.

That said, hosting, AI accounts, the annual apple developer account all cost money (and I've sunk a lot of personal time into this, and will continue to do so) so if you end up finding it useful and want to sponsor me it would be gratefully received [https://github.com/sponsors/KodeStar](https://github.com/sponsors/KodeStar) and if you don't want to do that, adding metadata, reporting issues, starring the repository and telling friends are all equally as gratefully received.

If you have any questions, you can ask here or [join the discord](https://discord.gg/nFFqRbkRn6)

## 评论（123/124）

> **asimovs-auditor**（1 分） · 2026-11-09T04:36:54+08:00　
> Expand the replies to this comment to learn how AI was used in this post/project.

---

> **ls_kode**（-6 分） · 2026-11-09T04:42:47+08:00　
> The post had no AI help, probably why I messed it up a couple of times creating it :D The project itself has AI assistance, as detailed at the top of every repository to ensure no-one is mislead and in the post itself. As mentioned in the post, I've been a software developer for 20 years and AI has been used to help get it to its current state.

---

> **corn-sandwich**（2 分） · 2026-11-09T05:10:01+08:00　
> Any plans to integrate with koreader?  One of the things that's kept me on BookOrbit is their Koreader plugin/dashboard.  BookOrbit itself is heavier than i need with a smaller library, so ill definitely try this out and see how it stacks up.

---

> **TheLamer**（0 分） · 2026-11-09T05:26:49+08:00　
> Is koreader for audiobooks ?

---

> **ls_kode**（3 分） · 2026-11-09T05:26:52+08:00　
> Yes, it's in the backlog here [https://github.com/users/KodeStar/projects/1/views/1?filterQuery=release%3Av2.7.0+korea&pane=issue&itemId=284621381&issue=KodeStar%7Caudiosilo-server%7C234](https://github.com/users/KodeStar/projects/1/views/1?filterQuery=release%3Av2.7.0+korea&pane=issue&itemId=284621381&issue=KodeStar%7Caudiosilo-server%7C234) It's currently planned for 2.7.0 but might slide to 2.8.0 as I don't have a kobo or anyone that can help test it, but it's definitely something I want to get in.

---

> **Far_Squirrel_6148**（2 分） · 2026-11-09T05:27:47+08:00　
> This looks very clean and nice. I built my own Audio App because I need Mopidy and Navidrome controls in the same app. I might slop-fork some parts though.

---

> **corn-sandwich**（1 分） · 2026-11-09T05:31:37+08:00　
> Nice.  Im spinning it up and am happy to test when you get there.  All i have is a jailbroken kindle.

---

> **Mashic**（0 分） · 2026-11-09T05:38:25+08:00　
> any plans to make a native termux port?

---

> **ls_kode**（2 分） · 2026-11-09T05:41:14+08:00　
> Koreader is for ebooks, but with the readalong functionality you can use it to update books on e-ink devices and keep the ebook and audiobook in sync

---

> **mitchins-au**（55 分） · 2026-11-09T05:42:15+08:00　
> What advantages does this have over the much more mature Audiobookshelf?

---

> **Perfekthuntr**（10 分） · 2026-11-09T05:45:27+08:00　
> I love the open DB aspect, and I'm genuinely impressed by the memory usage benchmarks, but as someone who keeps both books and audiobooks side by side I find this less useful. I do hope it does well as competition is always good for making everything better.

---

> **ls_kode**（1 分） · 2026-11-09T05:46:04+08:00　
> Sounds good, not sure my wife would let me jailbreak her kindle, but I’m sure i’ll be able to figure something out, I have a kobo lying around somewhere, just need to find it

---

> **Leflyingsaucer**（0 分） · 2026-11-09T05:48:06+08:00　
> Hey ! Very nice work !
> Anu chance to have your app published on the official TrueNas catalog ?

---

> **ls_kode**（1 分） · 2026-11-09T05:48:39+08:00　
> [https://audiosilo.app/blog/audiosilo-vs-the-competition/](https://audiosilo.app/blog/audiosilo-vs-the-competition/)

---

> **AlBundysPants**（11 分） · 2026-11-09T05:49:38+08:00　
> OP posted a link to comparison above.

---

> **ls_kode**（1 分） · 2026-11-09T05:50:30+08:00　
> I'm not sure, I'll have a look into it

---

> **elcool0r**（-1 分） · 2026-11-09T05:50:48+08:00　
> I dont think that I'll jump ship from abs as my primary use is to connect a carplay compatible client and I am happy with it. But when you are develping an app that is tied to audible maybe look into a release tracker & notification. Audible has a public but undocumented api which i used to vibe code a nice webapp [https://github.com/elcool0r/audiobook-tracker](https://github.com/elcool0r/audiobook-tracker)
> maybe it is some feature inspiration as audible totally lacks it. also totally continue with mark of the fool! :D

---

> **ls_kode**（3 分） · 2026-11-09T05:54:21+08:00　
> What is wrong with keeping them side by side? Audiosilo doesn't stop you doing that, and if you have both the audiobook and the ebook, you can use the bridge and agent containers to add readalong functionality. Without the bridge, you can still open the book and manually read at the same time, but more advanced functionality is in the backlog.

---

> **ls_kode**（1 分） · 2026-11-09T05:55:14+08:00　
> I'll look into it, I've never tried adding something there before though.

---

> **VogelimBart**（4 分） · 2026-11-09T05:58:03+08:00　
> Yeah performance is fine and all, but what features set it apart?

---

> **ls_kode**（1 分） · 2026-11-09T05:58:17+08:00　
> Audiosilo has both carplay and a release tracker, it also allows you to automatically back up Audible books that you have preordered when they become available. You can also watch series you are interested in directly on [meta.audiosilo.app](http://meta.audiosilo.app) without using audiosilo and set up notifications / calendar integration.

---

> **Perfekthuntr**（3 分） · 2026-11-09T06:02:03+08:00　
> I may give it a try then, I would love to see a Kindle sync style behavior that lets me listen in the car, autosyncs my progress to the ebook. I know that's not an easy ask (I'm well aware it's actually an insanely hard problem to solve)
>
> Also OIDC support please, I'd test drive it tomorrow if that was enabled

---

> **ls_kode**（1 分） · 2026-11-09T06:02:32+08:00　
> That was also in the comparison post, at the bottom. But things like released IOS and Android apps, carplay and android auto, watch support, readalong, character sheets, recaps, Audible integration (automatically or manually backing up books as they are released), there are a bunch of upcoming features on the project tracker as well.

---

> **VogelimBart**（2 分） · 2026-11-09T06:04:03+08:00　
> Cool thx!

---

> **ls_kode**（5 分） · 2026-11-09T06:05:45+08:00　
> Yeah, OIDC is on the roadmap. Koreader support will likely come soonish, which would require jailbreaking your kindle to install it, but I don't know of another way to get syncing on a kindle .

---

> **kernald31**（2 分） · 2026-11-09T06:19:42+08:00　
> You can use KOReader on Linux, for what it's worth, you don't need a dedicated device.

---

> **kernald31**（1 分） · 2026-11-09T06:21:09+08:00　
> As much as I don't see myself moving away from ABS, the open database is definitely a cool project, props to you for that. I hope it gets the traction it needs, and Audible stops being essentially the only reference database for audiobooks.

---

> **ls_kode**（2 分） · 2026-11-09T06:21:34+08:00　
> Good to know, thanks. That will likely make it easier to get something working.

---

> **corn-sandwich**（0 分） · 2026-11-09T06:28:26+08:00　
> Do you plan to also support ebooks in the library?  With the readalong support and comparisons to Audiobookshelf, i expected the ebooks to also be imported.

---

> **Nill_Ringil**（0 分） · 2026-11-09T06:30:59+08:00　
> What about migrating from AudioBookShelf? Are there any tools or instructions?
>
> I use ABS, and I already have edited book titles and series, listening history, and everything like that there.
>
> Is it possible to move to AudioSilo while keeping all of that? Or will I have to do everything from scratch?

---

> **ls_kode**（2 分） · 2026-11-09T06:33:43+08:00　
> It already works as a datasource for ABS [https://meta.audiosilo.app/audiobookshelf](https://meta.audiosilo.app/audiobookshelf), additionally, you don't have to move away from ABS, you can run them side by side, and even import listening data from ABS [https://audiosilo.app/blog/moving-from-audiobookshelf/](https://audiosilo.app/blog/moving-from-audiobookshelf/)

---

> **ls_kode**（3 分） · 2026-11-09T06:35:49+08:00　
> Yes, though I'm not 100% sure yet if ebooks only will be supported, or only alongside an audiobook. It's certainly not my main focus at the moment anyway.

---

> **ls_kode**（2 分） · 2026-11-09T06:38:50+08:00　
> Yes, they can run alongside very happily, take a look at [https://audiosilo.app/blog/moving-from-audiobookshelf/](https://audiosilo.app/blog/moving-from-audiobookshelf/) that lets you move listening history, more details are here [https://docs.audiosilo.app/users/admin/import](https://docs.audiosilo.app/users/admin/import) also any ABS meta json that lives alongside the books is read as well.

---

> **corn-sandwich**（1 分） · 2026-11-09T06:39:37+08:00　
> Yep, i get it.

---

> **thermita**（0 分） · 2026-11-09T06:40:54+08:00　
> Buenas tardes, acabo de instalar Audio Silo autohospedado y me pide un Código de invitación, como lo soluciono?

---

> **ls_kode**（1 分） · 2026-11-09T06:44:39+08:00　
> Revisa los registros de la instalación; ahí encontrarás los detalles. [https://docs.audiosilo.app/users/getting-started/first-run](https://docs.audiosilo.app/users/getting-started/first-run)

---

> **ls_kode**（1 分） · 2026-11-09T06:46:45+08:00　
> Si te refieres a un dispositivo, ve a la sección de administración / Personas / Administrador y, a continuación, haz clic en «Vincular un dispositivo».

---

> **LittlePocketDev**（2 分） · 2026-11-09T06:58:06+08:00　
> Are you actually using it yourself?
>
> I started playing around with the [web demo](https://demo.audiosilo.app/) and noticed some weird behavior with the mini-player. It keeps jumping around unexpectedly when I click on it, and sometimes even when I'm not interacting with it.
>
> Here are a few screenshots for reference:
>
> [https://ibb.co/S7Dp05zw](https://ibb.co/S7Dp05zw)
>
> [https://ibb.co/sdjhg16D](https://ibb.co/sdjhg16D)
>
> [https://ibb.co/KjNkG5s9](https://ibb.co/KjNkG5s9)
>
> Overall, thanks for sharing your project! Just wanted to flag this issue.

---

> **ls_kode**（1 分） · 2026-11-09T07:11:30+08:00　
> Yeah, i saw that issue yesterday. I use the ios app the most, but will get that fixed.

---

> **Mediocre_Safety5743**（2 分） · 2026-11-09T07:30:26+08:00　
> From what I have seen moving listening history over is usually the annoying part when people switch these apps. The low memory use sounds good though.

---

> **ls_kode**（3 分） · 2026-11-09T07:39:27+08:00　
> It's fairly simple to do on AudioSilo if you are coming from ABS [https://audiosilo.app/blog/moving-from-audiobookshelf/](https://audiosilo.app/blog/moving-from-audiobookshelf/) and [https://docs.audiosilo.app/users/admin/import](https://docs.audiosilo.app/users/admin/import) explain how to do it

---

> **ls_kode**（2 分） · 2026-11-09T07:46:34+08:00　
> It's being tracked here [https://github.com/KodeStar/audiosilo-frontend/issues/244](https://github.com/KodeStar/audiosilo-frontend/issues/244)

---

> **ls_kode**（2 分） · 2026-11-09T07:55:14+08:00　
> OIDC support can be tracked here [https://github.com/KodeStar/audiosilo-server/issues/235](https://github.com/KodeStar/audiosilo-server/issues/235) feel free to add any additional details if you have any.

---

> **Unique-Budget-5839**（0 分） · 2026-11-09T08:03:43+08:00　
> Does the importer report which books or history entries failed to match before applying changes? A small test library with renamed files and two editions of the same title could make migration mistakes easier to spot before moving a whole collection.

---

> **ls_kode**（1 分） · 2026-11-09T08:13:44+08:00　
> https://docs.audiosilo.app/users/admin/import#step-3-review-and-apply

---

> **spadak**（0 分） · 2026-11-09T08:25:24+08:00　
> Just installed on unraid, works great!

---

> **Ck-retro**（0 分） · 2026-11-09T09:54:54+08:00　
> Where is everyone grabbing audio books these days? Any good sites?

---

> **autistic-dick**（1 分） · 2026-11-09T10:00:53+08:00　
> I couldn’t resist and spun up the server to give it a go. It helped me find quite a few duplicate authors. The health page is very cool!
>
> I had a few quick questions though.
>
> What is the correct flow or way to get back to the admin page? Just go to /admin endpoint? Might be overlooking the link if there is one. I’m wondering if I did something wrong since I keep getting redirected to the QR page when I go to my public url.
>
> Then other question is more of a feature request. Would you consider adding support/integration for ReadMeABook or some other indexer/downloaded integration? I use Absorb with Audiobookshelf and Absorb provides the integration and I’ve become dependent on it.

---

> **r__kie**（1 分） · 2026-11-09T11:05:41+08:00　
> How does progress sync work if you listen offline on Android, then use the web player before the phone reconnects? Can an old offline position overwrite the newer one?

---

> **Hallc**（5 分） · 2026-11-09T12:18:59+08:00　
> So you list 4.4s as the indexing time but then go on to say.
>
> > It would be misleading to call 4.4 seconds the end of all its background work.
>
> So you're stating it's dramatically faster at a glance in your table and then saying it's not that fast? If you want to have an actual fair comparison you'd surely want to show it once all the background work is done?

---

> **Command-Forsaken**（1 分） · 2026-11-09T13:03:08+08:00　
> Neat. I used Heimdall back in the day. Might check this out as wifey wants books.

---

> **phlegm-fighter**（1 分） · 2026-11-09T13:10:04+08:00　
> Welp, you have a lifelong user from me as long as you stay free, and the same attitude in this post 🤝

---

> **Spirited_Cheesus**（0 分） · 2026-11-09T13:29:47+08:00　
> +1

---

> **Lanten101**（1 分） · 2026-11-09T13:30:41+08:00　
> Would be usefull to have audiobookshelf compatible API as it has established support apps

---

> **wtanksleyjr**（4 分） · 2026-11-09T13:49:30+08:00　
> Audible plus Libation; Downpour.com (mostly no DRM and good sales); Libro.fm (no DRM at all); Google Play (use "export" on many books to get m4a).

---

> **ls_kode**（2 分） · 2026-11-09T15:32:53+08:00　
> I don’t know a way to find out when the others have finished background work (but it will be longer than the indexing time), just when they have finished indexing. Even if you were to count the background work as indexing (it’s not) it’s still 30s vs over 3 minutes (minumum + whatever background work they do after) for the next fastest

---

> **H2OKing89**（1 分） · 2026-11-09T15:36:56+08:00　
> Does this work with `xHE-ACC`?

---

> **ls_kode**（3 分） · 2026-11-09T15:40:59+08:00　
> I did think about that, but then that becomes an ever moving target I have to support. I could take another look to see how plausible it is, but it’s not currently a high priority for me.

---

> **wryterra**（17 分） · 2026-11-09T17:53:08+08:00　
> Yes and I read the comparison. It didn’t tell me anything audiosilo does that audiobookshelf doesn’t. Ita faster at initial scan? Ok cool, but I did my initial scan years ago. It uses less memory? Ok cool but I’m not short of memory. Does it do anything new or different?

---

> **MrsMirage**（0 分） · 2026-11-09T18:00:07+08:00　
> Besides just trying something new, what would be the argument to switch over from audiobookshelf.
> I read your comparison, and while it's impressive from a technical point of view, I don't get how this would change anything on a daily basis since indexing the library is a one time event.
>
> Also any possibility to use Prologue and/or Absorb with it?

---

> **ls_kode**（1 分） · 2026-11-09T18:09:00+08:00　
> I guess it depends on your setup. If you use Audible then having books automatically backed up to your server as they release is useful, as well as showing upcoming releases, but if you don't, it's not. Ongoing resources isn't a one time event, but if you don't care about that, it's also not compelling.
>
> Prologue and Absorb could absolutely be updated to support AudioSIlo, but that is up to the developers, especially Prologue as it's not open source, so until/unless AudioSilo becomes more popular, they probably aren't going to.
>
> Honestly, I think AudioSilo looks and works better, but that's a personal opinion.
>
> There is no reason you can't run both at the same time and see what you think.

---

> **Mashic**（1 分） · 2026-11-09T19:05:29+08:00　
> 1. Can you add an option to lock seek controls in case of accidental tap on Android.
> 2. It uses more ram on ubuntu than audiobookshelf 130 MB vs 70 MB.

---

> **ls_kode**（1 分） · 2026-11-09T19:46:39+08:00　
> 1. Yeah, that's not a bad idea. If you do accidentally seek, if you open up the player there is an undo chip for several seconds, or you can look at the history and go back to where you were in the interim, I've filed it here for tracking https://github.com/KodeStar/audiosilo-frontend/issues/245.
> 2. On RAM: in my tests it normally idles well under Audiobookshelf, so I'd like to work out what's different on your setup. Could you tell me:
>
> 1. How you measured it (`docker stats`, Portainer, htop/top RES, something else), and whether it's Docker or the plain binary?
> 2. Roughly how big the library is, and how many CPU cores the machine has?
> 3. Whether something was playing or you'd just been browsing when you checked, and whether it drops if you leave it idle for 10-15 minutes?
> 4. Was Audiobookshelf measured doing the same thing?
>
> Playing a book shouldn't add much on the server side because it streams straight from disk, but the server does hold on to memory for a while after you've been using it, and some tools also count the system's file cache.

---

> **LetMePaintDeath**（2 分） · 2026-11-09T19:59:37+08:00　
> Just installed on Unraid - This is feeling really good. Extremely responsive on my Android phone, feels very nice.
>
> Some feedback!
> Is there a way to make the background for the ebook reader completely black for OLED screens? I rely on this for reading and can't change from ABS until this is available. It would also be good to make it so the reader can be more immersive - mostly just auto hiding away the title, chapter selection, and font buttons at the top so that it is only book content on the screen.
>
> Secondly, the matches are so quick, it's crazy how fast it finds and provides the match for a book. That said, it's been really surprising me some of the books it hasn't been matching. For instance, it couldn't match Naomi Klein's newest book 'End Times Fascism', which is not exactly an unknown. Could there be something I'm missing here or a setting to change?
>
> I really like it so far and look forward to see how things go! (I'm honestly likely to change as soon as that Black OLED thing is possible)

---

> **Mashic**（1 分） · 2026-11-09T20:14:36+08:00　
> Proxmox, ubuntu 24.04 lxc, 4 cores cpu, 16GB of ddr5 ram, 500 audiobooks library, using docker stats:
>
> Same stats in idle and while listening on 1 device.
>
> 06f901bbfe21   audiosilo          0.00%     103.2MiB / 8GiB     1.26%     4.2MB / 374MB     3.53GB / 112MB    25
> ee70e89ada90   audiobookshelf     0.02%     69.13MiB / 8GiB     0.84%     25.6MB / 158MB    479MB / 53.9MB    12

---

> **ls_kode**（4 分） · 2026-11-09T20:22:05+08:00　
> I've added your suggestions to the roadmap here [https://github.com/KodeStar/audiosilo-frontend/issues/246](https://github.com/KodeStar/audiosilo-frontend/issues/246) so you can track it, feel free to add any comments to it.
>
> For the question about mapping, it uses the community metadata project at [https://meta.audiosilo.app](https://meta.audiosilo.app) which relies on the community to fill in missing information, so if it didn't find it, then it's likely not there. Type it into the search bar there and if it isn't there it will give you some options for adding it.

---

> **LetMePaintDeath**（1 分） · 2026-11-09T20:28:36+08:00　
> Fantastic, that all looks perfect, thanks!
> Any chance for the Bridge to be available on Unraid community apps? I'm sure I'll work out just doing in through compose, but just curious for simplicity's sake.
> Thanks again!

---

> **ls_kode**（1 分） · 2026-11-09T20:33:00+08:00　
> Thanks, that's helpful. The BLOCK I/O column shows AudioSilo has read 3.5 GB from disk (mostly the library scan) vs 479 MB for ABS. `docker stats` counts some of the file cache from those reads against the container, so it may not be memory the server itself is holding. Could you run these two and paste the output?
>
>     docker exec audiosilo sh -c 'grep -E "VmRSS|RssAnon|RssFile" /proc/$(pidof audiosilo)/status; grep -E "^(anon|file|active_file|inactive_file) " /sys/fs/cgroup/memory.stat'
>     docker exec audiosilo sh -c 'sync; echo 1 > /proc/sys/vm/drop_caches' 2>/dev/null; docker stats --no-stream audiosilo audiobookshelf
>
> The first splits it into the server's own memory (`anon` / `RssAnon`) vs file cache (`file`). The second probably won't be allowed inside an LXC, which is fine, the first is the important one.

---

> **Mashic**（1 分） · 2026-11-09T20:41:47+08:00　
> VmRSS:     64816 kB
> RssAnon:           45320 kB
> RssFile:           19496 kB
> anon 46723072
> file 1735729152
> inactive_file 1689542656
> active_file 46153728
> CONTAINER ID   NAME             CPU %     MEM USAGE / LIMIT   MEM %     NET I/O          BLOCK I/O        PIDS
> 06f901bbfe21   audiosilo        0.00%     103.7MiB / 8GiB     1.27%     4.45MB / 385MB   3.53GB / 113MB   25
> ee70e89ada90   audiobookshelf   0.03%     71.05MiB / 8GiB     0.87%     26MB / 255MB     601MB / 55.1MB   12

---

> **ls_kode**（2 分） · 2026-11-09T21:15:20+08:00　
> Thanks, thats about what I was expecting. The server process itself is using about 45 MB (`RssAnon` / `anon`). The rest of the 103 MiB that `docker stats` shows is the Linux file cache from reading your library and the database (`active_file` 44 MB), which the kernel charges to the container but hands back the moment anything else needs memory. The scan read a lot more from disk than ABS (the 3.5 GB in BLOCK I/O), so more cache ended up counted against it.
>
> For a like-for-like comparison, the same command for ABS would be:
> `docker exec audiobookshelf sh -c 'grep -E "VmRSS|RssAnon" /proc/$(pidof node)/status'`

---

> **TheyCallMeDozer**（8 分） · 2026-11-09T21:28:28+08:00　
> so sell me on this, why should I replace audiobookshelf with your app??

---

> **ls_kode**（1 分） · 2026-11-09T21:48:20+08:00　
> I've added a ticket here [https://github.com/KodeStar/audiosilo-bridge/issues/61](https://github.com/KodeStar/audiosilo-bridge/issues/61) to track that, the short answer is yes it's possible, just need to figure out the logistics. It's much simpler with compose, because they are split up on purpose, server has read only access, bridge has write access, and the agent container (if you use it) is silo-ed off on it's own network with no access and is just fed data to work on from the bridge.

---

> **Mashic**（1 分） · 2026-11-09T21:55:40+08:00　
> I did `docker compose down && docker compose up -d`, ram usage is ~27MB now.

---

> **ls_kode**（1 分） · 2026-11-09T22:05:49+08:00　
> Install it alongside and see for yourself if it fits you needs, mount the library readonly. If you don't like it, remove it, no harm no foul. If the "How does it compare to the competition?" section in the post above isn't compelling then stick with ABS. I'm sure ABS is perfectly fine for a lot of people, and maybe in the future AudioSilo will add a feature that makes you reconsider and that's ok too :). there's nothing wrong with some healthy competition.

---

> **Unique-Budget-5839**（1 分） · 2026-11-09T22:07:20+08:00　
> That answers the review question. Seeing the skipped books with reasons and listening time before applying makes it much easier to judge the impact of a migration.

---

> **TheyCallMeDozer**（4 分） · 2026-11-09T22:15:38+08:00　
> its not an attack, its just, you have walls of text for everything, very few people have the time and even more recently paitents to read through alot of text (unfortunate side of modern life and connectivity) so a suggestion, build a gride, simple tick box difference that someone can quick glance at. To me i see  your page wall of text, search for ABS, click to again get a wall of text that can be explained in a simple 1 page grid like this, it would speed up peoples review and quick understand. Unfortunatnly very few people will sit and read through a wall of text when trying to quick understand why they should switch from somehting they have used for years to a brand new app, which could be better, but they would have to read through walls of text to understand why its better and how it works
>
> https://i.redd.it/m4205wtrhl0i1.png

---

> **ls_kode**（1 分） · 2026-11-09T22:19:53+08:00　
> It's not an attack on you either, sorry if it came across that way, here is the paragraph from the wall of text that hopefully answers your question, but the reason I said to try it alongside is trying it will probably answer the questions better than me typing a load of text:
>
> >The short version is AudioSilo is faster than the others and uses less resources, but lacks some of the features the others have, in particular OIDC (It's on the roadmap) and 3rd party integrations (though there is an api and [developer docs](https://docs.audiosilo.app/developers)), as it's just not as mature yet. But at this point it also has an incredible amount of features, it has the server, a web player, apps for ios, android, apple watches (wear os is planned for the next release), carplay, android auto, audible integration (automatic or manual backups from audible to your server), upcoming releases, readalong (this is new and not well tested yet, hopefully improvements will come in 2.7.0), a community metadata database, character list, recaps and much more.
>
> I will also look at adding a comparison table at the top of the blog posts to make it easier.

---

> **TheyCallMeDozer**（0 分） · 2026-11-09T22:25:34+08:00　
> That paragraph has me going to install it to try it out, straight to the point. When posting in future, use that text as an TLDR and you will get more users.
>
> If there is one feature I can suggest extra, on the driod and ios app, make sure there is a resume after a call or alert. its the one place that kills ABS for me and other people I know. I could be swimming/running/driving listening to a book, someone calls me, the book stops, even if I don't answer it from my headset the book is just paused, i have to stop what im doing to go restart it, or spend the rest of the activity in silence.

---

> **ls_kode**（1 分） · 2026-11-09T22:32:27+08:00　
> Here's the quick-glance version (AudioSilo 2.6.0 vs Audiobookshelf 2.37, same box, same 1,000-book library):
>
> | Feature | Audiobookshelf | AudioSilo |
> |:--|:--|:--|
> | First scan, 1,000 books | 3 min 41 s | 4.4 s |
> | CPU used by that scan | 1,098 s | 11.6 s |
> | Memory once loaded and idle | 197 MiB | 28 MiB |
> | iOS + Android apps | ⚠️ official apps in beta | ✅ App Store + Google Play |
> | CarPlay | ⚠️ third-party app | ✅ |
> | Android Auto | ✅ | ✅ |
> | Apple Watch | ⚠️ third-party app | ✅ (Wear OS next release) |
> | Spoiler-safe recaps + characters | ❌ | ✅ |
> | Audible backup + listening sync | ❌ | ✅ (with the Bridge) |
> | Upcoming releases in your series | ❌ | ✅ |
> | Podcasts | ✅ built in | ⚠️ needs the Bridge |
> | Ebook library (EPUB/PDF/comics) | ✅ | ⚠️ audiobook's EPUB only, with read-along |
> | Edit tags / upload from browser | ✅ | ❌ read-only by design |
> | Single sign-on (OIDC) | ✅ | ❌ on the roadmap |
> | Third-party apps + integrations | ✅ big ecosystem | ❌ API only so far |
> | Import ABS history + bookmarks | n/a | ✅ |
>
> Full numbers and how they were measured: https://audiosilo.app/blog/audiosilo-vs-the-competition/

---

> **ls_kode**（1 分） · 2026-11-09T22:41:26+08:00　
> I'll double check, I think it restarts, I'm trying to think when I'm walking the dog and I get a call, does it restart automatically or do I press the headset to start it again. I know it continues after an alert, the audio drops out to tell me how long the last km took before continuing on its own.
>
> \*edit\* confirmed. Answering a call, the audio continues after the call ends, ignoring a call the audio continues after it stops ringing.

---

> **ls_kode**（2 分） · 2026-11-09T23:04:14+08:00　
> Take a look at [https://audiosilo.app/blog/audiosilo-vs-the-competition/](https://audiosilo.app/blog/audiosilo-vs-the-competition/) again, I added a comparison table at the top.

---

> **Bichslapin**（1 分） · 2026-11-10T00:14:52+08:00　
> Doesn't seem like it's within scope of the project, but thought I'd ask. Is there any ebook support? Even if the reader sucks it's nice to be able to open an ebook in abs if I forget my dedicated reader.

---

> **ls_kode**（2 分） · 2026-11-10T00:34:56+08:00　
> Yeah there is, the support is fairly new and it only works as a companion for an audiobook and only epub is currently supported. There is readalong support with the bridge installed, otherwise you can manually move position. Koreader support is on the roadmap for 2.7.0 as well as some other improvements.

---

> **Hostman_com**（2 分） · 2026-11-10T00:54:30+08:00　
> Making the metadata database work with Audiobookshelf is a good move. People can use it and contribute missing books without switching players.
>
> https://i.redd.it/og4s2ymdam0i1.png

---

> **ls_kode**（3 分） · 2026-11-10T01:15:18+08:00　
> Absolutely, I honestly don't care if people use AudioBookShelf or AudioSilo, I built AudioSilo primarily for me and I'm happy with how it's turning out. They were actually both created [within about a month of each other initially](https://github.com/KodeStar/audiosilo-old/). Like when I started AudioSilo, ABS wasn't a thing, which seems crazy now.
>
> Improving the metadata database is a net gain for everyone in my opinion so I'm conscious of trying to make it as accessible as possible.

---

> **C0rn3j**（0 分） · 2026-11-10T02:09:27+08:00　
> It's all LLM generated, so that's not surprising.

---

> **C0rn3j**（8 分） · 2026-11-10T02:14:01+08:00　
> If you like adventure, it's a great option, because half the commits are non-descript "Simplify pass" or "Code review fixes", so maintaining this thing in the long term is going to be FUN, and makes it clear this is just an LLM holding the wheel, as a sane developer would not just throw a variant of "fixes something" at every change description.
>
> Am not joking, see for yourself - https://github.com/KodeStar/audiosilo-server/commits/main/
>
> And for comparison - https://github.com/advplyr/audiobookshelf/commits/master/

---

> **Auratama**（16 分） · 2026-11-10T02:34:41+08:00　
> Wow, those docs are borderline unreadable wordsalad from Claude. Can't even find very basic information about features.

---

> **TheyCallMeDozer**（2 分） · 2026-11-10T02:41:50+08:00　
> perfect that works way better, then just text the visuals are easier to follow and quicker to understand.... tiktok has really fried alot of peoples brains unfortunatnly its something to think of catering to

---

> **ls_kode**（-6 分） · 2026-11-10T03:02:22+08:00　
> 🤣 yeah they need a bit of love, was there something in particular you were looking for? Did the search not help at all?

---

> **Beelze_Bubi**（1 分） · 2026-11-10T03:39:23+08:00　
> Love the concept, directly lead me to ignore my dinner by 2h to play around with everything. The possibilities of the community metadata blew my mind.
> I probably won't daily drive it (just yet) as I heavily switch between audio book and ebook and use BookBridge as a Whispersync alternative. As has been mentioned, 3rd party support is on the roadmap so I'm positive that I can daily drive this very soon.
>
> Also, is it just me or is the player control on iOS kinda funky with bluetooth headphones? I use the AirPods and the Skip command translates to next chapter and not skip X seconds. I wished, I could configure this but maybe it's just me using it wrong...

---

> **drpencilcase**（1 分） · 2026-11-10T04:06:20+08:00　
> It would be great to have android automotive app as well in addition to android auto. Not sure how easy/hard would be to add that to the current android player.

---

> **ls_kode**（1 分） · 2026-11-10T04:52:15+08:00　
> Hmm, I only use the controls for on or off on my headphones 🤣  I'll have a look if it's configurable though, currently iOS send next track which is mapped to next chapter, it is probably possible to let users choose what it does though, I've added it here so it can be tracked [https://github.com/KodeStar/audiosilo-frontend/issues/247](https://github.com/KodeStar/audiosilo-frontend/issues/247)

---

> **ls_kode**（1 分） · 2026-11-10T04:56:46+08:00　
> I'm a carplay user so not 100% sure what that is 🤣 but I've added it to the roadmap penciled in for 2.8.0, you can track it at [https://github.com/KodeStar/audiosilo-frontend/issues/248](https://github.com/KodeStar/audiosilo-frontend/issues/248) feel free to add any useful details

---

> **mrrask**（-3 分） · 2026-11-10T06:11:35+08:00　
> Well, you are just dismissing the advantages, that doesn't mean they aren't there. I haven't tested this yet, but the trust-me-bro comparisons do show why one would use an alternative to ABS. And then there's always the fact that this actually feels and looks like something made in this decade, unlike ABS.

---

> **wryterra**（3 分） · 2026-11-10T07:23:55+08:00　
> I'm not dismissing the advantages.
>
> If a scan is longer, but the results are more accurate, then the longer scan is preferable. Giving speed as the only metric is not compelling.
>
> If more memory is used but the application is more performant as a result that's a good thing, giving memory used as the only metric is not compelling.
>
> They're synthetic benchmarks that look nice and convince gullible people and they're right at the top where unique and interesting features should be.

---

> **ls_kode**（-3 分） · 2026-11-10T08:44:21+08:00　
> See if you find them any easier now.

---

> **ls_kode**（1 分） · 2026-11-10T08:51:42+08:00　
> That's the point though, the longer scan times aren't getting more accurate results, AudioSilo is running significantly faster and getting significantly better results. It's using less memory and is more performant.
>
> \*edit\* Also the linked post has been updated to give headline details upfront (including some of the features) in a table, rather than having to scroll through all the text.

---

> **ls_kode**（1 分） · 2026-11-10T09:02:26+08:00　
> There isn't currently a way to go from the player to the admin page, so yeah, just got to /admin for now, I'll have a think on it.
>
> I can look at what is involved for ReadMeABook, but it's not currently a priority.

---

> **ls_kode**（1 分） · 2026-11-10T09:04:15+08:00　
> It uses newest wins, if there is a discrepancy it will ask which one to use. At least that's the theory, I haven't extensively tested that scenario.

---

> **steel_reserve_211**（1 分） · 2026-11-10T10:16:57+08:00　
> Lmao literally why 😂😂😂

---

> **RandoMcGuvins**（1 分） · 2026-11-10T13:15:48+08:00　
> Your comparisson doc isn't accurate. Audiobookshelf's app isn't in beta in android. I can find that error within 1min, doesn't look good.

---

> **Shurialvaro**（1 分） · 2026-11-10T14:09:54+08:00　
> Hey man, pretty neat program! Is there a possibility we can get a volume slider on the web player?

---

> **ls_kode**（1 分） · 2026-11-10T15:13:56+08:00　
> That’s why it’s partial, not no. The iOS app is in beta and the list is full. I can see how you might be confused though, I’ll split the apps into 2 rows to make it clearer.

---

> **wryterra**（-2 分） · 2026-11-10T15:57:15+08:00　
> Yes it has been. But my post was written at a time when it hadn’t been and the focus was entirely on performance metrics not features.
>
> As it happens I personally find AudioSilo even less compelling now that the features are laid out as the answer to what it does differently appears to be “less”.
>
> Nonetheless, good luck with it.

---

> **ls_kode**（1 分） · 2026-11-10T16:11:52+08:00　
> Thanks, and no problem, I’m not trying to convert anyone away from ABS, if it works for you stick with it, healthy competition is never a bad thing. There’s also no reason you can’t run them side by side as just a list of features doesn’t really tell you how anything works.

---

> **wryterra**（-4 分） · 2026-11-10T16:12:51+08:00　
> Running something side by side when it doesn’t have features I want seems like a waste of time and effort.

---

> **tiktoktic**（1 分） · 2026-11-10T16:59:22+08:00　
> That comparison page is near unreadable due to the volume of text. Was it auto-generated?

---

> **ls_kode**（0 分） · 2026-11-10T18:00:10+08:00　
> Yes, I don't know the other apps well enough to compare them, I used those apps because they were in the LibraForge comparison (nothing to do with me, the LibraForge dev posted on the discord channel), and I didn't want my own bias creeping in, so I asked Claude to create a fair comparison. It set up each of the apps in the same environment and ran the tests. I agree it's pretty wordy, though I found the details interesting, but that just might be me. I'm updating the post to be more condensed.

---

> **tiktoktic**（1 分） · 2026-11-10T18:08:54+08:00　
> It’s a really, really difficult read.

---

> **Nill_Ringil**（2 分） · 2026-11-10T21:49:49+08:00　
> Thanks, it looks interesting.
>
> Maybe when I have some free time, I’ll try migrating from AudioBookShelf to AudioSilo, and your project will have one more user :-)

---

> **Nill_Ringil**（2 分） · 2026-11-11T01:11:49+08:00　
> That’s it, I’m now a user of yours.
>
> You have Home address and Away address. I really missed that in ABS and kept thinking I should get around to opening an issue about it.
>
> AudioSilo already has this feature.
>
> I’ll also check out what your Bridge is all about, but overall, I started it up pointing to my ABS library, everything started up fine, I went to \`/admin\` and finished configuring it, launched the mobile app, and so far I’m happy.
>
> Thanks for your work!

---

> **ls_kode**（2 分） · 2026-11-11T01:16:33+08:00　
> Good to hear :D

---

> **fuckyouabunch**（3 分） · 2026-11-11T03:10:19+08:00　
> It's not a Play Store beta, but the releases are all betas:
>
> https://github.com/advplyr/audiobookshelf-app/releases

---

> **RandoMcGuvins**（1 分） · 2026-11-11T19:07:25+08:00　
> I stand corrected, you're right. It's still in beta.
>
> I'm surprised as the app is so well polished.

---

> **RandoMcGuvins**（1 分） · 2026-11-11T19:51:26+08:00　
> ok some feed back. I'm using a synology NAS and android phone.
>
> * I had to faff around with permission.
> * Docs don't say to make a data or a backup folder. had issues there, permission again.
> * audiobookshelf import didn't work. Just kept bring up the same window in a new tab
> * More faffing around with getting the android app
> * Finally got the app working and it wants a username and password. Didn't have a option to set that up in the setup process....
> * So many books aren't matched correctly while they are matched correctly in AbookShelf, as in 70% books missing
> * Was a nightmare trying to fix your book matching to the point I gave up. In Abookshelf I can bulk match it without issues.
> * Adding users is a shit experience.
>
> Best thing I can say about it, is that it didn't mess with abookshelf and I could go back to it easily.

---

> **ls_kode**（2 分） · 2026-11-11T20:19:00+08:00　
> Thanks for at least giving it a go, sorry you had issues, you are the first person I've heard of that struggled so much 🤣 I'll see if I can improve the docs. Not sure why the import didn't work for you, noone else has reported problems, but I'll see if I can make it more idiot proof, and maybe there has been a regression, I'll look into it. The android app is a pain, iOS approve updates to the app in 5 - 12 hours, the play store seem to take 7 - 14 days, that's outside my control, hence why there is an option for the APK. Username / password is optional (only admins need a password), there is also a button to scan a QR code, that is the recommended way to login and how the docs tell you to do it, but maybe I should make the button bigger or more obvious as it's how most people will be logging in. The matching is done from the community database, it currently has about 300,000 books in it, so there are definitely gaps, part of the point is to get people to help fill out that database by adding books that are missing. We'll have to agree to disagree on the adding users experience. I don't know how it could be much easier than going to People, click invite someone, put a name and what they can access and then send them the invite link. They click on the link and scan the QR code.
>
> As I said though, thanks for trying it out. 😄
>
> \*edit\* I just re-read my comment and realised you might take it that I was calling you an idiot, that wasn't my intention 🤣
>
> \*edit2\* Found a setup redirect bug that explains the ABS import issue, this only happens on the setup flow, doing it from settings / import after finishing setup does not have the same issue, so thanks for flagging that, there are a few other improvements that can be made as well, I've added issues for them on the project and scoped them for 2.7.0, here is a list of the issues that have been added from your feedback, thanks again.
>
> [https://github.com/KodeStar/audiosilo-server/issues/365](https://github.com/KodeStar/audiosilo-server/issues/365)
> [https://github.com/KodeStar/audiosilo-server/issues/366](https://github.com/KodeStar/audiosilo-server/issues/366)
> [https://github.com/KodeStar/audiosilo-server/issues/367](https://github.com/KodeStar/audiosilo-server/issues/367)
> [https://github.com/KodeStar/audiosilo-server/issues/368](https://github.com/KodeStar/audiosilo-server/issues/368)
> [https://github.com/KodeStar/audiosilo-server/issues/369](https://github.com/KodeStar/audiosilo-server/issues/369)
> [https://github.com/KodeStar/audiosilo-server/issues/370](https://github.com/KodeStar/audiosilo-server/issues/370)
> [https://github.com/KodeStar/audiosilo-frontend/issues/264](https://github.com/KodeStar/audiosilo-frontend/issues/264)
> [https://github.com/KodeStar/audiosilo-docs/issues/277](https://github.com/KodeStar/audiosilo-docs/issues/277)
> [https://github.com/KodeStar/audiosilo-docs/issues/278](https://github.com/KodeStar/audiosilo-docs/issues/278)
> [https://github.com/KodeStar/audiosilo-site/issues/60](https://github.com/KodeStar/audiosilo-site/issues/60)

---

> **ls_kode**（1 分） · 2026-11-11T20:29:04+08:00　
> Additionally to my other comment I don't use Synology (my Nas is running on unraid) so your feedback as a Synology user is helpful, I will ensure the docs are updated with Synology specific information.

---

> **RandoMcGuvins**（1 分） · 2026-11-11T20:32:21+08:00　
> A lot of the permission issues was synology being synology. A lot of chown cmds from ssh. It's why I posted my experience. I've done some coding in my younger years and yeah... you can't underestimate the general public.
>
> * I used the QR code on my phone and it took me a website, not the app.
> * I used the invite code, still logged me in as admin. I was using it from the docker logs though instead of generating a new one.
> * From my experience I make a server (abookshelf, navidrome, sunshine/moonlight etc..) I log in as admin, make users then login in via the user. While I found the user login setup it wasn't higher in the setup section. But I understand what you're getting up. Set your own defaults > add users with their defaults > send invite codes.
> * I'm a single user on this system I don't really care if I'm logged in as admin. Wanted to give you feedback as if I had multiple users.
> * I don't want user metadata fixes. I want what's on audible or audible in my area (AU). I left it on default and most of books didn't match.
> * There's no option for the apk as your new github page got removed due to it's low lifespan. Even when I go to your site, there isn't an obvious android link. Seems to be Iphone/iplayer focused
> * I had issues finding the books that didn't match to try and match them. Wasn't intuitive.
>
> I know I'm coming across like an asshole. I'm just trying to be blunt and focused on my experience. I want your app to work, I want more options.

---

> **RandoMcGuvins**（1 分） · 2026-11-11T20:46:10+08:00　
> Ah almost forgot to tell you the good.
>
> * It did work on synology working on permission
> * nice themeing
> * grabbed the books quickly
> * nice landing page with 1st setup
> * Was able to find you app on play store without issues
> * Easy docker compose file
> * Volume boost!!! I miss this feature with Abookshelf
> * Nice options for skipping forward and back.
>
> Some design choices I would change
>
> * How you've done the series. the book stacking thing is weird. I want to glance and recognise a title
> * Accessabily options. Some of us use abooks due to bad sight. Font scaling, theme choices, icons over text etc...

---

> **ls_kode**（2 分） · 2026-11-11T22:15:23+08:00　
> Interesting. I never bothered to create a user for myself (though I have created users for my wife and kids), I just use the admin account. Also, using the invite code from the docker logs will indeed log you in as the admin, that's its purpose, but it doesn't explicitly tell you that, so I'll fix that. If you left it on default then it will have been the us version, there is a ticket for choosing the closest region which is marked for 2.7.0, but that will only work if the AU regions are listed in the database as well, currently the US and UK regions are the most filled out. I may not have been clear on what the user metadata database means in this context [https://meta.audiosilo.app](https://meta.audiosilo.app) is a separate project that is aimed at making data available for developers and users, audible doesn't have a public api (though it's private one can currently be accessed, that may not always be true) and it's also not the only supplier of audiobooks (though the most prolific). Having the community metadata as the only option is in the hopes that users help get the community database filled out, but I can understand your frustration with things not matching.

---

> **RandoMcGuvins**（1 分） · 2026-11-12T16:34:51+08:00　
> Good point on a community metadata source.
>
> Honestly, I was harder on it than I should have been. Just a long day and tinkering when I should be relaxing lol.

---

> **Hichiro6**（1 分） · 2026-11-13T02:29:07+08:00　
> Took minutes to install with an hermes agent, already listening my first audiobook.
> Don't know what ABS work but I m happy with your app

## 关联链接

- http://fanart.tv/
- http://linuxserver.io
- http://linuxserver.io/
- http://ls.io
- https://audiosilo.app/blog/audiosilo-vs-the-competition/
- https://audiosilo.app/blog/server-2-6/
- https://audiosilo.app/pricing/
- https://discord.gg/nFFqRbkRn6
- https://docs.audiosilo.app/developers
- https://docs.audiosilo.app/users/getting-started/quickstart-docker
- https://docs.audiosilo.app/users/getting-started/running-a-bridge
- https://fanart.tv/get-an-api-key/#casestudies
- https://github.com/KodeStar/audiosilo-old
- https://github.com/KodeStar/audiosilo-server
- https://github.com/linuxserver/Heimdall
- https://github.com/sponsors/KodeStar
- https://github.com/users/KodeStar/projects/1/
- https://meta.audiosilo.app
- https://meta.audiosilo.app/

## 导航

- 项目页：[[10-项目/fanart.tv_07b7ac57]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
