---
type: "corpus"
item_id: "f422a9605ef16473"
title: "Show HN: TIE Fighter co-op in 11 days, built from 11 years of Wing Commander"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50565475"
project_url: "https://fireflyk64.github.io/makingtf"
author: "daniel_rh"
published_at: "2026-11-19T20:00:57Z"
captured_at: "2026-11-20T09:45:52+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - hn_show
  - author_daniel_rh
  - story_50565475
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: TIE Fighter co-op in 11 days, built from 11 years of Wing Commander

> [!info] 一句话导读
> dosbox3d · the multiplayer layer

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50565475>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：daniel_rh　|　发布：2026-11-19T20:00:57Z
> 项目链接：<https://fireflyk64.github.io/makingtf>
> 采集：2026-11-20T09:45:52+08:00　|　id：`f422a9605ef16473`

## 正文

dosbox3d · the multiplayer layer · November 2026
TIE Us Together: TIE Fighter Co-op
Related: the making of Wing Commander Multiplayer
 An 11 year journey to play DOS Wing Commander together
 From memory dumps in 2015 to a browser and a room code in 2026.
Watch on YouTube
Play it in your browser
While the Falcon, Tydirium Shuttle, Snowspeeder, and sometimes even the Y-Wing had both a pilot and co-pilot, the majority of vehicles in Star Wars had a solo pilot (you could argue that the Falcon also had a Solo pilot, as expounded upon in that self-referential Solo: A Star Wars Story scene no one asked for) . With the introduction of X-Wing vs TIE Fighter and myriad follow-on clones and modifications, including Star Wars: Squadrons and even Star Wars Battlefront, multiplayer combat has been both common and enjoyable. However, the one aspect that has been missing for me is pure co-op multiplayer for the most memorable early Star Wars entry in the genre: TIE Fighter.
The charming magic of the pixelated Concourse, the cutscenes, and the arrogant Imperial officials as your commanders and colleagues immersed players in a galaxy far, far away in a way that I haven't seen perfectly reproduced. With the technology that broadcast the Wing Commander action across the network, it seemed plausible the same ideas could also work in TIE Fighter. However, TIE Fighter had challenges that required a new kind of sync.
Requirements
TIE Fighter's missions were very large, spread across kilometers. The original X-Wing vs TIE Fighter used a deterministic simulation and kept clients in sync exactly. This shook out a number of nondeterminism bugs for that title, but it required the network to operate at exactly physics-speed. This may have been a good option for LAN play with full control of the game engine. This project has neither: it adds multiplayer to TIE Fighter itself, the earlier game, where those nondeterminism bugs were never fixed.
For the chosen solution, it was useful to look at the requirements of this project:
The game code must not be altered
Variable-latency network link
Dozens of craft over tens of kilometers
Large number of distant projectiles
Lasers that must hit fast-moving, maneuverable craft, if aimed correctly
Sections
01 - Linking together two battles
 02 - Similarities to and changes from Wing Commander multiplayer
 03 - Finding a 32-bit game inside a 16 MB machine
 04 - Hooking TIE Fighter
 05 - Calling TIE's functions
 06 - Craft memory layout
 07 - Design choice: whether to run in lockstep
 08 - Who flies what
 09 - Near, mid and far
 10 - The anatomy of a frame
 11 - Teaching the Imperial stormtroopers to aim
 12 - Events that needed to be synced
 13 - A sign bug from 1995
 14 - Knowing when a flight is over
 15 - Two new cockpits for fan favorites
 16 - Conclusion
01 Linking together two battles
The solution was modeled on the Wing Commander multiplayer approach with a couple of key enhancements. Each pilot has the full simulation running on their own machine. The data being sent falls into four categories:
Who flies what
Where each craft is
Which shots were fired
Which hits landed
The overall design uses Lobbylink to bind together two browsers, giving them a peer-to-peer link. All the logic for how to apply the data from the wire to the game and from the game out to the wire exists in the modified DOSBox itself. The code for this resides in the TIE layer ( src/cpu/wcnet_tie*.cpp ). The patched DOSBox executable, compiled to WASM, runs in the browser and executes the unmodified game ( Z_TIE__.EXE in the GOG release) under DOS/4GW.
How two machines coordinate a co-op session.
Here are two players' screens at the same moment of the new Z-95 Combat Chamber challenge (two Z-95 Headhunters against the Empire's own craft). Both targeting displays show the same TIE Bomber (T/B): 0.27 km from the host, 0.45 km from the guest.
The host (left) and the guest (right), the same frame of the same fight. Note on the Z-95 Screenshot
The DOSBox mod creates the Z-95 challenge by altering every craft in the mission.
A table of equivalents swaps Rebel craft for Imperial ones and back.
The Z-95 cockpit is cut from the gunboat's at run time.
The Combat Chamber is treated identically to the campaign battles, allowing 2-3 pilots at once.
02 Similarities to and changes from Wing Commander multiplayer
The multiplayer design was crafted for Wing Commander I and II.
 TIE Fighter uses the same plumbing, including:
Lobbylink's WebRTC data channels (one reliable and ordered, one best effort) for the transport
The host relaying between guests
The protobuf envelope
The per-instruction hook dispatcher
The text line drawn over the picture
The web page: rooms, the public lobby, chat, voice, control setup
However, the 32-bit TIE Fighter has substantially more complex missions, with many flight groups and ships in the arena.
Simply broadcasting every craft every frame would cost too much. To function, TIE Fighter needed the following additions:
An address finder for the running executable
The address map
Dynamic craft ownership handoffs
Update rates by distance
A 32-bit trampoline
Flight control bug fixes
With these additional features, the same multiplayer technique translated to this game and became more general for the next set of DOS games. The following table illustrates the differences between these two engines and which features were unique to each:
Wing Commander I and II TIE Fighter
 The program 16-bit real mode, overlays 32-bit protected mode under DOS/4GW, one flat address space
 Found by its segments a scan of memory for data only it has
 Hooks keyed on CS:IP the low word of EIP, then the full address
 Frames the host paces a fixed rate; the wingmen take the host's frames each game keeps its own clock; frame times vary
 Craft a few, inside a sphere of action up to 32 at once, spread over tens of kilometers
 Sync frames in step an owner per craft, reports by distance
03 Finding a 32-bit game inside a 16 MB machine
The first challenge was finding the game in memory: DOS/4GW loads the 32-bit program into extended memory itself, and nothing tells the emulator where. I remembered the rank table from the manual:
Rank Manual Points Executable Points
Flt. Officer 10,000 20,000
Lieutenant 50,000 50,000
Captain 150,000 100,000
Commander 250,000 250,000
General 500,000 500,000
I scanned the machine's memory for little-endian encodings of the manual's rank thresholds. Sadly, the game must have been rebalanced a bit after the manual went to print, so
the final numbers were actually 20000, 50000, 100000, 250000, 500000 at 0xC1E10 . The multiplayer harness repeats this scan four times per second until the game load completes.
 With the rank table found, the data is placed, and the code can be located below it: DOSBox searches for the first bytes of tie_updatetime and laser_createprojectile . The code and the data turned up at linear 0x1FA000 and 0x2A5000. These act as guideposts and the rest of the necessary functions and data are found relative to these guideposts.
Searching through the emulated machine's memory for the game's code and data, placed by DOS/4GW.
04 Hooking TIE Fighter
Previously, the Wing Commander hooks were keyed on the 16-bit CS:IP. However, since TIE Fighter runs 32-bit code, its EIP register is too wide for that comparison. The hook is structured so that only the low 16 bits of an instruction's address are watched; on a hit, the full address is compared before the hook runs. This table lists every place in the game that is hooked to make TIE Fighter multiplayer:
Image address Place Why it was hooked
 0x577F4 tie_updatetime the top of each frame: network in and out, controls
 0x5CDA0 user_inputforplane the player's stick, once a frame
 0x5F801, 0x5F831 (inside user_inputforplane) sign-extend the joystick value (fixing an original bug from '95)
 0x5FAE1 (inside user_inputforplane) the bank into a turn, left out in "point to aim"
 0x32448 move_moveobjects copies written; the trampoline's calls run here
 0x2E0E4 laser_createprojectile a shot fired
 0x1433C collide_laserhitcraft a bolt meets a craft
 0x148F0 collide_damagecraft damage applied
 0x17BF8 create_createcraft a craft made
 0x16B8C create_createmission mission set up: to map players to craft
 0x82504 shipext_Get_Mission_Path the mission file chosen so all play the same mission
 0x218D8 fediskio_loadspecies craft types chosen: cockpits, voices
05 Calling TIE's functions
Just as with the Wing Commander multiplayer effort, the most reliable way to make bolts, deal damage and credit kills is to call the original software's own functions. The trampoline for TIE Fighter is similar to the Wing Commander one, but it uses the Watcom register calling convention, which places up to four arguments in eax, edx, ebx and ecx, and simply pushes the return address onto the stack. Upon return, both ESP and EIP are back at their old values. At that point, just as before, either another queued call is executed or the entire register state is restored, including the flags.
A call into the game made of CPU state alone. The 16-bit Wing Commander layer does the same in real mode.
06 Craft memory layout
While the DeLorean may need to reach 88 miles an hour to time travel, a TIE Fighter instead requires 88 bytes for its flight record, including speed. Spacecraft occupy slots 0 to 31, projectiles are in 32 to 79 and finally debris and explosions occupy the remainder. Each craft also has a 0x21A-byte CraftData record: its AI, target, throttle, hull and shields. Syncing objects requires surprisingly few fields: place, attitude, velocity and the axes, then hull, shields, systems and the AI's countdown.
For TIE Fighter, slots are the same on every machine: the mission's own setup creates the same craft in the same slots, so a slot number names a craft across the network. This matters later, when distant craft are driven by each machine's own AI.
// the units the game counts in
1 km = 40,960 world units
a mission second = 236 ticks (the clock: 4 ms ticks)
a frame at 59 fps = 4 ticks (frameticks, 0xEB712)
a full turn = 65,536 (pitch 0x4000 = level)
a direction = Q15, 16 bits (move vector, rotational axes)
a T/F's top speed = 225 (3,600 in hyperspace)
a laser's damage = its bolt's collision radius
07 Design choice: whether to run in lockstep
Since both machines load the same mission file with the same random seed, it stands to reason that, with a deterministic timestep and deterministic physics, only the inputs would be required to simulate the game forward. In fact, that was the basis of the entire design of the TIE Fighter sequel, X-Wing vs TIE Fighter. However, this approach is also quite difficult, and its lead programmer wrote an illuminating article on the challenges they faced along the way: The Internet Sucks: Or, What I Learned Coding X-Wing vs. TIE Fighter .
Experiences from the X-Wing vs TIE Fighter developers
We knew this approach would have its own problems. The problem we anticipated with the most anxiety was the one we had seen many times before in our "VCR" feature. When playing back a recording of the player’s input, the game would sometimes produce results that were completely different from the original flight. In the past, bugs in the code that were otherwise harmless inevitably caused these "divergence" problems.
For example, we might use a local variable as a Boolean flag to decide between two possible actions for a non-player craft. If the variable were accidentally used before being set, the decisions would be random depending on the value of the variable’s location on the stack. This type of bug was usually not noticeable, except when playing back a film. But when playing back a film, the bug could cause a craft to take a different action from the action it had taken when the film was recorded. This difference would quickly "ripple" through the rest of the game world, as craft that were dependent on the actions of that craft made different decisions as well.
If this kind of thing happened during a multi-player game, the players would quickly be experiencing two completely different simulations. We hoped to deal with this "out of sync" problem in two ways. First, we hoped that we would be able to find most of these bugs, and thereby avoid the problem occurring in the first place. Second, we devised a mechanism for detecting when the problem occurred, and "re-syncing" the game by sending the data that had diverged.
We were able to develop some pretty effective techniques for finding "out-of-sync" bugs. Thanks to those techniques and the long period of testing, we actually found most of those bugs. We were also able to work on the "re-sync" mechanism, and we found that on the LAN, we could re-sync a game so quickly that you hardly even noticed when an "out-of-sync" bug had occurred.
Initially, both machines load the same mission file with the same random seed, so TIE Fighter starts out well: the same craft arrive with the same orders on both machines. However, each frame moves everything by its own measured frameticks , and the frame rate wanders with what is on screen: from 59+ in an empty region of space to 33 in a busy one. Two games agree only with the same inputs at the same frame times, and two machines never have those. The only possible lockstep solution would be to pin frameticks to the slower machine's, but that could cause variable gameplay, and it would require per-frame synchrony. Based on these facts, the simpler approach, chosen here, was to give each craft one owner, a machine that is authoritative for it, and to have every other machine show a copy kept in step by the owner's reports.
08 Who flies what
From the outset, the game host owned most of the craft. However, this could cause unexpected twitches in the fast-moving targets on the guest machine, and it would result in an unacceptable aiming experience. A copy steered by reports would arrive a few milliseconds late and appear as a jump. TIE Fighter, more than other games, rewarded keen prediction and aiming capabilities. To add network jitter into the mix would dilute the skill aspect of the game.
The approach we took was simple: the guest takes ownership of very near craft in its view that the host is not targeting, and keeps ownership of its own target. This lets a player target a craft and fire a few lasers to dispatch it without any network jitter. Specifically, a guest takes a craft within 2.5 km and 45° of its nose (lasers' reach), or its own target within 4 km, unless the host is targeting it. Ownership is a bit sticky to avoid too much flapping: a craft is given back only once it is past 1.25 × the reach or 60° off the nose, or the target is dropped. Moreover, a craft changes owner at most once a second. Between two guests, the first to target a craft has priority, then the nearer one.
A: in reach and in view: the guest's. B: near but behind: the host's. C: the guest's target, 3.8 km out: the guest's. D: in the guest's view but the host's target: the host's. E: far from every guest: the host's.
09 Near, mid and far
A battle can hold 30 craft spanning across 40 km, dotted through more than thirty thousand cubic kilometers. Sending all of them every frame would cost about 50 KB a second. Instead, borrowing ideas from my thesis , among others, I made the update rate fall with the distance from the other pilot. Far craft are flown by each machine itself, which approximates their behavior. For instance, distant Star Destroyers will fire their own turbolasers.
How often a craft is reported, and who flies it on the machine that does not own it.
 Near under 2.5 km
 reported every frame
 within 10 m: written as reported; further: eased in at 300 m/s at most
 its AI held; its owner's shots come over
 hits: the shooter decides, the owner applies
Mid 2.5 to 10 km
 every 10th frame
 between reports the game's own move carries the copy along its move vector
 still a copy within 5 km: no AI of its own
Far past 10 km
 one craft every 30 frames, in turn: each every 10 to 20 s, sent reliably
 beyond 5.5 km of this pilot: flown by this machine's own AI
 its shots shown for show; damage only on its owner's machine
 pulled toward each report over the time until the next
This illustrates how the same craft appears on both host and guest machines.
10 The anatomy of a frame
Applying updates from afar requires care, and the order in which they are applied matters.
 Outgoing reports are taken at the beginning of each frame; any later, and the local dynamics have already nudged the craft. Likewise, incoming reports are written into the copies after the AI, weapons and physics have run, but before anything moves.
A frame in the order the game runs it, and what the layer does at each watched place.
11 Teaching the Imperial stormtroopers to aim
Since TIE Fighter is focused on precision and aim, lasers are a place where latency can disrupt gameplay. A rule of thumb helped bring the question about lasers into focus: whoever fired a bolt decides whether it hit based on that client's view of the full scenario.
If the laser bolt is created near enough to another pilot, then it is sent to that pilot and the other pilot's machine creates the bolt using laser_createprojectile from the original code, using its view of the shooter's craft location. The call to collide_damagecraft is skipped for a bolt that hits a craft owned by another machine. Instead, the shooter's machine sends a TieHit and shows a preview of the damage (the struck shield first, then the hull). The owner then puts a stand-in bolt in a free projectile slot (its segment, type, radius and shooter) and calls collide_laserhitcraft directly. Shields, components, messages and the flash all come from the game. The owner remembers whose hit began a death and names that pilot in its reports; the shooter's machine then calls collide_updatekills , so the kill is credited to the right pilot.
A guest's shot at a craft the host flies, from the trigger to the kill.
On a network, what a pilot sees is always a little old. With 150 ms of lag each way, the guest could observe each hit 170 to 190 ms before the host applied it. But in the end both copies' hulls agreed. Friendly fire works identically: a shot that leads its target and hits a friend behind it is applied like any other hit.
At a T/F's top speed (225: 4,100 units, 100 m, a second), 100 ms of lag moves it 410 units, a third of its own length.
 A perfectly aimed shot, tested on another machine against its older picture, would miss by that much.
Instead, the design was built on three assumptions to mitigate lag:
The guest is probably aiming at a craft its own machine flies. The ownership rule hands the guest every craft within 2.5 km and 45° of its nose, and its own target within 4 km. On the guest's machine those craft move by the game's own AI and physics every frame, with no report in the loop, so the lead the pilot sees is correct.
The shooter's own math decides. The game's own hit test ( collide_laserhitcraft ) runs on the shooter's machine, against the picture the pilot aimed at. The owner of the craft is told the result and never tests it again against its own picture.
The owner applies it to the craft, wherever the craft now is. The hit travels as "craft 7, this far from its middle", not as a point in space. A stand-in bolt in a free projectile slot carries the shooter's bolt type, radius and segment, so shields, hull, systems, messages, the kill and the flash can use the game's own code.
The hit is decided on the guest's screen and sent as the craft and the impact's offset from its middle. On the host, the craft has moved on; the flash still lands on it.
One assumption still being tuned is that ownership does not flip in the middle of a burst: a craft leaves the guest only past 1.25 × the reach, 60° off its nose, or with the target dropped, and changes owner at most once a second. These feel like arbitrary constants because they are, and they will likely need to be adjusted in the future. The exception is a craft the host is targeting too: it stays the host's, and the guest sees a copy written from the host's reports every frame. Either way, the guest's hits on it are still decided on the guest's screen, so they still count even though another machine flies the craft. The price is the famous tradeoff in shooter-decides netcode: on the target's screen, a hit can arrive a moment after the shot looked like a miss. Luckily, this is a co-op game against AI pilots, so the trade is unlikely to cause much consternation.
An AI craft that the guest's machine flies works the same way. Its AI aims at the host's craft as the guest's machine shows it (a pilot's craft is reported every frame), and its hits are decided on the guest.
A bolt… Decided on Applied on Seen in the tests
 of the guest, on a craft the guest flies the guest the guest: the game's own call the usual case: the ownership rule gives the guest what is in its sights
 of the guest, on a craft the host flies the guest the host, by a stand-in bolt HI2W: 20 and 28 a run, every one applied
 of an AI craft the guest flies, on the host the guest the host HG3M: the host shot down by one
 remade from a TieShot , touching anything nowhere nowhere: its shooter's machine decides every shot shown on both screens: 327 and 245 in HI2W
 of a far craft this machine's AI flies here, for show only its owner's game deals damage 299 shown on a guest in battle 2 mission 1
 on a craft already dead on its owner's machine the shooter dropped: "not ours to apply" 18 of 19 applied in battle 2 mission 1
12 Events that needed to be synced
Mission triggers run on every machine, but the machines can disagree about a craft, especially at a transition such as a craft entering a hangar or reinforcements arriving. Examples of this kind of divergence include:
reinforcements called: the frigate showed up only for the pilot who called
a craft inspected: its flag, its group's count and the "has been inspected" message
the death of a far craft, which lasts some 60 ticks and fell between two reports
a departure through hyperspace or into a hangar, which a held copy never makes
In response, each is now sent as a reliable TieEvent the moment it happens.
The recipient of the TieEvent does the game's bookkeeping: setting flags, showing messages, or scoring the exit. Here is a running log of two connected machines:
Slots drift apart after a missed death; identified when a craft failed to show up for one player.
13 A sign bug from 1995
When trying the Z-95 Headhunter, one of the less maneuverable craft, I noticed that steering left turned it left, then rapidly right. The user_inputforplane function scales the stick by the craft's turn rate with xor eax,eax; mov ax,[inputdelta]; imul eax,ebx; sar eax,15 . The stick is a signed value, but mov ax into a cleared eax reads it unsigned and does not sign-extend it. Thus an axis of −d becomes 65,536 − d, so the result is 2·scale − d·scale/32,768, kept as 16 bits. When the scale is almost 0x8000, 2·scale wraps to nearly zero and the error vanishes.
 The Empire's fighters happen to have almost exactly the right scale to hide the bug (0x7FFF: the error is 2 units). However, the Z-95 has 0x5555, so a soft left becomes a hard left, and past two thirds of the stick the sign flips to a hard right. The shuttle and Y-Wing are affected by the same bug. The fix sets one register at the instruction after each sar , so that eax holds the signed product. OpenTIE has a similar fix in its own port.
The turn the game takes from the stick across: a Z-95 as the game computes it, and signed.
Drag-to-aim was endearing in the old game, and my mouse went through kilometers and kilometers of wheel motion as I brought my TIE around for another pass. But modern games usually prefer a point-to-aim mechanic for steering. This mechanic steers by the square of the pointer's distance once it leaves a small dead zone, an 8 × 8 pixel box around the gunsight. By default, craft bank as they turn, but this felt counterintuitive with point-to-aim. To zero out the banking, a hook at 0x5FAE1 hands the bank amount a zero. Sadly, TIE Fighter has no keyboard laser trigger. Space is largely unused, so the code now binds Space to hold the left mouse button in flight, except when the game itself is waiting for Space.
14 Knowing when a flight is over
The DOS build leaves maingameflag at 1 from a flight's end until the next flight is set up. So it cannot tell the debriefing from the flight, which left an awkward aiming reticle over the serious debrief conversation. It also took over the mouse, so that the player could only leave the debrief room by flying the mission again, like the Emperor's very own Mr. Bones' Wild Ride for his elite pilots. The mission end flag is a better trigger, with a caveat: the hyperspace arrival is a scene of its own that ends with the flag set for some 155 ms. For now, the workaround is to count a flight as over only once the flag has been set for 1.5 seconds.
The two flags through a flight, and the layer's "in flight" before and after the fix.
15 Two new cockpits for fan favorites
When playing TIE Fighter, the minute I heard the officer say "How pathetic. They must really wish to die flying those Z-95 Headhunters," I always wondered what it would be like to actually be inside one of those Z-95s. They seemed so inferior to the TIE Fighter, yet sported shields (paper thin) and the extra power that went along with them. Since the TIE Combat Chamber missions were tutorials for the controls, they seemed like excellent candidates to modify to use the Z-95 Headhunter. It would also be a chance to recycle that memorable line. However, the ship lacked a cockpit.
Similarly, after seeing Return of the Jedi, I always wondered what it was actually like to pilot an Imperial shuttle. Plenty of the Cygnus Spaceworks Assault Gunboat missions were solo missions. Since the Assault Gunboats were so much more capable than the Imperial shuttles, there was an argument that adding a second gunboat would be too strong. Instead, the second player (or both, if ion cannons were not required) would be put in the other Cygnus Spaceworks craft: the Lambda -class T-4a shuttle, the type the Rebels flew as the Tydirium .
Neither has a cockpit in the game's files. The shuttle's craft record names no cockpit at all; the game would ask for CP640\.INT . The Z-95's borrows the name XWING, and TIE Fighter ships no such cockpit. Since the game's art is never shipped with the page, anything new has to be made from the files in the player's own GOG package, so both cockpits are made at run time, by code, from the player's gunboat files.
Left, the gunboat as the game draws it. Middle and right, the shuttle and the Z-95: every pixel moved, cut or recolored by code from the gunboat's files.
When fediskio_loadspecies is called, the mission has been read and its craft types marked, but no craft or cockpit has loaded yet. There the player's craft is named SHUTTLE or Z95, and the files are written out beside the game's own. A cockpit's description ( .INT ) lists 28 views of 36 bytes, 95 instruments of 6 bytes from 0x3F0, and the instruments' sprite file. The new ones are the gunboat's with the view names changed, so gauges, scopes and displays sit where the gunboat's do. A view file holds a PANL sprite (the panel), a MASK (where space shows through), and a palette.
From the player's gunboat files to two new cockpits, at one hook, before the game looks for them.
// PANL: the panel sprite, one byte code at a time
0..250 a run of (op & 3) + 1 pixels of base + (op >> 2)
251 b a new base colour
252 c n n + 1 pixels alternating c, c + 1
253 n c n + 1 pixels of colour c (colour 253 itself: see-through)
254 end of the row
255 end of the sprite
 // MASK: for each of the 3-D view's rows (325 of 480 forward)
a signed state (not negative: space first), then run lengths that flip it
a run past 255: 0, then the rest − 256; past 511: 0, 0, the rest − 512
The shuttle: the gunboat's V struts are found in the mask as the longest stretch of rows where a hidden run, with space on both sides, moves smoothly. A line is fitted to their middles and widths and the bands cut out, the scopes' disks kept.
Two legs of an A are drawn leaning in, 122 pixels over 282 rows, pushed out until each outer edge just leaves the screen on row 313. Each leg's row is copied from a strut row that leans the same way, stretched to the leg's length, and drawn only where space shows, so the dashboard and scopes stay in front. A 24-row bar runs along the top with the scopes hanging from it.
The Z-95 (from my sketch: an arched canopy and a long nose): the struts come out, an arch goes in (the upper half of an ellipse, its legs down to the side consoles, each pixel a strut's row across its width), and a long nose runs from the dashboard's middle to the horizon.
The nose is drawn in the struts' own greys, picked from the panel's palette by brightness: lit along its top, a ridge seam, panel lines and seams across. Its foot sits flush on the display's bevel, row 277.
What the code works on: the masks, before and after. The struts on the left are found again here, for the picture, the way the code finds them: every row of both stretches.
The Z-95 reads its instruments from its own sprite file, the gunboat's with sprites 30 to 33 redrawn. The shield display's picture of your craft from behind is now a simple Z-95 rear view, --8[]8-- , one of the simplest and most accurate ASCII art views (a wing with a gun at each tip, an engine each side, the canopy on top). The targeting display's mask is chosen inside the program by the craft's number. While a shuttle or Z-95 flies, the emulator writes the gunboat's 480 bytes over the default and puts them back afterwards. Finally, the side views (keypad 7, 4, 1 and up; the game mirrors 9, 6, 3) are cut the same way. The shuttle's left-forward view gets the A's leg, the Z-95's the canopy hoop.
In flight, battle 10 mission 1: the host's gunboat (left) and the guest's shuttle (right).
16 Conclusion
In conclusion, the majority of the work was accomplished by adding the initial multiplayer to Wing Commander . Adding it to TIE Fighter proved that it was a repeatable pattern that could be applied to virtually any DOS game. Lobbylink continues to be an excellent, protocol-independent way to set up peer-to-peer links. I was worried that TIE Fighter's more crowded missions and precise aiming would be a poor fit for a loosely synced design where state is sent between peers repeatedly, but instead a simple design worked well. It's still very likely that, during the modem era, the best design for X-Wing vs TIE Fighter was the path its developers chose, sending inputs and keeping the simulations in lockstep, but in the current era of the Internet, it seems possible to sync craft of interest at high enough rates to make a game like TIE Fighter playable across the net.
Addresses are those of TIE95 (the GOG build of Z_TIE__.EXE ); they come from OpenTIE and were checked against the program. The pictures are frames from two-player flights.

## 评论（1/1）

> **daniel_rh** · 2026-11-19T20:01:10.000Z　
> Author here. A couple of weeks ago, I posted the Wing Commander together project https://news.ycombinator.com/item?id=50369895 which took 11 years (on and off). Folks in the video comments asked if the same approach would generalize to TIE Fighter.I gave it a try and added it to the TIE Fighter 32-bit DOS/4GB game in about 11 days with some machine-assisted tooling helping porting the hook layer, writing the cockpit generator for that Tydirium Shuttle I always wanted to fly and helping me debug some of the sync errors.TIE Fighter had these large spanning missions and relied a lot of exact aim as a gameplay mechanic, so I decided to have ownership of NPC craft shift around between players.
> And turns out since TIE Fighter has a demo from 1994, you can give it a try and if you like it can buy the GOG version. You can try it here: https://fireflyk64.github.io/tf/ , and hopefully I’ll see you online. Many thanks to the OpenTIE project for the address map.

## 导航

- 项目页：[[10-项目/fireflyk64.github.io_b1c2898b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
