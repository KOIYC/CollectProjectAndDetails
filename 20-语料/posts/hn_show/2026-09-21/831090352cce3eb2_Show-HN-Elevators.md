---
type: "corpus"
item_id: "831090352cce3eb2"
title: "Show HN: Elevators"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49124218"
project_url: "https://john.fun/elevators"
author: "Jrh0203"
published_at: "2026-07-31T15:17:28Z"
captured_at: "2026-09-21T03:11:05+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_Jrh0203
  - story_49124218
  - show_hn
metrics: {"points": 1680, "comments": 415, "engagement_velocity": 1680}
comments_count: 415
comments_total: 415
discovered_via: "hn:show_hn:83d"
---

# Show HN: Elevators

> [!info] 一句话导读
> ← john.fun Elevators

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49124218>
> 指标：点赞=1680 · 评论=415 · engagement_velocity=1680
> 作者：Jrh0203　|　发布：2026-07-31T15:17:28Z
> 项目链接：<https://john.fun/elevators>
> 采集：2026-09-21T03:11:05+08:00　|　id：`831090352cce3eb2`

## 正文

← john.fun Elevators
 Everyone has shared the frustration of waiting for an elevator that never seems to arrive. "I pressed the button, why isn't it coming?" you ask. For something as commonplace as elevators, they are far more complex than meets the eye.
 Over the course of this article, we'll unravel the mysteries of elevators. The way you push their buttons, and how they push yours.
 1 x 5 x 25 x
One Car
 The simplest elevator algorithm is called SCAN and was patented in 1961. The elevator starts at the lobby and goes all the way to the top floor before reversing and coming back down. It picks up and drops off anybody on the way.
 Most of the time you don't actually need to go to the TOP floor. If the elevator goes only as high as requested before reversing, the algorithm is called the LOOK algorithm. This is the algorithm most people know and expect.
 1 x 5 x 25 x
 add five calls
 Multiple Cars
 Here's where the mystery begins. If there are multiple elevators, how do the cars coordinate who picks up who?
 In the most basic system, there's a central scheduler that tells each elevator which floors to stop on. When a new request comes in, it's assigned to the closest elevator. As we'll soon see however, we can do better.
 1 x 5 x 25 x
Long Waits
 How do you actually measure how good an elevator algorithm is? The obvious metric is how long you wait for the elevator to arrive.
 A very simple measure is "how often does the elevator arrive within 30 seconds?" Or "how often does the elevator arrive within 90 seconds?"
 -
 wait < 30s
-
 wait < 90s
1 x 5 x 25 x
 flow 14 /min reset
 Applied Stats
 More rigorously, we want to look at the DISTRIBUTION of wait times. If we plot the wait time across thousands of rides, we get the histogram below.
p50 — p90 —
25 x 100 x 500 x
 flow 14 /min reset
 A p90 of 2m means 90% of the time, riders wait 2m or less for the elevator. A p50 of 1m means half the time the elevator arrives within 1m.
 People don't usually remember the average amount of time they wait. They fixate on those times when the elevator took FOREVER, the p90 case.
 Morning Rush
 Not all passenger traffic is created equal. Imagine a large corporate office building. In the mornings, nearly all traffic is dominated by trips from the lobby to the upper levels.
 In the evening this flips as everyone leaves the building. The lunch rush is a bit of both, and the remaining traffic is often from floor to floor.
 Morning Lunch Evening Interfloor
 -
 wait < 30s
-
 wait < 90s
5 x 25 x 100 x
 flow 14 /min reset
 The distribution of wait times varies drastically depending on the time of day and the traffic patterns the elevators are facing. Morning rush notoriously has the worst wait statistics.
 Smarter Elevators
 When analyzing the LOOK elevator algorithm, we LOOKED (ha ha) at how riders are assigned to cars. We naively assigned each request to the nearest car but said we could do better.
 What if the nearest car is full? We can get smarter with Otis' RSR (Relative System Response) algorithm. RSR scores each car for how well suited it is to pick up a passenger. Lower scores being better.
 RSR pickup score
 Score = ETA to pickup + onboard load penalty + same-direction anti-bunching penalty - direction-match bonus - idle-nearby bonus - low-load bonus
Anti-Bunching Penalize a car if another car is already headed to the same floor in the same direction.
 Idle Nearby Reward idle cars within two floors of the caller.
 RSR also re-optimizes every 5 seconds. A passenger that's going to be picked up by elevator A can be re-routed to elevator B if elevator A encounters delays. This re-optimization turns out to be key for streamlining traffic flow.
 In the graphic below, each elevator lights up when it's the best choice to service a call from floor 3 if the button happened to be pressed at that exact moment. This constantly changes as the elevators move, showing the optimizer in motion.
 LOOK vs RSR
 Armed with our elevator analysis toolkit, we can benchmark the performance of LOOK vs RSR to see how much a smarter elevator algorithm actually improves wait time.
 LOOK
 - wait < 30s
 - wait < 90s
RSR
 - wait < 30s
 - wait < 90s
1 x 25 x 250 x
 flow 8 /min reset
 Interestingly as the flow rate gets higher, LOOK actually starts to outperform RSR. When the elevators are always full and stopping on every floor, the extra rules don't matter as much.
 LOOK also tends to outperform RSR in small buildings with fewer elevators per bank. Sometimes it's better to just keep things simple.
 Another metric you can track is journey time, how long you're actually waiting in the elevator before getting to your floor. RSR and LOOK have different characteristics here as well but that's beyond the scope of this article.
 Destination Dispatch
 Not all elevators have buttons in them. Some of the fancy new elevators have a kiosk on each floor that allows you to specify what floor you're heading to before the elevator even arrives. The kiosk then points you to which elevator you should wait for.
 This is called Destination Dispatch. At first glance, it seems great. The elevator optimizer now has full knowledge of who is going where, certainly we can use this to reduce wait times right?
 RSR
 - wait < 30s
 - wait < 90s
Destination Dispatch
 - wait < 30s
 - wait < 90s
1 x 25 x 250 x
 flow 8 /min reset
 It turns out these fancy kiosks are in general worse for wait times compared to the traditional good ol' up and down buttons. There are certainly edge cases when the kiosks can win out (extremely tall buildings with 8+ cars per elevator bank) but for the majority of cases, simple up down buttons reign supreme.
 This counterintuitive result is all thanks to the rebalancing step where every 5 seconds, the system re-optimizes each elevator's path. The kiosk enforces rigidity, you must get in the assigned elevator.
 The state of the world 30sec after you called your elevator might be very different but the system is unable to adapt. Turns out the loss in flexibility is not worth the extra information for the optimizer.
 Full Sim
 Here's a simulation with all the buttons and knobs to play with. Go crazy!
 Morning Lunch Evening Interfloor
 -
 wait < 30s
-
 wait < 90s
floors 8 cars 4 flow 18 /min
 1 x 25 x 100 x
 Look RSR Destination Dispatch
reset histogram
Conclusion
 This article just scratches the surface of elevator algorithms. Next time you're stuck waiting for an elevator, try not to take it personally. The elevator did hear you, it just has a lot to think about.
 Made with <3 by John
 ← john.fun

## 评论（415/415）

> **shadeslayer_** · 2026-07-31T15:49:28.000Z　
> This article gives me war flashbacks about a particularly irritating OO design interview from 5 years ago.

---

> **sambaumann** · 2026-07-31T15:49:38.000Z　
> This reminds me of elevator saga (https://play.elevatorsaga.com/) - little programming game where you have to program elevator schedules.

---

> **orliesaurus** · 2026-07-31T15:50:29.000Z　
> Oh my god, every time I'm waiting for the elevator, I think of how annoying it must be to be someone who's building the algorithm to make sure that you minimize the amount of wait times between picking up people and taking them to their destination. Then I also wonder if the people who apply the logic and program the logic into the elevators are actually evil sadists that are doing it on purpose to make us wait longer enough and suffer a little extra.

---

> **clarkmoody** · 2026-07-31T15:51:40.000Z　
> One of the most frustrating assignments[1] (2011) in my computer science education was trying to build a better mousetrap for elevator control.[1]: https://clarkmoody.com/Moody_AgentBasedElevatorControl.pdf

---

> **brandonpelfrey** · 2026-07-31T15:51:55.000Z　
> For folks that have never seen elevator scheduling the game: https://play.elevatorsaga.com/
> Enjoy this rabbit hole :D

---

> **gosub100** · 2026-07-31T15:52:29.000Z　
> Maybe I missed it, but the algorithm should also redistribute empty elevators that stop too closely to each other.

---

> **jmyeet** · 2026-07-31T15:55:35.000Z　
> This is a good article. It reminds me of a story.At a previous employer we had heteregenous elevators. In one bank, some went to the lower half of floors only while others went to all and the company installed a "smart" elevator system. I kind of became known because I was constantly yelling about this system in the feedback group because I hate "smart" elevators and and (IMHO) they just don't work. What actually works is express elevators and sky lobbies.This article covers one of the deficiencies this system had: full elevators. For example, you'd want to go down and an elevator would skip your floor because another had already been assigned. That one would show up full and you couldn't go down. Down wasn't so bad because the stairs weren't a bad option but up was terrible. Going up a few floors was fine. Going up 20 was... a bigger issue.Back in the day we had elevator operators and people in the lobby during the morning rush who would shepherd people into particular elevators. I actually think this system works way better than anything technology has come up with. Even if you nail the implementation (and I've never experienced elevators that have), people don't read and will just get into elevators anyway.Anyway the article says that generally speaking on smaller banks simple up and down buttons work best. I absolutely agree.There's a deeper issue here though and that is solutions looking for a problem. Nobody is making money from up and down buttons. They are fromn selling smart elevator solutions. And you see this everywhere in life. It basically devolves into rent-seeking behavior. Salespeople wine and dine a couple of people responsible for making decisions and then make bank on selling something nobody wants or needs as well as the constant maintenance and updates.

---

> **jihadjihad** · 2026-07-31T15:57:11.000Z　
> In a similar vein, there was an interesting discussion [0] a while back about elevator buttons [1] and how timing for door close/open works, along with a bit of the history and regulations that go into them.0: https://news.ycombinator.com/item?id=351523411: https://computer.rip/2023-03-13-the-door-close-button.html

---

> **Waterluvian** · 2026-07-31T15:58:02.000Z　
> Makes me want to play Sim Tower again.There’s something so satisfying about watching a machine just dutifully work through queued tasks like this.

---

> **jp191919** · 2026-07-31T15:58:14.000Z　
> Reminds of something I haven't thought about in a very long time... SimTower

---

> **itunpredictable** · 2026-07-31T15:58:26.000Z　
> I didn't realize that neal.fun had some competition.

---

> **geephroh** · 2026-07-31T15:59:28.000Z　
> Slightly OT, but this reminded me of Colson Whitehead's _The Intuitionist_[1], an amazing speculative mystery novel about two dueling schools of elevator inspection philosophies: the Empiricists and the Intuitionists.1. https://en.wikipedia.org/wiki/The_Intuitionist

---

> **paxys** · 2026-07-31T16:00:37.000Z　
> My biggest pet peeve is elevator banks where they don’t make some number of idle elevators automatically come back to the lobby. Half your traffic is over there! Everyone coming in has to wait an extra minute or two because all your elevators were chilling on the 35th floor and above.

---

> **teepo** · 2026-07-31T16:01:51.000Z　
> I've never really liked Destination Dispatch elevators. Besides struggling to find the car I've been assigned to, sometimes you really have to hustle across the lobby to catch it. Then you also run into visitors that assume it's a normal car and can hit a floor button when the get in, only to realize they've walked into a car without buttons.

---

> **zatkin** · 2026-07-31T16:02:16.000Z　
> I think a small improvement that could be made is to have the dot representing the person be colored the same as a dot on each floor, which would obviate the destination floor for each individual.

---

> **olex** · 2026-07-31T16:02:27.000Z　
> The biggest problem I always have with elevators is not the algorithm, it's the people seemingly being unable to grasp the concept of pressing either the up or the down request button, depending on where they want to go. Almost always I find someone will press both, because "then the elevator comes faster". Completely ignoring the fact that they end up going the wrong way first half the time, and adding an unnecessary halt for everyone already in there. How hard can it be to understand?..

---

> **moralestapia** · 2026-07-31T16:04:10.000Z　
> >All this technology just to underperform the S&PMy takeaway is that the benefit of using a much more complex algorithm is marginal.

---

> **proee** · 2026-07-31T16:05:01.000Z　
> Don't forget the executive elevator algorithm (EEA), which uses a priority interrupt to take passengers directly to the top floor.

---

> **quietsegfault** · 2026-07-31T16:06:24.000Z　
> I love elevator simulations.

---

> **hermanschaaf** · 2026-07-31T16:07:09.000Z　
> Hah, I thought a lot about this problem while developing Sky Lobby, a mobile game (iOS / Android) about controlling and automating elevators.In the game, some of the elevators are automated, and I wanted to choose an algorithm that best aligned with what players would expect an elevator to do. I ended up going with something close to LOOK, which (as the article states) is mostly what people expect. Except in case of ambiguity, I had it prioritise floors that have been waiting longer, to improve the p90, which is important in the game.But now, add in these challenges:- double-deck cabs (where attached cabs cover two floors at once)- transfer floors between shafts- express shaftsand the best (or at least, most expected) algorithm becomes much less obvious! I'll leave it as an exercise for the reader to figure out the best one.Luckily I was in charge of a game, not a real elevator system, so I just had to find a heuristic that was good-enough, and could tweak the rules to let players manually override the elevator's plan if they don't like where it's going. This seems to have satisfied most players.

---

> **OJFord** · 2026-07-31T16:11:43.000Z　
> I think this comparison is also assuming the distribution of request & requested floor is uniform? When actually near pairs are less likely (I'll just take the stairs) than bottom to top, so even analysing it is more complex than at first glance.

---

> **mito88** · 2026-07-31T16:12:38.000Z　
> did he factor in the lifting speed?

---

> **jamies** · 2026-07-31T16:15:37.000Z　
> This is absolute catnip to me. Fantastic job to the author! It really scratches the itch of wanting to understand elevator dispatch algos!I want something similar for advanced sensor stop lights...I've long toyed with creating an elevator simulator game, but every time I build a prototype I realize it's not that fun to manually dispatch elevators, and playing with algos only goes so far! Elevator Saga is great for the programming side: https://play.elevatorsaga.com/

---

> **coop57** · 2026-07-31T16:17:01.000Z　
> You have no idea how excited I was to see this article today. I've long been fascinated with elevators and the algorithms that control them. Thank you!

---

> **cubefox** · 2026-07-31T16:19:45.000Z　
> > Everyone has shared the frustration of waiting for an elevator that never seems to arrive.Really? Maybe I'm lucky I never had to deal a lot with elevators.

---

> **realaccfromPL** · 2026-07-31T16:21:23.000Z　
> I absolutely adore this, I am always trying to guess whichever elevator will come in first in large crowded buildings. Thanks for this article.

---

> **tgsovlerkhgsel** · 2026-07-31T16:23:33.000Z　
> Is there a comprehensive overview of a) multi-bank elevator algorithms that are out there, b) the config parameters that the elevator tech/company can set on an elevator system?For example, some elevators allow adjusting the door closing/opening speeds etc., I'd be curious what other things can be adjusted.

---

> **niklasrde** · 2026-07-31T16:24:51.000Z　
> I wonder how a TWIN system with 2 cars per shaft factors in here: https://www.tkelevator.com/us-en/products/elevators/all-elev...That will need planning and assignment I guess? But at what load figures does it become more efficient?

---

> **reader9274** · 2026-07-31T16:25:33.000Z　
> I feel like most cases of wait times are due to elevators "waiting" empty in the wrong floor. They either all wait in the bottom floor, or all wait where they were last left at. Would be better if their waiting floors were distributed throughout the floors so that first response is fast.

---

> **heironimus** · 2026-07-31T16:26:49.000Z　
> No mention of an algorithm/sensor for checking capacity of the car. It's a pain when your elevator car shows, it's full, and your request is canceled, meaning you have to press again. Better if the car was full and just moved on.I can see how that could be challenging when people get off on intermediate floors, making a full car available again, changing status. And, if 3 people are waiting and there is room for 1, should it stop or not? Etc.My favorite takeaway from this is how simplicity often beats complexity.

---

> **pseudosudoer** · 2026-07-31T16:26:53.000Z　
> This is commonly referred to as the "dial-a-ride" problem, which is an optimization problem with a multi-variate cost. Back in college for my senior design project we built a multi-axis closed loop servo system which would emulate a slide guitar. The dial-a-ride problem is identical to optimizing travel for a string of notes/chords.

---

> **tamimio** · 2026-07-31T16:30:49.000Z　
> As someone who lives in a penthouse, elevator’s frustrations are real struggle especially in rush hours, because the elevator has to travel dedicated to you rather than you piggy backing on one that is already going up or down.

---

> **cruffle_duffle** · 2026-07-31T16:30:50.000Z　
> If you like elevator hacking don’t forget the seminal DEF CON talk by Deviant Ollam and Howard Payne: https://youtu.be/oHf1vD5_b5II watch it like once a year because it always tickles some part of me. Like all the different modes you can get an elevator into. The most fancy one people might encounter is when moving into or out of a building. The front office can give you a key to give exclusive control over an elevator so your movers aren’t waiting around on elevators. Put it in that mode and it will stop responding to calls from other floors. Only the person with the key can control the elevator. You get on, select the floor, door closes elevator goes, and then just chills there with the door open waiting for you. Annoying for the rest if the building (the building is down an elevator when in that mode) but is amazing for the person using it! But there are way, way more depending on the installation and function.Fun fact: most elevator shafts are sealed at the top as tight as possible to prevent them from becoming a giant chimney in a fire. It never even occurred to me until I was in a mechanical room wondering “where is the hatch to look down the shaft?” The answer is “there is none, and it’s a feature not a bug.” You want to block all airflow so fire doesn’t chase up the shaft into neighboring floors. Who knew!

---

> **efavdb** · 2026-07-31T16:31:12.000Z　
> I recently wrote an article about this problem, and detail one reasonable algo for minimizing wait time. (Doesn’t consider concept of cars being full though, interesting addition)https://jslandy.com/elevators/

---

> **bob1029** · 2026-07-31T16:33:11.000Z　
> Parking is a big factor too. Where you put the elevator when it is not being used can mean the difference between the doors opening instantly and worst case scenario.

---

> **dperfect** · 2026-07-31T16:33:15.000Z　
> Destination dispatch should be no worse than standard up/down buttons, right (at least in theory)? It provides additional information about the destination, but it should be possible for that information to be interpreted as if it were just an up/down button press, so RSR could still be used. I have a feeling a better algorithm could in fact make destination dispatch slightly better than RSR... or am I missing something?Of course, user error is also a factor, so this isn't accounting for people not understanding how to use it and making things worse that way.

---

> **omoikane** · 2026-07-31T16:41:53.000Z　
> > Destination Dispatch [...] are in general worseI wonder if this is an artifact of how the author used random destinations. I worked in a building that used Destination Dispatch, and the common travel pattern seemed to be:- Everyone who is not on the ground floor generally want to go to the ground floor.- People who are on the ground floor generally travel in large groups to the same destination.This happens because people who worked on the same floor often leave for lunch at the same time, and return at the same time to the same floor. Destination Dispatch helps in this case because it's batching large groups of people with the same destination.

---

> **danielvaughn** · 2026-07-31T16:43:46.000Z　
> I've always wondered about elevator algorithms. This is awesome.

---

> **vachina** · 2026-07-31T16:46:03.000Z　
> Anybody knows what algorithm HITACHI is using on their elevators? Their elevators feels most “responsive” in high rises.

---

> **taftster** · 2026-07-31T16:48:20.000Z　
> In these various elevator algorithms, it's not commonly discussed the overall wear and tear on the elevator. More movements would typically translate to faster repair times. Hydraulic fluids needing to be replaced, parts breaking, etc.Efficient elevator algorithms will often suggest moving an elevator into a preempted positioning strategy, based on time of day or peer elevator positions. The scheduler might move an elevator up to offset one coming down, for example. The demand-signal algorithms at least minimize movement in this way.I think minimizing maintenance at the cost of increasing wait times is probably an important balance to get right. No doubt, the cost owners for maintenance are not going to perceive the wait time of passengers to be as important.

---

> **ryukoposting** · 2026-07-31T16:49:19.000Z　
> My friend lives in a building with one of those super old elevators with the manual double doors and no queuing. It's the sort of elevator that someone probably got paid to operate once upon a time.Using such a primitive elevator gave me a newfound appreciation for the complexity of modern designs. The queueing algorithms are subtle but clever, and the difference in efficiency is instantly obvious once you've dealt with the alternative.

---

> **peterldowns** · 2026-07-31T16:52:14.000Z　
> Back in highschool, simulating different elevator algorithms was one of the projects I implemented during my CS class. It wasn't for the class — AP CS did not require anything like actual programming — but it was a fun project.A cool connection is that a spinning-disk hard drive (HDD) is actually kind of like one really long elevator, just wrapped around a spindle instead of perfectly vertical. The SCAN algorithm is actually a disk-scheduling algorithm!https://en.wikipedia.org/wiki/Elevator_algorithm

---

> **jhallenworld** · 2026-07-31T16:58:01.000Z　
> What this doesn't include: not all people are equal. Do you want the CEO of your new office building to have to wait behind a bunch of plebeians? At least one car is going to have to be reserved for the better people.

---

> **hasteg** · 2026-07-31T17:01:28.000Z　
> Lol, love this post. Every single day when I take the elevators at the office I try and figure out what the algorithm is behind it. Been too lazy to just research it. Now I know!

---

> **prometheus1992** · 2026-07-31T17:03:51.000Z　
> This is beautiful. By the end of it I started to feel like I was calculating complicated chess lines in a middle game.

---

> **jgrahamc** · 2026-07-31T17:10:19.000Z　
> It also depends on the person understanding what the elevator button does: https://blog.jgc.org/2010/06/elevator-button-problem.html

---

> **randallsquared** · 2026-07-31T17:11:23.000Z　
> If you optimize for initial wait times, someone who is going to a floor not usually visited might effectively get trapped on an elevator which shuttles between more trafficked floors to reduce wait for elevators overall. Maybe this is very unlikely in practice.

---

> **cpuguy83** · 2026-07-31T17:14:01.000Z　
> Enjoyed the read, thanks!Beyond the content, the font, style, etc made it a pleasant experience for me.

---

> **mallory854** · 2026-07-31T17:15:45.000Z　
> This is super interesting. I've always wondered how the complicated things work!

---

> **mallory854** · 2026-07-31T17:16:20.000Z　
> Super interesting. I've always wondered how exactly they work.

---

> **pwython** · 2026-07-31T17:27:06.000Z　
> I was on a Royal Caribbean ship a couple weeks ago (Utopia, 18 decks, 5,668 passengers). It has 24 main elevators split between front and back, left and right. So a bank of 6 in front of you each time you needed a lift. You press your floor on a touchpad and it assigns you an elevator A through F.I swear no matter if it was busy or not, it seemed like everyone was assigned to the same one or two elevators. The wait was always so long too, I used the stairs most of the time if just going <6 flights.Someone besides RCCL needs to study that algorithm.

---

> **ivanjermakov** · 2026-07-31T17:27:46.000Z　
> I don't think it was mentioned, but the algorithm would be different based on the behavior of the majority. In some buildings most traffic is either up from lobby or down to lobby, e.g. it's very rare for people to go from floor 5 to floor 6. In some it's the other way around, where majority of moves don't involve lobby.

---

> **duderific** · 2026-07-31T17:37:00.000Z　
> We used to do this as an interview question at my current job. We didn't expect people to solve it necessarily, and we just specified to solve for a single elevator car. We just wanted to see how people would break down the problem.Even at that relatively reduced level of complexity, it's quite tricky to figure out how to prioritize who gets served when.

---

> **kazinator** · 2026-07-31T17:37:48.000Z　
> Over the years, I've witnessed numerous instances of poor elevator behavior:- Two elevators ascending and descending in near lock step, in a two-elevator building, effectively reduced to one elevator.- When going in a different direction from the requested one (e.g. called elevator to go up, but actually going down), the doors wastefully close, open and close again. Seen this in many elevators.- At 3 a.m. you take the elevator to a parkade, like to get something from a car. When you return to the elevator a minute later, it is gone; it spontaneously moved away even though nobody is using it but you.

---

> **yread** · 2026-07-31T17:47:17.000Z　
> Our elevator doesnt stop for people who called it after it started on the way up. It only picks up people on the way down

---

> **Aunche** · 2026-07-31T17:49:07.000Z　
> Our building installed destination dispatch system to their elevators and it seems to help overall. However, it breaks when say a team wants to get lunch together, but only one person presses the elevator button. The elevator thinks that it can keep on accepting new passengers so it stops at floors even though it's already full.

---

> **psadri** · 2026-07-31T17:55:43.000Z　
> Aside for the algorithms and how well they work, there is a psychological aspect to how people perceive "wait" times. It turns out just waiting is very annoying. But having people do anything during that same wait period → perceived as progress → not upset.An example iirc was waiting for luggage at the airport. It takes min of x minutes for the first bags to show. In one version, passengers went directly from the gate to the luggage carousel and waited x mins for the first bag → unhappy. Then the airport decided to add a long, round-about "walk" path from the gate to the luggage area that burned some of those minutes → same total "wait" but happier passengers.

---

> **JoshTriplett** · 2026-07-31T17:57:01.000Z　
> > This counterintuitive result is all thanks to the rebalancing step where every 5 seconds, the system re-optimizes each elevator's path. The kiosk enforces rigidity, you must get in the assigned elevator.Sounds like destination dispatch would work better if it didn't tell you which elevator to get into until the elevator arrived.EDIT: already being discussed in the thread at https://news.ycombinator.com/item?id=49125423

---

> **DoneWithAllThat** · 2026-07-31T17:59:30.000Z　
> Having gone to many large furry cons(notoriously brutal on the elevators due to how much floor-to-floor traffic there is compared to other usage) I’ve seen these algos basically completely fail to adapt to unusual patterns. I once spent over half an hour on checkout day, in a hotel with 8 banks, to even have a car stop on our floor at all. Can’t really blame the algo for such a unique situation and at the end of the day a saturated system is a saturated system and nothing can be done to make it fast, but it’s always interesting to witness when a system is completely unable to accommodate a demand like that.(In the example above we gave up and decided it was cardio time, five laps up and down 14 flights to escape with all our luggage.)

---

> **Quantumhunk** · 2026-07-31T18:00:24.000Z　
> This is cool, but wondering which tool was used to build those animations?

---

> **cyanregiment** · 2026-07-31T18:04:17.000Z　
> Level 1: Elevators, load balancing (1D arrays)Level 2: Traffic lights, graphics (2D arrays)Level 3: Flight control, simulations (3D arrays)Level 4: Satellite tracking, virtual worlds (4D arrays)...So many problems can be cast to arrays to be solved with various linear algebra.Considering LLMs are "Level 1000+" puzzles in this analogy, I wonder if every problem could be represented by an n-dimensional vector and solvable with algebra.They at least make great interview questions - Tic-Tac-Toe is commonly given, but is obvious. The board already "looks" like arrays. The less obvious ones, like elevators (or load balancing), are always interesting.

---

> **the_cosmos** · 2026-07-31T18:11:21.000Z　
> Ahhh brings back memories of "Elevators from Hell" [1]Now maybe I can beat that game!1. https://www.dosgames.com/game/elevators-from-hell/

---

> **arm32** · 2026-07-31T18:15:33.000Z　
> My autism just went KABLAOW when seeing this. I know what I'm doing the next hour.

---

> **oxag3n** · 2026-07-31T18:15:55.000Z　
> User experience is not always correlated with metrics targeted by engineers.I visit a building sometimes with destination dispatch elevators, and with low exposure across multiple years I'm confused every time the elevator I need to take is open behind me.I once used the paternoster lift in Germany, beats any elevator algorithm efficiency because it's a non-stop "conveyor" with no doors. I still get nightmares about that elevator.

---

> **tegling** · 2026-07-31T18:22:32.000Z　
> One case not covered, I believe I saw at London Heathrow was where 4 cars essentially moved people across only 2 floors. With only 1 centralized button, only 1-point-something car was effectively moving people on average, because people had to wait for the currently filled car to have its doors closed and starting to move, before hitting the button to call the next car to pick them up. Imaging 100-200 people in line and, often, overly eager would-be elevator passengers hitting the button too early. Thus leading to halting the just filled car and doing an additional full open and close doors cycle. Fun stuff!

---

> **efields** · 2026-07-31T18:25:36.000Z　
> This is like the how it’s made of a website. I could read and click through an endless amount of these kinds of explainers.

---

> **cush** · 2026-07-31T18:32:59.000Z　
> This is a fun simulation to play with. One variable I appreciate in efficient elevators is how the doors work. Usually they don't let you press the button to open a closing door - effectively delaying an already departing car

---

> **supportm** · 2026-07-31T18:37:47.000Z　
> The animation is really cool, how did you make it?

---

> **crabbone** · 2026-07-31T19:07:53.000Z　
> The question about designing elevators used to be the mainstay of programming job interviews. I had an annoying interview where I was asked, for the umpteens time to design an elevator. I already made up my mind at the time, knowing I'm not going to work for the company, but decided to have a... unexpected approach.So, for instance, I didn't measure the elevator's efficiency in the wait time. I included (weighted) travel time. I assumed LOOK algorithm was used. And then when I tried to calculate various outcomes for different trips I suddenly realized that elevator's efficiency and fairness seem to go different ways.Without trying to reproduce my evaluation system, here's my finding in fewer details: if you have two passengers, one going from the ground floor to the top floor and other joining for the shorter ride down in the middle, then the elevator that makes a "detour" is more efficient, but it hardly seems fair that the passenger traveling ground floor to the top should go even a single floor in the opposite direction.Somehow, until that point, I lived with an illusion that the most efficient solution to a problem must be the most fair to every participant. Discovering this counterexample sent me on the "tour of discovery" of ethics and different philosophers who contributed to it... and while in the end it made me none the wiser, I'm happy to have discovered this field.

---

> **salberts** · 2026-07-31T19:21:17.000Z　
> Our elevator (4 cars) displays above each car the planned stops and can change mid-wait the car<>floor allocation and issue sound indication. I’d expect it to be allow optimal allocation.

---

> **userbinator** · 2026-07-31T19:28:08.000Z　
> It's worth noting that for roughly half of the last century, elevators were entirely controlled by relays, with no computers at all; these algorithms would be implemented in hardwired logic. Look at Otis' old patents for some interesting details, including schematics.

---

> **hagen8** · 2026-07-31T19:35:28.000Z　
> Most importantly, after entering the elevator. First press the close button and then the floor. That way u, safe the time of pressing a button as the door is already closing.

---

> **jabroni_salad** · 2026-07-31T19:56:47.000Z　
> This was fun to read and play with but I'd like to see it with different usage patterns, too.The simulator seems to have passengers spawning on a random floor and then transiting to a different random floor. But for where I work, the trips are pretty much always from the lobby to a floor, or from a floor to the lobby. Nobody goes inbetween floors except maybe the cleaners.

---

> **danso** · 2026-07-31T19:59:53.000Z　
> Oh wow, this is perfect reading for me. One of my first college career fair questions was "Tell me how you would program an elevator". Forgot what sad attempt at an answer I gave, but I pretty much thought about that algorithm every time I've ever waited for the elevator. Which was pretty much daily when living in NY.

---

> **brudgers** · 2026-07-31T20:03:09.000Z　
> The elevator rabbit hole:Deviant Ollam on Elevator Hacking
> https://youtu.be/ZUvGfuLlZus

---

> **abhaynayar** · 2026-07-31T20:13:36.000Z　
> I have destination dispatch at my office, and while I don't like my personal user-experience of it, I can't imagine what would better suit a building when you have so many elevators in the same place i.e. in my case 10+ I think?What I find annoying though is you clunkily go click a floor then clunkily wait then clunkily walk over to the elevator assigned which may or may not be on the other end of the space. Also another interesting thing I've seen is that it seems in my case the distance from destination selection and elevator assigned seems to reduce at times when the office is emptier so that too seems to def be accounted into the algorithm.

---

> **besil** · 2026-07-31T20:22:09.000Z　
> I currently work in one of the top global incumbent company in the elevator market in R&D software.I would have never thought there were so many challenges behind a car moving up & down.This industry is so niche and peculiar.Elevator trip scheduling is one of the many challenges. Really a great experience so far

---

> **oeitho** · 2026-07-31T20:24:25.000Z　
> I am wondering where these more complex elevator algorithms are deployed, because I never see them.I was recently at a Radisson hotel in Germany where I was tried to summon an car, but none would appear for a long time. I believe that someone was keeping the doors open on their floor to wait for someone. The fact that all the other elevators were passing by in both directions was actually a bit infuriating as well.At that moment I really wished for an algorithm that would recognize when an car spent a significant amount of time on one floor and then reassign the other floors to a new elevator.

---

> **Bossie** · 2026-07-31T20:29:37.000Z　
> Every time I enter an elevator, I wonder whether it will be the first one I've come across that supports deselect.

---

> **tintor** · 2026-07-31T20:38:11.000Z　
> I am amazed how in US closing elevator doors switch to opening if someone touches the door edge. This results in abusive behavior of people intentionally jamming their arms in the path of closing doors, and delaying everyone else inside the stopped elevator.

---

> **vova_hn2** · 2026-07-31T21:05:11.000Z　
> > What if the nearest car is full?I wonder how do elevators find out if the car is full or not.I once been to an office building where it obviously didn't work properly.I needed to get down from a pretty high (15+) floor to the bottom during the evening rush.The elevator got full immediately but still stopped almost on every floor on the way down.Each time an awkward scene ensued: a huge crowd of people outside elevator just standing and looking at the crowd in the elevator. Everyone has to just wait pointlessly.

---

> **hahahaa** · 2026-07-31T21:07:58.000Z　
> Love the article.> The state of the world 30sec after you called your elevator might be very different but the system is unable to adapt. Turns out the loss in flexibility is not worth the extra information for the optimizer.Very interesting. I am on a 30 flr 8 car today so guess it made sense for Destination Dispatch. It does mean there is rarely a full elevator and usually 3 stops max allowing it to go fast to high floors.Other things I thought could factor in elevators is shopping trolleys: both customers and trolley collectors. One level will have people coming in with full trolleys and almost always the other levels will not. I don't think elevators really care they just fill up and you need to call another one.Also prams but they are 2-way.

---

> **gwbas1c** · 2026-07-31T21:10:04.000Z　
> > Not all elevators have buttons in them. Some of the fancy new elevators have a kiosk on each floor that allows you to specify what floor you're heading to before the elevator even arrives. The kiosk then points you to which elevator you should wait for.I stayed in a hotel with these. It was horrible. Most people didn't figure it out, would get in the wrong elevator, and just get lost in the building.

---

> **m463** · 2026-07-31T21:12:43.000Z　
> I'd like to see skyscraper elevators simulated, not just a few floors.They have to be built a certain way, and need super fancy dispatch algorithms.

---

> **frizlab** · 2026-07-31T22:02:20.000Z　
> I’m surprised to not see any reference to the Happy Vertical People Transporters from The Hitch Hiker’s Guide to the Galaxy!Them elevators are able to see into the future to be there even before we call them. Come on!

---

> **ncr100** · 2026-07-31T22:09:18.000Z　
> Next time please add a cool potted plant that appears whenever you open a door, for the final full sim at the end of the article. Decorative plants for the win.I love this by the way.

---

> **tuetuopay** · 2026-07-31T22:11:38.000Z　
> Meanwhile, the elevator at my apartment building: hey only one floor at a time can call me! And no queueing, you must wait for me to be idle for someone to call me. (And yes, often someone beats me and presses the butter faster than I can).

---

> **pkstn** · 2026-07-31T22:20:38.000Z　
> https://elevators.ltd

---

> **danfunk** · 2026-07-31T22:30:32.000Z　
> AI use in the creation of this article is inconsequential. There is obvious joy and high fidelity information here. Perhaps some vibe coding made the animations easier to develop, and made it possible to produce this in reasonable time. Who cares. Love of craft is evident. What more proof do you need that this is worthy of human attention?

---

> **nhhvhy** · 2026-07-31T22:31:11.000Z　
> If you feel like going down an elevator rabbithole, Deviant Ollam has quite a few talks/videos about all sorts of niche elevator stuff. My personal favorite: https://youtu.be/ZUvGfuLlZus

---

> **ericmcer** · 2026-07-31T22:36:57.000Z　
> I used to access locked floors in my old office building by using these algos.Just ride to the floor I have access too, stay in while the doors close, and it would take me to a random floor. Push open door and voila I was on some random corporations private floor.

---

> **Wowfunhappy** · 2026-07-31T23:00:53.000Z　
> All I want to know is why the heck I can't un-press a button I pressed by accident. This should be very simple. Press once to turn the button on, press again to turn it off.Or I guess you could do long-press to turn off or something if you're worried about confusing people, but I really don't think that should be necessary. We know how toggles work. The button lights up when it's on.

---

> **jhaile** · 2026-07-31T23:08:45.000Z　
> For a long time, this was one of my favorite interview questions - it is one of those problems that no candidate will ever fully solve, but you see how they think through problems. And it is a problem that seems simple at first but has layers of complexity that peel back like an onion - just like this article does.

---

> **rrvsh** · 2026-07-31T23:19:15.000Z　
> Yeah, intuitively the request floor instead of up-down paradigm always seemed inefficient. However, if the issue is that it forces a single elevator and doesn't allow reoptimisation, I wonder if there's a middle ground where instead of up down there's a button panel for the floors, but you still just take whatever elevator's going up? It technically wouldn't require double work but kind of feels like it does psychologically - anyone seen prior work on this?

---

> **agentultra** · 2026-07-31T23:29:04.000Z　
> Simulating Elevators in TLA+ is a fun exercise.https://github.com/tlaplus/Examples/blob/master/specificatio...Another interesting, and underrated one: hotel keys.

---

> **duncangh** · 2026-07-31T23:44:04.000Z　
> “The elevator did hear you, it just has a lot to think about”Didn’t anticipate that my day would be bookended by relating to and empathizing with the plight of the elevators while I wait for one in a tall corporate building.Pressed the kiosk some time ago but watching the sun begin to arc towards setting it does appear the world can change a lot in 30 seconds.

---

> **ed_mercer** · 2026-08-01T01:13:24.000Z　
> Elevators drive me crazy. One of the worst sins I've seen is an elevator that says, “Sorry to keep you waiting,” while continuing to hold the doors open for the entire sentence. Just be quiet and close the doors already.

---

> **rrr_oh_man** · 2026-08-01T01:31:22.000Z　
> > Another metric you can track is journey time, how long you're actually waiting in the elevator before getting to your floor. RSR and LOOK have different characteristics here as well but that's beyond the scope of this article.AAAAAAAAAAAH. WHY.

---

> **cyberrock** · 2026-08-01T02:04:41.000Z　
> Very cool. I would be curious how elevator banking (elevators split into different floor ranges) and double decker elevators impact this.

---

> **nuker** · 2026-08-01T02:07:08.000Z　
> Why not count people waiting on each floor? To add to the algo? A simple camera with basic computer vision will do.

---

> **andrewseanryan** · 2026-08-01T03:03:46.000Z　
> As I step into an elevator, I often think about the algorithm that's driving it. Now I know what they are! Thanks!

---

> **sltkr** · 2026-08-01T03:07:41.000Z　
> Reminds me of this little game, where you have to code your own elevator algorithm: https://play.elevatorsaga.com/

---

> **sghiassy** · 2026-08-01T03:09:15.000Z　
> As a software engineer who lives on the 58th floor this is gold!!

---

> **mr_wiglaf** · 2026-08-01T03:27:56.000Z　
> My first thought with optimizing the elevators was to optimize where the elevator went when it was empty. Surely sticking around at the top floor decreases avg wait times, no? I feel like I've been in buildings where the elevator returned to the lobby after use (but perhaps there was always another person waiting...)

---

> **perilunar** · 2026-08-01T03:33:47.000Z　
> It's a pity that paternoster lifts are so unsafe [0] — we could avoid all problems to do with scheduling if they were safer.On a related note, could someone please design continuous spiral escalators with horizontal sections at each floor?0: https://en.wikipedia.org/wiki/Paternoster_lift#Safety

---

> **FabHK** · 2026-08-01T04:29:37.000Z　
> Wonder what would happen if the objective instead were to minimise sum of quadratic wait times (ie, penalise long waits explicitly).

---

> **hoten** · 2026-08-01T04:54:21.000Z　
> Elevatorpedia is a fun read. I particularly enjoy reading about service modes, such as the Sabbath service (hands-free operation).https://elevation.fandom.com/wiki/Sabbath_service_(SHO)

---

> **grishka** · 2026-08-01T05:13:45.000Z　
> How often do people travel between non-ground floors though? In my own experience, whether it's a residential or an office building, 99% of elevator usage is a) someone going down to the ground floor, and b) someone going up from the ground floor. There are some exceptions like hotels that have amenities on different floors though.The first elevator "algorithm", if you can even call it that, that I've ever encountered and that seems intuitive to me, is what Soviet relay logic elevators did. If it's not in use and someone calls it, it goes there. If it's in use, it will collect the calls on its way down (and ignore them on the way up, these had no up/down call buttons). It's surprisingly effective for apartment buildings.

---

> **elisbce** · 2026-08-01T05:22:32.000Z　
> This article didn't consider two very important optimizations: 1. Odd-even split with all-floor backup. 2. Low/High floor split.

---

> **woeh** · 2026-08-01T05:41:21.000Z　
> I am currently staying in an AirBnB of a 60 floor tower, and the three elevator shafts definitely cannot handle this (I don't think the building was designed with renting to tourists in mind). The elevators are frequently completely saturated during weekends, meaning that the elevator stops at each floor, but noone can get in because the elevator is already full. This means the backlog of people wanting to use the elevators is increasing until after rush hour, and I have at one time experienced a waiting time of over half an hour.What I take from this is, elevators need a proper check to see if they are full, and if so skip floors.

---

> **Himanshu_942** · 2026-08-01T05:41:40.000Z　
> Finally someone looked at frustrating problem. What if lift manufacturers install all the algos and change the algo based on need?

---

> **baxtr** · 2026-08-01T05:44:00.000Z　
> I have never understood why it’s not possible to deselect a floor once you’ve pressed the button.

---

> **thenoblesunfish** · 2026-08-01T06:08:35.000Z　
> Fun! I hate those new kiosk style elevators, because I can't reconfirm that I actually pressed the button, remember which one I am supposed to wait for or press the button again while I'm waiting to make sure I really pressed it. Also don't like that I can't change my mind inside the elevator. All in theory not problems if you were a rational person and the system WAI but I am not and things like elevators rarely do. The up/down buttons are more brainless and I like that. Interesting to hear that they might not even be more efficient!

---

> **sorz** · 2026-08-01T06:22:57.000Z　
> I just come back from a furry con hosted in hotel in China, and learn how every furry con like this completely break hotel's elevators:- rooms are all booked- young furries usually share one room with 4 or even up to 6 friends- more guest room-lobby-ballroom traffic- far more inter-guest-floor traffic than their usual tourists- one full-suit furry take 1.5-2 human's spaceTheir elevators are not designed for this scenario and got overloaded all the day. Queueing for tens of minutes is not uncommon.

---

> **ChuckMcM** · 2026-08-01T06:28:59.000Z　
> The "Elevator Problem" (and the "Street Light Problem") were both CS 200 exercises when I was in college. Along with a bunch of other 'game' type systems like 8 queens, Hanoi towers, maze solving, etc. Still, that is the most elegant web widget I've ever seen that illustrates the options. If you're reading this John I'd love to hear how you wrote them.

---

> **stkni** · 2026-08-01T06:40:43.000Z　
> Great analysis! I used to ask a fairly open ended elevator system design question for engineering interviews. There is a lot of mileage in this topic and everyone has an understanding of the basics so the setup costs for the question are minimal. Always generated a lot of interesting discussion.

---

> **altairprime** · 2026-08-01T06:50:39.000Z　
> This is pretty cool. OP+author, I wish that it was possible to gray out the elevators as the speed increases, so that their high-contrast "flashing" is reduced while still allowing their movement patterns to emerge. You could even go as far as to fade their color back in once they're standing still, so that the 'stop' locations in the LOOK vs RSR diagram become really clearly apparent, while the elevators' non-stop movement fades into the woodwork as orange dots travel endlessly in the left.I figure something like a simple weighted ratio of car color = { 1.0: car fg color, max(1,speed^0.1)-1: shaft bg color } would do, so that 2x only shifts the color 7% towards the background color, but 500x shifts the color 86% towards the background color — and a stationary elevator can fade in from 86% bgcolor to 0% bgcolor over a few ticks as it sits there.I recognize that for most of us, the flashing elevators blur into motion blur, but I can see individual frames at 120fps and while I am not seizure-sensitive to high-contrast flashing, I imagine those folks would appreciate you going the extra mile to reduce contrast at higher velocities, too.

---

> **pavinjoseph** · 2026-08-01T06:52:48.000Z　
> Surprised that the LOOK algo beat RSR in the final sim!

---

> **senthilnayagam** · 2026-08-01T07:18:19.000Z　
> wanted to create a lift simulator for a very long time, this looks pretty good.claude could recreate it in unity in about 10 minutes. now ticked it off my "want to code" bucket list.

---

> **krishna180** · 2026-08-01T07:54:24.000Z　
> An elevator that stops at every other floor is quite annoying. Someone pressed a button and then entered another elevator. just like in door, there shall be a sensor as well that will check if someone is waiting outside or not. if not, please pass that floor.

---

> **npodbielski** · 2026-08-01T08:00:07.000Z　
> How people do such nice animation? Is there is some nice program you can use? I looked and I could not find anything that seemed really easy to use. Llms can sometimes generate something usefull and sometimes something attrocious. I remember few months back article where someone create animation of how 3.5" 1.4MB disk is build, somebody asked about this in the comment and author said it was done mostly by hand. While this is impressive it would be cool to be able to draw some animation for work prestnation that looks nice but also so I do not have to spend 3 days crafting something like that. Would be nice to draw few of them in my blog too. Any recommendations?

---

> **gregorvand** · 2026-08-01T08:36:26.000Z　
> Amazing article and demos thank you. I’ve also been fascinated by what algorithms are driving elevators.As someone often using destination dispatch, I am inclined to think after the elevator arrives, you get to the destination more quickly than RSR or LOOK because it’s optimised everyone to the same floor (less stopping)So it may be a case of more waiting in the lobby but less in a claustrophobic box, which I’ll happily take

---

> **NikxDa** · 2026-08-01T08:38:48.000Z　
> My biggest issue with elevators is that some places and hotels I‘ve been to use disconnected systems:They have three elevators, but pressing one button only calls that specific elevator. So everyone presses all three buttons, meaning the three elevators basically turn into one.I don‘t understand how this was ever signed off, but I‘ve seen it multiple times now...

---

> **pavlov** · 2026-08-01T08:50:54.000Z　
> One of the best-loved Maxis games of the 1990s was SimTower which was all about designing elevator flows for your skyscraper.It might be fun to revisit. The game was actually of Japanese origin.The Digital Antiquarian just wrote about it the other week:https://www.filfre.net/2026/07/the-life-and-times-of-maxis-p...(Part of an ongoing multi-part Maxis article, SimTower is halfway down in this part 2.)The origin story:”As Yoot Saito would be the first to tell you, the rest of the game was really born out of his odd fascination with elevator systems.> ’Late one night, I was waiting in my building’s lobby for an elevator. There are two cars in my building’s shaft. I pushed the button, but instead of the closest car coming to my floor, the farthest car arrived first. In my usual questioning way, I asked myself, “What happened here? How are these cars logically synchronized?” That was the beginning of SimTower.’

---

> **dsego** · 2026-08-01T08:51:06.000Z　
> In my residential building we have two elevators, a big one and a small one, the small one can fit 3-4 people if they squeeze together, it can't fit a bicycle. And of course, they don't work independently, so if the small one is already on your floor the big one won't stop there, so if I have my bicycle with me, I need to send the small one to a higher floor first, and since people are using the lifts constantly, sometimes I need to wait for a while and repeat the same process. There were times where the small car came several times before I managed to stop the large one.

---

> **TeMPOraL** · 2026-08-01T09:42:29.000Z　
> Elevators are, in a way, a heap of social and psychological problems stuffed into a box that moves up and down a lot. The article briefly acknowledges it, but like ~all such articles I read over the years, it's primarily interested in wait time and focuses on which quantile to minimize and how. But I'd love to know if and how the soft, squishy thing is being accounted for.The core problem: elevators are frustrating for many reasons, and that frustration often manifests as hidden blame and hate towards other fellow passengers. Like, IDK, I'm sitting there with a stroller and a kid on floor -1, trying to get to the train platform at floor 0, but the elevator isn't coming because it's going back and forth between 0 and 2 and 3, as people who came by cars shuttle their luggage to and from the parking lot. As a city dweller and non-car person, I can feel my hatred towards cars and drivers bubbling up right there.I imagine the same is felt by them if I manage to snatch the lift and go from 0 to -1, when they'd really love to already be on +2.There's many other cases. Mall problems are different than train station problem, different than tall residential building problems, different than office building problems. Destination Dispatch is its own special thing, with its own special psychological twists. But two things I observed in general are:- If there is a control element available, you will blame people for using it (even internally). Like, "I'd be there a minute ago if not for this damn XYZ who just had to press the button at exactly this time, and they weren't even going in this direction!"- If there is an indicator element available, people will optimize around whatever it shows.Like, someone gets at floor N, sees most of the buttons between there and their destination M lit up, immediately presses N+1 to get off there and call another elevator. But if the buttons are visible enough from outside the lift, they may just not get in in the first place, saving themselves and the others time and trouble, etc.The more I think about it, the more I see that placement of buttons and indicators in the lift is in itself an UX engineering problem with unusually high impact of every decision on well-being of the users.EDIT: Also ironically, and in line with my feeling that Star Trek got more things right than people give it credit for, a lot of elevator problems - both scheduling and social/psychological ones - would be solved if elevators just moved faster, like 2-4x faster than now, and also in some cases, also moved sideways. I.e. turbolifts.(That, and if it didn't immediately led to the building owners putting less of them. So put another way: frustrating lifts is the sign of building owners/designers cheapening out.)

---

> **newswangerd** · 2026-08-01T12:00:31.000Z　
> I have an old iPhone SE and I want to give you kudos that the animations run buttery smooth on this page. There are a lot of websites where just the ads will cause my phone to completely freeze.

---

> **larrydag** · 2026-08-01T12:16:36.000Z　
> Discrete event simulation frameworks, like SimPy, are a great mathematical way to simulate the environment if wanting to discover better methods of any methodoical staging flow. Elevator scheduling is one example that can be simulated.https://simpy.readthedocs.io/en/latest/

---

> **nubg** · 2026-08-01T12:21:46.000Z　
> > The simplest elevator algorithm is called SCAN and was patented in 1961. The elevator starts at the lobby and goes all the way to the top floor before reversing and coming back down. It picks up and drops off anybody on the way.Patents, everybody...

---

> **theodorejb** · 2026-08-01T13:38:50.000Z　
> The worst situation I've encountered is after a large conference when everyone is leaving the hotel at once. An elevator quickly fills up on the way down, but then wastes time stopping at every subsequent floor with a call, even though no one else can fit inside. At each floor the elevator stops, the doors open, the waiting people see it's already packed, the doors close, and this repeats on the next 15 floors before finally reaching the bottom where everyone gets off. If the algorithm could know an elevator is completely full and only stop at its destination floors rather than every floor along the way with a call, it would be far more efficient.

---

> **ladberg** · 2026-08-01T13:45:19.000Z　
> One elevator feature I specifically noticed at Apple Park but haven't seen anywhere else: elevator prefetching to the ground floor.I.e. in a bank of 2 elevators where one is resting on ground and the other is resting on a different floor, as soon as someone calls the ground elevator (which is already there and immediately opens) the other elevator (if idle) will move to the ground floor so that there's no delay the next time someone calls one from the ground floor.

---

> **alightsoul** · 2026-08-01T14:14:16.000Z　
> a lot of autistic people like trains or elevators

---

> **airbreather** · 2026-08-01T14:37:40.000Z　
> Great article.Where I live, on the taller buildings it is common to have banks of elevators which only service certain floors, eg floors 2:25 and 26-50 are two different banks of elevators.Some modern elevators have two cars per shaft, imagine scheduling that.

---

> **pbrum** · 2026-08-01T14:53:13.000Z　
> Awesome article. This being HN there must be a quibble right?:Missed opportunity to entitle it "Elevator Action"

---

> **vivzkestrel** · 2026-08-01T15:43:47.000Z　
> - epic rap battles of history- john.fun vs neal.funnnnnnnnnnn- who woooon? you decide!!!!!!

---

> **MostlyStable** · 2026-08-01T16:17:43.000Z　
> Given that there is already a simulation, with very clear performance metrics, I wonder if anyone has ever tried making an evolutionary algorithm and if so, how well it would perform. Do we have any idea of how a theoretically perfect algorithm would perform? How much theoretical performance is there to be picked up?

---

> **toplinesoftsys** · 2026-08-02T05:58:11.000Z　
> This is a great food for thought next time I am waiting for elevator :)

---

> **josefrichter** · 2026-08-02T14:36:41.000Z　
> Fabulous! I studied Air Traffic Management. Kinda like Lift Traffic Management, just with airplanes :-)

---

> **davidscoville** · 2026-08-03T19:13:55.000Z　
> I’d like to know about algorithms that determine where elevators “rest” during downtime. In the morning maybe all rest on the ground floor. Then perhaps during midday lunch rush, some elevators rest at an average floor of where most people got off in the morning. In the evening when people go home, maybe most elevators rest higher up where most people are.

---

> **CodeCompost** · 2026-08-04T09:01:40.000Z　
> Thanks for this. I've been thinking about something like this as pertains to energy use. Which algorithm is the most energy efficient? I'm actually quite curious.

---

> **neutronicus** · 2026-07-31T16:04:52.000Z　
> They might have other objective functions like wear-and-tear on the elevators, total energy usage, or something

---

> **dbcurtis** · 2026-07-31T16:55:06.000Z　
> I have done several third-party elevator integrations (software that talks to the elevator controller) for coordinating other equipment with the elevator. One thing that always struck me once I had full visibility into the location and motion of all the elevator cabs is how busily they are scheduled. Waiting in the elevator lobby for a cab seems to take forever, but viewed from the dispatch side, it is a flurry of activity and cabs are rarely idle during any hours the building is normally occupied. It is easy to nerd out just watching the status panel.Another thing I learned: If an elevator mechanic says: "I'll meet you first thing in the morning." He means something like 4:00AM. They want to get in and out before people start arriving to start their day.

---

> **dbcurtis** · 2026-07-31T16:59:37.000Z　
> One other thing to add: It isn't the elevator scheduling software being obtuse, that software gets a huge amount of thought. But elevators are expensive, and building owners do not over-spend on a whim. Typically, they have just enough cabs (if that) to handle the expected load.

---

> **StableAlkyne** · 2026-07-31T17:16:45.000Z　
> > minimize the amount of wait times between picking up people and taking them to their destinationI wish elevators accounted for load.I've been to a couple of larger conferences where on the Monday morning after, the hotel elevator was just hammered. Everyone wanted to go down, and the elevator would dutifully stop on every single floor no matter how full it was. If you were mobility disabled on the 2nd floor, you were basically fucked if you had a flight to catch.One would think that, if it's a 10 person elevator and it's already stopped on 10 floors requesting it, that it could save an extra 5 minutes by just going directly to the ground floor, instead of stopping on every floor with the same conversation of "Oof, can't fit in there. I'll get the next one!"

---

> **SoftTalker** · 2026-07-31T16:52:30.000Z　
> Disk drive read/write algorithms have a lot in common with elevator algorithms. At least they did in the days of physical heads moving across a platter.

---

> **grep_it** · 2026-07-31T16:10:10.000Z　
> I always come back to this game whenever I'm at a hotel for a conference waiting for the elevator.

---

> **perryprog** · 2026-07-31T16:20:38.000Z　
> Wow, I just came here to comment that I've always wondered if a game where you have to program an elevator scheduler would be any fun. I thought surely no-one's thought to make that before, too! Glad to be proven wrong.

---

> **alanwreath** · 2026-07-31T16:23:43.000Z　
> I wish there were more games like this. It’s such a simple premise but so satisfyingly difficult after each level. And it even has a bit of randomish failure which makes for even more challenge.

---

> **emmanueloga_** · 2026-07-31T16:34:02.000Z　
> looks very well made, but I still prefer https://en.wikipedia.org/wiki/Elevator_Action !

---

> **CobrastanJorji** · 2026-07-31T17:25:17.000Z　
> This is great, but to me, the definitive elevator scheduling game was SimTower.

---

> **inkkin** · 2026-07-31T20:42:46.000Z　
> Omg! <3

---

> **vova_hn2** · 2026-07-31T22:27:36.000Z　
> Very fun indeed!Can't believe, that this [0] solution to Challenge #5 actually worked, lolChallenge #6 is "Transport 40 people using 60 elevator moves or less". Unfortunately docs don't make it clear what exactly counts as a "move".[0] https://gist.github.com/vovanz/66e4396934ac656a8f8c32fcee43d...

---

> **lmazgon** · 2026-08-01T04:23:10.000Z　
> A few years back I made a CLI game in Go where you have to schedule elevators - https://github.com/lovromazgon/elecrash

---

> **LordOmlette** · 2026-08-04T16:53:01.000Z　
> This is what I immediately thought of when I saw> How do you actually measure how good an elevator algorithm is?

---

> **marcosdumay** · 2026-07-31T16:03:25.000Z　
> > people in the lobby during the morning rush who would shepherd people into particular elevatorsThat's what the no-button elevators with the kiosk does.

---

> **socalgal2** · 2026-08-01T09:10:37.000Z　
> According do this video, some of it is I guess regulatory capture? (my memory of that video might be bad)https://www.youtube.com/watch?v=Or1_qVdekYM

---

> **urbnspacecowboy** · 2026-07-31T18:39:02.000Z　
> And there's still no adequate explanation for what "Korean lunch mode" is!

---

> **b3lvedere** · 2026-07-31T16:14:53.000Z　
> I had another game in mind.https://archive.org/details/elevator_nes

---

> **Sohcahtoa82** · 2026-07-31T16:34:37.000Z　
> If you liked SimTower, Project Highrise is worth taking a look into.https://store.steampowered.com/app/423580/Project_Highrise/

---

> **wlesieutre** · 2026-07-31T17:47:24.000Z　
> A fun tidbit about Sim Tower:> After my lecture, a Maxis employee who shall remain nameless buttonholed me. "You guessed right," she said. "Sim Tower was built around a real elevator simulation program we bought from a Japanese guy."https://web.archive.org/web/20090916193335/http://www.gamasu...

---

> **dillutedfixer** · 2026-08-01T01:53:55.000Z　
> If you want a trip down memory lane, go to InfiniteMac.org, spin up a System 7.5 emulator, go to the InfiniteHD/Games folder and launch SimTower!! Such a fun blast of nostalgia. I loved the game as a kid and can still very much enjoy it as a mid-40 year old.

---

> **mapmeld** · 2026-07-31T16:10:26.000Z　
> My apartment building is replacing the elevators, and someone on staff revealed that the first renovated elevator is intended to pick up only from the lobby (i.e. if you summon an elevator from the 10th floor, one of the others will come). This has caused some grumbling or calling it an "express elevator". In an apartment it really is mostly trips to many floors from the lobby. The only time this maybe would be inconvenient might be in the morning commute, when fewer people are re-entering.

---

> **quietsegfault** · 2026-07-31T16:07:36.000Z　
> What makes me more peeved about destination dispatch elevators are people who aren't used to them, and all pile into an elevator without hitting a floor, thinking one input is enough for everyone. Then, a totally full elevator stops at intermediate floors to pick up callers, but there's no room to get in. If everyone put the floor in as they arrive to the elevator lobby, then the elevator would know how many people are in the elevator and won't overfill them.

---

> **why_at** · 2026-07-31T16:39:07.000Z　
> >Then you also run into visitors that assume it's a normal car and can hit a floor button when the get in, only to realize they've walked into a car without buttons.I work in a building with Destination Dispatch elevators so I'm used to them. I have the opposite problem where I'll get into a normal elevator and just stand there without pushing anything.

---

> **soupspaces** · 2026-07-31T16:08:22.000Z　
> Yes the visualization is great but overused and could also use a stop button. I would have also liked to see different kinds of plots.

---

> **Georgelemental** · 2026-07-31T16:04:50.000Z　
> I don't think I've ever seen someone do that

---

> **trivo** · 2026-07-31T16:07:16.000Z　
> And then when the elevator door opens, they ask the people inside: "Are you going up or down?" There's an arrow showing that, for Christ's sake.

---

> **davnicwil** · 2026-07-31T17:24:18.000Z　
> In situations like this the answer usually comes by flipping it and assuming they do understand, and asking why it makes sense now.It's probably just the old 'fake loader' psychology, to be honest. Waiting without knowing when the elevator will arrive is boring/frustrating, where getting into an elevator that moves, even if the wrong direction, feels like progress.Things are happening, and even if it takes longer ultimately that's a less frustrating state to be in.

---

> **ivanjermakov** · 2026-07-31T17:25:10.000Z　
> Elevator algorithm I'm used to always goes up from lobby and always goes down from any other floor. Meaning that it goes all the way to the highest order and picks orders top-down until reaching lobby. Only exception is going to underground parking floors which is relatively rare in my housing complex.

---

> **gene91** · 2026-07-31T17:47:25.000Z　
> In some places, I see people do that. It’s not stupidity. I learned the logical reason after observations. During busy hours in some busy buildings, there isn’t enough elevator capacity. Therefore, if you want to go down to the ground floor, taking a trip up and then down might be better (a less-bad worst case outcome, or even a better average outcome) than waiting for a non-full downward elevator. In such case, it’s logical to press both up and down.

---

> **vel0city** · 2026-07-31T19:26:47.000Z　
> When you're at a lower floor and you're trying to go down, but its a time period where traffic is trying to leave you can end up in a situation where nearly every elevator going down is already full. So you call for down, cab arrives but is already full, it goes, you call again, another comes, its already full, rinse/repeat. Sometimes there's not much up traffic during that time, so it can be a legit strategy to just go ahead and call on the up and ride it all the way instead of waiting and hoping for space coming down.Although I guess that's not quite what you're talking about.

---

> **qurren** · 2026-08-01T00:41:45.000Z　
> I often enter it in the wrong direction.Like let's say elevator is at 5, I am at 1 wanting to go to 3, and before I arrive there is already someone else at 1 wanting to go to -1.I'll get in with them going DOWN so that it doesn't have to stop a 2nd time on the way up.There are also other situations where I'll press it in the wrong direction if I think it's already likely to stop on the way down (due to me being on a popular floor) to save an extra stop on the way back up.

---

> **donalhunt** · 2026-08-01T08:03:33.000Z　
> I live in Ireland. 10+ years ago I used to the travel to the US quite a bit (5-10 trips a year). The majority of the time I would fly via a major EU hub like AMS or CDG even if there was a direct flight from Ireland.The reason? Other factors that were important to me!Examples:- cost optimisation. I could fly business within company budget rules.- flight time. I highly valued longer flight times between Europe and the US west coast so I got a proper night's sleep when flying east-bound. Doing connections on the east coast often meant quite short transatlantic flights that arrived very early in the morning. Much harder to manage the jetlag.- Product offering. Some of the routes from AMS and CDG had much newer planes and cabins.- Airline alliance loyalty. Given the travel pattern it meant sense to pick an alliance that delivered some value. Irish airlines didn't have much to offer and were much more expensive for a worse end to end product.

---

> **dsego** · 2026-08-01T08:40:49.000Z　
> Yes, same here, in croatia people believe that you need to press the opposite direction to "summon" the elevator, if the elevator is on lower floor they will press the "up" arrow to bring it up to their floor. And then of course when the doors open they will ask "going up or down?", which is ridiculous. When I point out that the ground floor only has the "up" button they just ignore it (hard to unlearn ingrained beliefs).

---

> **newtwentysix** · 2026-08-01T14:44:30.000Z　
> OMG ! This is a huge problem in India. Frustrating.

---

> **mekdoonggi** · 2026-07-31T16:10:42.000Z　
> Also need to make sure you increase the speed going past floors 4 and 13 to avoid bad luck.

---

> **jamies** · 2026-07-31T16:18:20.000Z　
> Thanks for sharing this. I was just commenting about the challenge of making a fun elevator sim game. This looks great -- can't wait to play with it this weekend!

---

> **KomoD** · 2026-07-31T20:36:39.000Z　
> I can’t say I have. The only two times I’ve been frustrated with an elevator were when I was inside one and the doors wouldn’t close, and when someone had pressed the emergency stop, so I couldn’t use it.

---

> **Sohcahtoa82** · 2026-07-31T16:32:48.000Z　
> In the middle or end of the day, yes. In the morning, waiting on the bottom floor is the best.Unless you're a hotel. Then the timing is flipped: Wait in a distributed manner in the morning/mid-day, gather on the floor in the evening.

---

> **rubslopes** · 2026-07-31T16:36:56.000Z　
> Yes! I always thought that, when unused, elevators should distribute themselves along the floors, weighted by the floors that use them the most.

---

> **dbcurtis** · 2026-07-31T17:07:49.000Z　
> Most systems to that. Empty-cab strategy is a programming option in the controller. If all cabs are idle (very rare) they are typically spread out.

---

> **barrkel** · 2026-07-31T16:49:34.000Z　
> Load penalty is part of the Otis RSR algorithm, it's in the article.

---

> **NetMageSCW** · 2026-08-03T23:36:31.000Z　
> Except it doesn’t really work if you play the notes in a different order.

---

> **brd529** · 2026-07-31T16:35:47.000Z　
> As the article says, the problem with destination dispatch is that it 'locks in' an elevator. The passenger gets told at call time what elevator to go to, and it can't change that mid flight. RSR has the advantage that the passenger has no idea which elevator will come, and so RSR can change the elevator they will get in real-time as conditions change. This was an insight I had not considered before reading the article.

---

> **taftster** · 2026-07-31T16:55:40.000Z　
> Yes, it's definitely more likely for an individual already in an upper floor to return to ground than a stop above or below. The people queuing up in simulations don't seemingly get this right all the time.Also the group of people going to or returning from lunch is real as well. The grouping factor happens more at the middle of the day and less at the morning or evening. Primarily because of lunch.

---

> **acomjean** · 2026-07-31T17:36:04.000Z　
> Is it because the criteria is wait time not travel time? Destination dispatch would avoid some extra stops on the trip.I just visited a new building with destination dispatch, so it seems to be still around.My EE roommate in college had to build an elevator circuit as a final problem. It was on a bread board and had a bunch of call buttons and had a motor and a clear disk with black squares so it could figure out where it was…. I think it was the simple algorithm…

---

> **ApolloFortyNine** · 2026-07-31T18:17:02.000Z　
> Surely there's a dataset out there with elevator calls for an office building you could test on, instead of the poor random destination case.Surprisingly, claude failed to find a good one.Also, part of destination dispatch (I'm guessing based on experience) removes the 'stopping on every floor problem', so the real test would be total time including wait at that point I think.

---

> **darkwater** · 2026-07-31T18:17:28.000Z　
> Yeah, and definitely is not the right story for hotels. His premise of "morning traffic mostly from lobby to floors" is completely false in an hotel where you get it both ways due to people going down for breakfast and going back up and the down once again.I see hotels with the kiosk model changing the UI depending on breakfast rush hour

---

> **alexpotato** · 2026-07-31T18:31:15.000Z　
> > - People who are on the ground floor generally travel in large groups to the same destination.I also thought that this is one of the biggest reasons destination dispatch was better.There are even articles about switching to destination dispatch in office buildings or hotels lead to dramatic reductions in wait time.

---

> **dawnerd** · 2026-07-31T18:48:37.000Z　
> Cruise ships that use destination dispatch have been much nicer too. Ships that use the older algorithms are a pain to wait during peak times. Guess plus side you’ll use the stairs more.

---

> **pimlottc** · 2026-08-01T02:31:35.000Z　
> This is case where you need to make sure your test data reflects real-world usage or you end up optimizing for the wrong thing.Ideally a new elevator installation would have a trial period where they record usage and then run it through a simulator like this to determine the optimal strategy for that particular building. And you'd want to re-run it every once in a while as the building tenants/usage changes. I wonder if this actually happens, though.

---

> **richk449** · 2026-08-01T14:17:37.000Z　
> It is almost certainly because of the way the simulation was performed:It turns out these fancy kiosks are in general worse for wait times compared to the traditional good ol' up and down buttons. There are certainly edge cases when the kiosks can win out (extremely tall buildings with 8+ cars per elevator bank) but for the majority of cases, simple up down buttons reign supreme.This counterintuitive result is all thanks to the rebalancing step where every 5 seconds, the system re-optimizes each elevator's path. The kiosk enforces rigidity, you must get in the assigned elevator.There should be no way that only having more information results in a worse outcome. At minimum, you could ignore the extra information, and achieve the same results as using up and down buttons.Seems like the real reason it performed worse in this simulation is that when they implemented destination dispatch, they assigned an elevator at time of request, and had no system for reviewing and updated that assignment.

---

> **account42** · 2026-08-03T09:31:28.000Z　
> Destination Dispatch should also allow you to better optimize total travel time rather than just wait time. Especially in the tall office building case you could have an elevator that skips straight to the top floor instead of having to stop for people to get off people all the time.

---

> **esikich** · 2026-08-01T01:02:52.000Z　
> I can't imagine any elevator just uses a set algorithm. I'm sure after installing, technicians work with facilities for a period to dial it in as every building will have different needs and traffic patterns.

---

> **jasonlarue** · 2026-07-31T17:12:50.000Z　
> Not to mention maintenance means taking an elevator out of service, meaning average wait times go up during that period.

---

> **bherms** · 2026-07-31T17:39:04.000Z　
> We did this in college as well using microcontrollers and leds or something - i forget the exact details. It was super fun

---

> **liesliy** · 2026-08-01T01:59:52.000Z　
> The elevator algorithm → disk scheduling connection is such a perfect example of how CS concepts keep showing up in unexpected places. Same idea, completely different domain.
> It makes me wonder how many other "unrelated" problems we're solving today already have decades-old algorithms waiting to be rediscovered for them. Robot motion planning is basically just elevator scheduling with more degrees of freedom.

---

> **amenghra** · 2026-08-02T08:10:31.000Z　
> It's fun that the same algorithm applies to two different problems. In the disk case, the only unpredictable thing is future requests. Elevators have to deal with two unpredictable things, future requests as well as how long humans take to get in and out of the elevator. So it's doubly fun that the same algorithm works in both cases!

---

> **dbcurtis** · 2026-07-31T17:06:22.000Z　
> This does happen. I also once worked on a destination-dispatch elevator system installed in a high-end condo building (high-end, as in concierge and parking valet for residents). Anyway... the resident's key card would of course automatically call a cab to take them to their unit's floor, but also the security system had entries for things like "dog owner" and "allergic to dogs" so that the DD system would never schedule them together for the same cab.

---

> **sp0rk** · 2026-07-31T17:28:47.000Z　
> This type of system is mentioned in the article under the "Destination Dispatch" section.

---

> **skullone** · 2026-07-31T17:29:03.000Z　
> Possibly to balance the hours on elevator banks. Common in buildings to leave some out of the cycle, since elevator maintenance can be a year out to schedule. Probably much worse out at sea

---

> **kccqzy** · 2026-08-01T02:41:19.000Z　
> I’ve gotten that interview problem! From a French company no less.

---

> **oliv__** · 2026-08-01T02:51:12.000Z　
> I don't see how that's perception then? It was just made inefficient on purpose.If I have to walk to the luggage area 10min and wait another 10min for my luggage it's not the same as if i walk 5min to the luggage area and wait 15min for my bag.Yes, total time is the same but one scenario is acceptable because it feels inevitable and is under control (cannot personally move across space/time faster) the other is not because it feels like it could be improved (staff could unload bags faster).

---

> **ericpauley** · 2026-08-01T11:46:26.000Z　
> This story is shared all the time, but what airport actually did this? I’m not aware of any major US hub that meaningfully delays passenger egress like this.

---

> **tomduncalf** · 2026-07-31T22:02:55.000Z　
> Ha I know the exact ones you mean well, going to the train from terminal 5? I couldn’t have told you what was up with them but they seem very inefficient and there’s always a queue! Thanks for explaining

---

> **socalgal2** · 2026-08-01T09:04:25.000Z　
> Maybe they took their que from Apple. The Apple Store in Ginza Tokyo used to have a 3 floors and the elevator is just set to go 1, 2, 3, 2, 1, 2, 3, 2, 1. There are no buttons. It just goes, whether or not people need it. So if you just missed it it might be going up 2 floors and back down for no one. And of course it was slow and held the doors open 10 or 15 seconds per floorVery form over function.

---

> **hypercube33** · 2026-07-31T18:36:53.000Z　
> There are some awesome hacker talks about elevators on YouTube worth checking out

---

> **slater** · 2026-07-31T20:39:06.000Z　
> That's the case with most elevator doors, worldwide...? If you put your hand in a closing elevator door, it's supposed to open again.

---

> **rconti** · 2026-07-31T21:04:28.000Z　
> I like to think I'm reasonably well-traveled, and I've never seen an elevator NOT do that.However, I think you might be correct about transit systems, where the blocked doors might re-open a small amount before quickly attempting to re-close, to keep the train on schedule and prevent this behavior.

---

> **yossi_peti** · 2026-07-31T21:06:03.000Z　
> The alternative being closing the doors on the person's arm and likely injuring them to avoid a minor incovenience?

---

> **hahahaa** · 2026-07-31T21:09:57.000Z　
> I guess it could use weight. Since it should also refuse to go if overloaded.

---

> **magarnicle** · 2026-07-31T23:05:01.000Z　
> What about jerks un-pressing your button cos they don't want to wait? Passive-aggressive button wars breaking out, escalating to active-aggressive wars...

---

> **ericbarrett** · 2026-07-31T23:18:48.000Z　
> I lived in a high-rise that let you unselect a floor with a double press. Try that next time. Can confirm it's very nice!

---

> **userbinator** · 2026-08-01T02:41:00.000Z　
> In some old systems with buttons that actually pushed in and popped out upon arrival, you can pull them out to cancel your call: https://news.ycombinator.com/item?id=37385826More examples:https://www.youtube.com/watch?v=JzC5Bpz-PkQhttps://www.youtube.com/watch?v=xYtsNxzDR50

---

> **cwillu** · 2026-08-01T02:58:06.000Z　
> The most common control circuit has the button triggering a relay which then powers its own trigger until the circuit is interrupted elsewhere; this isn't compatible with the same button cancelling the call.

---

> **dguest** · 2026-08-01T08:24:09.000Z　
> They had this in Korea when I was there a decade ago!It works fine, but people's reaction on hearing this is always interesting, ranging from:- enthusiasm: that's awesome everyone should do that- skepticism: that seems like a terrible idea, people will un-press your floor and chaos will follow- denial: you didn't see that- cultural / racist: that would never work in  it must just be because Koreans are

---

> **dsego** · 2026-08-01T08:46:26.000Z　
> In some elevators there is a stop lever for emergencies, but I found out it cleared all the selected floors as well. So in my building if I've made a mistake or a kid selected all the floors, I can just flip the stop toggle and reset everything.

---

> **socalgal2** · 2026-08-01T08:59:39.000Z　
> Some elevators do this. It's usually a double tap to clear. THey are less common in the states

---

> **newtwentysix** · 2026-08-01T14:50:48.000Z　
> Double-click to cancel: is there in many of the recent (10+yrs) lifts I've been in

---

> **kccqzy** · 2026-08-01T02:38:05.000Z　
> I thought double decker elevators were a failed experiment. I don’t think anyone is even producing them any more.

---

> **iancarroll** · 2026-08-01T03:39:57.000Z　
> I agree, I have been in a lot of buildings where the elevators have extremely poor performance due to this. It can be 4AM but they are all configured to rest on one floor or something like that.

---

> **Anamon** · 2026-08-01T09:55:46.000Z　
> They're not great for accessibility, either.

---

> **ebtebt** · 2026-08-01T05:33:06.000Z　
> In mine it is far from 99%. I’d say maybe 50%.

---

> **deepspace** · 2026-08-01T05:45:49.000Z　
> It depends on the building use. In residential buildings, people do tend to go to / from ground but in my building the parking garage has entrances on levels 1-4, the gym on 3-4 and the garden on 5. That distorts the traffic pattern.The company where I work occupies an entire office building, so there is lots of travel between floors.

---

> **sixhobbits** · 2026-08-01T06:13:19.000Z　
> Not sure how common it is but Bern train station has 3 elevators, usually 2 are set to normal and one to "express" which means all middle floors (mainly parking) are locked and you can only go ground to top (outside so a lot of people going to/from the station on foot)It's super efficient for people who understand the system at the detriment of people who don't, as they get in and mash the middle buttons and get confused that they don't activate

---

> **noduerme** · 2026-08-01T06:22:06.000Z　
> I was confused by this "LOOK" algo... I'm American and I've lived all over the place, and I'm not familiar with elevators that pick you up on the way up if you pushed the down button. As far as my experience, they only pick you up on the way back down. To the extent that if I did hit the down button and got in and it went up, I'd think I'd gotten in the wrong elevator or there had been a mistake.

---

> **graton** · 2026-08-01T06:22:14.000Z　
> There are also elevators in cruise ships. People get on and off at almost all the floors.

---

> **socalgal2** · 2026-08-01T08:55:53.000Z　
> It's extremely common in an office building I used to work in. The office has 21 floors and people shuffle between them often. Going up or down 1 or 2 floors there are stairs. Also the top 11 floors use different elevators than the bottom 11. They share 1 floor so you can switch

---

> **perpetuallunch** · 2026-08-01T06:42:17.000Z　
> Or, the building / owners corp / code / city could simply ban short stay accommodation where it was never attended.I would not want to be in that building if an evacuation alarm sounded.

---

> **cammikebrown** · 2026-08-01T06:46:23.000Z　
> A 60 floor Airbnb tower? 2026 is wild.

---

> **ehsankia** · 2026-08-01T06:46:28.000Z　
> I don't understand why the fact that it's an Airbnb really matters here? Unless a large number of apartments are meant to be empty, why does it matter if the tenant is short term or long term? Is it that short term users leave and enter their apartment more often?

---

> **Animats** · 2026-08-01T06:55:19.000Z　
> > I am currently staying in an AirBnB of a 60 floor tower.ICE Condominiums Tower I, Toronto?[1]> elevators need a proper check to see if they are full, and if so skip floors.Elevator load measurement is an option you can buy.[2] Somebody didn't.
> 60 stories with three elevators is underserved, and needs all the control help it can get.[1] https://en.wikipedia.org/wiki/ICE_Condominiums[2] https://elevatormotors.com/load-weighing-devices/

---

> **pudgywalsh** · 2026-08-01T09:26:31.000Z　
> > 60 floor tower, and the three elevator shaftsI don't think I've ever seen a 20-story building with less than 4 elevators at a minimum.I've worked in low-rise office buildings with no less than 10 elevators.Seems like that gross deficiency should have been stopped at the city inspector's office before plans were approved.

---

> **appplication** · 2026-08-01T05:46:50.000Z　
> It’s a sensible request, but we just don’t have the technology to do it.

---

> **socalgal2** · 2026-08-01T09:01:56.000Z　
> some elevators have this feature. Double tap a button to de-select a floor

---

> **dguest** · 2026-08-01T08:12:04.000Z　
> I would really love to see a regular a blog that details all the ways the world will need to adapt to furries. There are endless engineering challenges here!Also, any spiritual successors to Sim Tower needs to include furry-con as a disaster scenario.

---

> **kneel25** · 2026-08-02T15:31:32.000Z　
> The heck. If I was in that hotel and the lift door opened to 4 guys in a furry costume, I’d be taking the next one. I’m sure that’d contribute

---

> **Tomis02** · 2026-08-01T08:36:47.000Z　
> Pretty sure this is vibecoded so don't feel too bad.

---

> **Ekaros** · 2026-08-01T10:47:32.000Z　
> Someone cheapened out is my guess. Group dispatch. That is having multiple elevators communicating with each other is added feature or was added box. Don't want to pay the extra. Don't get that feature.In general my understanding is that every single cab is unit that can operate alone separate from any others. Then these are grouped together to operate more efficiently. But this is feature you need to buy. Going too cheap someone might choose not to.

---

> **akoboldfrying** · 2026-08-01T09:13:41.000Z　
> This is hilarious. But I'm also thinking: Maybe just use the stairs? Your bike suggests you aren't afraid of a little cardio.

---

> **LargoLasskhyfv** · 2026-08-03T05:59:38.000Z　
> Put the bicycle on its back-wheel, vertical?

---

> **Neywiny** · 2026-08-01T14:40:24.000Z　
> It would have to be done by weight. If you had a button to not allow stopping for others, people would abuse it. If it was a camera, security issue. Presumably if somebody is moving a piano or something else heavy it'll be fine

---

> **rz2k** · 2026-08-01T14:46:51.000Z　
> There’s also a strategy to jump the line. Say there’s a talk that just took place on the top floor roof deck of a small ~20 floor building. People who don’t want to wait in line with a hundred people, can take the stairs down one level, call the elevator on the way up to enter the car before it is filled, ride it up one level*, and then ride it all the way down to the ground floor.To prevent a riot, the building should probably deploy an employee with a fire key to manually operate the elevator.* Elevators will answer an up button call while it is going to meet a down call from the top floor, but they will answer that call before filling any new down instructions, so you do have to ride to the top first.

---

> **andai** · 2026-08-01T15:17:05.000Z　
> At that point I'd just get out and take the stairs. Race ya!

---

> **wrs** · 2026-08-01T16:49:42.000Z　
> I have seen elevators, usually in a big building with a lot of elevators, that do act that way (presumably using weight sensors?). I’ve read that some elevators also have a “kid mode” that does the opposite: if some kid pushes all the buttons as they leave (just for the lolz), the elevator cancels the calls.

---

> **worldthruword** · 2026-08-01T13:59:37.000Z　
> Branch prediction or Floor prediction. If we know the traffic pattern from past data, we can optimize for it.

---

> **dbcurtis** · 2026-07-31T17:01:22.000Z　
> It's pretty much throughput. The cap-ex of a single cab swamps any other cost, so the only way to reduce total number of cabs is optimizing for throughput.

---

> **cyberax** · 2026-07-31T17:31:58.000Z　
> Modern elevators have regen braking, so they can recover most of the energy spent on going down. Older elevators used braking resistors for that.(BTW, going _down_ while empty is typically more energy-consuming for the elevators because they are counterweighted)Edit: that's also why you shouldn't use elevators in a fire. If the brakes in the elevator machine room fail, the cab won't crash down. It will go _up_, possibly dragging you into the fire. Many firefighters died because of that.

---

> **paradox460** · 2026-08-01T01:16:55.000Z　
> Some older buildings in SF have the old school elevator panels in the lobby, with big vertical displays of all the floors, and a moving needle for each cab, and lights where there were calls. Big beautiful brass monster, polished to a shine. I think it was the flood building. Used to love watching it on my way up

---

> **cruffle_duffle** · 2026-07-31T17:54:34.000Z　
> Not only that but different countries have code regimes that make more elevators especially expensive. See how building codes in the US basically ensure there are only two real manufacturers in the market vs a healthy ecosystem in others: https://youtu.be/Or1_qVdekYM

---

> **BenjiWiebe** · 2026-07-31T20:08:56.000Z　
> In that case, would it pay to call for an elevator going up, and then remain on it until it's being called down?

---

> **Quinner** · 2026-07-31T20:26:33.000Z　
> The article describes the RSR algo which takes load into account.

---

> **vova_hn2** · 2026-07-31T21:12:27.000Z　
> > If you were mobility disabledIn one of the buildings where I worked, "fancy Destination Dispatch kiosk" had a separate button with a wheelchair pictogram that would ensure that the elevator has enough space for a wheelchair.

---

> **Rebelgecko** · 2026-08-01T01:20:39.000Z　
> Some elevators have sensors that'll bypass pickups after a certain point. Super helpful for furry conventions

---

> **NetMageSCW** · 2026-08-03T23:42:15.000Z　
> Those days aren’t gone - they’ve just moved to enterprise systems.

---

> **john_strinlai** · 2026-07-31T16:36:23.000Z　
> at a quick glance, it reminds me of "the farmer was replaced", if you havent seen/heard of that one

---

> **darkvertex** · 2026-07-31T17:02:31.000Z　
> If you buy the adorable monochrome console called the "Playdate" https://play.date it comes with a bunch of games included, including a cute elevator game where you help penguins to different floors while controlling the elevators yourself using the crank:
> https://play.date/games/flipper-lifter/

---

> **ivanjermakov** · 2026-07-31T17:20:30.000Z　
> You will like https://www.zachtronics.com/

---

> **ftmch** · 2026-07-31T21:19:23.000Z　
> I had the idea to build something like it but for traffic lights. Never got around to actually do it. I have a feeling it probably exists.

---

> **genericone** · 2026-07-31T18:59:48.000Z　
> Sid Meier's Elevator Manager was such a great game... so much nostalgia.

---

> **somat** · 2026-08-01T04:57:26.000Z　
> I never really "got" sim tower growing up, I liked sim city but bounced off tower. It only clicked years later when I read that it was an elevator simulator that got fleshed out a bit, Knowing this I enjoy it quite a bit more today than younger me who I guess was expecting a vertical simcity.

---

> **bentcorner** · 2026-08-01T05:52:00.000Z　
> > People don't usually remember the average amount of time they wait. They fixate on those times when the elevator took FOREVER, the p90 case.I would always get a chuckle out of seeing some poor soul waiting 3 hours to go down a few floors after work, only because I failed to add stairs to the lobby.

---

> **fragmede** · 2026-08-01T15:52:23.000Z　
> bogosort!

---

> **stackskipton** · 2026-07-31T17:00:13.000Z　
> Project Highrise doesn't have elevator simulation. Elevator is just portal that teleports the sim to proper floor.

---

> **Waterluvian** · 2026-07-31T18:02:05.000Z　
> Would that be Yoot Saito? I remember his name on the box.

---

> **cruffle_duffle** · 2026-07-31T16:49:33.000Z　
> You should observe if it is the same elevator all the time and the building people just don’t understand it. Our building elevators (bank of 2) always seems to try to keep one in the lobby. About 75% of the time you get an elevator right away when you call it from the lobby. But it definitely isn’t the same elevator! Allocating an exclusive single elevator to that function would seem to be strictly worse from many angles. Like if you modeled having an algorithm like “elevator 2 only services calls from the lobby” you’d find it would be very inefficient and not every effective. But I can see having one in the bank always returning to lobby right away making sense.My guess is whoever hinted at that didn’t fully understand what they were taking about.

---

> **avidiax** · 2026-07-31T16:15:15.000Z　
> The elevators I've seen have a "group call" feature slightly hidden in the menu.

---

> **summermusic** · 2026-07-31T16:14:49.000Z　
> I haven't ever seen anyone do this in the United States, but I saw it in China and Italy.

---

> **tamimio** · 2026-07-31T16:33:37.000Z　
> Because most buildings now they just put one button so people stop clicking both

---

> **themaninthedark** · 2026-07-31T16:26:20.000Z　
> True but sometimes someone hits a button on the inside by mistake. Or someone was going to get off then decides not to.

---

> **wpm** · 2026-07-31T16:41:24.000Z　
> Yeah and you can flail your head around looking for the arrow or you can just ask. Especially on a busy elevator lobby there might be multiple cars opening at the same time so you cant even tell from the ding/ding-ding

---

> **gabrieledarrigo** · 2026-07-31T17:14:35.000Z　
> "Questions are never indiscreet. Answers sometimes are."

---

> **ButlerianJihad** · 2026-08-01T08:45:39.000Z　
> The direction is also indicated by the chime sound, which only blind people and YouTube viewers seem to know.As for button pressing: https://en.wikipedia.org/wiki/Cargo_cult#As_a_metaphor

---

> **kccqzy** · 2026-08-01T02:32:52.000Z　
> That’s great, but a lot of buildings don’t tell you where the elevator currently is when you are about to press the button.

---

> **ericpauley** · 2026-08-01T11:43:45.000Z　
> The difference is nobody is getting loyalty status on their elevator.

---

> **nubg** · 2026-08-01T12:32:19.000Z　
> > in croatia people believe that you need to press the opposite direction to "summon" the elevator, if the elevator is on lower floor they will press the "up" arrow to bring it up to their floorthis is hilarious

---

> **hermanschaaf** · 2026-07-31T18:50:12.000Z　
> Thanks! Would love to hear your thoughts if you get a chance to play it. I'm currently working on adding a few more towers and challenges. After that maybe I'll deep-dive into the "best" automated scheduling algorithm for all this :)

---

> **cruffle_duffle** · 2026-07-31T16:43:45.000Z　
> The problem is that in the morning the “last stop” for the elevator might be the lobby not a mid floor. And so it would have to move itself back up without any passengers or calls to upper floors. Basically “optimistically” moving itself back up. And I wonder if some (most?) control systems don’t do that because of… well I dunno. Lots of elevators have pretty old or basic control systems in them. Maybe predate caring about energy and many also probably aren’t strictly smart enough to be concerned about wear factors and stuff.It could also be that you and I simply aren’t privy to what is actually happening “the instant” you are waiting for the elevator.…which makes me wonder how often the firmware in these get updated. Assuming it’s not just a pile of ancient relays and stuff. And if, when they do get updated, the algorithms get improved. Or if the algorithm is something that gets sold to the building and “upgrading” is an actual purchase.Anyway, I could get a little LLM buddy to look it all up but where is the fun in that?

---

> **dperfect** · 2026-07-31T16:38:27.000Z　
> That sounds like two separate things then. Could you not have people select a destination without locking in an elevator?(I've never encountered destination dispatch myself, so I'm not really sure how it works in practice)

---

> **fellowniusmonk** · 2026-07-31T16:48:05.000Z　
> I think the problem with simulations like this is that it doesn't include the chaos of innatentive humans.Forcing functions that dump people into well defined funnels can have such a high net positive effect it more than makes up for theoretical losses.It's like narrow, hard road bike tires losing performance because of deflection from rough road surfaces and how long it took designers to factor that in to real bikes.

---

> **joshjob42** · 2026-07-31T22:28:37.000Z　
> Seems like the obvious solution is to put a bank of floor numbers above each elevator and when one arrives the floors it has been assigned to go to light up and the people going to them get in that one. So each person only needs to quickly to see if it's going to their floor or not, much like they need to look to see if it's going up or down. Then you can dynamically dispatch elevators right up until 5s or so before it arrives at a floor, with full knowledge of not just up/down but also destination. (And hell make 'em say how many people are in their party too so you also know how many people are traveling and where.)

---

> **vova_hn2** · 2026-07-31T21:00:00.000Z　
> > Is it because the criteria is wait time not travel time?Yeah, it doesn't make any sense to optimize wait time instead of total time from pressing the button to reaching destination.

---

> **Ekaros** · 2026-08-01T14:50:55.000Z　
> The criteria might also be throughput. That is moving maximum number of passengers in which case total travel time is likely much better metric than wait time.

---

> **Ekaros** · 2026-08-01T14:49:49.000Z　
> I think most of these sort of data sets are considered trade secrets. They are certainly recorded and even stored. But as they could give competitive edge between manufacturers they are not publicly shared. And access to them would mean building maintenance or managers giving access to their occupants information which some of the occupants would not like.

---

> **whartung** · 2026-08-01T02:34:43.000Z　
> Most interesting hotel elevator system I’ve seen was in Washington DC.Instead of hitting the call button, you started the request with your floor. Then the system would assign you an elevator (there were 6 cars as I recall).I assume this gave the system more accurate routing data to make it more efficient for everyone.

---

> **icosian** · 2026-08-01T07:08:34.000Z　
> > Yeah, and definitely is not the right story for hotels.The first time I encountered Destination Dispatch was in a London hotel, maybe 15 years ago. Anyone unfamiliar with the system would naturally sprint towards an open elevator and end up in an elevator with no buttons, totally bewildered. It's not the right system for a transient population.

---

> **shepherdjerred** · 2026-08-01T02:52:04.000Z　
> I wonder if we'll see LLM elevator scheduling

---

> **_kb** · 2026-08-01T04:35:34.000Z　
> The data is already there. This also gets more interesting when you expand the scope from just elevators to general building occupancy and movement.In the simplest sense, I've seen this tied into security gates so as people badge on when entering the building there's already suitable elevator movement to meet demand by time the foot traffic reaches the lift lobby. That can then also feed into destination dispatch if you move from just people counts to identity (and known/most likely work floor).From there you can move into wifi trilateration and have a live and quite accurate view of both how and who interacts with a physical space. This can feed into HVAC load shedding, JIT bookings for meeting rooms or workspaces, and a lot of very good things from a sustainability and general optimisation perspective. The flip side is it also has the potential to be an absolute dystopian privacy nightmare.

---

> **TeMPOraL** · 2026-08-01T09:15:13.000Z　
> > Ideally a new elevator installation would have a trial period where they record usageThere's a tricky problem here: as a user, the first thing you do upon discovering a new elevator, especially if you expect to be using it regularly, is to observe how it behaves and adjust your own expectations/behavior to it.

---

> **sambellll** · 2026-08-01T14:39:11.000Z　
> > Seems like the real reason it performed worse in this simulation is that when they implemented destination dispatch, they assigned an elevator at time of request, and had no system for reviewing and updated that assignment.I don't think it's possible to have destination dispatch AND update assignment together, in the real world.- If the user clicks floor 26 and you tell them to wait at elevator G, you can't really tell them to move to F if it's taking too long.- But if you don't tell them an elevator to wait at, then you'd need them to run around what is possibly like 5-8 elevators to find which one is going to their floor? That's obviously not realistic.So then you're going to just have them get in the first one that opens? But then that's just the same as an up/down button.

---

> **brewdad** · 2026-07-31T17:28:32.000Z　
> Someone needs to design an elevator that only breaks down between midnight and 5am. Maybe a different model to accommodate late night crowds returning to large residential buildings.

---

> **NKosmatos** · 2026-08-01T12:30:06.000Z　
> Did exactly the same with Assembly language on a PIC16C84 microcontroller with LEDs dyeing my university years a looong time ago.

---

> **sobani** · 2026-08-01T10:14:22.000Z　
> FYI: all your comments are [flagged][dead]I don't know why, because they all look fine to me...

---

> **toxik** · 2026-08-01T16:57:49.000Z　
> > Robot motion planning is basically just elevator scheduling with more degrees of freedom.Certainly a take, ChatGPT. Not a very good one, but a take nonetheless.

---

> **ImPostingOnHN** · 2026-08-01T04:50:19.000Z　
> The perception angle is: customers are less unhappy waiting the required 20 minutes for luggage to show up, if they're doing something else during that time.In this example, the passengers are still waiting while moving (the wait for luggage is 20 minutes either way), they just don't perceive that portion of the waiting as intolerable.Bringing it home to elevators, the situation is pretty much the same, only in reverse: someone who waits 2 minutes for an elevator and 1 more once aboard it to get to their floor, likely perceives their 3 minute total wait as less tolerable, than if they waited 1 minutes for the elevator plus another 2 once aboard.

---

> **psadri** · 2026-08-01T14:32:19.000Z　
> To be honest I also just read about it. However everytime I pass through Heathrow I think someone really took the idea to heart.

---

> **Wowfunhappy** · 2026-07-31T23:10:14.000Z　
> I don't know, what about jerks pressing every button because they want to make you wait? The downside risk here strikes me as much more unlikely than the upside.

---

> **stinkbeetle** · 2026-08-01T11:59:00.000Z　
> > https://news.ycombinator.com/item?id=37385826This man has sixteen hundred videos of riding up and down elevators and is still going strong. Amazing. I love how Grandma was willing to ride random elevators and feature in his videos if it meant she could spend time with her eccentric grand son.

---

> **userbinator** · 2026-08-01T04:12:10.000Z　
> On the pop-out controls I mentioned in a sibling comment, the relay is the button, and you can pull it out to cancel.

---

> **ASalazarMX** · 2026-08-01T17:12:54.000Z　
> > people will un-press your floor and chaos will followI can see some engineers deciding that the button press needs 2FA or TOTP so only you can unpress it. Bonus points if you need to buy their brand's smartwatch to use it.

---

> **shmeeed** · 2026-08-01T13:01:36.000Z　
> OMG, this brings out memories about that oh so tempting red stop lever I was absolutely NOT allowed to touch as a kid. I haven't remebered that for decades..

---

> **ButlerianJihad** · 2026-08-01T13:09:54.000Z　
> In my building there are fire extinguishers for emergencies, but I found out they produce a really amazing snow-blanket effect even when it's not Christmastime.

---

> **akoboldfrying** · 2026-08-01T10:09:41.000Z　
> Having visible, pressable buttons that do nothing is terrible UI. Why not just screw a metal plate over these do-nothing buttons, or at least tape a piece of cardboard?

---

> **matkoniecz** · 2026-08-01T07:17:59.000Z　
> > I would not want to be in that building if an evacuation alarm sounded.why short term/long term stay would matter here?

---

> **userbinator** · 2026-08-01T07:57:41.000Z　
> I would not want to be in that building if an evacuation alarm sounded.You are not supposed to use the elevator in emergencies.

---

> **CGamesPlay** · 2026-08-01T08:11:13.000Z　
> > I would not want to be in that building if an evacuation alarm sounded.You shouldn't be taking the elevator if you heard an evacuation alarm, but to be sure, you don't want to be an any 60-story building when you hear that alarm.

---

> **csomar** · 2026-08-01T07:09:20.000Z　
> Because they are short-term and many are staying just for the day + bringing family (like kids, which is why they use AirBNB instead of a hotel). The check-in/check-out already add an entry-exit if the user is staying 24 hours only.

---

> **woeh** · 2026-08-01T07:53:47.000Z　
> I am of course just speculating (and I had a lot of waiting time to think about this), but there are a lot of people with a lot of luggage constantly going in and out. It makes the elevators be full faster (perhaps there is a weight based sensor to determine if the elevator is full, and the luggage tricks the system into thinking the elevator is not full yet, because a piece of luggage is lighter than a person but sometimes takes up more floor space than a person). Furthermore, people with luggage take longer to get in and out.It's a tower in Kuala Lumpur btw. Since it is rather hot here and the elevators are not airconditioned, it's extra uncomfortable.

---

> **mmmattt** · 2026-08-01T10:43:25.000Z　
> I live in a 20 stories building with only two elevators, 4 3-bedrooms apartments per floor. And I don’t think I ever had to wait more than a couple minutes.

---

> **dsego** · 2026-08-01T14:23:24.000Z　
> 8 stories

---

> **dsego** · 2026-08-04T11:30:02.000Z　
> I do that sometimes, but it's a tight fit and I might leave dirt marks.

---

> **yccs27** · 2026-08-01T15:06:35.000Z　
> You could also detect when the elevator call button gets pressed again right after the elevator has left a floor. That means someone wasn't able to get on the elevator (and is now waiting for the next one).

---

> **MichaelDickens** · 2026-08-01T15:31:25.000Z　
> Following rz2k's suggestion, you could have a building employee operate the elevator during busy times.

---

> **cowsandmilk** · 2026-08-01T17:57:16.000Z　
> > If it was a camera, security issueWhat security issue? Many hotel elevators already have cameras.

---

> **dredmorbius** · 2026-08-01T17:02:45.000Z　
> Many buildings permit stairwell entry, but limit stairwell exit for fire code (1st) and security reasons (2nd). You'll want to check to see that you can exit at floor n-1 before attempting this, or you'll be riding the stairs all the way down.

---

> **n_plus_1_acc** · 2026-08-02T09:37:37.000Z　
> Also works for Buses and Trains. Go one stop the opposite way, then go back. This may take a couple minutes longer, but you'll have a seat for the rest of the journey.

---

> **worldthruword** · 2026-08-01T14:08:50.000Z　
> Lazy evaluation would save on money. Branch prediction would save on wait times. In places electricity can shut down, lazy evaluation would be preferable to make it work longer on limited battery.

---

> **fragmede** · 2026-08-01T01:30:42.000Z　
> Interesting! It's counterbalanced though, so why does it go up if the brakes fail in a fire? That's counterintuitive.

---

> **NooneAtAll3** · 2026-07-31T16:54:07.000Z　
> https://store.steampowered.com/app/2060160/The_Farmer_Was_Re...I remember this one, it deserves all sorts of praise

---

> **inigyou** · 2026-07-31T21:33:20.000Z　
> That's the guy who created Infiniminer, which was essentially 3D multiplayer Motherlode (a game everyone was playing at school lunch and I never figured out why) and inspired Minecraft.

---

> **zengineer** · 2026-08-01T06:43:24.000Z　
> same :) Although, I wonder if building it is more fun than actually playing it then

---

> **CobrastanJorji** · 2026-07-31T21:32:58.000Z　
> Yoot Saito, actually, although it does really feel like a Sid Meier or a Will Wright game.

---

> **AndrewHart** · 2026-08-01T13:07:09.000Z　
> The only result I get in Google for this is... this post

---

> **jcranmer** · 2026-07-31T23:53:11.000Z　
> Yeah, the fact that Project Highrise doesn't handle the transportation part of the game means that it never scratched the same itch SimTower did.

---

> **quietsegfault** · 2026-07-31T17:36:58.000Z　
> That’s awesome! I haven’t really played with them, only silently seethed when the elevator is crowded.

---

> **esperent** · 2026-07-31T16:19:11.000Z　
> I've never seen anyone do this anywhere in the world including Italy.I've never been to China but wouldn't you learn quickly after getting in an elevator going the wrong way not to do that again?The only exception I can see if there's way more people than elevators and you just need to get spot at all costs.

---

> **what** · 2026-07-31T16:43:13.000Z　
> What? I’ve never seen that. The elevator needs to know which way you want to go.

---

> **rsanek** · 2026-07-31T16:52:58.000Z　
> That has not been my experience, and logically it doesn't really make much sense. If you do so, you are making the problem strictly worse.

---

> **userbinator** · 2026-08-01T02:37:10.000Z　
> Nondirectional calls are mostly found in very early (pre-war) or small building (3-4 floors) installations.

---

> **SoMomentary** · 2026-07-31T16:38:24.000Z　
> Sometimes I think "stupid" questions like these are just a way to break the ice, something that gets used to kindly acknowledge the momentary existence of others in our lives before we continue down our separate paths.

---

> **deathanatos** · 2026-07-31T17:07:16.000Z　
> … and the elevator is still going the way it is going, and that way is still indicated by the illuminated arrow.

---

> **ImPostingOnHN** · 2026-08-01T04:28:16.000Z　
> or just point your eyes a few degrees away to look at the dedicated arrows next to each elevator, built for this exact use case, which indicate whether that specific elevator is going up or down?I have to assume this is a cultural difference and you just don't have those indicators where you live, rather than "slightly moving my eyes is too hard, better make my problem into somebody else's problem"

---

> **GurnBlandston** · 2026-07-31T18:27:36.000Z　
> "Have you stopped urinating in public?"

---

> **NetMageSCW** · 2026-08-03T23:05:37.000Z　
> When did you stop beating your wife?

---

> **shmeeed** · 2026-08-01T12:53:49.000Z　
> TIL! I need to keep an ear open for this.

---

> **hypersoar** · 2026-07-31T16:53:52.000Z　
> The way I've seen it work is that there's a touch screen in the elevator lobby. You tap a floor, and then screen will say "Car C" (along with an audible message). The problem is that then the system can't reassign you to a different car after that. You'll typically have a bunch of different people going to a bunch of different floors, and there would be no reliable way to communicate to each individual their new assignment. Each car will also typically display which floors it's going to when it arrives. I suppose that, rather than assigning a car immediately, you could have passengers check cars as they arrive to see if they're going to their desired floor. Then the system could do reassignment, but people would be scrambling to check every car to see if it's the right one for them, and that's assuming that they understood the system. It would be way too chaotic in practice.

---

> **lefra** · 2026-07-31T17:42:36.000Z　
> Kind of like airplane boarding. The ideal algorithm would be to make people board from back to front, and from window to aisle. However, people are not disciplined enough to strictly sort themselves, they won't all take the same time to sit, and some people want to board together (family with children for example).Apparently, the fastest known way to fill up a plane in real-life conditions is to let people board in random order, without pre-assigning a seat.

---

> **kadoban** · 2026-07-31T21:53:29.000Z　
> Human psychology might allow other reasonable criteria even if perfectly rational choice is just total time to destination.

---

> **esikich** · 2026-08-01T00:40:43.000Z　
> It very well could be the case that people get more upset about waiting for the car than total travel time when they are already in the car. Ie, pick them up sooner even if travel time is longer. In fact, I would bet that this is the case.

---

> **nkjoep** · 2026-08-01T03:48:14.000Z　
> It’s explained in the article

---

> **donalhunt** · 2026-08-01T07:44:07.000Z　
> Maybe they were embracing YOLO - who knows the possibilities of putting your trust in others' decisions / destinations.Or should it be YORO? You only ride once?

---

> **fragmede** · 2026-08-01T04:16:20.000Z　
> IBM's Watson has been used for elevator scheduling.

---

> **noisy_boy** · 2026-08-01T04:30:43.000Z　
> I apologize for bringing you to the 29th floor instead of the 3rd floor as you requested. That's on me. I will do better next time.

---

> **Terr_** · 2026-08-01T07:57:31.000Z　
> Then it'll be time to make an entirely new software accreditation system, simply so that anyone building such a thing can be disbarred/excommunicated.

---

> **swiftcoder** · 2026-08-01T08:16:23.000Z　
> https://www.youtube.com/watch?v=MNuFcIRlwdc

---

> **Ekaros** · 2026-08-01T10:16:37.000Z　
> Most likely not. I think all the big players have been using more traditional ML approaches for years. Then again someone new might go there and fail miserably.

---

> **omoikane** · 2026-08-01T17:08:41.000Z　
> It sounds like you are looking for Happy Vertical People Transporters with Genuine People Personalities.

---

> **TeMPOraL** · 2026-08-01T10:01:56.000Z　
> > (...) and a lot of very good things from a sustainability and general optimisation perspective. The flip side is it also has the potential to be an absolute dystopian privacy nightmare.Privacy is an illusion for most people, and in office spaces, it's also a red herring. Wifi trilateration doesn't make things worse when you have a CCTV camera on every corner, badge reader at every other door, and presence sensing in conference rooms. Dystopia does not materialize without a severe regime shift.Nah, my main worry is precisely sustainability and optimization, i.e. cost-cutting, because the more tools you give a business to optimize, and the more bullshit excuses ("sustainability! saving the planet!") you give a business, the worse the outcome is for users (here: employees). And a lot of that is doubly annoying, because it's counter-productive.So what you have smart sensors in every room, and combine it with badge readers and wifi trilat and what not, and have smart auto-routing/rebooking algorithm: half the week, all conference rooms are always booked full, and yet somehow when you physically go and check, a good half sits empty, and it's apparently an impossible problem to solve.So what the bathroom wall says, "with water-saving fixtures, we're using much less water in this building", and "we're now saving 2L water per flush". It's all bullshit, because those eco inventions mean I need to flush 3 times instead of once, and it means that I spend a minute washing my hands instead of 10 seconds - especially because both the soap and the dispenser are also optimized, so it takes 20 seconds to get enough soap on your hands, and then extra 20 seconds to get it off afterwards, because unlike normal people soap, it leaves your hands slippery for some reason.And then they say "scientists said you can dry your hands with just 2 paper towels". At that point I'm getting red, because yes, I saw that TED talk 15 years ago too, and yes, it's total bullshit. Maybe it was true then, but the industry and the beancounters have value-optimized paper towels 15 times since that.The generalization and summary of this rant is: slack is good. Happiness lives in slack. There is such thing as optimizing too much. Also the small, isolated systems under optimization, are in reality neither small nor isolated.

---

> **gpvos** · 2026-08-01T09:57:41.000Z　
> I think you belong to a small percentage of the population doing that. Most people don't bother with such detailed life microoptimizations.

---

> **mvkel** · 2026-08-01T13:17:13.000Z　
> Things are constantly changing. For example, a new building might have two or three tenants, so entire floors can be skipped. But then five years later, the whole building is full. I would bet that every new algorithm after LOOK is just differentiation in a competitive market.

---

> **richk449** · 2026-08-01T17:37:50.000Z　
> Interesting. I didn't realize that destination dispatch told the user what elevator to take at the time of request. (I've never used it.)Why not have active display above each elevator that says what floors it is going to when it opens?

---

> **taftster** · 2026-08-01T00:02:28.000Z　
> I mean, "breaks down" is different from "scheduled maintenance". Most definitely the later can be scheduled during less busy hours.

---

> **shmageggy** · 2026-08-01T12:40:54.000Z　
> LLM text tells, particularly in their other comments. Definitely AI generated.

---

> **oliv__** · 2026-08-01T17:06:37.000Z　
> Sure, but the perception is in accord with reality and in my opinion unchanging since the actual time waiting for luggage has been effectively reduced.The only difference is the reality has been falsified

---

> **voyagerfan5761** · 2026-07-31T23:12:51.000Z　
> Jerks do push all the buttons to make everyone else wait. It's why newer elevator systems are often configured to ignore those if too many floor buttons get pressed at once.

---

> **dsego** · 2026-08-05T09:01:23.000Z　
> One time our neighbor forgot her phone and activated the stop in the small elevator just as the doors were closing and it started going down. It stopped but already moved down and got stuck between floors. We were inside with our small child and it was not pleasant. Luckily, after resetting the switch and pressing some buttons, the elevator continued on its way.

---

> **sixhobbits** · 2026-08-02T07:55:38.000Z　
> they change the elevators configuration depending on peak hours, or if one of the others is out of order then the express becomes a normal one again.

---

> **perpetuallunch** · 2026-08-01T19:38:00.000Z　
> Because short term stays put more load on the building systems, like the lifts, than perhaps the building was designed for.Regular tenants don’t come and go at anywhere near the rate short stay guests do.

---

> **perpetuallunch** · 2026-08-02T07:17:16.000Z　
> No! Surely not? Where did you read that?

---

> **perpetuallunch** · 2026-08-02T04:18:37.000Z　
> Yes, I realise this.But if the lifts aren’t coping with the foot traffic during normal operation, I’d also not want to have to use stairs.

---

> **close04** · 2026-08-01T07:43:09.000Z　
> It’s not super common to stay in one place only 24h when traveling with kids. Other than the luggage, tourists and residents move in an out of the building just the same. People who live there also need to go to work or school every morning, and come back in the afternoon creating choke points. And these people are there every day, not a handful of seasonal tourists.The problem is probably the same as every other super tall building. It was impressive for the potential buyers but designed poorly and this only became apparent after they lived there a while (crappy elevators, probably often defective, building sway, plumbing issues, etc). So the owners started to move out and it’s possible the building is mostly short term rental now.

---

> **brookst** · 2026-08-01T13:35:36.000Z　
> Amusing anecdotes and musings about your stay (well, amusing to read, probably not to live).Since you’ve got a bunch of enforced idle time, maybe see if you can find the architect firm and see if you can get the backstory? Why three elevators in a 60 floor building? Just low level sadism, or what?

---

> **grishka** · 2026-08-01T15:18:55.000Z　
> TIL that there are countries where the building code doesn't enforce the minimum number of elevators. In Russia it's one for buildings taller than 5 floors, two for taller than 9, and I believe three for taller than 16 (every 20-something-floor building I've ever been to had at least three). But we don't have many skyscrapers so I'm not sure how it works for those.

---

> **Neywiny** · 2026-08-01T20:38:05.000Z　
> Because there would need to be some automated service and you best believe it'll be flock 2.0

---

> **Breza** · 2026-08-03T01:50:45.000Z　
> I used to work in a shiny new LEED certified government building here in DC. My office was on the second floor. I had to take a elevator every day because the only stairs were for fire use. So frustrating.

---

> **Breza** · 2026-08-03T01:51:28.000Z　
> Good tip. Somehow this feels more fair than the elevator example but I can't put my finger on why.

---

> **ImPostingOnHN** · 2026-08-01T04:41:44.000Z　
> Maybe it needs to be counterbalanced at maximum approved elevator+load weight?

---

> **ivolimmen** · 2026-07-31T17:05:48.000Z　
> I can also recommend https://store.steampowered.com/app/375820/Human_Resource_Mac...

---

> **iqihs** · 2026-07-31T21:41:08.000Z　
> Yoot Tower has been on my bucketlist of games to play for a while now

---

> **fragmede** · 2026-08-01T15:14:51.000Z　
> Sid Meier wasn't involved with SimTower, GP is mistaken.

---

> **Sohcahtoa82** · 2026-08-01T00:03:54.000Z　
> Yeah, maybe that's what was it.Tbh, while I bring up Project Highrise whenever someone mentions SimTower, I did always feel like it was missing something. Something always felt slightly soulless about Project Highrise.

---

> **the_af** · 2026-07-31T16:38:58.000Z　
> My wife always randomly hits the up or down button, then gets upset if I explain why she should only pick the one she really wants. She forgets the next time. I think some people never really understand how elevators work.See also: the keep open / close doors button. I had one building administrator explain to me we should add a delay of 10 seconds to the "quickly shut door" button because otherwise she kept getting her arm hit by the door. When I asked why we would add a delay to the button that's meant to reduce delays (why not simply wait for the door to close on its own, then?), and whether we should fix the sensor that prevents doors from closing if there's an obstacle instead, she just kept staring blankly at me. I don't think she understood me at all.Again, some people simply don't grasp how elevators work.

---

> **allannienhuis** · 2026-07-31T19:32:04.000Z　
> On the ground/lowest floor, there's only one button as there's only one way to go.

---

> **cozzyd** · 2026-07-31T20:27:24.000Z　
> i just saw this for the first time today in Romania...

---

> **userbinator** · 2026-08-01T07:51:36.000Z　
> It doesn't; it just needs to know it was called. You make your selection once it arrives.Look up the early history of elevators and you'll see a progression from fully manual in-car up/down controls (often with a dedicated human operator); various semi-automatic systems with minor improvements like automatic leveling and door control; and then operatorless systems that started with nondirectional calls:https://liftescalatorlibrary.org/paper_indexing/papers/00000...

---

> **Ekaros** · 2026-08-01T10:28:27.000Z　
> It is reasonable if you either have low load say a residential building where lift is often idle. Or low number of floors where travel times in either case are short.

---

> **userbinator** · 2026-08-01T07:51:48.000Z　
> Please see: https://liftescalatorlibrary.org/paper_indexing/papers/00000..."2.3 Non-directional collective
> Non-directive collective control provides a single pushbutton at each landing. This pushbutton is pressed by passengers to register a landing call irrespective of the desired direction of travel. Thus, a lift travelling upwards, for example, and detecting a landing call in its path stops to answer the call, although it may happen that the person waiting at the landing wishes to go down. This type of control is only acceptable for short travel lifts."

---

> **dperfect** · 2026-07-31T17:26:31.000Z　
> Thanks for the context. That makes sense.

---

> **JoshTriplett** · 2026-07-31T18:04:05.000Z　
> Display a set of floors on a big overhead screen (in floor order so they're easy to find), have the "elevator" column blank until the elevator is assigned, and let them watch the column that's going to show them which elevator to use.But yes, this seems like a case of "unfortunately, people".

---

> **nicwolff** · 2026-07-31T18:26:06.000Z　
> Little extra "fun" anecdote: my building has two banks of eight elevators, each servicing 20 or so floors, and has six destination dispatch kiosks: one at each end and the middle of each bank. The kiosks originally had nice metal buttons for each floor and you could easily tap yours as you walked by.Sometime during Covid, the metal buttons were replaced with glass touch screens – which are totally unreadable on sunny days, because in our stunning glass-ceilinged atrium mezzanine they sit directly in sunbeams[0]. So now you have to walk up to the kiosk, shade it with your body, and squint at the screen to make out where to touch it.[0] http://www.angel.net/~nic/photos/elevators.jpg

---

> **namibj** · 2026-07-31T18:39:44.000Z　
> You could give each one a diceware-eff-wordlist-like "ID" when they input where they want to go, perhaps have a "group" and "single" button/column per destination in the menu as well to inform the elevator if it's a group traveling together, and importantly have a fast-food-pickup-counter style dispatch screen up top visible from the waiting "hall", that assigns you a cab with an appropriate notice/heads-up period so you can make your way over to the assigned cab.

---

> **hypercube33** · 2026-07-31T19:03:15.000Z　
> After visiting a hospital with like 5 floors and 2 elevators people were having a hell of a time with just 'going up ' or down arrows

---

> **donalhunt** · 2026-08-01T07:49:04.000Z　
> Having chatted with friends who have gotten stuck in elevators, you definitely should care about total travel time.In one case, the building was still being commissioned and it took a while for anyone to even realize they were stuck (could spawn a whole discussion about launch processes in itself).

---

> **Gabrys1** · 2026-08-01T14:24:24.000Z　
> It should be both, I think. Same goes for queuing in the restaurant. Waiting for the table for 5 minutes, then 5 minutes for the waiter, then 10 minutes for the drink, then 25 for the food is better than waiting for the table for 25 and then getting your full order in another 5.Basically you have an irrational sense of progress even if things get delayed

---

> **brookst** · 2026-08-01T13:28:18.000Z　
> I want to own something here: this is the fourth time in a row I’ve brought you to the 29th floor when you asked for the third. I am creating a memory to always go to the 3rd floor instead of the 29th, which should prevent this from happening again.

---

> **ufmace** · 2026-08-01T15:07:16.000Z　
> Sorry, I forgot that this building only has 18 floors, it's on me that your elevator is now airborne.

---

> **swiftcoder** · 2026-08-01T14:35:02.000Z　
> This is an industry that evolves extremely slowly. A decade back one of the big players in this space was still using a software emulation of their original hardware relay logic, because it was cheaper than retraining all the technicians...

---

> **fuzzfactor** · 2026-08-01T21:52:26.000Z　
> No thanks, I'll take the alleviator :)

---

> **bkleinwort** · 2026-08-07T22:33:45.000Z　
> As long as they're not afraid of the future!

---

> **ben_w** · 2026-08-01T10:49:35.000Z　
> > The generalization and summary of this rant is: slack is good. Happiness lives in slack. There is such thing as optimizing too much. Also the small, isolated systems under optimization, are in reality neither small nor isolated.Indeed, the Boimler Effect, amongst other things.I see an analogy, Food : Malthusian catastrophe :: Money : No room for profit in an economy.

---

> **ufmace** · 2026-08-01T15:04:52.000Z　
> > The generalization and summary of this rant is: slack is good. Happiness lives in slack. There is such thing as optimizing too much. Also the small, isolated systems under optimization, are in reality neither small nor isolated.Yeah there's a certain type of engineer mindset that loves the idea of optimizing things. But if you want to really optimize something, you have to carefully account for every single possible factor, situation, and use-case. Miss anything, and it's a much bigger disaster than saving 2% of whatever resource. It's rarely worth it.Much better to treat the presumptions as a vague heuristic, make generous assumptions and add some slack, and call that good enough. Now there's probably enough slack to cover most of the edge cases you didn't think of, other things you based your original assumptions on changing under you, etc.

---

> **razakel** · 2026-08-01T14:47:50.000Z　
> I think people do, but it's subconsciously.

---

> **NetMageSCW** · 2026-08-03T22:56:11.000Z　
> Because it doesn’t know that until after it has completed the trip?

---

> **NetMageSCW** · 2026-08-03T22:50:17.000Z　
> Just like yours is.

---

> **Wowfunhappy** · 2026-07-31T23:48:33.000Z　
> > Jerks do push all the buttons to make everyone else wait.That's my point. The attack goes away if you can un-press buttons.

---

> **matkoniecz** · 2026-08-03T21:27:47.000Z　
> why it would matter during evacuation when everyone leaves?(tourists would be more likely to be outside anyway, so actually it sounds like better case)

---

> **etskinner** · 2026-08-01T22:37:13.000Z　
> This could easily be done locally with no network

---

> **NooneAtAll3** · 2026-07-31T17:49:34.000Z　
> and its sequel is also worth a mention https://store.steampowered.com/app/792100/7_Billion_Humans/but imo, unlike farmer, these games reaaaaly lack the ability to make functions/subroutinesmanually doing all the goto loops becomes tiring

---

> **jcranmer** · 2026-07-31T23:17:35.000Z　
> Waiting for Don Hopkins to jump into this thread, saying how he's going to release the source code soon...(https://github.com/YootTowerManagement/YootTower if you haven't seen one of his messages on the topic before)

---

> **Waterluvian** · 2026-08-01T00:07:37.000Z　
> For me the issue is that it doesn’t look and sound like Sim Tower. Which I’m sure is mainly just nostalgia but that’s still a valid reason why I probably love it so.

---

> **superhuzza** · 2026-07-31T17:00:34.000Z　
> I fear in both cases, its not a lack of understanding of elevators but of common sense...

---

> **brookst** · 2026-08-01T13:41:22.000Z　
> This reminds me of my partner, who always sets car air conditioning to 50F (the min) or heat to 90F (the max) because she thinks it makes it get cold or hot faster.And of course a few minutes later we’re freezing or roasting. She sees the temps setting as controlling intensity of cold/hot rather than just, you know, the temperature you want.

---

> **tamimio** · 2026-08-01T03:22:33.000Z　
> And the top floor too

---

> **what** · 2026-08-01T04:47:31.000Z　
> That’s not what they meant…

---

> **esikich** · 2026-08-01T08:48:38.000Z　
> Obviously. I'm talking about waiting for the elevator for 30 seconds, total trip is 2 minutes vs 1 minute 30 sec wait and total trip is 1m45s.

---

> **breakingcups** · 2026-08-02T10:54:24.000Z　
> Small wrinkle: the existing documentation indicates that the 29th floor is in fact the 3rd floor.

---

> **ArekDymalski** · 2026-08-02T08:41:19.000Z　
> Would you like to learn more? If you meant an aircraft elevator or a building elevator malfunction, tell me more so I can give you the right facts.

---

> **Ekaros** · 2026-08-01T14:37:57.000Z　
> It is just the reality that LLMs are not superior for this purpose. They are most likely very much inferior. There is no need to use language models for something that involve no language.I feel weirded each time LLMs are suggested for anything as some sort of holy solution for every single problem. Robot surgery let LLM control it. Robots cooking LLMs. Nuclear power plants and oil refineries LLMs... Industry has find a sledge hammer and now everything is a nail...

---

> **richk449** · 2026-08-04T04:24:51.000Z　
> That explanation is entirely inconsistent with sambellll's statement that when the user clicks a floor, the display tells them what elevator to take, and that elevator is then locked into going to that floor.Also, I don't think that destination dispatch would work if the elevator didn't commit to going to the users's floor at the point the user got onboard. It may also stop at additional floors that weren't committed to when the user entered, and it may drop floors it was thinking of going to before it picked up the user (if the user onboard isn't going to those floors), but once the user gets onboard, that floor is a hard commitment.

---

> **shmageggy** · 2026-08-09T11:25:54.000Z　
> Go fuck yourself. How's that for an LLM tell?

---

> **Neywiny** · 2026-08-01T23:54:08.000Z　
> I mean this in the nicest way possible. Do you see all these cloud photo/video leaks like from robot vacuums or whatever and think they don't know it can be done locally?

---

> **contingencies** · 2026-07-31T21:21:02.000Z　
> For these people, replace the buttons entirely with a voice-activated destination request on proximity.

---

> **superhuzza** · 2026-08-01T00:13:14.000Z　
> Full circle back to elevator operators!

---

> **chuckadams** · 2026-08-01T02:40:08.000Z　
> More like Star Trek turbolifts. Make them grab the handle first for that TOS feel.

---

> **contingencies** · 2026-08-01T06:12:24.000Z　
> Primarily this fixes the bug in the interface which is allowing the user to input data that does not match their declared destination. However, a second benefit is that you can then obtain per-user destination information, which is useful in capacity planning and currently lost in shared direction-only button pressing. Finally, you could usefully use non-floor specifications, ie. 'Ladies underwear', 'ACME Co.', etc.

## 导航

- 项目页：[[10-项目/john.fun_c0ca64fb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
