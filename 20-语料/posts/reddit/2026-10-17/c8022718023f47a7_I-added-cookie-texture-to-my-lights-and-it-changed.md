---
type: "corpus"
item_id: "c8022718023f47a7"
title: "I added cookie texture to my lights and it changed the whole scenery"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/IndieDev/comments/1wzoagq/i_added_cookie_texture_to_my_lights_and_it/"
author: "BeastGamesDev"
published_at: "2026-10-07T13:22:02+08:00"
captured_at: "2026-10-17T13:37:06+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-10-17"
pub_day: "2026-10-07"
tags:
  - 语料
  - reddit
  - r/indiedev
  - Upcoming!
metrics: {"score": 4048, "comments": 119, "upvote_ratio": 0.9940431868950111}
comments_count: 119
comments_total: 119
discovered_via: "reddit:14d+settle10"
---

# I added cookie texture to my lights and it changed the whole scenery

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/IndieDev/comments/1wzoagq/i_added_cookie_texture_to_my_lights_and_it/>
> 指标：得分=4048 · 评论=119 · 赞踩比=0.9940431868950111
> 作者：BeastGamesDev　|　发布：2026-10-07T13:22:02+08:00
> 项目链接：—
> 采集：2026-10-17T13:37:06+08:00　|　id：`c8022718023f47a7`

## 评论（119/119）

> **BeastGamesDev**（2 分） · 2026-10-07T13:23:05+08:00　
> If you want to check the full game and wishlist here is a Steam page - [https://store.steampowered.com/app/5249980/Looks\_Like\_You/](https://store.steampowered.com/app/5249980/Looks_Like_You/)

---

> **No-Gain-6206**（198 分） · 2026-10-07T13:35:15+08:00　
> Cookie... texture?

---

> **TheRuneless**（494 分） · 2026-10-07T13:37:30+08:00　
> It makes such a big difference!! These little things are often overlooked but add such depth. Also for optimisation sake, its nice to have that option instead of casting true shadows :D

---

> **BeastGamesDev**（39 分） · 2026-10-07T13:40:08+08:00　
> That's the term 😂
>
> Basically what it does is it lets the light to have a "body". You can think of it like it has already baked shadows inside the light component

---

> **BeastGamesDev**（9 分） · 2026-10-07T13:40:39+08:00　
> That's a fact. Small details make the best games

---

> **mitchricker**（210 分） · 2026-10-07T13:45:59+08:00　
> > Cookie... texture?
>
> So called because the technical term (cucoloris) is difficult to pronounce.

---

> **Chudfrog**（76 分） · 2026-10-07T13:46:36+08:00　
> What's the difference between this and 'true shadows'? Is this some lower resource technique?

---

> **BeastGamesDev**（162 分） · 2026-10-07T13:49:38+08:00　
> Basically this is not a shadow per se. Cookie texture is a white - black image that tells a light where it should lit the objects. White stand for light, while black is a "shadow".
> Shadow in here is not casted, which makes additional draw calls. Instead in the dark spot there is simply no light

---

> **Chudfrog**（27 分） · 2026-10-07T13:51:11+08:00　
> Interesting. Thanks for the info :)

---

> **BeastGamesDev**（10 分） · 2026-10-07T13:54:50+08:00　
> No problem :) Hope you understood it well

---

> **BeastGamesDev**（45 分） · 2026-10-07T13:55:25+08:00　
> That's an interesting one, didn't know that

---

> **sharypower**（13 分） · 2026-10-07T14:00:41+08:00　
> Make a window little but brighter as well

---

> **BeastGamesDev**（3 分） · 2026-10-07T14:01:51+08:00　
> Yeah I'll do it :)

---

> **Entire_Shoe_1411**（3 分） · 2026-10-07T14:23:05+08:00　
> It depends how transparent the window is though. If it's very clear then do not increase the brightness

---

> **BeastGamesDev**（3 分） · 2026-10-07T14:24:48+08:00　
> Theyre 100% opaque. You don't see through them

---

> **Morpheyz**（24 分） · 2026-10-07T14:54:16+08:00　
> Looks great! In the left scene it doesn't really look like the light is coming from the window at all. Although I have to agree that it seems that the light is a bit too bright.

---

> **BeastGamesDev**（4 分） · 2026-10-07T14:58:45+08:00　
> I agree that left side doesn't look correct at all, that's why such details matters in game dev :)

---

> **Mechanikalbaby**（32 分） · 2026-10-07T15:00:20+08:00　
> Generally called gobos in the industry. But, funny enough, I have never heard it called this.  Cheers

---

> **isolatedLemon**（83 分） · 2026-10-07T15:23:34+08:00　
> I thought it was because it is like a cookie cutter for lights lol

---

> **tiny_battles**（4 分） · 2026-10-07T15:36:35+08:00　
> wow you diid amazing job

---

> **artbytucho**（2 分） · 2026-10-07T15:38:30+08:00　
> The perfect use for the cookie texture.

---

> **BeastGamesDev**（4 分） · 2026-10-07T15:39:54+08:00　
> ![gif](giphy|T9JtEyoJ43gY4wLOqW)

---

> **kr4ft3r**（1 分） · 2026-10-07T15:45:34+08:00　
> I suspected this works on static objects only so I looked this up in Unity docs - "If there are no dynamic objects that can enter the area with a light cookie shadow, a user is unlikely to notice a difference between the cookie and a real-time shadow". Seems like my suspicion was correct? If yes then this greatly limits the usability.

---

> **Unaveragejoe777**（4 分） · 2026-10-07T15:50:32+08:00　
> A huge improvement. Lighting makes such a difference

---

> **TizianoDAnzi**（2 分） · 2026-10-07T15:50:45+08:00　
> Is it called cookie because changes the shape of the shadow like a cookie cutter? I always wondered

---

> **BeastGamesDev**（2 分） · 2026-10-07T16:08:34+08:00　
> It works on dynamic objects aswell

---

> **BeastGamesDev**（1 分） · 2026-10-07T16:10:16+08:00　
> You can see this effect on my capsule art on steam - I didnt bake lights for it and characters here are shot under the same light I showed in this post

---

> **ImSamhel**（1 分） · 2026-10-07T16:14:53+08:00　
> I'm not very familiar with graphics things, so this looks impressive! Does anyone know anything about how does it affect performance?

---

> **kr4ft3r**（1 分） · 2026-10-07T16:21:43+08:00　
> Thanks for answer, now I wonder what they meant by that in docs.

---

> **Aligyon**（2 分） · 2026-10-07T16:25:31+08:00　
> Is this like light functions in unreal? I'm learning lighting for my studio. All these things are super interesting

---

> **BeastGamesDev**（1 分） · 2026-10-07T16:27:00+08:00　
> Unity docs are outdated in many areas, it may be the case. Or either you were reading about other rendering pipeline. Im using HDRP

---

> **BeastGamesDev**（2 分） · 2026-10-07T16:29:28+08:00　
> Its a really cheap effect in terms of performance

---

> **vshk04**（3 分） · 2026-10-07T16:34:07+08:00　
> can you explain to me what it is like im a dumass? cuz that looks amazing but idk what cookie textures even are

---

> **BeastGamesDev**（13 分） · 2026-10-07T16:53:18+08:00　
> It's a white-black texture you apply into your light component.
>
> Basically what it does is it projects this texture on the whole light making it bright on white parts of the texture and non-lit on the dark parts.
>
> An example in real life - when a bug sits on the lamp, it applies a shadow on the ground which lamp lits. This bug is the dark spot in the cookie texture :)
>
> See here - [https://docs.unity3d.com/6000.1/Documentation/Manual/Cookies-introduction.html](https://docs.unity3d.com/6000.1/Documentation/Manual/Cookies-introduction.html)

---

> **unlessgames**（3 分） · 2026-10-07T17:09:58+08:00　
> It's a play on the word "cucoloris".
>
> https://en.wikipedia.org/wiki/Cucoloris

---

> **That_Classroom_2182**（1 分） · 2026-10-07T17:28:03+08:00　
> Sieht gut aus

---

> **LowTide_Jip**（2 分） · 2026-10-07T18:08:37+08:00　
> feels like the light is coming through the window now

---

> **Eatmeatgames**（2 分） · 2026-10-07T18:17:19+08:00　
> Looks amazing

---

> **TizianoDAnzi**（1 分） · 2026-10-07T18:28:02+08:00　
> Today I learnt!

---

> **luisduck**（4 分） · 2026-10-07T18:38:28+08:00　
> Can I think of it as cached shadow mapping?

---

> **Dadabeam**（1 分） · 2026-10-07T19:06:53+08:00　
> เป็นการปรับที่ได้ผลลัพธ์ออกมาดีเยี่ยมเลย สวยครับ

---

> **Painterly_Vertex**（6 分） · 2026-10-07T19:16:33+08:00　
> Cookies are super good. You can put a scrolling cloud shadow cookie on your main directional light and change the whole look of a basic outdoor scene, or get nice shifting shadows in a forest, and cookies can be used in procedural games too that might not be able to handle fancy or baked lighting to really improve how light sources look.

---

> **trade_ida5458**（2 分） · 2026-10-07T19:19:13+08:00　
> WOW
>
> ![gif](giphy|5aLrlDiJPMPFS)

---

> **vshk04**（4 分） · 2026-10-07T19:47:42+08:00　
> thanks man

---

> **JayQix**（1 分） · 2026-10-07T20:13:53+08:00　
> It adds dimension to the scene. The only issue now is it's too bright compared to the light source- the windows.

---

> **Black_Cheeze**（1 分） · 2026-10-07T20:17:10+08:00　
> It really does change the whole scene. The shadows make it feel so much more alive.

---

> **TimberHaint**（0 分） · 2026-10-07T20:21:14+08:00　
> Very nice!

---

> **TheLastNeonDev**（1 分） · 2026-10-07T20:48:21+08:00　
> nice!

---

> **iLikeTheUDK**（1 分） · 2026-10-07T20:57:23+08:00　
> What is this game?! The art style is very Rayman 2

---

> **WAWE_Games**（1 分） · 2026-10-07T21:21:57+08:00　
> wild how much mood you get out of basically a black and white image lol

---

> **cdmpants**（14 分） · 2026-10-07T21:28:15+08:00　
> A shadow map stores depth like a z buffer and has a more complex rendering technique, whereas a light cookie is more like if you stuck a cardboard cutout in front of your light to project shadow puppets onto the wall.

---

> **livingonthehedge**（1 分） · 2026-10-07T21:31:55+08:00　
> I think they're trying to say it's "fake" baked lighting.  So if nothing in the scene moves, it will be impossible to know that it was faked.
>
> But if there is a dynamic object (that can move) then eventually the trick could be spotted, and seen through as fake.
>
> In short they are establishing that the cookie is baked to look the same as real baked lighting, but it lacks the real-time mechanism to adapt to moving objects.
>
> So cookie lighting is "simplified" baked lighting.

---

> **crai-crai**（1 分） · 2026-10-07T22:12:18+08:00　
> oooooo this looks sick!! gonna save this for later to do a similar technique for my future games, eheh

---

> **RafaSC00**（2 分） · 2026-10-07T22:35:56+08:00　
> much much better, congrats!!

---

> **BeastGamesDev**（1 分） · 2026-10-07T23:46:03+08:00　
> Looks Like You, here is Steam page - [https://store.steampowered.com/app/5249980/Looks\_Like\_You/](https://store.steampowered.com/app/5249980/Looks_Like_You/)

---

> **ShunkashutoStudio**（1 分） · 2026-10-07T23:46:13+08:00　
> Yeah, shadows really make a huge difference.

---

> **BeastGamesDev**（1 分） · 2026-10-07T23:46:28+08:00　
> Yeah, that is wild :)

---

> **BeastGamesDev**（1 分） · 2026-10-07T23:46:50+08:00　
> If you want to support me, I would appreaciate any wishlist on the game! <3
> [https://store.steampowered.com/app/5249980/Looks\_Like\_You/](https://store.steampowered.com/app/5249980/Looks_Like_You/)

---

> **Thisismyredusername**（1 分） · 2026-10-07T23:47:36+08:00　
> It looks like it's being ray traced

---

> **BeastGamesDev**（1 分） · 2026-10-07T23:48:05+08:00　
> Yeah, once you're familiar with them, there are endless possibilities

---

> **Baalzeg**（1 分） · 2026-10-08T00:29:47+08:00　
> Para un ambiente de camara fija, esto es estupendo! Pero, si hay movimiento 3d de camara, y tú personaje puede pasar por encima, asegúrate de que luzca bien. A veces son ideas que, en concepto, funcionan, pero a la hora del gameplay no.

---

> **KaleidoscopeNo3639**（1 分） · 2026-10-08T00:45:48+08:00　
> I like what it looks like on the floor, but when looking right at the window it does not look like there is that much light coming through.

---

> **StrawberryPlagueDoc**（1 分） · 2026-10-08T00:55:27+08:00　
> The change is ethereal!

---

> **iLikeTheUDK**（1 分） · 2026-10-08T00:55:32+08:00　
> Need anyone else on your dev team? I can do some graphics (mostly 2D but also 3D), shaders, sound design and music

---

> **Boosted_Gear0**（1 分） · 2026-10-08T01:26:23+08:00　
> Is this same as.. baked lighting? shadow maps? Light maps?

---

> **SufficientWriter3483**（17 分） · 2026-10-08T01:43:02+08:00　
> game?
>
> ![gif](giphy|hqTguNdEoA1ooYxeog)

---

> **BeastGamesDev**（2 分） · 2026-10-08T01:53:21+08:00　
> Im a solo dev, thanks :)

---

> **BeastGamesDev**（4 分） · 2026-10-08T01:54:44+08:00　
> Looks Like You - [https://store.steampowered.com/app/5249980/Looks\_Like\_You/](https://store.steampowered.com/app/5249980/Looks_Like_You/)

---

> **larevacholerie**（8 分） · 2026-10-08T03:00:35+08:00　
> I thought that was called gobo? I've always called them gobo lights

---

> **eraistudio**（1 分） · 2026-10-08T03:17:48+08:00　
> crazy how much one texture does. is that realtime or baked?

---

> **FireDog8569**（3 分） · 2026-10-08T03:25:01+08:00　
> Is cookie texture like... Baked lighting orrrr?

---

> **Beautiful_Math6991**（0 分） · 2026-10-08T03:59:19+08:00　
> Nice trick !!

---

> **BeastGamesDev**（2 分） · 2026-10-08T04:52:51+08:00　
> No, its just a mask for a light to tell the light where it should not lit the objects

---

> **BeastGamesDev**（1 分） · 2026-10-08T04:53:22+08:00　
> The one on screen is realtime, but it also works baked

---

> **Tanjiroko**（3 分） · 2026-10-08T05:19:04+08:00　
> The Details make the game

---

> **TheUFCVeteran3**（3 分） · 2026-10-08T08:59:28+08:00　
> Wow, I would have never realised that but it shows how much it changes the scene (and for the better, imo).

---

> **swanbedbug**（2 分） · 2026-10-08T09:33:36+08:00　
> Oh so it's like Gobo lights

---

> **laserofdooom**（2 分） · 2026-10-08T09:43:00+08:00　
> woah looks really cool. def looking forward to playing it

---

> **_TERRANE_**（3 分） · 2026-10-08T09:44:07+08:00　
> That's what they're called in theater. It's a 'stencil' type plate that you slide on the front of the light.

---

> **BeastGamesDev**（1 分） · 2026-10-08T10:12:51+08:00　
> Happy to hear that!

---

> **Meotwister**（2 分） · 2026-10-08T11:34:07+08:00　
> I think we used to call the colored sheets on lights gobos? Who knows though

---

> **Sekret_One**（2 分） · 2026-10-08T13:20:46+08:00　
> . . .
>
> Oh because the shadows are "baked" in and not cast. I get it

---

> **Quest_Craft**（2 分） · 2026-10-08T14:44:47+08:00　
> Huuuge diffrence!! Good job.

---

> **HeroOfCorn**（2 分） · 2026-10-08T15:07:44+08:00　
> From "ooo i can silksoar" to peak

---

> **Memerenok**（1 分） · 2026-10-08T15:47:47+08:00　
> anyways, do you use baked lighting?

---

> **greyhoodie18**（1 分） · 2026-10-08T18:43:20+08:00　
> eyy that's a really good upgrade, looks amazing

---

> **zerofruit**（1 分） · 2026-10-08T19:42:55+08:00　
> If this game 1st/3st person game, it would make great difference in the mood of the game

---

> **theBarnDawg**（1 分） · 2026-10-08T20:11:52+08:00　
> While this method is putting a light map on the floor surface?

---

> **TheThiefMaster**（1 分） · 2026-10-08T22:26:38+08:00　
> Yes you wouldn't get shadows from any extra objects unless you also had a shadow map.

---

> **eraistudio**（1 分） · 2026-10-08T23:21:07+08:00　
> nice, thanks. gonna try it, curious how it holds up on mobile

---

> **bartolomey-wong-3rd**（1 分） · 2026-10-09T04:28:14+08:00　
> Very nice examples, I would love to try that with the cloud passing over some scenery.

---

> **Dear-Neck5299**（1 分） · 2026-10-09T07:33:29+08:00　
> The atmosphere has become much more realistic; the lighting design is something worth learning from.

---

> **MSX321**（1 分） · 2026-10-09T23:49:10+08:00　
> Indeed, it's very useful, I've also used it recently in a game

---

> **EricMakesOffcut**（1 分） · 2026-10-11T02:31:51+08:00　
> How does that work? It looks amazing. Is this just directional light?

---

> **haikusbot**（1 分） · 2026-10-11T02:32:03+08:00　
> *How does that work? It*
>
> *Looks amazing. Is this just*
>
> *Directional light?*
>
> \- EricMakesOffcut
>
> ---
>
> ^(I detect haikus. And sometimes, successfully.) ^[Learn&#32;more&#32;about&#32;me.](https://www.reddit.com/r/haikusbot/)
>
> ^(Opt out of replies: "haikusbot opt out" | Delete my comment: "haikusbot delete")

---

> **Far-Manufacturer-482**（1 分） · 2026-10-11T08:55:19+08:00　
> I really like the result; it looks very good.

---

> **FreakyChest**（1 分） · 2026-10-11T09:41:13+08:00　
> Odd that it really does seem to make the scene more dense. Never knew a shadow could do that. That is awsome!

---

> **_Salandit**（1 分） · 2026-10-11T23:47:00+08:00　
> W Haiku

---

> **xmi2025**（1 分） · 2026-10-12T10:43:50+08:00　
> This makes the window feel so much more realistic, awesome work!

---

> **GoodPlayful9051**（1 分） · 2026-10-12T12:54:20+08:00　
> I love this what a great idea, how performant is it?

---

> **Zoryth**（1 分） · 2026-10-12T22:26:05+08:00　
> Small lighting decisions can have a greater visual impact than considerably more expensive geometry.
>
> Especially in horror, the irregular distribution of light is part of what makes an environment convincing. It's often the shadows that establish the atmosphere.

---

> **IndieDev-ModTeam**（1 分） · 2026-10-12T22:56:13+08:00　
> This does not happen often on r/indiedev, but so many community members reported your submission as spam, that it had to be removed. This is a warning. Please do not spam the subreddit with AI generated responses

---

> **OkRange6240**（1 分） · 2026-10-13T02:35:15+08:00　
> Thats Amazing i learned a new thing today..

---

> **asiyeap**（1 分） · 2026-10-13T02:46:33+08:00　
> did you make the cookie texture yourself? im always surprised how much a small lighting change can do for a scene

---

> **okymi_**（1 分） · 2026-10-13T06:57:20+08:00　
> Stylé

---

> **youreitgames**（1 分） · 2026-10-13T08:16:36+08:00　
> Woah never heard of cookie texture before, it looks great!

---

> **BourbonEmpireTheGame**（1 分） · 2026-10-13T10:52:27+08:00　
> A cookie makes everything better.

---

> **Bubba201012**（1 分） · 2026-10-13T10:59:41+08:00　
> This actually looks rlly cool

---

> **CiroGarcia**（1 分） · 2026-10-13T15:03:47+08:00　
> Is there an advantage for this over baked lighting? As I understand this you have shadow textures like any other asset, that would require manual modifications if the related assets are modified

---

> **fahrettinshouse**（1 分） · 2026-10-13T17:31:57+08:00　
> Huge difference! Light cookies really do wonders for ambient depth and mood. The window shadow pattern looks so much more grounded and atmospheric!

---

> **jigglypoppp**（1 分） · 2026-10-14T00:53:27+08:00　
> good

---

> **Rfytann**（1 分） · 2026-10-14T03:48:27+08:00　
> Grosse différence

---

> **flutterboilerplate**（1 分） · 2026-10-14T06:26:42+08:00　
> Wow

---

> **EastFortune4931**（1 分） · 2026-10-14T09:53:28+08:00　
> Very nice!

---

> **KoiOasis**（1 分） · 2026-10-14T11:27:30+08:00　
> That's a huge difference, nice work.

---

> **Alone_FFH**（1 分） · 2026-10-14T15:46:35+08:00　
> Ooo, very cool! I’ll take note of it.

---

> **brokengnome**（1 分） · 2026-10-14T21:48:33+08:00　
> That's really cool! Very nice!

---

> **SaltElection3521**（1 分） · 2026-10-16T06:37:40+08:00　
> Such a big difference ! Looking good

---

> **AfterThisGames**（1 分） · 2026-10-17T11:58:12+08:00　
> Looks awesome

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
