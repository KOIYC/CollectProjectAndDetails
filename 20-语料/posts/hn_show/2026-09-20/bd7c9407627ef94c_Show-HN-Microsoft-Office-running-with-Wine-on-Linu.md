---
type: "corpus"
item_id: "bd7c9407627ef94c"
title: "Show HN: Microsoft Office running with Wine on Linux with no virtualization"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49746401"
project_url: "https://github.com/Tombert/office365_flake"
author: "tombert"
published_at: "2026-09-17T20:52:22Z"
captured_at: "2026-09-20T09:37:54+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_tombert
  - story_49746401
  - show_hn
metrics: {"points": 90, "comments": 87, "engagement_velocity": 90}
comments_count: 87
comments_total: 87
discovered_via: "hn:show_hn:90d"
---

# Show HN: Microsoft Office running with Wine on Linux with no virtualization

> [!info] 一句话导读
> Tombert/office365_flake

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49746401>
> 指标：点赞=90 · 评论=87 · engagement_velocity=90
> 作者：tombert　|　发布：2026-09-17T20:52:22Z
> 项目链接：<https://github.com/Tombert/office365_flake>
> 采集：2026-09-20T09:37:54+08:00　|　id：`bd7c9407627ef94c`

## 正文

# Tombert/office365_flake

A set of Nix Flakes and scripts to get Office 365 working on Linux without virtualization.

- Stars: 39
- Forks: 0
- Watchers: 39
- Open issues: 0
- Default branch: main
- Created: 2026-09-16T22:44:01Z

## Languages

- C
- Nix
- Python
- Shell

## Top Contributors

- Tombert (51 contributions)

---

## README

# Microsoft 365 on Linux via umu + GE-Proton (Nix flake)

Microsoft 365 (click-to-run Office) famously does not work on stock Wine. This flake is a
best-effort attempt to run it through **umu-launcher** with **GE-Proton** (the Wine build that
Valve/GloriousEggroll ship for games) instead, with the Bottles project's **ProtoSoda** Wine core
available as a second runner. It packages nothing from Microsoft: the Office Deployment Tool and
Office itself are downloaded at install time by the `ms365` script. You need a Microsoft 365
licence to sign in.

## Where the recipe comes from

* A February 2026 report in the Bottles tracker of Office 365 x64 running on Wine 10.20 with
 `corefonts msxml6 riched20 gdiplus`, the Office Deployment Tool and a couple of DLL copies.
* The classic ruados / eylenburg Office-on-Wine notes (Direct2D registry tweak, copying the
 `AppvIsvSubsystems*` and `C2R*` DLLs next to the Office binaries).
* The September 2026 Bottles announcement that Microsoft 365 installs, signs in (with 2FA) and runs
 Word on their Soda 11 Wine core in a Windows 10 prefix. GE-Proton 11 is the same Wine 11
 bleeding-edge lineage, and ProtoSoda is that Soda core in Proton layout, so both are offered.

## Usage

```sh
nix run .#ms365 -- install        # create prefix, winetricks, fetch ODT, download + install Office
nix run .#word                    # or: nix run .#ms365 -- run word ~/doc.docx
nix run .#ms365 -- status
nix run .#ms365 -- help
```

Or install it: `nix profile install .#ms365` gives you `ms365`, `ms365-word`, `ms365-excel`, ...
plus `.desktop` entries.

The install downloads several GB into `~/.local/share/ms365/odt/Office` and then runs the
click-to-run installer inside the prefix. Leave the installer window alone; it looks frozen for
long stretches.

## Knobs

All optional, all environment variables:

| Variable | Default | Meaning |
|---|---|---|
| `MS365_RUNNER` | `ge` | `ge` (nixpkgs `proton-ge-bin`), `protosoda` (Bottles Soda core), or an absolute Proton dir |
| `MS365_PREFIX` | `~/.local/share/ms365/prefix` | Proton compat-data dir (Wine prefix lives in `pfx/`) |
| `MS365_PRODUCT` | `O365ProPlusRetail` | ODT product id (`O365BusinessRetail`, `O365HomePremRetail`, `ProPlus2024Retail`, ...) |
| `MS365_CHANNEL` | `Current` | Update channel |
| `MS365_VERSION` | unset | Pin an Office build, e.g. `16.0.18129.20158`. Older builds are less likely to trip Wine |
| `MS365_EDITION` | `64` | `64` or `32` |
| `MS365_LANG` | `en-us` | Language |
| `MS365_EXCLUDE` | `Teams OneDrive Lync Bing Groove` | ODT `ExcludeApp` ids. Add `Outlook OneNote Access Publisher` for a minimal install |
| `MS365_WINETRICKS` | `corefonts msxml6 riched20 gdiplus` | Verbs applied before install |
| `MS365_ODT_SETUP` | unset | Use a local ODT `setup.exe` instead of downloading the current one |
| `MS365_SCA` | `0` | `1` switches to Shared Computer Activation (business subscriptions only) instead of vNext token licensing |
| `MS365_RADV_DEBUG` | unset | AMD driver flags to export as `RADV_DEBUG` (debugging aid, not needed) |
| `MS365_TRACE_MODULE` | unset | debugging: the shim logs every export lookup into this DLL and every failed lookup (`MS365_DEBUG=1` to see them) |
| `MS365_WAYLAND` | `1` | Wine's Wayland driver in a Wayland session; `0` for X11/Xwayland (popup menus close instantly there under sway and other wlroots compositors) |
| `MS365_DPI` | unset | Wine dpi. Unset: 96 × the focused sway output's scale (capped at 180, see "Known problems") on the Wayland driver, 96 on X11 |
| `UMU_LOG` | unset | `1` or `debug` for umu output |

Example, try the Soda core with a minimal install:

```sh
MS365_RUNNER=protosoda MS365_EXCLUDE="Teams OneDrive Lync Bing Groove Outlook OneNote Access Publisher" \
  nix run .#ms365 -- install
```

## Debugging

* Logs: `~/.local/share/ms365/logs/` (umu/wine stderr) and `~/.local/share/ms365/odt/logs/` (ODT).
* `ms365 exec regedit`, `ms365 exec winecfg`, `ms365 exec cmd`, `ms365 winetricks `.
* `ms365 install download` / `ms365 install configure` rerun a single phase.
* `ms365 reset --yes` deletes the prefix but keeps the downloaded Office payload.
* If a run wedges, `ms365 kill`.

## What it took (and where it stands)

Status as of 2026-09-16 with GE-Proton11-7 and Microsoft 365 Apps build 16.0.20326.20144:

* The Office Deployment Tool downloads and installs the full suite inside the prefix.
* Word starts (with `/q`, no splash screen), draws its start screen and ribbon, and shows the
 Sign in button. On first start it also raises a "Microsoft Office cannot verify the license"
 dialog because the licensing shim below reports no licences. Sign-in / activation has not been
 verified yet.
* Excel, PowerPoint, Outlook and the rest are installed but untested.

Fixes the flake applies automatically, each one found by reading the Wine and Click-to-Run logs:

| Problem | Fix |
|---|---|
| Installer error 0-2031 (17002): integrator aborts in `sppc.dll.SLInstallLicense`, a Wine stub | `sppc/`: replacement Software Protection Platform client DLL that accepts licence installs and reports nothing installed |
| Installer crash in the LastRun task: Wine's WinRT `PackageManager` returns `E_NOINTERFACE` for a newer interface and Office dereferences NULL | `appxdeploymentclient` DLL override disabled; Office logs the failure and continues |
| Excel never touches ole32, so the ole32 shim (all of the fixes below that live in it) never loaded there | the same DLL is also installed as `ms365shim.dll` and loaded into every process through `AppInit_DLLs`; whichever instance loads second stays passive |
| Word: `CoRegisterActivationFilter` missing from ole32 (mso30win32client dereferences NULL) | `ole32-shim/`: forwarder `ole32.dll` that re-exports the builtin (kept as `ole32_wine.dll`) and implements the function |
| Word: `SetFileShortNameW`, `FindPackagesByPackageFamily`, `SetThreadpoolTimerEx` not exported by Wine's kernel32; the loader binds them to aborting stubs | the ole32 shim registers a loader notification and rewrites those import slots in every module with benign replacements |
| Word: special user APCs (`QueueUserAPC2`) dispatched wrongly by this Wine, Office aborts | the shim hides `QueueUserAPC2` from `GetProcAddress`; Office uses its pre-20H1 path |
| Word: splash-screen thread crashes in combase during COM apartment teardown, Office's crash handler kills the app | Word is launched with `/q` |
| `mso.dll` and friends live in Office's VFS tree; the App-V redirection layer is unreliable under Wine | the VFS tree is mirrored into `Program Files` with symlinks |
| Office offers safe mode after every crash via a modal prompt | the launcher clears the Resiliency key before starting an app |
| Sign-in dies with 53u4r / 12009 after the password (or on the email page) | Wine's winhttp/wininet reject unimplemented option codes with 12009; the shim accepts them (winhttp 77/140, wininet 11) |
| Licensing dialog fails with E_NOINTERFACE | shim serves `ILanguageStatics` and `IJsonObjectStatics`, which Wine's WinRT factories lack |
| Word exits at start on the legacy licensing path | product set to vNext licensing mode (LicensingNext = 2), SCA off by default |
| Ribbon font/size boxes, Comments/Editing/Share buttons and the title-bar search field are solid grey blocks; a control only shows its text while hovered, icons vanish under the hover highlight | GE-Proton 11's Wine (11.0 base) ships a `d2d1` that ignores the fill mode of geometry groups. Office draws each control's border as two nested rounded rectangles with even-odd fill (a ring); Wine fills the union, and the compositor stretches that slab over the text. `d2d1-fix/` ships `d2d1.dll` from nixpkgs' Wine 11.16 (fixed upstream in February 2026) with its builtin signature blanked so Proton loads it, registered as a native override. |
| Dialogs (e.g. "save changes?") make the whole window flicker and the document area draw at the wrong scale on the Wayland driver; Excel shows black crosshair lines across the window | Office draws dialog shadows with unowned layered `MSO_BORDEREFFECT_WINDOW_CLASS` popups; the Wayland driver makes each an independent toplevel, sway tiles them and the layout reshuffles until the dialog closes. The shim gives those windows an owner (the active window), so they become transient and float |
| "Missing proofing tools" banner and no spell checking although the dictionaries are installed | Office finds its proofing tools through the Windows Installer API (component paths, feature states, "qualified components" per category and language), registrations the Click-to-Run integrator never writes under Wine. `msi-components.py` rebuilds all of them from the package manifests, and the ole32 shim answers the MSI calls Office makes with an empty product code (its "whichever package owns it" convention, imported by ordinal) from the registered products |

Debug aids: `MS365_DEBUG=1` writes Proton's Wine log with `+seh`; `MS365_DEBUG=1 PROTON_LOG="+module"`
lists every unresolved import ("No implementation for ..."), which is how the kernel32 gaps were
found. Office's own logs land in `drive_c/users/steamuser/AppData/Local/Temp` (`PUTER-*.log` for
Click-to-Run, `Diagnostics/ /` for the apps).

## Licensing and sign-in (where it stands)

Office licenses itself through the Windows Software Protection Platform (SPP), which Wine does not
have. The `sppc/` shim is a minimal stand-in: it stores the licence files the installer hands it,
serves the SKU policies from them, and lets the out-of-box 5-day Grace licence run with a persisted
timer. Nothing is reported as activated and no product keys are installed. Office's full SPP
validation still fails under Wine (0xC004E003), and on the legacy licensing path Word then refuses
to run ("Word has run into an error ... repair now?").

The flake therefore puts the product into Microsoft's token-based licensing mode ("vNext",
`HKCU\...\Common\Licensing\LicensingNext\ = 2`, what Microsoft 365 Apps use since
version 1910). In that mode Office skips the SPP validation, starts as "Unlicensed Product", and
licenses itself from the signed-in account through the Office Licensing Service. Shared Computer
Activation (`MS365_SCA=1`) is the alternative token mode for business subscriptions; a personal
subscription is refused there with "cannot be used to activate Office in shared computer
scenarios" (0x80004005).

Sign-in works with a personal Microsoft account: OneAuth is kept, both Web Account Manager paths
are switched off (`Common\Identity` and the Policies hives), the OneAuth broker is disabled and its
login page is rendered by the Edge WebView2 runtime (feature gates under
`ExperimentConfigs\ExternalFeatureOverrides`). The WebView2 runtime is not in the flake recipe yet:
`ms365 winetricks webview2` (680 MB) installs it into the prefix. Two request paths needed help from
the ole32 shim: Wine's winhttp and wininet reject option codes they have not implemented with
error 12009, which Office reports as sign-in error 53u4r / code 12009, so the shim accepts those
tuning options.

What has been verified: sign-in completes, Word shows the account's OneDrive documents, and Office
fetches the account's entitlements. What has not: an actual licence, because the test account had
no Microsoft 365 subscription that includes the desktop apps. In that case Office tries to open its
in-app purchase dialog, a WebView2 window in DirectComposition mode, and Wine's DirectComposition is
a stub, so Word exits with code 64 instead. Buy or manage the subscription on the web, then sign in
again in Word.

Other WinRT gaps the ole32 shim fills for the licensing code: `Windows.Globalization.Language`
statics (`ILanguageStatics`) and `Windows.Data.Json.JsonObject` statics (`Parse`/`TryParse`, built
on Wine's `JsonValue`).

## Known problems

* **Proofing categories are mapped by file role.** The Click-to-Run manifests list which qualified
 component categories a language package publishes but not which file each one stands for;
 `msi-components.py` maps them by name (speller and "Normal" dictionary to MSSP*.LEX, grammar to
 MSGR*.LEX, hyphenation and thesaurus split between engine DLL and lexicon). Spelling works; if
 hyphenation or the thesaurus (Shift+F7) refuse a language, those two mappings are the suspects.
* **Right-click and other popup menus close immediately under sway on the X11 driver**
 (`MS365_WAYLAND=0`). Office activates its popup, hides and re-shows it while positioning it, and
 sway's Xwayland layer moves keyboard focus back to the main window in between; Wine then sends
 Office the message that cancels the menu. The Wayland driver, the default, keeps focus inside Wine.
* **Wayland driver and HiDPI.** The driver reports the monitor at 96 dpi, so the launcher sets Wine's
 dpi from the sway output scale. At exactly 192 dpi Word overflows its main thread's stack while
 building its first window (an Office recursion; same on GE-Proton 11-6 and 11-7), so the automatic
 value is capped at 180, which renders and takes input correctly on GE-Proton11-7. GE-Proton11-6's
 driver mixed pixel and logical coordinates in the window geometry (input offset, no input at all
 at 168/180 dpi) and could get disconnected for committing a surface before its configure; the
 flake pins 11-7 for its Wayland fixes.
* **Direct2D comes from a different Wine** (`d2d1-fix/`): nixpkgs' Wine 11.16 `d2d1.dll` runs on
 GE-Proton 11's Wine 11.0. It only depends on public DLL interfaces, but if a future Proton bumps its
 Wine past the fix the override becomes unnecessary; if a future nixpkgs Wine adds a dependency the
 Proton base lacks, the launcher's log will show `d2d1` failing to load.

## Expectations

This is the college try, not a guarantee. Things that historically break: Microsoft account sign-in
(WebView2/Edge based), OneNote, Teams, and anything touching WinRT `Windows.*` APIs. If the
installer dies early, pin an older build with `MS365_VERSION`, or switch runners.

# Snapdrop

## 评论（87/87）

> **overclock-api** · 2026-09-17T21:06:52.000Z　
> Good work. I had assumed Office and Wine had been an unsolvable problem due to how long it had been around.What specifically breaks? My understanding is that the modern version of Office is in reality a combination of many things: the licensing layer, the .NET bits, the Click-to-Run packaging, and finally the app. If it turns out that the real hard part is the licensing/activation flow rather than the app itself, that is a more interesting discovery in that the problem is less about the app itself and more about how the distribution works. Which might also explain why it got easier to tackle.

---

> **farseer** · 2026-09-18T06:29:41.000Z　
> I feel like the entire world needs to take a plunge towards LibreOffice for the good of all.

---

> **alright2565** · 2026-09-18T16:31:28.000Z　
> I've done something similar with a CAD app, where I've used AI tools to package it as a Nix flake. It's a really good format for wine packaging since it makes it so easy to patch wine in ways that would never be accepted upstream, and it makes launching it just one command vs needing to deal with other people's potentially broken wine prefixes.

---

> **jmkni** · 2026-09-18T16:41:07.000Z　
> What version of Office are we talking about?

---

> **PeterStuer** · 2026-09-18T16:51:16.000Z　
> 365 on Linux with a sup? Why would MS not celebrate this? Windows consumer has been a loss leader for quite some time, and entreprise wont touch it till its 100% cleared.

---

> **robinpie** · 2026-09-18T16:59:14.000Z　
> Awesome!

---

> **TiredOfLife** · 2026-09-18T17:01:16.000Z　
> The bottles project https://x.com/brombinmirko also has been progressing with alpha being promised "soon"

---

> **rkagerer** · 2026-09-18T17:04:43.000Z　
> That's ok, I still prefer Word 2003 to the bloated, web-wired, ribbon-infested garbage that came after.https://news.ycombinator.com/item?id=47202540

---

> **Kwpolska** · 2026-09-18T17:14:18.000Z　
> Show HN is for things you made, not things where all commits are made by Claude.

---

> **pluc** · 2026-09-18T17:17:42.000Z　
> It's cool to see things that were entirely unnecessary popping up with the help of AI. Nobody ever cared enough to do this, nobody is going to use this, but now we can just shit it out knowing full well nobody is going to care. Just had to sacrifice humanity's knowledge and a few professions to get there.

---

> **tiahura** · 2026-09-18T17:44:56.000Z　
> Bravo! Beat me. Been working on this for a bit.

---

> **28304283409234** · 2026-09-19T00:59:43.000Z　
> Ok but why. Why on earth would i want to run microsoft office in 2026?

---

> **tombert** · 2026-09-17T21:14:54.000Z　
> Actually not that much breaks now!The hardest part was the activation, but some patience with Claude seemed to get that working.At least with Sway, I had trouble getting anything with X11 working, particularly anything involve "pop ups". That includes right-click menus and stuff like that. Wayland works much better.It also took a very long time to get the dictionary loaded for spell-check, and then a very long time to get the red squigglies working.

---

> **cyanydeez** · 2026-09-18T10:56:03.000Z　
> I've been trying to slowly do this. But muscle memory and visual cues, embedded for 15 years just keep winning.None of my excel sheets are just numbers, they're tied to database pulls and those dont work either.Just trying to do the same things like merge cells I'm searching through a bunch of menus wondering what the hell it's called.Theres a gui that looks similar but not enough. If they really want adoption, they need to completely add a office-clone mode and accept the consequences.

---

> **tombert** · 2026-09-18T15:37:01.000Z　
> I agree with you in principle, and I honestly genuinely kind of hate Microsoft Office and I haven't used it or LibreOffice since I learned how to do LaTeX and Pandoc and Typst.That said, whether or not it should be the case, a lot of people want specifically proper noun Microsoft Office (TM), not something "as good or better" than Microsoft Office.I think getting people people towards a less horrible computing setup, for most people, requires it being done incrementally.

---

> **Daviey** · 2026-09-18T16:32:43.000Z　
> The biggest blocker for me is having confidence my output renders the same with people using MS Office, pdf output isn't always sufficient.

---

> **revolvingthrow** · 2026-09-18T16:35:53.000Z　
> The network effect of social media has nothing on the network effect of ms office

---

> **brightball** · 2026-09-18T16:46:16.000Z　
> Makes me wonder about aiming all those subscriptions at LibreOffice. How fast could it be improved to gain parity or surpass MS Office?Maybe the new Omarchy foundation thing will take it on. DHH has pretty publicly been asking for a version of office for Linux.

---

> **TiredOfLife** · 2026-09-18T16:58:23.000Z　
> That would require LibreOffice not being shit.

---

> **fluidcruft** · 2026-09-18T17:01:43.000Z　
> I can't tell what's going on with all the LibreOffice drama and whether it's a zombie on life support after the professional community management class kicked all the actual developers out (my take away).

---

> **bastardoperator** · 2026-09-18T17:03:40.000Z　
> I avoid both like the plague. These apps make me feel less productive and the docs they produce always look ugly to me. I would rather md, html or latex.

---

> **chris_money202** · 2026-09-18T17:03:51.000Z　
> The word editor isn't really Microsoft's product, it's just one of the many entry points to the Microsoft Office cloud sphere where all the data can be interconnected and shareable.

---

> **ducktective** · 2026-09-18T17:04:21.000Z　
> For starters, universities and government offices should not expect a proprietary format. Everyone should accept OpenDocument Format (ODF) or a similar FOSS format. MS Office, LibreOffice, OpenOffice and whatnot can compete in editing and rendering open formats.Come to think of it, this is a good proposal for EU, thanks for the USB-C, by the way :)

---

> **glimshe** · 2026-09-18T17:11:28.000Z　
> I think LibreOffice is an outdated and overall awful piece of software. It's not like Open Source champions like Linux, Blender and Godot at all.Its only advantage is being Free. This product couldn't survive in the market if it was paid, arguably at any price. I really tried it to use and love it, but LibreOffice is just terrible.

---

> **GuB-42** · 2026-09-18T17:28:25.000Z　
> Except that Microsoft Office is just better.But with the awesome job Microsoft does at breaking it, maybe in a few years, LibreOffice will be a good alternative, if the LibreOffice guys don't screw up too much on their side.

---

> **mahboi** · 2026-09-18T17:40:45.000Z　
> Realistically, the world is just gonna AI-plow their way through old moats like this. Don't know about new ones.

---

> **tombert** · 2026-09-18T16:34:30.000Z　
> Yeah, completely agree.I absolutely love Nix Flakes; they feel, to me, like what Docker was supposed to be. A little self-contained packaged environment that gives you a place to do any kind of custom hacks deterministically.

---

> **tombert** · 2026-09-18T16:48:00.000Z　
> The latest version of Office 365. Well, latest as of about four or five days ago. It required me to buy a month of it for $15.I have been trying to get one of those gray-market keys from Groupon working, but that has proven to be very difficult because there's a lot of weird kernel-level stuff going on for verification because those are done with volume-licenses. If I were willing to pay full-price for a regular Office 2024 Home and Business key I think it would be relatively easy to adapt this to get it working, but I don't want to sink $200 for software I'm unlikely to ever actually use.

---

> **milgrum** · 2026-09-18T17:15:03.000Z　
> probably the support burden, plus they already have o365 web apps that work on linux. office breaks in new and exciting ways on windows all the time, and they have full control over that. I <3 linux but I never want to support wine office in an enterprise environment, sounds like a total nightmare

---

> **tiahura** · 2026-09-18T17:48:22.000Z　
> Because they want to phase out the windows apps too.

---

> **tombert** · 2026-09-18T17:07:10.000Z　
> Interesting, I hadn't heard of this actually, though it looks like there's a good chunk of overlap in what we were doing.I suspect what they're doing is better than what I did. I just was happy I got something working and wanted to share.

---

> **tombert** · 2026-09-18T17:09:42.000Z　
> Yeah, I think I mentioned it here a few months ago, but I got Office 97 working with Wine, and I was sort of flabbergasted at how usable it still is. It worked fine with my system's TrueType fonts, it does all the formatting I care about, and given that it's nearly 30 year old software it runs obscenely fast. If I weren't a grumpy die-hard CLI person I would probably still consider using it.All that said, there are a lot of people who want the absolute latest MS Office. I don't get it either.

---

> **mahboi** · 2026-09-18T17:36:56.000Z　
> I'm glad this is still a complaint. I used Office 2004 (same as 03) until 2013, when I absolutely couldn't anymore because of docx incompatibility. My wife still uses 07, sadly it's ribboned.

---

> **aroman** · 2026-09-18T17:17:15.000Z　
> Shall we also ban projects that are not authored directly in bytecode? Surely it's not really "made by hand" if you used a higher level interpreted language.
> But seriously: software engineering is all about leveraging abstractions/indirection where appropriate for the job to be done. It's kind of... the whole point: https://en.wikipedia.org/wiki/Fundamental_theorem_of_softwar...

---

> **tombert** · 2026-09-18T17:21:57.000Z　
> To be fair, I actually emailed HN moderation before I submitted this because I actually sort of agree. They said I should go ahead and submit it because there might be some interest in this.

---

> **drnick1** · 2026-09-18T17:22:54.000Z　
> Yes, sure, let's pretend we are back in 1995 and write C by hand on a beige Pentium tower.

---

> **qwerpy** · 2026-09-18T18:21:14.000Z　
> Disagree, if it provides value to me I don’t care who or what built it. This provides value to me. I’m stuck on windows and eventually want to get out, and MS Office (specifically OneNote) is one of the remaining hurdles. This gives me hope that it’s only a matter of time. For the anti-AI people they can wait for someone can do a "proper", artisanal human-written version that builds on the problems that were solved by the AI-written version here.

---

> **tombert** · 2026-09-18T17:20:46.000Z　
> Uh, what?I actually think a lot of people cared enough to do this; the entire Wine project sort of exists specifically because people want Windows software on Linux.I know multiple people who have said that they won't use Linux specifically because it doesn't have the full-fat desktop version Office on there."Unnecessary"? Sure, I guess, I don't like MS Office and I don't use it, but a lot of people seem to really like it, whether or not they should.

---

> **cyberax** · 2026-09-18T17:23:06.000Z　
> Is anything YOU do useful?This is a very useful project for me, because I occasionally need real Excel.

---

> **mahboi** · 2026-09-18T18:15:50.000Z　
> This is pretty necessary for tons of people considering Linux

---

> **tombert** · 2026-09-18T17:51:35.000Z　
> I mean, all I did was use a large chunk of free time and Fable tokens. I wish I could say that my big brain and software engineering prowess is what got it working, but mostly it was just staring at text and not having anything better to do.

---

> **tombert** · 2026-09-19T04:43:16.000Z　
> I'm with you. You're not my parents.

---

> **yjftsjthsd-h** · 2026-09-18T16:57:10.000Z　
> > At least with Sway, I had trouble getting anything with X11 working, particularly anything involve "pop ups". That includes right-click menus and stuff like that. Wayland works much better.? Sway is a Wayland compositor

---

> **passthejoe** · 2026-09-18T17:43:32.000Z　
> Today's generation of kids is using Google Apps in school and has no ties to MS Office. SAAS in general will make MS Office much less relevant. Things like Canva and Photopea are doing the same to Adobe.

---

> **MrDrMcCoy** · 2026-09-18T16:42:30.000Z　
> That has been a lot less of a problem lately. Why not try again and open a bug report if there's an issue?

---

> **hagbard_c** · 2026-09-18T16:45:51.000Z　
> As long as that is the goal Microsoft can block uptake of any competitor simply by making sure that is never achieved. They have a lot of history with this - DOS ain't done 'till 1-2-3 won't run etc. - so you can rest assured that they'll do it again. Maybe you should change your output so it isn't as reliant on 'rendering the same', i.e. make it less complex and with that less easy for Microsoft to claim the error lies with the other party? Word is not a DTP package nor a typesetter, it is a document editor. Fancy layout has never been the forte of this class of programs, they're meant to make sure the output works on different computers, different printers, different monitors.

---

> **drnick1** · 2026-09-18T17:18:05.000Z　
> When is a PDF not sufficient? I write all my reports/letters in LaTeX and if someone complained about receiving a PDF, I would send them the source and wish them good luck.

---

> **varispeed** · 2026-09-18T17:02:59.000Z　
> You can try to use LibreOffice all you want, until you receive a form to fill where LibreOffice doesn't display checkboxes and recipient won't accept "x", because their automated software only uses MS Office and won't properly attribute it to questions.

---

> **ray_kay777** · 2026-09-19T23:43:47.000Z　
> Yep, I've seen this come up time and time again in the legal world and Microsoft 365 is so entrenched in the legal world that there is 0 chance of change in at least the next decade, and probably in the next 20 years.

---

> **varispeed** · 2026-09-18T17:03:43.000Z　
> With such an advancement of AI, can't parity be vibe coded?

---

> **DaSHacka** · 2026-09-18T17:06:43.000Z　
> Can you elaborate more on this? This is the first time I'm hearing about it.

---

> **mahboi** · 2026-09-18T19:46:50.000Z　
> It's not even the only "Open" vs "Libre" drama. There's SSL too.

---

> **tombert** · 2026-09-18T18:19:37.000Z　
> Can't speak for every graduate program or every school, but when I was in grad school at University of York, we actually used Overleaf with LaTeX a lot, since it allowed shared collaborative editing.I liked that because it's still an open format.

---

> **kasabali** · 2026-09-18T18:35:59.000Z　
> The problem with this is Microsoft foresaw it and pushed (bribed?) OOXML through ISO and now there's no standing on "forcing" an open standard without OOXML being one.

---

> **winrid** · 2026-09-18T17:14:11.000Z　
> OpenOffice is older and outdated compared to Libre, which did you try?

---

> **anon48293** · 2026-09-18T17:27:53.000Z　
> Try onlyoffice

---

> **ducktective** · 2026-09-18T17:46:49.000Z　
> >outdatedWhat modern features are you looking for in a say, document editor? My experience with LibreOffice Writer and Calc has been excellent. I'm happy there is no modern AI or cloud integration noise or ribbon bars with excessive whitespaces.

---

> **nonethewiser** · 2026-09-18T19:39:11.000Z　
> I always wonder how people can suggest LibreOffice over Word or Google Docs. Its much worse. Either people are just extremely motivated to use it or they don’t actually use it.You are exactly right that it is not an open source success. I wish it were.

---

> **mahboi** · 2026-09-18T21:09:06.000Z　
> Also, it's not even a joke anymore how Wine is the most stable Linux ABI

---

> **aroman** · 2026-09-18T17:18:32.000Z　
> nix + LLMs is the most fun I've had with personal computing since I burned an Ubuntu live CD in middle school

---

> **creshal** · 2026-09-18T18:04:15.000Z　
> doc vs docx is whatever, what kills older offices for me is the 64k row/col limit in excel. That was only fixed with the ribboned versions. :(

---

> **rkagerer** · 2026-09-18T23:24:22.000Z　
> Do you have the docx compatibility pack installed?

---

> **mahboi** · 2026-09-18T18:16:54.000Z　
> That's solid

---

> **pluc** · 2026-09-18T17:25:42.000Z　
> I'm not talking about WINE, I'm talking avout what you had Claude build to use it.If this were a proof of concept and you had the ability to say what you did different to make it work better than previous attempts that would be great, but i don't think you know.

---

> **tombert** · 2026-09-18T17:00:25.000Z　
> I use it as my desktop environment. I was using XWayland at first to get this working since that was historically the norm with Wine stuff, but that ended up being really glitchy. The latest versions of Wine/Proton actually have native Wayland support though so once I forced that it ran significantly better.I don't know if this is an XWayland problem, or a problem with X in general, since I don't have any computers running X anymore.

---

> **tombert** · 2026-09-18T17:49:16.000Z　
> Sure; honestly this is just for people like my parents.I am slowly trying to build the case that they should switch to Linux, especially if they expect me to play IT for them.

---

> **afavour** · 2026-09-18T17:02:06.000Z　
> Because there’s no one and done testing for it. You need to check every document you make with Office (so you’re paying for Office anyway…) to ensure it’s correct.All very well for an open source software project but for software you’re using day to day to achieve other, business central, goals, it’s a lot of lost time with little benefit.

---

> **tombert** · 2026-09-18T17:25:27.000Z　
> That is actually why I got into LaTeX in the first place!My resume was initially done with LibreOffice and I'd send recruiters a PDF, and they would ask for a .docx, and when I would send that they would screw up all the formatting by inserting their ugly logo on the top.When I "ported" my resume over to LaTeX, I would send the PDF and they'd ask for a .docx, I would say "Oh, the resume is done in LaTeX. Here's a link to the source and instructions on how to compile it, feel free to do what you need".Then they would just submit the raw PDF.

---

> **Daviey** · 2026-09-18T18:02:53.000Z　
> When I need other people to continue editing it.I also prefer LaTeX, I've written hundreds of letters, multiple papers, a few thesis and my CV (maintained for the last ~20 years). But the defacto for business documents sadly isn't LaTeX.

---

> **fluidcruft** · 2026-09-18T17:11:14.000Z　
> https://news.ycombinator.com/item?id=47599305https://news.ycombinator.com/item?id=47652324

---

> **vrighter** · 2026-09-18T19:06:29.000Z　
> how about requiring the format to actually be specified? Isn't ooxml filled with tons of chunks saying "and then this will behave like word 95 did" and not specify what tat is

---

> **glimshe** · 2026-09-18T17:50:17.000Z　
> Both. Neither is a viable mass-market alternative in my opinion. Cross-platform office software is just a difficult problem. I think they could be appropriate for some nonprofit/government work, which I think is where they do well today.

---

> **staindk** · 2026-09-18T19:23:52.000Z　
> I mostly just want UI icons that make sense. The LibreOffice icons all look samey to me, can never find what I'm looking for.

---

> **tombert** · 2026-09-18T17:56:52.000Z　
> Same. I've had a lot of good luck getting Claude to make Flakes and then adding it to my Jovian Steam console to play it; it allows me to even pre-set stuff like mappings for my Xbox controller.https://hub.brucewillis.sexy/~tombert/game-flakes/sources (I promise, safe for work, despite the URL).

---

> **tombert** · 2026-09-18T17:31:08.000Z　
> The stuff that was done differently was the shim to get the activation working, and the fact that modern Wine has native Wayland support that helps avoid a lot of graphical glitches.I'm not entirely sure what your point is though? Are you suggesting I don't know how to write software? I've been doing this for a very long time, well before generative AI.

---

> **hagbard_c** · 2026-09-18T17:22:52.000Z　
> > for software you’re using day to day to achieve other, business central, goals......you should use something which is reliable, no more complicated than needed for the purpose, which assures documents made now can be read in the distant future, keeps your confidential information out of the wrong hands and which is sure to be available to anyone who needs to have access to it.Doesn't really sound like Microsoft Office is a good fit if you ask me.

---

> **menotyou** · 2026-09-18T20:25:12.000Z　
> ..or they would just not submit it at all.

---

> **illiac786** · 2026-09-19T04:19:17.000Z　
> What? And this got approved by ISO?!?

---

> **winrid** · 2026-09-18T19:30:10.000Z　
> I agree with that. They are only usable if you're fairly technical.

---

> **afavour** · 2026-09-18T18:33:13.000Z　
> You want to use the same stuff your clients use, that’s guaranteed to look the same on their computer. So Office it is.

---

> **tombert** · 2026-09-18T20:29:23.000Z　
> As far as I am aware that never happened. Every time this particular situation has happened, I have gotten a callback.

---

> **vrighter** · 2026-09-19T06:11:25.000Z　
> It sure did! and because those products aren't sold anymore, it's impossible to legally implement the standardc as even with the "full" spec, you need to reverse engineer stuff from unavailable software

---

> **hagbard_c** · 2026-09-18T19:53:33.000Z　
> Well, you want to be using what your clients can read, it doesn't have to the the same software. This is true for most file formats - audio, video, image/graphics (the latter more restricted due to other entrenched proprietary formats) - but the 'office' space (no pun intended) is still suffering from decades of abuse of its position os operating system vendor by Microsoft. Windows is only getting worse with every release so it is just smart business sense to steer away from it and things depending on it. Microsoft Office is one of the few remaining reasons often quoted for staying with this deteriorating platform so there are other incentives to move away from it. The best moment for moving away from Windows was years - or decades - ago. The second best moment is now.

---

> **Daviey** · 2026-09-19T10:08:43.000Z　
> If you did this to me, fine.If you had done this to a recruiter that funnels screened people to me, I'd make sure to not interview you. It shows total lack of awareness of how to deal with non-tech people, verging on arrogance.

---

> **tombert** · 2026-09-19T10:52:32.000Z　
> …what?How would that work logistically? You would get a regular resume with formatting that isn’t fucked up and you would think “this is a guy who I shouldn’t hire”? You’d have a stack of resumes, all of which are broken, and you’d see one that isn’t and that would be a red flag?How exactly is it “arrogant”? I didn’t like that my resume formatting was breaking because of the people who insisted on inserting their ugly logo on top the page. I had historically asked them to stop doing that, or at the very least to show me the end result before they submitted, and they would simply not work with me. I think my solution actually demonstrates a lot of awareness in how to deal with “non-tech people”.

---

> **Daviey** · 2026-09-19T13:41:13.000Z　
> The recruiter wouldn't compile anything, they'd just tell me "this guy sent me a GitHub repo instead of a CV", or more likely just not mention your application. A recruiter who reliably funnels screened people to me is worth far more than any single application, so that's how it plays out logistically - you get dropped and never hear about it. "As far as I am aware" is carrying a lot of weight there.The arrogant bit is "here's a link to the source and instructions on how to compile it, feel free to do what you need". A recruiter asking for an editable version wants something they can drop their letterhead on and forward to the client. Handing them a build task assumes they have both the skills and the inclination to meet you on your toolchain. Nobody expects you to be their typesetter either; the difference in skills isn't the problem, assuming the difference away is.That mismatch is the part I'd actually be screening for. A company is mostly non-engineering people: sales, support, HR, PMs who can't read a diff. The recruiter is the one non-technical person in your hiring pipeline, and how you handle them is a sample of how you'd handle the fifty you'd work alongside. If the instinct is to make them come to your toolchain rather than meet them where they are, that plays out in every meeting and every "quick question" from sales for as long as you're employed. The CV is the one document whose entire purpose is to sell you to a non-technical audience, and handling that poorly is telling.I've maintained my own CV in LaTeX for ~20 years and would never dream of sending a recruiter a Makefile and telling them to work it out.Sent to me directly? Fine, I'd read the repo, probably be impressed, might even see if I could improve mine from it. That was never the scenario though.

---

> **tombert** · 2026-09-19T19:26:56.000Z　
> I don't agree with you being mass-downvoted, since you're just espousing your opinion, even if it's one I don't agree with.That said, I think we're at a fundamental disagreement here; the recruiters would screw up the formatting in a way that would make the resume say things that are flatly untrue. It's not just aesthetic. For example, I used to put the amount of experience I had in different technologies, and because they would break the alignment it would look like I had more years experience with Node.js than Node.js had even existed at that point.When I would politely ask recruiters to, at the very least, send me the updated resume with their ugly logo so I could point these things out, they would universally agree and then never actually do it before sending it to the potential employer. This was literally 100% of the time, there was not a single outlier here. That's not nothing; a competent interviewer might think they've caught me in a lie and not move forward. I'm no exception; if I saw that a person said they had more experience with a technology than the laws of physics would dictate, I would assume they're full of shit and pass on the resume.So you tell me, what exactly should I do? Waste my time and the technically incompetent recruiter's time and the interviewer's time because they think I'm more qualified for something than I ever said I was? Or I could simply, hear me out, create a situation where these "non-tech people" can't screw this up, because they invariably would. I guess you can call it "arrogant" if you want, but I really think it's considerably less douchey than wasting everyone's time.With the advent of LLMs they could point Claude to the LaTeX source and get it in any format they want. Or they could, and I think they largely did, just forward the raw PDF (which I always provided), maybe using Preview to insert their ugly logo somewhere where it doesn't screw up formatting. If they had asked me to do the logo insertion, I would have inserted it myself because I'm not incompetent with typesetting.Frankly, though, the resume is actually working as intentional, because I do not believe that I would be a good culture-fit on your team so it would be best not to waste your time anyway.

## 导航

- 项目页：[[10-项目/github.com_8e89b866]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
