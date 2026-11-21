---
type: "corpus"
item_id: "3f0feae6aab21761"
title: "Show HN: Full Production Studio, 77 open-source AI skills for video creators"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50577746"
project_url: "https://github.com/alfaris/full-production-studio"
author: "ahmedfaris_me"
published_at: "2026-11-20T16:51:51Z"
captured_at: "2026-11-21T14:45:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-21"
pub_day: "2026-11-20"
tags:
  - 语料
  - hn_show
  - author_ahmedfaris_me
  - story_50577746
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Full Production Studio, 77 open-source AI skills for video creators

> [!info] 一句话导读
> alfaris/full-production-studio

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50577746>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ahmedfaris_me　|　发布：2026-11-20T16:51:51Z
> 项目链接：<https://github.com/alfaris/full-production-studio>
> 采集：2026-11-21T14:45:01+08:00　|　id：`3f0feae6aab21761`

## 正文

# alfaris/full-production-studio

استوديو إنتاج متكامل — 77 open-source AI skills for video & content creators (ideas, content, motion, pro editing). Installs on Claude, Codex, Cursor, Gemini, ChatGPT.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: Other
- Homepage: https://alfaris.github.io/full-production-studio/
- Default branch: main
- Created: 2026-11-05T19:03:15Z

## Languages

- HTML
- JavaScript
- PowerShell
- Python
- Shell
- TypeScript

## Topics

- agent-skills
- claude-code
- claude-skills
- content-creation
- motion-graphics
- remotion
- video-editing
- youtube

## Top Contributors

- alfaris (15 contributions)
- claude (5 contributions)

---

## README

**English** · العربية

# 🎬 Full Production Studio

### 🌐 Browse all skills →

77 open-source **AI skills** for video & content creators, covering every stage from the first idea to the final export.
A **studio director** that runs the whole pipeline, plus the first **Arabic-first** creator skills.
Works with Claude Code, Claude.ai, Codex, Cursor, Gemini CLI, ChatGPT, and any agent that reads `SKILL.md`.

Release
License: MIT
Contributions welcome
skills.sh

---

## What's inside

Without guidance, AI output for scripts and motion graphics tends to be generic. These skills give your AI what it's missing: hook formulas, retention structure, easing and timing taste, Remotion know-how, editing rhythm, and export pipelines.

| | Section | What it covers |
|---|---|---|
| 💡 | **Ideas** | Research, strategy, competitor analysis, finding angles |
| 📄 | **Content** | Scripts, hooks, titles, your own voice, writing for every platform |
| 🎥 | **Motion** | Code-based motion graphics, Remotion, sound design, simulations |
| ✨ | **Pro** | Editing, captions, color grading, reframing, clip extraction |

You don't need to be a programmer. Pick whichever install method below fits the AI you use.

---

## 🔍 See the difference

Same input, without and with the studio. The caption and typography frames are **real renders**, not mockups.

| | Without | With the studio |
|---|---|---|
| **Arabic captions** `arabic-captions` | | |
| **Arabic text animation** `arabic-motion-typography` | | |
| **Hook** `arabic-hooks` | «أهلاً بكم في هذا الفيديو، سوف نتحدث اليوم عن أهمية الذكاء الاصطناعي في صناعة المحتوى.» | **«طلبت من الـAI سكريبت وطلعلك كلام ممل؟ المشكلة مش في الـAI… المشكلة في أول ٣ ثواني.»** |

- **Captions:** with ffmpeg's defaults, “Claude Code” jumps to the end of the sentence and the question mark lands in the middle.
- **Typography:** splitting Arabic into letters (the usual tutorial approach) disconnects and reverses it.
- **Hook:** the generic opening reads “Welcome to this video, today we will talk about the importance of AI…”. The studio's version means “Asked AI for a script and got something boring? The problem isn't the AI… it's the first 3 seconds.” Written by Claude following the skill.

## 🎬 Start here: the Studio Director

77 skills is a lot. You don't have to know any of them. Install the studio and tell your AI:

> *"Use studio-director. Make me a 45-second reel about ___."*

`studio-director` runs the project like a real production: **idea → script → visual plan → motion → edit → captions → export**. At each stage it picks the right skill, checks the result against a quality gate, and asks you for one decision before moving on. It runs a team of department heads that each report back with a handoff: `motion-designer` for motion graphics, `colorist` for the grade, `sound-designer` for the mix, `packaging-lead` for title, thumbnail and captions, and `distribution-lead` for exports, cut-downs and posting.

## 🌍 Arabic-first skills

The first open skills built **for Arabic creators**, not translated. They handle dialects (Egyptian, Khaleeji, Levantine), right-to-left layout, Arabic captions that don't break, Arabic kinetic typography, and Arabic YouTube SEO.

| Skill | What it solves |
|---|---|
| `arabic-voice` | Turns stiff, AI-sounding Arabic into the creator's real spoken dialect |
| `arabic-hooks` | 12 hook formulas with Egyptian and Khaleeji examples |
| `arabic-script` | Full YouTube scripts timed to Arabic speech rate |
| `arabic-shorts` | Reels/TikTok/Shorts in one pass, with RTL-safe screen layout |
| `arabic-titles-thumbnails` | Titles + thumbnail text as a pair, RTL placement, Arabic fonts |
| `arabic-market-research` | What's underserved in Arabic, competitors, the Ramadan/season calendar |
| `arabic-youtube-seo` | Keywords across dialects, spelling variants, chapters, tags |
| `arabic-transcript-cleanup` | Fixes Whisper's Arabic mistakes, marks fillers for cutting |
| `arabic-captions` | Captions with joined letters, correct RTL punctuation, word-by-word highlights |
| `arabic-motion-typography` | Arabic kinetic text in Remotion/GSAP without broken letters |

## 📦 Starter packs

Don't want all 77? Install a pack:

```bash
# 🎬 Director: one skill that orchestrates everything else you install
npx skills add alfaris/full-production-studio --skill studio-director

# 🌍 Arabic creator
npx skills add alfaris/full-production-studio --skill studio-director --skill packaging-lead --skill distribution-lead --skill arabic-voice --skill arabic-hooks --skill arabic-script --skill arabic-shorts --skill arabic-titles-thumbnails --skill arabic-captions --skill arabic-youtube-seo

# ▶️ YouTuber
npx skills add alfaris/full-production-studio --skill studio-director --skill packaging-lead --skill distribution-lead --skill yt-plan --skill yt-script --skill yt-package --skill yt-retention --skill yt-seo --skill yt-chapters --skill yt-edit

# 📱 Reels / TikTok / Shorts
npx skills add alfaris/full-production-studio --skill studio-director --skill packaging-lead --skill distribution-lead --skill short-form-video --skill yt-shorts --skill hook-and-headline-writing --skill video-caption-creation --skill reframe-social

# 🎥 Motion designer
npx skills add alfaris/full-production-studio --skill studio-director --skill motion-designer --skill sound-designer --skill motion-design --skill remotion-motion-graphics --skill motion-design-html --skill review-loop --skill sound-design --skill arabic-motion-typography

# ✂️ Video editor: learns how YOU edit, per client (Claude Code)
npx skills add alfaris/full-production-studio --skill studio-director --skill editor-apprentice --skill colorist --skill sound-designer --skill arabic-transcript-cleanup --skill cutting-rhythm --skill filler-removal --skill captions --skill audio-edit --skill color-grade
```

---

## ⚡ Install

### 1) Any coding agent (Claude Code, Codex, Cursor, Gemini CLI, Copilot …), one command
Uses the open `skills` CLI, which detects the agents you have installed:
```bash
npx skills add alfaris/full-production-studio
```
Install only some skills:
```bash
npx skills add alfaris/full-production-studio --skill yt-script --skill motion-design
```

### 2) Claude Code plugin
```bash
/plugin marketplace add alfaris/full-production-studio
/plugin install full-production-studio@full-production-studio
```

### 3) Install script (copies into your agents' skills folders)
```bash
git clone https://github.com/alfaris/full-production-studio && cd full-production-studio
./scripts/install.sh            # macOS / Linux / Git Bash, every detected agent
./scripts/install.sh claude     # just Claude Code  (~/.claude/skills)
```
```powershell
.\scripts\install.ps1           # Windows PowerShell
.\scripts\install.ps1 -Agent cursor
```
Targets: `claude` → `~/.claude/skills`, `cursor` → `~/.cursor/skills`, `gemini` → `~/.gemini/skills`, `agents` → `~/.agents/skills` (the shared folder that Codex, Cline, Zed, Warp and others read; `codex` is an alias).

**Your own skills are safe:** if you already have a skill with the same name (e.g. your own `captions`), the installer keeps yours and tells you. Add `--force` (`-Force` on Windows) only if you want to replace it.

### 4) Claude.ai (web / desktop app)
Download a skill `.zip` from the latest release, then go to **Settings → Capabilities → Skills → Upload skill**.

### 5) ChatGPT, Gemini, Claude Projects, or any chat AI
Download a skill `.md` from the latest release. Each one is a single file with the skill and its reference docs. Paste it into:
- **ChatGPT** → custom GPT → *Instructions* (or upload it as *Knowledge*)
- **Gemini** → Gem → *Instructions*
- **Claude.ai Project** → *Project instructions* / *Project knowledge*

---

## 📚 Skills

### ⭐ Studio originals (16)

_Written for this repo: the studio director that runs the whole pipeline, plus Arabic-first skills for Arab creators_

| Skill | What it does | Source |
|---|---|---|
| `arabic-captions` | Creates correct Arabic subtitles and burned-in captions. Covers SRT/ASS files, right-to-left punctuation fixes, Arabic font rendering in ffmpeg, line breaking,… | alfaris |
| `arabic-hooks` | Writes scroll-stopping Arabic hooks and video openings (first 1–15 seconds) in the creator's own dialect, using formulas proven on Arabic Reels, TikTok, Shorts and… | alfaris |
| `arabic-market-research` | Researches the Arabic content market for a niche (what's working on Arabic YouTube, TikTok and Instagram, competitor channels, audience questions, seasonal moments like… | alfaris |
| `arabic-motion-typography` | Animates Arabic text correctly and beautifully in Remotion, HTML/CSS/GSAP and After Effects-style workflows. Covers right-to-left layout, word-level (never… | alfaris |
| `arabic-script` | Writes complete Arabic video scripts (YouTube long-form, explainers, tutorials, talking-head, faceless) that keep viewers watching, in the creator's dialect, with… | alfaris |
| `arabic-shorts` | Plans and writes Arabic short-form videos (Reels, TikTok, YouTube Shorts, Snapchat Spotlight) end-to-end in one pass, covering hook, 20–60 s script, shot list,… | alfaris |
| `arabic-titles-thumbnails` | Creates Arabic YouTube titles and thumbnail text as a matched pair, handling right-to-left layout, mixed Arabic/English, digit style, length limits, and readability at… | alfaris |
| `arabic-transcript-cleanup` | Cleans Arabic speech transcripts from Whisper, YouTube auto-captions or other tools. It fixes dialect words the AI turned into فصحى, restores English terms written in… | alfaris |
| `arabic-voice` | Captures an Arab creator's real speaking voice (dialect, rhythm, signature phrases, code-switching) into a reusable Voice Card, and rewrites stiff or AI-sounding Arabic… | alfaris |
| `arabic-youtube-seo` | Optimizes Arabic YouTube videos for search (keywords across dialects and فصحى, spelling variants, Arabizi, bilingual descriptions, tags, chapters, and hashtags) so… | alfaris |
| `colorist` | The studio's Colorist. Owns the color of a video for the studio-director, covering log/HDR conversion, exposure and white balance correction, shot matching, a creative… | alfaris |
| `distribution-lead` | The studio's Distribution Lead. Owns stage 7 for the studio-director, covering platform-correct exports, vertical and square versions, cut-downs and repurposed posts, a… | alfaris |
| `motion-designer` | The studio's Motion Designer. Owns stage 4 (motion graphics) for the studio-director, taking a Motion Brief and delivering a finished motion package (look, storyboard,… | alfaris |
| `packaging-lead` | The studio's Packaging Lead. Owns stage 6 for the studio-director, turning the finished video into everything a viewer sees before and around it, which covers the title… | alfaris |
| `sound-designer` | The studio's Sound Designer. Owns the sound of a video for the studio-director, covering dialogue cleanup, music bed and ducking, sound effects synced to picture and… | alfaris |
| `studio-director` | The director of Full Production Studio. Takes a raw video idea and runs it through the whole pipeline (idea → script → visual plan → motion → edit → captions → export),… | alfaris |

### 💡 Ideas (8)

_Research, strategy, competitor analysis, finding angles_

| Skill | What it does | Source |
|---|---|---|
| `find-your-margin` | Help a knowledge worker find where their attention earns the fattest margin when combined with AI. Maps their skill stack against AI capabilities to identify… | cdeistopened |
| `invisible-threads` | Discovers non-obvious thematic connections ("invisible threads") across a corpus of essays, articles, or transcripts. | cdeistopened |
| `seo-research` | Strategic keyword research and content planning. Use this skill BEFORE writing to identify opportunities, validate topics, and create a research brief. | cdeistopened |
| `youtube` | The ultimate YouTube creator skill. Covers channel audits, video SEO, retention-engineered scripts, hook writing, thumbnail briefs, content strategy, content calendars,… _Optional Python scripts in execution/ need a YouTube Data API key._ | AgriciDaniel |
| `yt-audit` | Audit a YouTube channel end to end - packaging, consistency, the first fifteen seconds, and what to fix first. Use for "audit my channel", "why isn't my channel… | Jakeschincariol |
| `yt-plan` | Plan a week or a month of YouTube uploads - what to post, when, and in what order, sized to the creator's actual capacity. Use for "plan my week", "content calendar",… | Jakeschincariol |
| `yt-retention` | Read a YouTube Studio audience-retention export and find where viewers actually leave, then say what to change. Use for "why do people stop watching", "my retention is… | Jakeschincariol |
| `yt-viral` | Find what is actually working in the user's niche on YouTube and rank it by how far each video beat its own channel, then name the formula. Use for "what's working… | Jakeschincariol |

### 📄 Content (30)

_Scripts, hooks, titles, voice, writing for every platform_

| Skill | What it does | Source |
|---|---|---|
| `ai-tells` | Checklist of patterns that make writing sound AI-generated (filler openers, stacked connectors, rule of three, hedging). Use when reviewing or de-AI-ing a draft… | cdeistopened |
| `anti-ai-writing` | Transform AI-assisted drafts into authentic, human-sounding content. This skill provides patterns to detect and eliminate AI tells, frameworks for natural writing, and… | cdeistopened |
| `cold-open-creator` | Create 25-35 second cold opens that hook listeners by dropping them into a specific moment that encapsulates the episode's themes. Merge Descript's character-driven… | cdeistopened |
| `dude-with-sign-writer` | Creates punchy, conversational one-liners in "Dude With Sign" style - bold statements that challenge norms, validate feelings, or poke fun at everyday truths. Use when… | cdeistopened |
| `email-writing` | Write authentic, human-sounding emails that build relationships and drive action. This skill should be used when drafting welcome emails, follow-ups, newsletters,… | cdeistopened |
| `ghostwriter` | Turn source material (notes, transcripts, outlines) into authentic, human-sounding writing such as newsletters, articles, social posts and emails, using voice… | cdeistopened |
| `hook-and-headline-writing` | Create attention-grabbing hooks and headlines using 15 proven formulas, sticky techniques, and the 4 U's test. This skill provides systematic frameworks for generating… | cdeistopened |
| `how-newsletters` | Writing style reference based on case studies of successful newsletters. This skill should be used when the user wants to write in the distinctive voice and style of… | cdeistopened |
| `human-writing` | Transform AI-assisted drafts into authentic, distinctive prose. Use this skill when (1) reviewing or humanizing AI-generated content, (2) writing content that must not… | cdeistopened |
| `meta-ads-creative` | Create high-converting Meta (Facebook/Instagram) ad creative using the 6 Elements framework, proven ad formats, and research-driven copywriting. Optimized for lo-fi,… | cdeistopened |
| `podcast-blog-post-creator` | Transform podcast episodes into compelling, SEO-optimized blog posts in a conversational voice. Creates narrative-driven explainers (~1,000 words) that weave guest… | cdeistopened |
| `podcast-production` | Complete workflow for producing podcast episodes from raw transcript to publishable YouTube and social media assets. Four-checkpoint system for strategic… | cdeistopened |
| `seo-content-writer` | Write SEO-optimized content that ranks AND reads like a human wrote it. Use this skill AFTER completing research with `seo-research` skill. | cdeistopened |
| `short-form-video` | Create short-form video content (Reels, TikTok, Shorts) using practitioner methodology. Covers production workflow from concept to publish, hook construction, format… | cdeistopened |
| `social-content-creation` | Transform newsletters, articles, and podcasts into platform-optimized social posts using 180+ proven templates. This skill uses the framework fitting method to extract… | cdeistopened |
| `text-content` | Create high-performing text posts for social media using framework fitting method. 360+ proven templates across LinkedIn, X, Facebook, and Instagram. Progressive… | cdeistopened |
| `transcript-polisher` | Transform raw podcast transcripts into polished, readable documents. This skill removes filler words, fixes grammar, adds structure, and preserves authentic voice. Use… | cdeistopened |
| `video-caption-creation` | Create on-screen text hooks and captions for short-form video clips. Built around the Complementarity Principle - on-screen text should ADD to what the viewer hears,… | cdeistopened |
| `voice-pirate-wires` | Write in the Pirate Wires style - authentic, conversational, contrarian. This voice is direct and confident with irreverent humor, takes obvious-but-unsaid positions,… | cdeistopened |
| `writing-style` | Prose and voice standards (anti-AI patterns, voice principles, sentence style) originally written for another team's newsletter. Use when the user asks for a style pass… | cdeistopened |
| `x-article-converter` | Convert blog posts or newsletters into X/Twitter articles with handles inserted and a posting strategy. Use when the user wants to turn an article into X content,… | cdeistopened |
| `x-posting` | Post and schedule content to X/Twitter. Use when batch processing social posts, promoting podcasts/blogs, or scheduling content. Handles guest tagging, template… | cdeistopened |
| `youtube-script-writer` | Write a high-retention YouTube script — explainer, tutorial, video essay, review, or talking head — on the packaging then cold-open then value-stack then retention… | mohitagw15856 |
| `youtube-title-creator` | Generate high-CTR YouTube titles and thumbnails using framework fitting method. Match content to 119 proven formulas from Creator Hooks, apply psychological principles,… | cdeistopened |
| `yt-chapters` | Write YouTube chapters from a transcript, validated against YouTube's own rules so they actually render. Use for "add chapters", "timestamps", "break this video into… | Jakeschincariol |
| `yt-comment` | Draft replies to YouTube comments in the creator's voice, triaged by which ones are worth answering. Use for "reply to my comments", "handle the comment section",… | Jakeschincariol |
| `yt-package` | Write and lint the title and thumbnail for a YouTube video as one pairing, checking truncation, duplication and vagueness before publish. Use for "title ideas", "what… | Jakeschincariol |
| `yt-script` | Write a YouTube video script from a raw idea - hook options off 21 formulas, scored, then the full spoken script with the retention beats marked. Use whenever the user… | Jakeschincariol |
| `yt-seo` | Write the description, tags and search-facing text for a YouTube video, aimed at the query a real person types. Use for "write my description", "tags", "SEO", "help… | Jakeschincariol |
| `yt-shorts` | Find the Shorts hiding inside a long video and write them, using the transcript to pick self-contained moments. Use for "cut this into shorts", "clip this", "repurpose… | Jakeschincariol |

### 🎥 Motion (10)

_Motion graphics, animation taste, Remotion, sound design, visuals_

| Skill | What it does | Source |
|---|---|---|
| `motion-design` 🧰 | Taste rules for Remotion motion graphics — timing, easing, springs, typography, color, texture, and scene continuity, with concrete numbers. Use whenever you create,… | whaleyxbt |
| `motion-design-html` | Code-only motion design pipeline (no After Effects) for Raphaël / Howseen: launch films, showreels, product promos, LinkedIn/X videos, meme clips. Use when asked to… _Needs Node + Playwright + ffmpeg (and Python for the helper scripts)._ | howseen-ai |
| `nano-banana-image-generator` | Generate AI images using Nano Banana Pro (Gemini). Use this skill when the user needs images - thumbnails, social posts, blog headers, or creative visuals. Follows an… _Needs a Google Gemini API key._ | cdeistopened |
| `remotion-graphics` 🧰 | Create ANIMATED motion graphics — kinetic word-by-word captions, animated lower-thirds/name tags, branded intro/outro title cards, data-driven graphics (count-ups,… | agamm |
| `remotion-motion-graphics` | Create and edit motion graphics videos with Remotion (React): intros and outros, logo animations, promos, text animations, captions on footage, and compositing images… | haidrrrry |
| `review-loop` 🧰 | Visual self-review loop for motion graphics — render a draft, build contact sheets at every timeline beat, look at them, critique against a checklist, fix, repeat. Use… | whaleyxbt |
| `sound-design` 🧰 | Procedural sound design with the sfx engine — writing a cue sheet against a video's timeline, which sound goes with which visual event, gain hierarchy, panning, musical… | whaleyxbt |
| `video-overlay` 🧰 | Composite a graphic onto video — text, a logo/image, a static transparent PNG, or an animated effect — and place it accurately, including locking it to a moving subject… | agamm |
| `video-transitions` 🧰 | Join two clips with a visible transition effect (wipe, slide, dissolve, pixelize, circle open/close, fade-to-black, etc.) using ffmpeg xfade. Use whenever the user… | agamm |
| `web-sims` 🧰 | Build a simulation-style video (agents, particles, 3D machines, fly-throughs) as one HTML page whose render(t) is a pure function of time, then capture it frame by… | whaleyxbt |

### ✨ Pro (13)

_Editing, captions, color, reframing, clips and post-production_

| Skill | What it does | Source |
|---|---|---|
| `audio-edit` | Clean up or mix a video's audio track — normalize loudness, reduce background noise/hiss, or add background music (optionally ducked under speech). Use whenever the… | agamm |
| `captions` 🧰 | Add subtitles/captions to a video — burn them into the picture, or export an .srt/.vtt file (for YouTube etc.). Use whenever the user wants captions, subtitles,… | agamm |
| `color-grade` 🧰 | Color-grade a video — apply a cinematic look / LUT, or generate and compare candidate looks for the user to pick. Use whenever footage looks flat/muted/cold and needs… | agamm |
| `cutting-rhythm` 🧰 | Make an edit feel flowing, natural and snappy rather than merely accurate — split edits (J/L cuts), where to place a cut relative to speech and motion, how long to hold… | agamm |
| `editor` 🧰 | Turn raw footage into a finished edit in a specific genre/format — montage, documentary, tutorial, news, workshop, vlog, trailer, explainer. Use whenever the user wants… | agamm |
| `editor-apprentice` | Turns Claude into a video editor's apprentice. Claude asks the editor to teach it how they work with each client, splits that workflow into stages, works the stages the… _Claude Code only; needs Python 3.10+, ffmpeg and faster-whisper (asks before installing)._ | hamzts1412-web |
| `edl-edit` 🧰 | Build a multi-clip edit as an auditable JSON "edit decision list" (EDL) — a list of clips with source/in/out and a written rationale per pick — that one command renders… | agamm |
| `filler-removal` 🧰 | Remove filler words and disfluencies (um, uh, like, you know, basically) from a talking-head video so it sounds like they were never said. Use whenever the user wants… | agamm |
| `grok-video-edit` 🧰 | Apply AI-generated visual edits to video using xAI / Grok — change object colors, add effects (smoke, fire, sparkles), restyle scenes, or alter what's in a clip ("make… | agamm |
| `reframe-social` 🧰 | Reframe a video to a different aspect ratio for social platforms — vertical 9:16 (Reels/Shorts/TikTok), square 1:1, or 4:5 portrait — from horizontal source. Use… | agamm |
| `youtube-clip-extractor` | Download YouTube videos, identify compelling clips from transcripts, cut clips with ffmpeg, and generate platform-optimized on-screen text and captions. Complete… | cdeistopened |
| `youtube-downloader` | Download YouTube video transcripts when user provides a YouTube URL or asks to download/get/fetch a transcript from YouTube. Also use when user wants to transcribe or… | cdeistopened |
| `yt-edit` | Turn a raw recording's transcript into an edit decision list - dead air, filler cues and retakes, with timecodes. Use for "edit this", "cut the dead space", "tighten… | Jakeschincariol |

🧰 = needs its upstream toolkit repo cloned (the guidance itself works anywhere).

---

## 🔄 Updating from upstream

Upstream skills are copied from the original MIT-licensed repos, unmodified except where noted, and each repo is pinned to an exact commit in `sources.json`. Skills written for this repo (the director and the Arabic skills) live in `originals/`; edit them there, not in `skills/`.
To pull newer versions, change a `ref` in `sources.json`, then run:
```bash
python scripts/studio.py sync    # re-copy skills, regenerate both READMEs + AGENTS.md + catalog.json
python scripts/studio.py check   # validate every SKILL.md
```
Each skill folder includes `UPSTREAM.md` (source, commit, any changes) and `LICENSE.txt`. Push a tag like `v1.1.0` and GitHub Actions publishes the release files.

## 🙏 Credits

The director and the Arabic-first skills are original to this repo. Everything else is a curated bundle, and all credit goes to the original authors:

| Repo | Author | License |
|---|---|---|
| youtube-agent-skill | Jake Schincariol | MIT |
| claude-youtube | Agrici Daniel | MIT |
| pm-claude-skills (youtube-script-writer) | Mohit Aggarwal | MIT |
| claude-motion | whaleyxbt | MIT |
| claude-motion-design | Howseen | MIT |
| claude-remotion-skill | haidrrrry | MIT |
| video-agent | agamm | MIT |
| content-os | cdeistopened | MIT |
| editor-apprentice | Hamza Sayed | MIT |

Full license texts are in `THIRD_PARTY_LICENSES/`. The packaging (scripts, READMEs, installers) is MIT; see `LICENSE`.

## 关联链接

- https://alfaris.github.io/full-production-studio/

## 导航

- 项目页：[[10-项目/github.com_e498520f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
