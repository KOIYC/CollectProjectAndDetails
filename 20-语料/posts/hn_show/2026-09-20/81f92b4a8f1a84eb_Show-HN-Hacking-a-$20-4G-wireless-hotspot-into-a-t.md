---
type: "corpus"
item_id: "81f92b4a8f1a84eb"
title: "Show HN: Hacking a $20 4G wireless hotspot into a texting device"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49712102"
project_url: "https://bkovac.github.io/modem-thing"
author: "bobili1234"
published_at: "2026-09-15T13:20:24Z"
captured_at: "2026-09-20T09:38:45+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_bobili1234
  - story_49712102
  - show_hn
metrics: {"points": 208, "comments": 37, "engagement_velocity": 208}
comments_count: 37
comments_total: 37
discovered_via: "hn:show_hn:90d"
---

# Show HN: Hacking a $20 4G wireless hotspot into a texting device

> [!info] 一句话导读
> Converting a $20 4G wireless hotspot into a texting device

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49712102>
> 指标：点赞=208 · 评论=37 · engagement_velocity=208
> 作者：bobili1234　|　发布：2026-09-15T13:20:24Z
> 项目链接：<https://bkovac.github.io/modem-thing>
> 采集：2026-09-20T09:38:45+08:00　|　id：`81f92b4a8f1a84eb`

## 正文

Converting a $20 4G wireless hotspot into a texting device

# Converting a $20 4G wireless hotspot into a texting device

Also known as: we have the Clicks Communicator at home.

The thing

## The motivation.

I don’t organize my things well. I try to, but quite often end up with a bunch of stuff on my desk. From various aliexpress orders and projects I’m working on, all the way to gifts and stuff I didn’t have time to find a place for.

That is exactly how this project came to be. At one point in time I had, lying on my desk:

- Various, hopefully openstick compatible, models - namely the:

- MF800 - one I ended up using
- UZ801 - OK size, but no battery or sufficienet visible GPIO
- USB drive form factor one I ditched because of other issues
- The Clicks Keyboard for iPhone 16 Pro Max (gift from my cousin - too bad I don’t have an appropriate iPhone 🥲)
- The Adafruit SHARP Memory Display board

And of course, my caveman brain combined the 3.

Okay, okay, not to lie I was probably a bit conditioned by knowing about:

- Beepy by sqfmi
- Playdate

## The modem.

Due to the mysterious laws of supply and demand, and the magic of supply chains - somehow you can get a 4G modem with WiFi, bluetooth, a display, fully battery powered and completely unlocked - for less than $20 shipped. This, of course, is the cornerstone of our project.

There are versions with and without a display. The non-display one just swaps the display for LED-s, though the PCB is the same. Display is a GC9107 powered one, but it looks like ass so i ditched it.

Linux can be installed trivially, powered by the wonderful openstick project. The stock device runs Android, but adb is accessible out of the box - and from adb you can go straight to edl and reflash the thing. Just make sure to save all the important partitions. There are also pins on the pcb which you can short out to get straight to edl.

Extracting the running device tree from the running android was a goldmine of information so be sure to do that.

Here are a few guides or links I found helpful:

- OpenStick github
- openstick.de
- wvthoog.nl blog - I think I used this kernel for starters
- extowerk.com blog
- This project’s GitHub repo might also help you

The real pain with openstick starts once you get to the drivers and device trees, but we will talk about that later.

## The keyboard.

There is not much to say about the Clicks Keyboard. It feels veeery nice to use, the only issue is you need to fork over quite a few clams - made worse because you are going to have to cut it 😱.

Regarding the protocol, it’s exactly what I expected with my previous experience of working with MFi devices - just a regular USB keyboard with an additional Apple proprietary endpoint which the iPhone can authorize with before allowing the keyboard to go through.

So for our device this means that it’s just a regular keyboard.

On a side note, there is a Clicks mobile app used for configuration/updates/whatever. The keyboard itself is powered by CH32V203 or similar. Custom code could be flashed but I don’t see any reason to to this currently. In the future I would like to have a configuration utility.

## The display.

I think the sharp display look great with the high contrast (and it plays well into my use case of a dumb device used only for messaging). Other than that, if there wasn’t much to say about the keyboard - then there is absolutely nothing more to say here.

It’s a display.

You send commands.

It displays.

## The adapter PCB.

One thing became clear to me quite fast - I was going to have to add a custom PCB. I wasn’t exactly sure what the MF800 had on-board, and I never did end up opening the shield can - but I am fairly certain there is no 5V booster on-board.

Because of the physical sizes, which we will go over further in the post, the USB connector will end up chopped off - so we need a way to handle that too.

The final PCB ended up handling the USB host mode power, USB host/device mode switching, display power and display signal level conversion.

PCB from the component side

I ordered the PCB along with assembly. And because 2 sided assembly is expensive, I made a few compromises to fit all the components on one side. The non-component side is used for the solder points for the PCB-to-PCB connections.

All files can be found on GitHub, but in short the PCB consists of:

- TUSB320 - for the USB mode switching
- SN74LVC8T245 - for the level shifting
- MCP1640 - the 5V booster
- TPS22917 (one high, one low) - for swithing VBUS/VBAT
- USB connector and FPC connector for the display
- test pads used to connect the adapter PCB to the MF800

## Enclosure 1.

The MF800 is quite a bit bigger than other opensticks, partly because of the battery it has to include, partly because of it’s slop nature.

MF800 without the back cover and with the (unnecessary) cut-out for the bootloader pins

So to fit inside a Clicks case, we either orient it verticaly and and up with a humongous abomination, or we trim the pcb to fit horizontally.

Top, with a the blue lines showing the USB data lines going from the connector and pads to the SOC

Bottom, red lines mark where I was planning to cut and the blue circle marks the via for USB data test pads

Notice that my right cut (on the bottom picture) cuts off the battery connection line, so this will have to be patched up later.

## Cutting.

Cutting the PCB went unexpectedly well. The device booted up immediately and everything seemed to work. Turns out there really were no crucial lines going through those areas of the PCB.

The cut PCB inside a test enclosure with the battery below and the patch VBAT wire

Only things I didn’t test were the USB connection and the 4G modem. The modem I was 99% sure wouldn’t be an issue as there is no reason to route anything for it under those areas - but regarding the USB I was worried that I hadn’t maybe nicked the via.

2D scan of the PCB, trimmed to the cut lines and extruded to match the measured thickness - a tight fit within the iPhone’s width

## Wiring 1.

I decided to reuse the pads from the old display. I don’t really know why anymore - possibly because my initial ideas was to use a rigid flex PCB and solder it similar to how the original display was. (which I decided against immediately upon seeing the prices)

Looking at all this now, it seems very dumb. I should have used the labeled pads next to the unpopulated micro SD connector. Note that never did check if these were shared with the SIM card though.

Since I could boot the device and I had the original android device trees, I extracted which pins were used for the display SPI. I then tested those with `gpioset` to make sure that I was indeed correct. Same goes for the power supplies (although I tested those by disabling them in the device tree and rebooting) and grounds.

Checking and mapping the pins with a multimeter

The first thing I wired and checked were the power supplies followed by the USB. This is because I could test this as an isolated unit. I was also more skeptical about this because it involved a bit of circuitry on my part as well as that iffy via.

Wiring the USB and the power supplies

Of course, it didn’t work initially. After probing around the pads and seeing that all the voltages were OK I noticed in my laptop’s `dmesg` that it TRIED to enumerate - meaning something was going on.

I also noticed that it says "high-speed". This caught me a bit off guard. I didn’t expect it to use "high-speed" USB. My first thought was that the wires were too long. But before shortening them, I tried a quick fix - twisting them more tightly - and it worked 😲!

Device’s USB Gadget enumerating

Immediately following this success, I tried to get the other direction working. This took some time. Turns out, not all aliexpress adapters correctly wire the CC lines. The keyboard did work immediately, though - only issue is I was afraid to test with it first in case something was wired incorrectly.

Events from the keyboard

## Wiring 2.

Before wiring the SPI lines to the display, I wanted to check if I had correctly reconfigured my device tree. I knew the pads were correct from the earlier testing, but there is quite a lot which can go wrong here.

```
spi@78b9000 {
    compatible = "qcom,spi-qup-v2.2.1";
    reg = <0x78b9000 0x500>;
    interrupts = <0x00 0x63 0x04>;
    clocks = <0x13 0x41 0x13 0x36>;
    clock-names = "core", "iface";
    dmas = <0x6d 0x0c 0x6d 0x0d>;
    dma-names = "tx", "rx";
    pinctrl-names = "default", "sleep";
    pinctrl-0 = <0x84>;
    pinctrl-1 = <0x85>;
    #address-cells = <0x01>;
    #size-cells = <0x00>;
    status = "okay";
    spidev@0 {
        //compatible = "linux,spidev"; 
        compatible = "rohm,dh2228fv";
        reg = <0>;
        spi-max-frequency = <16000000>;
        spi-cs-high;
    };
};
```

For example, qualcomm drivers are sketchy and the commented out compatible won’t actually export the `spidev`, so we scam it with this the dh2228fv compatibility.

Using the `spi-pipe` utility running in a loop, I was able to measure voltage change on the MOSI and CLK lines - which was enough for me to conclude that something was happening. I would, of course, prefer to do this with a scope or a logic analyzer - but I didn’t have any of those at hand.

Encouraged by the major success of power supplies and USB, I carelessly connected the display into the PCB (while the device was on 🤦).

Immediately something happened to the display and I was sure I broke it. Fortunately nothing came of this and the display was fine. (This actually happens every time I turn on the device. I don’t yet know if I should be concerned 😬.)

Once I reassured myself that nothing bad had happened, and that nothing was smoking or overheating - I proceeded with trying to get the display to work.

After an hour of slopping through this with AI python code I was absolutely nowhere. There were multiple possible points of failure. Level converter, bad routing, contacts, etc…

Turns out, as is quite common (IDK why), the qualcomm driver doesn’t handle the CS well (or correctly - or maybe it does but for other use cases). In any case, I tried again the same test script, but this time toggling the CS pin manually (via `libgpiod`) - and it actually worked.

Display showing a checkerboard test pattern

## Rewiring.

I was immediately dissapointed with the everything. From the "electrical" wire I used to connect the power supplies to the sketchy tiny magnet wire I used for the signals all the way to the twisted ground I wrapped around MOSI and CLK (which seemed to do nothing) - so I decided to rewire everything once more.

This time i used magnet wire for both signals and power, but this one was quite a bit thicker and also kept position once bent. I didn’t rewire the USB data lines though, as the pads on the main board look very iffy.

Much better, though still lacking solder mask/resin and tape

## Display kernel driver.

All the previous tests were done with just dumb python scripts, but the real way forward is with a kernel driver. There are quite a few drivers available, but the one I picked is ardangelo’s sharp-drm-driver. My reasons for wanting a `DRM` driver are as follows:

- allows me to use a direct output for eg. playing videos (like with `mpv`)

- this would work with a framebuffer as well, but that is sketchy in 2026
- i can run X/wayland on it easily

- maybe try and get into a desktop environment for the lols
- extend the driver to do partial updates
- still get the framebuffer interface

This worked almost immediately. I did have to playing around with CS and it’s active high default.

For probably the first time in my life I didn’t have any issues compiling the kernel module and running it. The mystery kernel I was running was a `6.12.1-msm8916` one with modules enabled. It had a `.config` file present which I took.

Next I downloaded the mainline linux `6.12.1` kernel and hoped that there weren’t any (or significant) changes. This ended up being enough, and after a few small patches to the driver the thing just worked.

Below is what the device tree ended up looking like. Notice that the CS logic being handled by the display driver.

```
spi@78b9000 {
    compatible = "qcom,spi-qup-v2.2.1";
    reg = <0x78b9000 0x500>;
    interrupts = <0x00 0x63 0x04>;
    clocks = <0x13 0x41 0x13 0x36>;
    clock-names = "core", "iface";
    dmas = <0x6d 0x0c 0x6d 0x0d>;
    dma-names = "tx", "rx";
    pinctrl-names = "default", "sleep";
    pinctrl-0 = <0x84>;
    pinctrl-1 = <0x85>;
    #address-cells = <0x01>;
    #size-cells = <0x00>;
    status = "okay";
    
    sharp_drm@0 {
        compatible = "sharp-drm";
        reg = <0>;
        spi-max-frequency = <4000000>;
        cs-gpios = <0x49 18 1>;
    };
};
```

Standard linux console login prompt showed up

Issue now is that the driver just rounds pixel color under some value to black, above that to white (or inverted, depends on parameters). For text (or if you do the visuals yourself in your app) this works great - but for a general purpose solution where you want to play videos or show images - this looks like ass. The fix for this is to add dithering to the driver.

A video looking bad with just color rounding

I added a custom sys value which allows the user to enable dithering, as well as to pick which algorithm they want:

- Atkinson for video
- Floyd-Steinberg for stills

All the initial functionality was left intact.

Big buck bunny looking great (played by stock MPV with DRM output)

You can find more information about this, or the DRM driver patches on the project’s GitHub repo.

## Enclosure 2.

With everything on my table and working, mainly meaning the dimensions are set and can be measured, I jumped into modeling the near-final case which I can hopefully put into the keyboard case without worrying about breaking anything.

This was kinda sketchy since apple doesn’t give dimensions of how far the USB-C connector is inside the iPhone - but I got around this by measuring apple standard USB-C cables (which fit snug up to the device) and interpolating from there.

Linux login, working out-of-the-box after setting USB to host

This print still wasn’t particullarly useful but served it’s purpose to confirm that the USB connector dimensions (among others) were measured correctly.

Also, 2 sidewalls didn’t print correctly and while modelling (this was before I receive’d one visible in the pictures) I didn’t have a display (except the one bonded to the devkit PCB) to model off of, so the cover is lacking.

Cover fits but no display slot, case still not trimmed

## Final enclosure (for now).

This is what ended up being the final enclosure. Mostly everything fit correctly. I first whipped up a quick test held together by kapton tape.

Final encloure, in the still-not-trimmed case held with kapton tape

This was the point at which, becuase of some ongoing life stuff, I temporarily lost access to a big chunk of my tools (mainly the 3D printer but also other stuff).

My hand being forced, I decided to hot glue the case together instead of printing a final final one which clips together.

I also forgot about the power button, which despite being on the PCB and working - didn’t get a case cutout and a plunger. This was solved with a small hole and a pin. Very ugly but it works.

Hot glued enclosure

Now the big boy moment - cutting down the keyboard case with no tools. It went about as well as you can expect. Though I made sure to cut less than needed so that I can sand it down and make it look pretty once I get my gear back.

It realistically doesn’t look that bad, but the edges could use some cleaning. The case hot glue protrusion is a bigger issue.

With the magic of top-down photos I have hidden most of this from you.

End result

I forgot to take photos while assembling this. It’s exactly the same as before plus a 4G flex PCB antenna which I soldered to the PCB and glued below the display on the top half of the enclosure. There is now also a mini SIM in it’s slot.

## Battery configuration.

The android device trees I copied from the device come predefined with the battery and charger configurations. These are also more advanced than the ones offered by the mainline linux i’m running.

Still, I expected it to be pretty easy to get something usable working. Big questions here were the battery information and power draw of my adapter PCB.

What the driver provided on the user level, however, was only the battery voltage in uV and a flag whether it’s charging or not. So the actual battery logic will be left up to my app as I’m not planning to mod the driver just for the battery percent value.

Charging seems to work fine. It also works via the keyboard USB passthrough port, but unfortunately only when the device is booted up.

## The missing.

Sleep currently stands as the biggest non-solved issue. Main reason is the lack of day-to-day testing of the device, especially with the modem turned on - and the lack of a convenient power button.

I’m planning to tackle this in the near future as I begin using the device for my messaging. I would like to get a fast bootup/shutdown going on at the very least.

Additional input methods, eg. a touch screen or a scroll wheel, would probably be the best additional feature. Touch, especially, can be done with very little space.

Those are followed closely by sound or vibration. Even a tiny speaker at like 8khz. There is sufficient PCB space for an amplifier as well as space for the speaker in the enclosure.

## The ugly.

Mainly the glue issue and the missing power button, both of which require a new print, plus the jagged edges on the keyboard case that need filing down.

The battery is held down by a bit of tape as it otherwise falls out when not in the case. Not a priority at the moment.

The big bottom bezel driving the enclosure height could also be shortened, but that would require sourcing a different battery with the same 3 pin connector among other things.

The helper PCB slides up inside it’s slot because the display FPC cable slightly pulls on it and I forgot to add tabs in the enclosure cover to keep it in place. Not ideal - but it’s only an issue when sliding the enclosure into the case.

Finally, a tiny portion of the display is covered by the case. Like 1-2 pixels on all edges. This will also be fixed with the next print.

All in all I’m very happy with the device, but a bit more work would do wonders for the visuals. In photos it looks fine - in real life it leaves a little to be desired.

If you are interested in replicating this or doing something similar, you can find most of the stuff on the project’s GitHub repo.

## Future.

I have deliberately omitted software from this post since that will only get ironed out with use, and I’m not a big fan of releasing projects I haven’t finished but didn’t drop.

Quick preview of the software

As of writing this I already found a memory leak in the original display driver. I also shipped a patch which fixes it. Stuff like this can’t easily be found without actual hands-on testing.

 The text was fully written by me, a human. You can contact me at veggie_privacy_8y at icloud dot com

## 评论（37/37）

> **xx_ns** · 2026-09-15T13:53:35.000Z　
> This is a really cool project! A mini cyberdeck that doesn't seem too impractical to use. Repurposing the Clicks keyboard is a genius idea.

---

> **dgf18** · 2026-09-15T14:13:32.000Z　
> Really cool!

---

> **harhargange** · 2026-09-15T14:54:05.000Z　
> I often ditch my phone and carry my hotspot device for my internet. The only drawback is that for viewing my texts and OTPs i end up putting the sim in my phone or opening up the web interface on my laptop. This seems to work very well as a dumbphone per se.

---

> **notpushkin** · 2026-09-15T15:41:11.000Z　
> This is really nice! It so happens that I’ve just bought a $10 4G dongle [1], guess I’ll have to check what’s inside now :-)[1]: like this: https://img.joomcdn.net/ea91b4418997d83d802339fad0bbcf878b9d...---Aside, but it appears some MSM8916-based dongles run Android UI despite having no display: https://github.com/u0d7i/uz801#screenshots

---

> **walrus01** · 2026-09-15T15:48:12.000Z　
> Based on the work the person has done, if they wanted to make something with an exceedingly long battery life, and the battery setup there already seems to be basically a 1S li ion, they could graft in a back side battery holder for two high quality 18650 cells in parallel. It would probably last weeks.

---

> **VinnyBarreca** · 2026-09-15T17:10:49.000Z　
> It would be pretty cool to put Hermes Agent or some agent system on that thing, assuming the OpenStick build has enough RAM/storage. That would be fire.

---

> **msm8916** · 2026-09-15T17:27:02.000Z　
> OpenStick is super old though, there are Linux and OpenWRT builders that track the upstream kernel, check hkfuertes and others.

---

> **catidegla** · 2026-09-15T19:10:03.000Z　
> One layer down from where this thread is looking: the SMS never lives in the Android userspace on these sticks. It sits in the modem's own store, either on the SIM or in modem memory, and the vendor web UI is just a thin thing reading it out of there.So you don't need a messaging app that still runs on Android 4.x. If the device exposes an AT port, AT+CMGF=1 then AT+CMGL="ALL" dumps everything, and AT+CPMS picks which store you're reading. On the Qualcomm ones that keep the AT port hidden behind QMI, libqmi reaches the same thing through the WMS service.

---

> **DingleDodies** · 2026-09-15T22:34:08.000Z　
> This is cool and all, but what is the point? I have a feeling it could be useful for me but what is it really for?

---

> **koinedad** · 2026-09-16T15:51:33.000Z　
> I love this

---

> **dividedcomet** · 2026-09-19T02:31:54.000Z　
> This is the coolest dang project

---

> **newhotelowner** · 2026-09-15T15:02:29.000Z　
> How do you check sms/OTP/text using web interface on your laptop?

---

> **blobbers** · 2026-09-15T16:35:15.000Z　
> If you move to an Apple set up, the phone can act as a hotspot and there is no need to take out your sim. Also... you have a physical sim card? I thought those became obsolete.

---

> **kotaKat** · 2026-09-15T19:56:03.000Z　
> I did some funny software porting on one of those dongles. At one point, I had it connected to a battery pack for power, joined onto my home WiFi for LAN/WAN access... and had the stick running the Open5GS cellular core stack, allowing my CBRS LTE base station to serve users on an in-home private LTE network by connecting to the cellstick over WiFi for management. (No, the stick's own cellular modem wasn't being used here at all. Just scavenged compute for the tiniest LTE core!)So... so cursed.

---

> **untitaker_** · 2026-09-16T00:45:25.000Z　
> it's most likely UZ801 (mentioned in the article)

---

> **djfergus** · 2026-09-16T11:54:55.000Z　
> Postmarketos works well on those and they have lots of info and links. [1]My biggest tip is to carefully back up every partition of the original firmware - there are many many seemingly identical variants and if you hose your particular baseband components you will lose your cellular functionality.[1] https://wiki.postmarketos.org/wiki/Zhihe_series_LTE_dongles_...

---

> **iamnothere** · 2026-09-15T16:25:23.000Z　
> A 10000mAh pouch battery would take up less room and provide more battery life. They are almost as cheap as 18650s too.

---

> **ACCount39** · 2026-09-15T17:22:52.000Z　
> What it has at its core is a smartphone chipset from 2014 - MSM8916 or so. Not exactly an AI compute powerhouse.

---

> **RIMR** · 2026-09-15T18:23:46.000Z　
> Truly, I couldn't imagine a worse platform to put a coding agent on. What even would be the point?It's got less than 512GB of RAM, no package manager, and virtually no storage.

---

> **ACCount39** · 2026-09-15T17:35:35.000Z　
> Oh, if it isn't the MSM8916 himself! Fancy seeing you out there in the wild - posting on HN no less!Is there a guide for cheap MSM8916 platforms you would recommend? There is a hkfuertes repo, but the one I found is archived. Not to say it doesn't work, but that doesn't instill much confidence.

---

> **notpushkin** · 2026-09-15T15:22:43.000Z　
> This probably depends on your particular dongle model. Back in 3G era, some carriers offered USB modems with SMS locked out in the firmware, but you could flash a firmware from a different operator (also install their variant of software, the only difference being the added SMS tab and a different skin) and then you can text and even use USSD! (No calls, though.)

---

> **knowaveragejoe** · 2026-09-15T15:35:40.000Z　
> https://messages.google.com/web/ is one way I'm aware of, I'm sure there's others depending on the messages app used.

---

> **harhargange** · 2026-09-15T22:17:37.000Z　
> yeah my vendor's dongle has this specific feature. A light also turns ON on the modem when SMS is received.

---

> **toast0** · 2026-09-15T19:47:42.000Z　
> Physical sims are as obsolete as 3.5mm headphones. They both continue to work and have different tradeoffs than 'modern' alternatives and you have a different selection of devices to work with.

---

> **notpushkin** · 2026-09-16T14:19:59.000Z　
> It’s a weird one! [ro.build.description]: [msm8916_32_512-userdebug 4.4.4 KTU84P eng.huanghonghuan.20250226 test-keys]
>  [ro.build.sw.custom.version]: [UFI003S_V03_ZX_DD_250226]

---

> **jsisto** · 2026-09-15T16:29:41.000Z　
> How is a 10000mAh pouch more energy dense than an 18650?

---

> **walrus01** · 2026-09-15T17:33:05.000Z　
> The neat thing about 18650s though is that you can put a battery door on it and make them swappable, if a person used a holder that can accommodate button top protected 18650 cells. The same cells can also be shared by a bunch of good quality flashlights and headlamps. I have several extremely useful headlamps from "sofirn" that take my choice of cell and have a built in USB-C charging port and charge circuitry protected behing a gasket and twist-open ip67 sealed cap. The pouch battery would be better as an integrated all in one product but also makes the thing a bit less modular.

---

> **warkdarrior** · 2026-09-16T03:47:24.000Z　
> Hermes is not a coding agent.

---

> **Matsta** · 2026-09-15T21:14:58.000Z　
> Not tried but seems like a fairly recent Arabian build (last release was June) https://github.com/Crychic-Band/msm8916-armbian

---

> **notpushkin** · 2026-09-15T15:45:36.000Z　
> It seems those modems run Android 4.x with the stock messaging app: https://github.com/u0d7i/uz801#screenshotsBut I guess you can install a custom messaging app that would sync the messages? (If there’s one that still supports such an old version of Android)

---

> **EvanAnderson** · 2026-09-15T20:39:15.000Z　
> Thanks for coming up with a very apt analogy. I wanted to reply but couldn't come up with something I felt good about.

---

> **bri3d** · 2026-09-15T16:37:03.000Z　
> By not having void air space in between cylindrical cells like you'd get with two 18650s? It's mostly just a matter of packaging.Pouches can be made to have better volumetric density than cylindrical cells quite easily, which is why laptops aren't generally full of cylinder cells anymore; the challenge is just providing them enough external support/compression and swelling allowance, which can be accomplished through chassis design.

---

> **iamnothere** · 2026-09-15T16:37:47.000Z　
> Pouch cells are lighter per mAh due to the lack of metal casing. But more than the casing, the form factor is better for a pocketable device. The cylindrical form factor sticks out, usually wastes some space, and can’t be neatly tucked behind a board or display.

---

> **iamnothere** · 2026-09-15T17:36:33.000Z　
> There are advantages in some applications, it’s just not a one size fits all tool. Slim devices aren’t really a good fit for them. They make sense in round devices (like a flashlight) or larger devices where space isn’t as much of a concern.

---

> **DANmode** · 2026-09-15T18:33:07.000Z　
> Thank you to both solder-nerds for contributing strongly to the thread, please don’t fight.

---

> **walrus01** · 2026-09-15T18:37:18.000Z　
> No fighting intended, I think it's interesting to see that there's many ways of doings things, and doing a sort of mental whiteboard exercise on what the benefits and drawbacks of different things are... Like, using cylindrical cells would let me share cells with my head lamp, swap cells, independently charge cells and keep spare charged cells ready.While using a pouch cell keeps the profile much more slim, portable, still has opportunities for really high capacity in watt hours, and allows for a more robust case design that doesn't have the structural weakness of a battery door.And if you put the pouch cell on a set of wires with a small pluggable connector to the main PCB (and a case that can screw open/shut) it's still an item the user can replace with 5 minutes and a screwdriver if it wears out from many cycles over a period of years.

---

> **iamnothere** · 2026-09-15T19:34:32.000Z　
> > And if you put the pouch cell on a set of wires with a small pluggable connector to the main PCB (and a case that can screw open/shut) it's still an item the user can replace with 5 minutes and a screwdriver if it wears out from many cycles over a period of years.True, and you could even enclose it in a quick swap hard shell case with contacts, like the old Nokia cell phone batteries. (Those are actually still good for some uses, I have a gadget that uses them.)We’re fortunate to live in an era of battery abundance.

## 导航

- 项目页：[[10-项目/bkovac.github.io_fee1ad50]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
