---
type: "corpus"
item_id: "407882b92264cfb4"
title: "I don't like passkeys"
source: "lobsters"
source_name: "Lobsters"
url: "https://lobste.rs/s/4a7qly/i_don_t_like_passkeys"
project_url: "https://hawksley.dev/blog/i-dont-like-passkeys"
published_at: "2026-09-18T07:52:18.949-05:00"
captured_at: "2026-09-20T03:19:19+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - lobsters
  - security
metrics: {"score": 68, "comments": 46}
comments_count: 47
comments_total: 47
discovered_via: "lobsters:hottest"
archived: true
archived_at: "2026-09-20T09:21:33+08:00"
archive_reason: "渠道停用"
---

# I don't like passkeys

- **来源**：Lobsters　|　**kind**：post
- **原帖**：https://lobste.rs/s/4a7qly/i_don_t_like_passkeys
- **指标**：得分=68 · 评论=46
- **作者**：—　|　**发布**：2026-09-18T07:52:18.949-05:00
- **项目链接**：https://hawksley.dev/blog/i-dont-like-passkeys
- **采集**：2026-09-20T03:19:19+08:00　|　**id**：`407882b92264cfb4`

## 正文

Published: 2026-09-18
Author: Ethan Hawksley

I don't like passkeys | Ethan Hawksley

# I don't like passkeys

By Ethan Hawksley

- 18th September 2026
- 4 min read

For the past few years, the tech industry has kept pushing passkeys as the ultimate solution to logging in. Many Big Tech companies “helpfully” inform you every time you sign in how much easier and effortless passkeys are. The only way to make them stop is either to concede and set up a passkey or dig into the settings to find the off-switch.

Google goes as far as to name the setting “Skip password when possible” (opens in a new tab), and Microsoft advertises that you should make your account passwordless (opens in a new tab).

Passkeys are a fantastic technology. Since they are bound to the site they are created for, they cannot be phished by a hacker’s fake login screen. If a site suffers a data breach, passkeys are asymmetric and cannot be recovered from the server-side details.

This leads to passkeys being the perfect fit for a corporate environment, but a poor fit for personal security. To an individual, the greatest risks are instead permanent account lockout, automated account bans, and device loss. By using passkeys, you gain better security against man-in-the-middle attacks but face the higher probability scenario of losing access to your accounts.

Phishing through the standard login flow is eliminated by passkeys, but it creates a false sense of security. An account’s security is still dictated by the weakest recovery method: SMS, email links, security questions, and so on. If these recovery methods aren’t enabled, then the risk of permanent lockout remains for the user.

## Hardware keys

By design, you cannot create a backup of passkeys on a hardware key: passkeys can only be added or deleted but never moved. Instead, you need to purchase 2-3 hardware keys and enroll every key for every site. This can quickly get expensive and doesn’t scale well as the number of accounts starts to grow.

Hardware keys support discoverable credentials, where websites can query for your username instead of you typing it in. These are becoming increasingly popular amongst website developers, yet have limits of 25-100 accounts (opens in a new tab) per hardware key, and top of the line keys can have up to 300. Once you exceed the limit, you must either delete some accounts or you have to buy another set of hardware keys.

## Synced passkeys

Both Apple and Google want your identity anchored to their operating systems. The “happy path” on their devices is to use their synced passkey management tied to your Apple or Google account. If their automated systems decide one day to ban your account (opens in a new tab), you irreversibly lose access to all your passkeys used across all third-party accounts too.

The FIDO alliance has been working to improve interoperability and make it easier to export passkeys, but the experience is still fragmented and inconsistent across providers. This is set to improve over the coming years, but currently it is too immature to rely on. Compare with a password, which is just a string you can easily export by hand if necessary.

## Third-party synced passkeys

When storing passkeys in a password manager like Bitwarden (opens in a new tab) or KeePassXC (opens in a new tab), you end up fighting the platform. Although operating systems have recently introduced APIs (like Android’s Credential Manager (opens in a new tab)) for third-party tools to hook into, the experience remains fragmented and lacks the decades of UX polish towards password autofill. Autofill outside the browser and inside native applications remains especially inconsistent. In the future, I believe third-party passkeys will be the way forward, but we are not there yet.

## When passkeys don’t work

Logging into accounts on devices you own is the ideal scenario for passkeys. When you have to handle a colleague’s computer, it gets much more inconvenient. You could plug in a hardware key, but you don’t always have access to the ports. You could sign in and use a synced passkey, but that involves trusting the computer to not leak all of your other passkeys. The last option is to use “Hybrid Transport” (opens in a new tab), where you scan a QR code and connect via Bluetooth simultaneously to the computer. Whilst this option is secure and works in theory, reality is plagued with edge-cases where connections fail or Bluetooth is straight-up unsupported.

## Passkeys aren’t ready yet

I believe enterprise users have good reason to use passkeys, but the ecosystem isn’t mature enough yet for individuals.

Whilst TOTP codes have known phishing vulnerabilities, the recovery and lockout risks of passkeys pose a greater day-to-day risk to most people than an AiTM proxy (opens in a new tab). A combination of randomly generated passwords stored inside a third-party password manager, paired with an independent TOTP app, gives control to the user without giving up the flexibility of plain text. For users who previously reused passwords across all their sites, passkeys are a huge step-up. For everybody else, it is currently a step back.

Written by Ethan Hawksley, a computer science student at the University of Warwick and author of The Second Maintainer.

## 评论（47/47）

**matklad**（40 分） · 2026-09-18T12:06:29.421-05:00：

I love passkeys as an additional login method. My stuff is typically locked behind email and/or password+TOTP, but I like to add passkey on top of that because logging in by just touching the fingerprint scanner is less clicks and faster than going through password manager or "login with X".

It's worth emphasizing that disliking passkeys as the exclusive login method is fully compatible with using them for 90% of logins.

**skobes**（33 分） · 2026-09-18T12:28:48.152-05:00：

Part of the problem with passkeys is that websites do not have a consistent philosophy as to whether they are an additional login method or a required second factor.

**vpr**（26 分） · 2026-09-18T14:04:45.392-05:00：

A combination of randomly generated passwords stored inside a third-party password manager, paired with an independent TOTP app, gives control to the user without giving up the flexibility of plain text. For users who previously reused passwords across all their sites, passkeys are a huge step-up.

I wish anyone dishing out security system design advice like this have a mandatory consultation with 10 people over 65, and probably 5 people who have managed IT security in any organization above 50 people.

Credential stuffing/reuse is a problem, sure, but these people are targeted on a daily basis by decently sophisticated phishers who will hop on a phone call with you.

Passkeys not being forwardable/MITM'able is a feature, not a bug. "Sir, just give me the OTP to confirm your identity". No amount of "We will never ask you for this code" disclaimers will save people.

Banks/financial institutions should be required to give you a non-forwardable hardware token that authenticates you, and governments should follow suit. In a sense, they already do (with ATM cards and chip passports), we just don't have any good interfaces for these tokens.

**abeyer**（6 分） · 2026-09-18T16:25:37.774-05:00：

I wish anyone dishing out security system design advice like this have a mandatory consultation with 10 people over 65, and probably 5 people who have managed IT security in any organization above 50 people.

I though the author was pretty clear that they weren't recommending that as a solution for everyone, but pointing out why passkeys are a step backwards for individuals who already do something like that.

**vpr**（6 分） · 2026-09-18T19:20:37.475-05:00：

a poor fit for personal security. To an individual, the greatest risks are instead permanent account lockout, automated account bans, and device loss. By using passkeys, you gain better security against man-in-the-middle attacks but face the higher probability scenario of losing access to your accounts.

He's talking about individuals; maybe implicitly technically-savvy individuals, though, honestly, I think he meant the general public.

permanent account lockout, automated account bans, and device loss.

These are the greatest risks to technically savvy people. People "immune" to phishing.

The biggest "technical bias" dog whistle is device loss. A lot of people are on unencrypted drives that never leave their house. Sure, when their house burns down, they lose pictures and access to some of their accounts, and they have to call support. Or, they have modern devices they renew periodically and their files have just been magically following them through the cloud and a 10$ a month subscription.

A lot of people's lives are also just not that digitized. They use accounts for bills and banking when they have to, and that's where they're being targeted for phishing.

Passkeys solve several attack vectors for real people at the cost of potential marginal friction for the most technical users. Yes, if you have your own key management setup and would never fall for phishing, sure, your rofi autopass bash banging setup works great and you get to backup your keys yourself. For everyone else, the bank can just ship you another key or ask you to come into the branch with 2 pieces of ID.

**ahelwer**（15 分） · 2026-09-18T10:57:20.605-05:00：

I like passkeys because I just think of them as yubikeys that live inside your devices, and I’ve long used yubikeys for everything. I don’t mess with all the various sync thingamabobs. I can’t remember the last time I signed into an account on someone else’s computer, or them mine. Not saying it doesn’t happen or it is an invalid use case. But computers have become very very personal things! Almost feels like someone asking to write in your journal.

**recursive**（28 分） · 2026-09-18T11:00:06.852-05:00：

I have a work computer. My wife has a desktop computer at home. I have a laptop. A tablet. A phone. The whole family have accounts on the desktop. The whole thing is very many-to-many. The ergonomics of passkeys are not appealing to me.

**soulcutter**（14 分） · 2026-09-18T12:16:35.949-05:00：

I use my password manager for managing passkeys across devices. The article covers this as Third-party synced passkeys.

For me this works very well in every common case I have. I ALSO want to have a username/password for the edge cases, and I use crazy length random passwords. If my passkeys were tied to my devices I’d hate them, but I don’t have the “fighting the platform” problems of the author - the ergonomics seem to “just work” for me.

The auth mechanism I hate the most is text message or email OTP. Not only do I think it’s insecure in comparison, but it’s inconvenient as hell to have to wait up to 30s many times to pass through the gate.

**proctrap**（2 分） · 2026-09-19T09:42:21.321-05:00：

I've set up KPXC for that but I still deny passkeys when I can - as the password auto-fill already works and is so much less obstructive. Heck let all the company stuff be as much passkey as possible, they really need it. But they have a god damn admin team that can recover accs if something breaks. Unlike $randomservice that decided to install a passkey silently in my device that I just lost.

**yshui**（5 分） · 2026-09-18T14:37:37.630-05:00：

but yubikeys are passkeys, and you can plug them into anything that has a usb port, no need to worry about syncing, or whether the particular passkey implementation is secure or not (is it TPM? is it a encrypted file on the disk?). i dislike on device passkeys, but i like passkey as a way to login because i can use yubikeys.

**itamarst**（2 分） · 2026-09-19T08:19:15.724-05:00：

Newer Yubikeys have NFC and so you can use them with non-USB phones too by waving them next to the correct part of the phone. Fiddly and occasionally unreliable, but also feels like magic when it works.

**elephantium**（3 分） · 2026-09-18T16:31:56.177-05:00：

My wife and I don't need to sign in on each others' machines often, but it does happen. Doing taxes is probably the biggest offender. I'd be unhappy if "downloading the tax form" meant resetting my entire Vanguard account.

Actual yubikeys would be better than passkeys in this case. The device-specific lockout issue isn't a factor.

**mxey**（1 分） · 2026-09-19T07:53:19.563-05:00：

You can use a passkey on your phone to log in once on a desktop by scanning a QR code shown by the browser. It’s pretty neat.

**TheGreatGazebo**（11 分） · 2026-09-18T12:11:54.369-05:00：

I hate on device passkeys, but I love yubikey

**algesten**（3 分） · 2026-09-19T05:10:01.203-05:00：

I use yubikey for work. Recently I had one die on me – just wouldn't show up as a USB device at all. Luckily our work policy is to have double yubikeys, so i didn't lose access. It was still very painful to reset all the sites.

**stephenr**（1 分） · 2026-09-19T05:12:06.191-05:00：

Wouldn't you have both keys setup before one dies?

**enpo**（2 分） · 2026-09-19T06:09:19.726-05:00：

I suspect that they needed to revoke the old key as a best practice, and that they'd probably add another new key as future backup key.

**matt-y**（11 分） · 2026-09-18T14:16:54.313-05:00：

Passkeys really seem like a tool best suited for power users. I don't feel that average people - who largely don't use password managers - are going to understand how to use them.

**Hales**（4 分） · 2026-09-19T06:58:14.978-05:00：

I agree.

When passkeys work: they're fine.

When passkeys break: they're a nightmare for non technical users.

If you focus only on the former then you miss the problem. By comparison an ordinary user has a better chance of understanding problems like forgetting their passwords, losing a yubikey, having a yubikey break, having their phone they use for 2FA break, etc. When an invisible passkey breaks... uh... what happened?

**diktomat**（2 分） · 2026-09-19T02:39:55.326-05:00：

Average people use passkeys with the password managers their system provides, without even noticing, or knowing that this is what login by TouchID etc means.

**siru**（1 分） · 2026-09-19T07:31:00.177-05:00：

In principle, I would love to agree with you. But my parents trying to figure out how to get passkeys to reliably work on their devices (a Win10 laptop without fingerprint scanner, an iPad from 2019, and an Android phone stuck in 2017) does not work as simply as relying on the "password manager their system provides".

**stephenr**（1 分） · 2026-09-19T05:16:12.699-05:00：

All the more reason to adopt passkeys.

The only credible argument for passwords being better relies upon someone using a random generated password in a secure password store.

People who don't use a password manager at all have the most to gain with passkeys.

**motet-a**（8 分） · 2026-09-18T13:25:46.858-05:00：

I don’t really agree, I maintaining a service with a fancy password-less authentication system using passkeys and one-time passwords sent by email, and I think passkeys are nice in this scenario:

- About 50% of the users log in with passkeys, as it’s super fast and convenient

- For users using a device that does not support passkey, they sign in with a one-time password sent by email

- Users who have lost their passkey or with a brand new device can still sign in by email the same way, and optionally create a new passkey immediately after that

It took me some time to polish it, but so far people don’t complain much. It’s not the most secure authentication system of the world, it is just passwordless and convenient.

IMO, one thing that could be improved in the spec is how passkeys are identified and named. In my case, I can’t easily get the name of the device to give meaningful names to passkeys (anti-fingerprinting measures on the web…) so it’s difficult to know which passkey is installed on which device. Sure, users could rename their passkeys themselves, but in practice almost nobody will do so.

In fact what’s really… interesting with passkeys is that they are very widely used, while I bet that most users have virtually no idea of what’s going on under the hood when they sign in on a website with a fingerprint! And it’s difficult to explain, many people believe the website can actually see their fingerprint, and won’t understand that a passkey is usually linked to one device.

**Pomax**（11 分） · 2026-09-18T15:01:16.799-05:00：

So what you're saying is you suspect users don't understand that their passkey is tied to their hardware and they're going to find out exactly how screwed they are the moment they switch hardware? Because they have no idea what's goin under the hood?

"I got a brand new laptop! ...oh no what happened I can't log into anything whyyyyy", or even just "I got a second laptop/tablet/phone but I can't log in???". Tying passwords to hardware, in a society that constantly cycles hardware, is a really, really weird idea.

**motet-a**（4 分） · 2026-09-18T17:10:38.877-05:00：

and they're going to find out exactly how screwed they are the moment they switch hardware?

It definitely happens sometimes, but with my application, they just have to login with an OTP sent by email.

Tying passwords to hardware, in a society that constantly cycles hardware, is a really, really weird idea.

Yes but quite often, it’s not actually tied to hardware but to your password manager. At least that’s how it works with iCloud. So it’s not that bad.

**orib**（3 分） · 2026-09-19T00:20:29.764-05:00：

How do you log in to your email that way?

**motet-a**（1 分） · 2026-09-19T01:12:16.681-05:00：

It’s a classic OTP: you receive an email with a temporary 6 digit code that you have to enter on the website. It’s more work that a magic link, but it resists against MFA fatigue attacks.

**proctrap**（5 分） · 2026-09-19T09:45:11.309-05:00：

It's good you're doing that. But my primary fear are all the implementations where this is not the case and passkeys are the only actually trusted source. I've had to battle with big FAANG company not letting me back in because some internal service flagged my login as suspicious (I had the password, email and TOTP). And combine that with a passkey stored on just one device and you're screwed. Plus I don't like the fact that the answer to this is "just use apple/ms/google passkey sync, what could go wrong".

**orib**（3 分） · 2026-09-19T10:11:31.851-05:00：

I'm trying to log into my email: how do I get the email again?

**ubernostrum**（6 分） · 2026-09-18T16:11:58.200-05:00：

Tying passwords to hardware, in a society that constantly cycles hardware, is a really, really weird idea.

Given that the comment you're responding to explicitly mentions having a magic-link backup/recovery method available, and given that all the big passkey implementations now implement cloud-based syncing across devices, this seems like a non sequitur.

**motet-a**（1 分） · 2026-09-18T17:16:04.006-05:00：

Exactly!

**lake**（4 分） · 2026-09-18T12:16:09.593-05:00：

I used to be really against passkeys because initially they failed for me too often. I nonetheless returned to trying them (or sometimes a platform like Google manipulated me into setting one up). Where I've started to use them, I have found that they now mostly work fine for me, synced with Bitwarden across GrapheneOS, desktop Linux, and macos.

I agree that being locked out of my accounts is probably the most real failure mode for me as an individual, more so than my credentials being stolen. I'm still suspicious of passkeys for that reason, and am glad that in situations where I lost a passkey (or for some reason it didn't work), I have been able to return to password auth. I hope I will always be able to.

But I did update my priors on them because the ones I saved to Bitwarden seem to work okay.

**alper**（3 分） · 2026-09-18T16:42:05.261-05:00：

I tried to add a passkey to 1Password and the entire process is very much non-obvious. Almost as if nobody really wants this to work well.

**diktomat**（2 分） · 2026-09-19T02:44:19.765-05:00：

„Have 1Password extension enabled in your browser -> click create passkey in the website’s account settings -> confirm 1Password modal” is non-obvious?

**alper**（1 分） · 2026-09-19T04:21:33.502-05:00：

None of that happened for me (a regular 1Password user).

**Sharparam**（1 分） · 2026-09-19T13:52:02.481-05:00：

Are you using the new "unified" "universal" mode in 1Password? That thing seems to have some glitches still.

**prussian**（3 分） · 2026-09-18T13:27:04.611-05:00：

I only use fido/passkeys/whatever at work and the fact that things like

https://github.com/Aldaviva/AuthenticatorChooser

Exist are why I hate them. I understand the limits of passwords, from a security standpoint, but they're still 1000x convenient than all this pointless menuing. Even stuff like getting my Windows password or the VPN login token requires painfully precise menuing.

**motet-a**（3 分） · 2026-09-18T13:33:56.000-05:00：

IMO Windows support for passkeys is much worse than other OSes... For instance you are required to enable Windows Hello to use passkeys. It does not make any sense, Windows Hello is not even necessarily biometric...

**tad**（3 分） · 2026-09-18T14:26:44.215-05:00：

It's because Windows Hello is both the system authenticator and the integration point for third-party authenticators. The "biometric Windows login" feature is one very small part of the system.

**stephenr**（1 分） · 2026-09-19T05:19:09.412-05:00：

This would be like saying you hate pizza because franchise pizza shops and frozen pizzas exist.

**samcat116**（2 分） · 2026-09-18T18:31:20.516-05:00：

I love passkeys. Any new web service I make is passkeys and OIDC only

**Slackwise**（1 分） · 2026-09-19T12:30:19.063-05:00：

All of these words are absolutely correct, but.... I still nudge non-technical people towards Passkeys stored in password managers, or at minimum generated passwords in them.

Maybe I'm in the minority, but I'm a big fan of sites dumping passwords entirely and either using single-auth sessions created via email links and passkeys as a convenience to bypass that. At that point the user only needs to secure their email, which is always a single point of failure anyway in security.

P.S. Nobody should be using Chrome's password manager for anything because it's fundamentally insecure. Please use Bitwarden or Proton Pass, or some other password manager instead.

**carlomonte**（1 分） · 2026-09-19T04:04:06.624-05:00：

i don't like passkeys either. it's about control (access control). for passkeys, control is with the smartphone, the yubikey, with whomever except for the user in need of authentication.

we have a decades old public+private key based authentication solution which works just fine: SSH. industry, please just copy that.

i understand that managing keys is beyond consumers. yet taking the keys out of the hands of advanced/professional users only leads to a situation where nerds (those who were previously your early adopters) refuse your new shiny.

this is another direction in which the industry appears to have gone too far.

**mxey**（2 分） · 2026-09-19T07:57:12.743-05:00：

SSH, the thing where there is a non-zero risk of somebody uploading their private key instead of their public key?

**carlomonte**（1 分） · 2026-09-19T09:38:56.334-05:00：

Comment removed by author

**colindean**（1 分） · 2026-09-19T11:00:06.286-05:00：

I'm working on rebuilding a web app for a technical community I run. Most participants are software builders but every now and then we get less tech savvy HR and sales folk.

The framework I'm using doesn't really seem to have some kind of a default or go to solution for IAM so I'm largely working on rolling my own.

I've largely settled on tokens sent by email— no link , just copypaste or retype— at account creation and login, with passkey as a fast lane option.

I was fixing to use only pass key but some friends talked me out of it: dealing with support requests for when somebody doesn't manage their passkeys well would be a serious disruption. I need to do email confirmation anyway so why not just reuse that same workflow for sending tokens and just eliminate the potential for fishing by just never sending a link?

Simplicity of implementation and ongoing maintenance is the most important to me. I want to run in person events, not be a principal software engineer, product designer, and site reliability engineer all rolled into one and not paid for it.

I'm probably working on the identity stuff the next time I work on the app which could be today or tomorrow but potentially next weekend, too.

I'd love others thoughts on this, but this article soundly represents the voices that talked me out of using only passkeys.

**Sharparam**（1 分） · 2026-09-19T14:04:04.048-05:00：

I've largely settled on tokens sent by email— no link , just copypaste or retype— at account creation and login

This flow sucks though. I have to deal with that bullshit every time I need to re-login to Claude Code at work and it is by far the worst login flow possible.
