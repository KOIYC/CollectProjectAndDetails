---
type: "corpus"
item_id: "2fe9c792d55bf3e5"
title: "Don’t Let Architecture Astronauts Scare You (2001)"
source: "lobsters"
source_name: "Lobsters"
url: "https://lobste.rs/s/3xfxnj/don_t_let_architecture_astronauts_scare"
project_url: "https://joelonsoftware.com/2001/04/21/dont-let-architecture-astronauts-scare-you"
published_at: "2026-09-19T07:08:52.631-05:00"
captured_at: "2026-09-20T03:40:49+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - lobsters
  - programming
metrics: {"score": 27, "comments": 13}
comments_count: 13
comments_total: 13
discovered_via: "lobsters:hottest"
archived: true
archived_at: "2026-09-20T09:21:32+08:00"
archive_reason: "渠道停用"
---

# Don’t Let Architecture Astronauts Scare You (2001)

- **来源**：Lobsters　|　**kind**：post
- **原帖**：https://lobste.rs/s/3xfxnj/don_t_let_architecture_astronauts_scare
- **指标**：得分=27 · 评论=13
- **作者**：—　|　**发布**：2026-09-19T07:08:52.631-05:00
- **项目链接**：https://joelonsoftware.com/2001/04/21/dont-let-architecture-astronauts-scare-you
- **采集**：2026-09-20T03:40:49+08:00　|　**id**：`2fe9c792d55bf3e5`

## 正文

Published: 2001-04-21
Author: by

Don’t Let Architecture Astronauts Scare You – Joel on Software

 April 21, 2001 December 5, 2016 by Joel Spolsky 

# Don’t Let Architecture Astronauts Scare You

When great thinkers think about problems, they start to see patterns. They look at the problem of people sending each other word-processor files, and then they look at the problem of people sending each other spreadsheets, and they realize that there’s a general pattern: sending files. That’s one level of abstraction already. Then they go up one more level: people send files, but web browsers also “ send” requests for web pages. And when you think about it, calling a method on an object is like sending a message to an object! It’s the same thing again! Those are all sending operations, so our clever thinker invents a new, higher, broader abstraction called messaging, but now it’s getting really vague and nobody really knows what they’re talking about any more. Blah.

When you go too far up, abstraction-wise, you run out of oxygen. Sometimes smart thinkers just don’t know when to stop, and they create these absurd, all-encompassing, high-level pictures of the universe that are all good and fine, but don’t actually mean anything at all. 

These are the people I call Architecture Astronauts. It’s very hard to get them to write code or design programs, because they won’t stop thinking about Architecture. They’re astronauts because they are above the oxygen level, I don’t know how they’re breathing. They tend to work for really big companies that can afford to have lots of unproductive people with really advanced degrees that don’t contribute to the bottom line.

A recent example illustrates this. Your typical architecture astronaut will take a fact like “Napster is a peer-to-peer service for downloading music” and ignore everything but the architecture, thinking it’s interesting because it’s peer to peer, completely missing the point that it’s interesting because you can type the name of a song and listen to it right away.

All they’ll talk about is peer-to-peer this, that, and the other thing. Suddenly you have peer-to-peer conferences, peer-to-peer venture capital funds, and even peer-to-peer backlash with the imbecile business journalists dripping with glee as they copy each other’s stories: “Peer To Peer: Dead!”

 The Architecture Astronauts will say things like: “Can you imagine a program like Napster where you can download anything, not just songs?” Then they’ll build applications like Groove that they think are more general than Napster, but which seem to have neglected that wee little feature that lets you type the name of a song and then listen to it — the feature we wanted in the first place. Talk about missing the point. If Napster wasn’t peer-to-peer but it did let you type the name of a song and then listen to it, it would have been just as popular.

Another common thing Architecture Astronauts like to do is invent some new architecture and claim it solves something. Java, XML, Soap, XmlRpc, Hailstorm, .NET, Jini, oh lord I can’t keep up. And that’s just in the last 12 months!

I’m not saying there’s anything wrong with these architectures… by no means. They are quite good architectures. What bugs me is the stupendous amount of millennial hype that surrounds them. Remember the Microsoft Dot Net white paper? 

> The next generation of the Windows desktop platform, Windows.NET supports productivity, creativity, management, entertainment and much more, and is designed to put users in control of their digital lives.

That was about 9 months ago. Last month, we got Microsoft Hailstorm. That white paper says:

> People are not in control of the technology that surrounds them….HailStorm makes the technology in your life work together on your behalf and under your control.

Oh, good, so now the high tech halogen light in my apartment will stop blinking randomly.

Microsoft is not alone. Here’s a quote from a Sun Jini whitepaper:

> These three facts (you are the new sys admin, computers are nowhere, the one computer is everywhere) should combine to improve the world of using computers as computers — by making the boundaries of computers disappear, by making the computer be everywhere, and by making the details of working with the computer as simple as putting a DVD into your home theater system.

And don’t even remind me of the fertilizer George Gilder spread about Java:

> A fundamental break in the history of technology…

That’s one sure tip-off to the fact that you’re being assaulted by an Architecture Astronaut: the incredible amount of bombast; the heroic, utopian grandiloquence; the boastfulness; the complete lack of reality. And people buy it! The business press goes wild!

Why the hell are people so impressed by boring architectures that often amount to nothing more than a new format on the wire for RPC, or a new virtual machine? These things might be good architectures, they will certainly benefit the developers that use them, but they are not, I repeat, not, a good substitute for the messiah riding his white ass into Jerusalem, or world peace. No, Microsoft, computers are not suddenly going to start reading our minds and doing what we want automatically just because everyone in the world has to have a Passport account. No, Sun, we’re not going to be able to analyze our corporate sales data “as simply as putting a DVD into your home theatre system.”

Remember that the architecture people are solving problems that they think they can solve, not problems which are useful to solve. Soap + WSDL may be the Hot New Thing, but it doesn’t really let you do anything you couldn’t do before using other technologies — if you had a reason to. All that Distributed Services Nirvana the architecture astronauts are blathering about was promised to us in the past, if we used DCOM, or JavaBeans, or OSF DCE, or CORBA.

It’s nice that we can use XML now for the format on the wire. Whoopee. But that’s about as interesting to me as learning that my supermarket uses trucks to get things from the warehouse. Yawn. Mangos, that’s interesting. Tell me something new that I can do that I couldn’t do before, O Astronauts, or stay up there in space and don’t waste any more of my time.

# AI Is an Elite Crime Spree  - BIG by Matt Stoller

## 评论（13/13）

**koala**（13 分） · 2026-09-19T07:18:49.396-05:00：

The article goes more in the direction of "when you think too much about abstraction, you stop thinking about the actual point of the software", which is a great point. However, in my head I've always focused on something else, perhaps less important: when you become an architect and disconnect from the day-to-day of writing and maintaining code, you lose your ability to reason effectively about software development.

**jrwren**（10 分） · 2026-09-19T08:17:46.640-05:00：

IMO it is much worse than that. At megacorps, solving complex problems is highly rewarded. This changes the incentive for writing the best, most simple, most elegant solution to the most complex solution. Anytime I see someone with Architect in their title at a megacorp, I think they love composing huge Rube Goldberg machines out of commodity software components. They have their list of popular tech and they have to tick off each checkbox. They might notice that a solution isn't using Kafka, oh no! Gotta have some Kafka in there! It gets added. Same for a workflow system. Gotta add the Temporal! They are playing pokemon and gotta catch every tech trend.

**hjvt**（2 分） · 2026-09-19T09:30:42.716-05:00：

Here's a recent discussion on a blogpost expressing a similar idea

And here's a (lack of) discussion on a talk that is also about the obsession the CS field has with "hard problems" that don't necessarily yield great results

**koala**（2 分） · 2026-09-19T11:14:20.447-05:00：

Heh, but I don't think overengineering is specific to architects or people who are detached from writing software. In my experience, people coding daily also do it.

It's true that organizations sometimes incentivize this, but I also think we all love to learn new shiny stuff.

On a different direction, I also think we often mistake what a "complex problem" is. For example, we've been writing CRUD apps for eons, and they still take an absurd amount of menial work to deliver. IMHO it's because a good generic CRUD framework is a complex problem but we do not realize it. The last innovation I found in this area I liked was... Django around 2011.

(And I'm not sure what makes some problems sexier, honestly. My best fit theory is that they must feel new. CRUD is an old problem.)

**viraptor**（3 分） · 2026-09-19T09:50:58.919-05:00：

when you become an architect and disconnect from the day-to-day of writing and maintaining code, you lose your ability to reason effectively about software development

That's a strong claim. I've not seen that in practice from people who used to do good day to day development. They ask questions as sharp as anyone else about projects.

**koala**（4 分） · 2026-09-19T07:08:52.801-05:00：

Earlier discussion here eight years ago. (Edit: fixed link, see child comment.)

I was reading yet another essay of the current mania, when the term "architecture astronaut" popped into my head. I have seen it used many times, and I think it's a useful term, but somehow I had missed apparently Joel coined it.

(It's a bit ironic and disappointing that I dug a bit to see what Joel is up to these days, though.)

**lightandlight**（2 分） · 2026-09-19T07:34:50.098-05:00：

The link in this comment goes to the article, not a previous discussion.

**koala**（1 分） · 2026-09-19T07:36:09.338-05:00：

Thanks, you were quick and the edit window had not expired yet, fixed it!

**vinipsmaker**（2 分） · 2026-09-19T09:49:33.214-05:00：

That was an excellent reading. Thank you for sharing.

**hongminhee**（2 分） · 2026-09-19T10:48:33.963-05:00：

Not related to the article's actual argument, but reading it gives me an odd feeling. It stirs up nostalgia for the rosy optimism of the early 2000s. Maybe it hits differently because that's roughly when I got into software development. Makes me wonder whether people looking back at this era, twenty years from now, will feel something similar.

**snej**（4 分） · 2026-09-19T11:07:53.746-05:00：

Yeah … it was an exciting time. We'd been through the dot-com crash, which brought a welcome bit of calm, and people were figuring out what to do with new stuff like dynamic HTML, XHR, structured data formats like XML, high-level networking APIs like Java's and Python's…

(Plus, for us Apple diehards, MacOS X had come out and made development so much easier and more powerful. I remember taking a Cocoa training class in late 2000 and my mind being blown at how easy it was to build a GUI app.)

I feel like it was Facebook (and secondarily Twitter) that ruined everything … but I’m sure if they hadn’t, someone else would have.

**lake**（1 分） · 2026-09-19T12:17:24.571-05:00：

I've shared a silly idea with my friends before that it was the death of Google Wave that marked the end of the 2000s techno-optimism (and this attitude of "we can do things that are both technically cool and broadly successful, because they are technically cool"). There was techno-optimism after that, but of a different kind. That would roughly coincide with FB/Twitter becoming more popular.

But any historical marker like that would be arbitrary, and all of it was an ongoing process.

**koala**（1 分） · 2026-09-19T13:54:48.664-05:00：

Lately I'm placing the end of the "golden age" at the rise of smartphones. For example, release of the first iPhone in 2007. But Google killed Wave in 2010, so more or less the same era. (I thought Wave was the future, the next big Google revolution after search and GMail. My crystal ball is not so good.)

To me the factor is the move to non-programmable, non-keyboard devices, which are much less "interactive" than laptops, desktops, etc. But likely it was also the increasing "commercial" activity on the Internet and a couple of other things.

## 关联链接

- https://www.joelonsoftware.com/2001/04/21/dont-let-architecture-astronauts-scare-you/
