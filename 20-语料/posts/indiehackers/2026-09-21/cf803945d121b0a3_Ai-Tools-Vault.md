---
type: "corpus"
item_id: "cf803945d121b0a3"
title: "Ai Tools Vault"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/ai-tools-vault"
project_url: "https://aitoolsvault.site/blog/chatgpt-images-2-5-review"
captured_at: "2026-09-21T09:47:43+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-09-21"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Ai Tools Vault

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/ai-tools-vault>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：<https://aitoolsvault.site/blog/chatgpt-images-2-5-review>
> 采集：2026-09-21T09:47:43+08:00　|　id：`cf803945d121b0a3`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
AI Tools Vault
 Discover, Compare & Explore the Best AI Tools
Visit Website
AI Tools Vault Discover, Compare & Explore the Best AI Tools
 Posts 30+
 Revenue $0 / mo
 Website Facebook
September 20, 2026
 I Almost Bought the Wrong AI Sales Tool for My 2-Person Sales Effort
Small team, trying to get outbound moving, and nearly signed up for a shiny AI email-writing tool before realizing it solved a problem I didn't actually have.
 What I got wrong at first
 I assumed the bottleneck was "our emails aren't good enough." Turns out — checked the actual numbers — my reply rate on decent-quality emails was fine when I reached the right people, and terrible when I didn't. The problem was never the writing. It was who I was writing to.
 That's the distinction that would've saved me a subscription: generative AI tools write content (emails, summaries, sequences). Predictive AI tools score and prioritize who's actually worth reaching out to. I was about to buy the first kind for a problem that needed the second kind. Apparently I'm not alone — only around 18% of field sales teams have activated any kind of AI lead scoring, despite 87% of sales orgs using AI in some form. Everyone's got the flashy tool. Almost nobody's got the boring, high-leverage one.
 What I actually needed
 Something to enrich and prioritize my lead list before I wrote a single email. Ended up looking at data enrichment tools instead of outreach-writing tools — completely different category, and the one that actually mattered for a team my size.
 The other thing worth knowing before buying anything in this space
 A lot of "AI SDR" marketing blurs a real distinction: is it actually deciding who to contact and when on its own (agentic), or is it a normal automated sequence with AI-generated text dropped in (still fundamentally scripted)? Worth asking directly — the price difference between the two is usually significant, and so is what you're actually getting.
 Where I ended up
 Smaller, more targeted list, worse-looking (less polished) emails than the AI-writer tool would've produced, way better reply rate. The lesson wasn't "AI doesn't help sales" — it was "match the tool to the actual constraint, not the flashiest demo."
 More detail on my blog: AI Tools for Sales Teams — What's Actually Worth Adopting , original on my site: AI Tools for Sales Teams in 2026 . If you're also hiring, the recruiting side has the identical generative-vs-predictive split: AI Recruitment Software .
 Anyone else here almost bought the wrong category of tool before catching it? What tipped you off?
13jawad
4 Likes
Comment
September 18, 2026
 What I Learned Building a Study Tool: Not All "AI for Students" Is the Same Product
Been building a small side project aimed at students this year, which meant actually studying the AI-tools-for-students space properly instead of just skimming listicles. Turns out the space is way less crowded with genuine competitors than the headline count of tools suggests — most of them aren't actually competing with each other.
 The split that actually matters
 Two fundamentally different products get lumped into "AI for students":
 Grounded tools like NotebookLM only answer from documents you give them. Can't hallucinate a fact that isn't in your uploaded material — the trade-off is it's limited to exactly what you fed it.
 General assistants like ChatGPT and Claude draw on broad training, which makes them more flexible but means they can occasionally state something wrong with total confidence, especially on specific academic details.
 This distinction mattered a lot for scoping my own project — I ended up building around the grounded approach specifically because the reliability story is easier to explain to a student user than "trust it, mostly."
 Where the actual tools land, by job
 Research/lit review: Consensus and Elicit for paper summarization at scale, Perplexity for cited web research, NotebookLM for grounded synthesis across your own uploaded sources.
 Writing: Claude for long-form academic writing specifically, ChatGPT as the general-purpose drafting partner, Grammarly for editing plus an authorship-tracking feature that's actually clever from a product design standpoint — it addresses the AI-detection false-positive problem directly instead of ignoring it.
 Studying: Quizlet auto-generating flashcards from uploaded material, NotebookLM's audio-summary feature for passive review.
 STEM: separate reliability model entirely, worth its own dedicated breakdown rather than folding into a general list.
 The integrity question, from a builder's perspective
 Every one of these products has to navigate the same tension: helpful enough to actually save time, careful enough not to enable straightforward academic dishonesty. The ones handling this well (Grammarly's authorship tracking is the clearest example) are building transparency into the product itself instead of leaving it as a policy problem for the user to manage alone. That's a genuinely interesting product design lesson beyond just the student-tools space.
 What this means if you're picking tools, not building them
 Don't collect every tool on every list. Pick two or three based on your actual bottleneck this semester — writing speed, dense-reading comprehension, research discovery, or problem-set verification — and skip the rest.
 More on this
 Longer version on my blog: Best AI Tools for Students and Researchers , original on my site: Best AI Tools for Students and Researchers in 2026 . Related if math/STEM is part of your workload: AI Calculator Online .
 For anyone else building in this space
 The genuine white space isn't another general chatbot for students — it's tools that solve the reliability and integrity problems honestly instead of pretending they don't exist. That's the harder, more interesting product to build.
13jawad
1 Like
Comment
September 18, 2026
 Claude Docs & Slides: Anthropic's New Update, Explained
This one is genuinely fresh — Anthropic only announced it on September 16-17, 2026, so if you're reading this within a week or two of publishing, you're getting one of the earlier breakdowns rather than a rehash of everyone else's coverage. Here's what actually changed, why it matters, and what to actually expect if you're a Claude user.
 What Anthropic just shipped
 Anthropic rolled out two new tools directly inside Claude: Claude Docs and Claude Slides . Docs brings a full rich-text editor into the chat interface itself — you ask Claude to draft a document, it can ask clarifying questions before starting, write the content, and leave comments explaining specific choices along the way, similar to working with a real collaborator rather than just receiving a finished file. Slides works the same way for presentations: describe what you need, Claude builds the deck, and you can ask it to edit specific slides or refine the whole thing conversationally.
 Finished work in both tools lives in Claude's Artifacts tab and exports cleanly to formats people already use — Word, PDF, Google Docs, or Markdown for documents; PDF or PowerPoint for slide decks. Documents also support real-time collaboration, meaning you can share a Claude Doc with a colleague and both edit it together, with Claude able to leave comments in the same style as a Google Docs collaborator would.
 The bigger structural change: "One Claude"
 This isn't just two new buttons bolted onto the existing interface. It's part of a larger consolidation Anthropic is calling "one Claude" — merging the standard chat experience with Claude Cowork (the more agentic, task-delegation mode Anthropic launched back in January 2026) into a single interface. Instead of deciding upfront whether you need a quick chat, a Cowork session, or a document-creation tool, you just describe what you need in one conversation, and Claude determines internally which capabilities and tools the task actually requires.
 Practically, that means research, multi-step agentic work, document creation, and presentation building can now all happen inside the same thread, without you manually switching modes partway through. Claude Design — Anthropic's existing visual creation tool for prototypes, slides, and marketing materials — has also been folded into this same unified interface.
 Why this matters beyond just "Claude got new features"
 The framing that stuck out most in the initial coverage came from an industry analyst who put it well: Microsoft and Google have spent the last couple of years bringing AI deeper into their existing productivity software, while Anthropic is doing the opposite — bringing more of the productivity environment directly into the AI. Over time, that's a genuinely different bet on where knowledge workers will actually get their work done, and it puts Claude in more direct competition with Microsoft 365 Copilot and Google Workspace's AI features than it was before this update.
 Worth noting: this is unlikely to trigger a mass migration away from Microsoft or Google's suites overnight — organizations don't rip out entrenched productivity software easily. But for a large share of knowledge workers, drafting or editing documents and presentations is already one of the most common daily uses of generative AI at work, and reducing the number of tools someone has to touch to get that done removes real friction, even if it doesn't replace an entire company's software stack immediately.
 Rollout timeline
 This is rolling out in phases rather than all at once. Pro and Max subscribers on web, desktop, and mobile are getting access first, over the coming weeks, with Team and Free plan users expected to follow afterward. Enterprise organizations are reportedly set to get a 30-day advance notice before the unified interface becomes the default experience for their accounts, which is a sensible approach given how disruptive a sudden interface change can be for teams with established workflows.
 What this doesn't change
 This is still Claude — the tools are additive, not a replacement for how the assistant already works. If you're not doing document or presentation work, day-to-day usage likely won't feel meaningfully different beyond the interface consolidation itself. The real shift is for people who were previously exporting Claude's output into a separate Word or PowerPoint file manually and then doing the formatting work themselves — that specific friction is what this update is aimed at removing.
 Related reading
 I also have this same breakdown on my site: Claude Docs & Slides: Anthropic's New Update . If you're generally tracking how different AI companies are shipping productivity-focused updates this year, I also covered 5 New AI Tools Worth Knowing About in 2026 , including a similar move from Google with native AI document tools inside Workspace — useful context for how this specific competitive dynamic is playing out across the industry right now.
 For the original reporting on this announcement, VentureBeat's coverage goes into more depth on the Cowork merger specifically, and Claude's Wikipedia entry is a good ongoing reference as this rollout continues over the coming weeks.
 The bottom line
 This update is less about a single flashy new capability and more about Anthropic making a clear bet: reduce the number of separate tools a knowledge worker has to open in a day, and route everything through one conversation instead. Whether that actually changes how people work day-to-day will depend on execution over the coming months, not the announcement itself — but the direction is clear, and it's worth watching how Microsoft and Google respond in turn.
13jawad
1 Like
Comment
September 12, 2026
 I Tested GPT-6 Astra on My Actual Side-Project Backlog. Here's What Held Up.
OpenAI released GPT-6 Astra on September 3-4, 2026. As a solo builder, my only real question about any new frontier model launch is: does this actually clear more of my backlog, or is it just a better benchmark score I'll never notice in practice. Spent a few days running it against real tasks before writing this up.
 What Astra is actually built for
 The pitch isn't "smarter chatbot," it's closer to "reliable computer operator." OpenAI's own list of target tasks reads like a solo founder's actual to-do list: filling out tax forms, updating CRM records, organizing calendars, researching online, drafting documents, analyzing data, building websites, running frontend QA, installing software, troubleshooting what's on screen. None of that is glamorous. All of it is exactly the stuff that eats a one-person team's week.
 The thing that actually mattered in my testing
 Task persistence. Previous models were fine at a single well-scoped ask but tended to drift or lose the thread on anything requiring more than a handful of sequential steps. OpenAI claims meaningful improvement here — better at staying focused, respecting task boundaries, and completing multi-step workflows without going off track. In my own testing on a multi-step research-then-draft task, it held together noticeably better across the full chain than I expected going in.
 The benchmark numbers back this up: 88% first-attempt success and 99.2% within four attempts on a multi-attempt task benchmark, versus roughly 56%/69% for the previous model. For a solo builder, that gap is the difference between "generate once and use it" versus "regenerate three times and manually stitch the good parts together."
 Pricing reality check
 $10 per million input tokens, $50 per million output tokens, ~1.05M token context window. Not cheap for high-volume use, but the context window size means fewer chunking workarounds for anything document-heavy, which is worth factoring into the actual cost comparison against a smaller, cheaper model.
 The part I wasn't expecting to find interesting
 OpenAI's own safety documentation is surprisingly candid about Astra's jump in cybersecurity capability — significant enough to meet their internal "Critical" threshold. The public version has real restrictions on advanced cyber tasks. Not directly relevant to most indie projects, but worth knowing if you're building anything security-adjacent, since it signals the ceiling on general-purpose capability is moving faster than most people are tracking.
 Verdict for solo builders
 Worth testing specifically on anything in your backlog that's multi-step and currently requires you to babysit the output across several iterations. Less obviously worth it if most of what you use AI for is single-shot content generation — the upgrade there is real but less transformative to your actual workflow.
 Further reading
 Longer breakdown on my blog: GPT-6 Astra: What OpenAI's New Flagship Model Changes , original on my site: GPT-6 Astra: From Answers to Work . Also covered ChatGPT Images 2.5 if you want to see how OpenAI's smaller updates compare to a release like this one.
 Anyone else running Astra against real backlog tasks yet, not just demos? Curious what actually stuck for other solo builders.
13jawad
1 Like
Comment
September 12, 2026
 I Almost Shipped a Wrong Number Because I Trusted the Wrong Kind of AI Calculator
Was building a small pricing calculator feature into my side project and used an LLM to sanity-check a multi-step markup calculation. It gave me a confident, clean, wrong answer. Explanation looked completely correct. Final number was off. Caught it by luck, not by suspicion — that's the scary part.
 What I learned about "AI calculators"
 Two totally different things get called this. Wolfram Alpha-style tools actually compute — symbolic math engine, deterministic, essentially always correct for well-formed problems. LLMs like the one I used predict the most statistically likely next answer based on patterns. Great at explaining, not guaranteed correct on multi-step math.
 The failure mode is the dangerous part: it doesn't fail obviously. It fails confidently, with clean reasoning wrapped around a wrong number, which is exactly the situation where you don't think to double check.
 What I do now
 Any actual computation that matters — pricing logic, unit conversions, anything a user-facing number depends on — goes through a deterministic tool (ended up scripting the math directly rather than trusting an LLM call for it). LLM stays in the loop for explaining things to users in plain language, not producing the number itself.
 The broader takeaway for other solo builders
 If you're using any AI assistant to generate or verify a calculation that ships to users, know which category it falls into first. "Sounds right" and "is right" are not the same thing with language models doing math, and the gap between them doesn't announce itself.
 More detail
 Longer version on my blog: AI Calculator Online — What Actually Works . Full breakdown on my site: AI Calculator Online . Also relevant if you're using AI around numbers generally: AI in Google Sheets .
 Anyone else caught a quiet wrong-number bug from an LLM before shipping? How'd you catch it?
13jawad
1 Like
Comment
September 11, 2026
 I Started Hiring for My Small Team and Finally Understood What AI Recruiting Software Is For
Never had to hire anyone before this year. Posted one role, got a genuinely overwhelming number of applications within 48 hours, and immediately understood why "AI recruiting software" is a whole category now. Here's what it actually does, from the perspective of someone with zero recruiting background trying to hire two people without losing a month to it.
 The actual problem
 I'm not a recruiter. I don't have a team to screen resumes for me. What I had was one open role and way more applications than I could reasonably read one by one while also, you know, running the actual product. That's the exact gap this software exists for.
 What actually helped
 Screening and ranking. Instead of reading every resume in the order it arrived, AI screening compared applications against the actual requirements I'd listed and surfaced a ranked shortlist. This alone turned an unmanageable pile into a list I could realistically review in an afternoon.
 Scheduling. Once I had people to actually talk to, coordinating interview times across everyone's calendars used to be its own part-time job. Automating that back-and-forth removed a genuinely tedious piece of the process.
 Communication. Candidates being left in silence is apparently one of the most common hiring complaints, and I get why — I nearly did it by accident just from being overwhelmed. Automated status updates meant nobody was left wondering if I'd forgotten about them, even during the busiest week.
 What I learned to be careful about
 The ranking is a starting point, not a verdict. I still read every shortlisted resume myself and made the actual call — the tool just meant I was reading twelve resumes instead of a hundred and forty. Also worth knowing: a lot of what's marketed as "AI recruiting software" is really a normal applicant tracker with AI bolted onto one or two stages, not something AI-native end to end. Matters less for a one-person hiring situation like mine, but worth knowing if you're evaluating something for a bigger team.
 Was it worth it for a team of one hiring for the first time
 Completely. The alternative was either paying for actual recruiting help I couldn't afford yet, or losing two weeks of building time to manual resume triage. This got most of the value of the first option without the cost, and mostly eliminated the second problem.
 Related
 Longer version of this same breakdown is on my blog: AI Recruitment Software — What It Actually Helps Recruiters Do , original on my site: AI Recruitment Software . If you're the one applying rather than hiring, AI Tools for Job Seekers covers the other side of this exact same shift.
 Anyone else here hired for the first time recently and had this same "oh, THAT'S what this software is for" moment?
13jawad
1 Like
1 Comment
Say something nice…
Post Comment
1
Recruiter here. Agree the ranking is a starting point. Two things I'd add from seeing this on the hiring side:
- Keyword screeners miss good people. Someone who writes "built our payments backend" instead of "Stripe API integration" can end up at #90 in the ranking. When I use these tools I also skim the bottom 20% of the list, and there's usually at least one strong candidate hiding there.
- Check the legal side if you hire in NYC. Under Local Law 144, employers using tools that screen, rank or score candidates must have an annual independent bias audit, publish the results, and give candidates notice before the tool is used. The law also covers remote roles that a NYC resident could fill. Penalties run from $500 for a first violation up to $1,500 per day of ongoing non-compliance.
Otherwise, +1 on the automated status updates. Leaving candidates without an answer does more damage to a small company's reputation than a slow process.
Caminied
·
4 days ago
 ·
Reply
September 10, 2026
 5 AI Tools I Actually Added to My Solo-Founder Stack in 2026
 As a one-person team running a couple of side projects, my rule for any new AI tool is simple: does it save me more time than it costs to learn. Most 2026 launches fail that test within a week. These five didn't.
Lovable
Went from app idea to working prototype in an afternoon instead of a weekend of scaffolding. For validating whether an idea is even worth building properly, this has become my default first step before writing real code. Doesn't replace engineering on anything that needs to scale, but for the "is this worth building" phase, it's exactly the right amount of tool.
n8n
My actual bottleneck this year wasn't building features, it was the manual glue work between tools — moving signup data, syncing a spreadsheet, triggering a notification when something happened elsewhere. n8n killed most of that. Similar territory to Zapier, but with more control and self-hosting options if you want to keep costs down as usage scales.
Google Pics
No design budget, no designer. Native AI image generation and editing inside Google Workspace means I can generate and tweak visual assets without leaving a doc or slide, and without paying for a separate design tool subscription I'd barely use. Comparable to what I found testing ChatGPT Images 2.5 for a different project — worth comparing both if you're choosing an ecosystem to commit to.
OpenCode
Not locked into one AI vendor for coding assistance, which matters more than people think when pricing and model quality shift as often as they have this year. Free core, paid usage-based tiers once you actually need more. Crossed 120,000 GitHub stars this year, which says something about how many other solo builders feel the same way about vendor lock-in.
ElevenLabs
Added a voice layer to one of my projects this year without hiring anyone or recording anything myself. Realistic enough that testers didn't immediately clock it as AI-generated, which was the actual bar I was trying to clear.
The actual filter
For a team of one, every tool has to justify its setup time against the hours it actually saves. All five of these cleared that bar within the first week of using them. A lot of the louder 2026 launches didn't make it past week one.
Longer version with more detail on my blog: 5 New AI Tools Worth Knowing About in 2026. Also wrote up how I'm using AI inside Google Sheets for lightweight project metrics, if that's useful too.
What's actually earned a spot in other solo builders' stacks this year? Curious what I'm missing.
13jawad
1 Like
Comment
September 9, 2026
 I Rebuilt My Product's Hero Images With ChatGPT Images 2.5. Here's What Actually Changed.
Every hero banner and in-app illustration on my side project has been AI-generated for a while now — no design budget, no designer, just me and whatever image model is currently best. OpenAI shipped Images 2.5 on September 8, 2026, and I spent a weekend re-testing my whole visual pipeline against it.
 The actual bottleneck it fixes
 If you've generated marketing assets with AI before, you know the loop: generate, almost right, ask for one small edit, and by the fourth or fifth edit round something else has quietly drifted — background color, a face, a layout element you didn't touch. That drift is what made iterative asset creation genuinely painful before this release. Images 2.5 is specifically built to change only what you ask for while keeping everything else stable across turns, and in my own testing on a set of product mockups, that held up through six consecutive edit rounds without the usual degradation.
 For a one-person team iterating on marketing assets constantly, this is the change that actually saves time — not the headline speed number.
 Speed, for what it's worth
 OpenAI claims up to 50% lower generation latency versus Images 2.0. I didn't benchmark this rigorously, but generation did feel noticeably snappier during rapid iteration sessions, which matters when you're cycling through ten variations of a hero image in one sitting.
 Two API tiers now, worth picking correctly
 For anyone calling this programmatically (I do, for auto-generating some in-app assets): there are now two models — Flare for fast, everyday generation, and Sunburst for precision editing workflows. I moved my one-shot asset generation to Flare and kept anything needing multi-round editing on Sunburst. Same pricing as before, so this was a free upgrade once I split the calls correctly.
 New tools I didn't expect to use as much as I do
 Sketch — I rough out a layout idea by hand and use it as a visual reference instead of trying to describe spatial composition in words, which I'm bad at. Genuinely useful for landing page hero concepts.
 Comment-based editing — point at the one thing that's wrong instead of retyping the whole prompt. Small thing, saves real time across a lot of iterations.
 Is it worth switching your pipeline over
 If your product does any repeated AI image generation — hero images, social assets, in-app illustrations — yes, this is worth testing this week. The consistency fix alone changes how usable multi-round editing actually is for a solo builder without a design background.
 Full breakdown with more examples from my testing: https://www.aitoolsvault.site/blog/chatgpt-images-2-5-review
 Anyone else running their whole visual pipeline on AI-generated images for a side project? Curious what your workflow looks like.
13jawad
1 Like
Comment
September 8, 2026
 I Used AI + Google Sheets as My Side Project's Backend for 3 Months. Here's What Held Up.
No budget for a real dashboard tool, no time to build one properly, and a side project that needed to track signups, revenue, and a few funnel metrics. So I did what a lot of indie hackers quietly do: built the whole thing in Google Sheets. The difference this time is AI made it good enough to actually rely on.
 The problem with the old way
 Manually pulling numbers from Stripe, my signup form, and an analytics tool into a spreadsheet every week was exactly the kind of repetitive task that eats indie hacker time without moving the product forward. I needed the data connected, not re-copied every Monday.
 What I actually built
 Live data connections instead of manual exports. Instead of copy-pasting from each tool weekly, I connected my key data sources directly into the sheet on an automatic schedule — closer to a lightweight Zapier -style automation than a manual habit. This alone killed the weekly "update the numbers" chore.
 Native AI functions for the boring analysis. Plain-language prompts to generate summaries, categorize signup sources, and build quick charts from raw data — directly in Sheets, no separate BI tool required. For a one-person project, standing up a real analytics stack never made sense. This got me 80% of the value for near-zero setup cost.
 AI-generated formulas instead of me writing them badly. I'm not a spreadsheet power user. Describing what I wanted in plain language and getting a working formula back saved real time I'd otherwise lose to trial-and-error nested functions.
 Bulk categorization for messy signup data. Signup source data was inconsistent — different capitalization, extra whitespace, inconsistent naming from different forms. Bulk AI text processing cleaned an entire column in one pass instead of a manual find-and-replace marathon.
 Where I drew the line
 I didn't try to build anything AI couldn't reliably verify — no AI-generated numbers going straight into anything financial without a manual check first. Fast and cheap is good. Fast, cheap, and wrong is worse than the manual process it replaced.
 Was it worth it
 For a pre-revenue-to-early-revenue side project, yes, clearly. The alternative was either paying for a proper analytics/BI tool I didn't need yet, or continuing to burn an hour every Monday on manual data pulls. This got most of the value of the first option without the cost, and completely removed the second problem.
 Full breakdown
 Wrote up the specific tools I used and what each is actually good for here: AI for Google Sheets: The 2026 Guide . Also have a step-by-step version on my blog if you want the more detailed walkthrough: AI for Google Sheets in 2026 — What's Actually Worth Using .
 Takeaway
 You don't need a real BI stack for a side project doing a few hundred rows of data a month. AI-in-Sheets covers that range surprisingly well, and it's a lot easier to migrate off a spreadsheet later than to justify a BI subscription now.
 Anyone else running their whole side-project dashboard out of Sheets? What's your setup look like?
13jawad
1 Like
Comment
September 8, 2026
 Choosing Between Sora, Gemini, and DeepSeek for a Side Project? Read the Fine Print First.
Was about to pick one of these three for a small side project and nearly made a costly mistake, so sharing before anyone else makes the same one.
 The mistake I almost made
 I was leaning toward building a small AI video feature on Sora's API — good output quality, straightforward per-second pricing. Then I actually read OpenAI's own help docs instead of just the launch blog posts, and found this: the Sora consumer app was already discontinued back in April 2026, and the API itself is scheduled to sunset on September 24, 2026. As a solo builder with zero appetite for migrating a core feature two months after shipping it, that single fact killed the plan entirely.
 Lesson: for anything you're betting a real feature on, check the platform's actual support/help docs for sunset or deprecation notices before you check the pricing page. The marketing page won't tell you this. The help center will.
 What these three actually are, for anyone comparing them like I was
 Not really competitors — different jobs entirely:
 Sora — video generation specifically. Currently the one with the biggest "should I actually build on this" question mark, for the reason above.
 Gemini — Google's general-purpose assistant, deeply wired into Workspace, Search, and Android, with genuinely capable native multimodal handling (images, audio, video) and a large context window on paid tiers.
 DeepSeek — open-weight, self-hostable, dramatically cheaper to run thanks to its architecture, and consistently strong specifically at coding and reasoning tasks. Not a video tool, not deeply ecosystem-integrated — a focused specialist.
 What I ended up doing
 Skipped Sora entirely given the sunset timeline. For the side project's actual need (some document-heavy processing plus occasional coding assistance for build scripts), went with a mix — DeepSeek for the cost-sensitive coding tasks, Gemini for anything touching Google Docs data directly since the integration was already free. No video feature for now; revisiting once a stable, actively-maintained option settles into that gap.
 The actual takeaway for other solo builders
 Before committing a core feature to any AI API, specifically check for a deprecation or sunset notice in the provider's help center, not just their pricing or launch page. It takes five minutes and could save you a very expensive rebuild later. Sora's situation right now is a good real-world example of exactly why that check matters.
 Further reading
 Longer version of this on my blog: Sora vs Gemini vs DeepSeek — What They Actually Do , original on my site: Sora vs Gemini vs DeepSeek . Also covered GPT-6 Astra if you're weighing OpenAI's other recent releases for your own stack.
 Anyone else nearly build on something that turned out to be getting sunset? Curious how you caught it, if you did.
13jawad
1 Like
Comment
People
 13jawad Founder
Stay informed as an indie hacker.
 Market insights that help you start and grow your business.
Subscribe
Follow @IndieHackers on X for stories and insights about founders building profitable online businesses, and to connect with others in the Indie Hackers community.
 © Indie Hackers, Inc. · FAQ · Terms · Privacy · Cookie Settings / Policy ·
Community
 Top Today Top This Week Top This Month Join
Products
 All Products Highest Revenue Add Yours
Databases
 Ideas Products Stories

## 关联链接

- https://www.aitoolsvault.site/blog/chatgpt-images-2-5-review

## 导航

- 项目页：[[10-项目/Ai-Tools-Vault_41d465b9]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
