---
type: "corpus"
item_id: "8237951271bb0076"
title: "I Vibe-Coded My Way Out of Angular Upgrades"
source: "devto"
source_name: "dev.to"
url: "https://dev.to/gramli/i-vibe-coded-my-way-out-of-angular-upgrades-4fkh"
project_url: "https://angular.dev/update-guide"
author: "Daniel Balcarek"
published_at: "2026-10-15T07:10:18Z"
captured_at: "2026-10-26T09:53:38+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-15"
tags:
  - 语料
  - devto
  - ai
  - vibecoding
  - angular
  - showdev
metrics: {"reactions": 90, "comments": 64, "reading_time": 3}
comments_count: 60
comments_total: 64
discovered_via: "devto:showdev"
---

# I Vibe-Coded My Way Out of Angular Upgrades

> [!info] 一句话导读
> Do you also hate upgrading Angular versions? Because I do. I maintain a few open-source projects, and upgrading Angular is probably my least favorite maintenanc…

> [!meta]- 语料信息（点开展开）
> 来源：dev.to（post）
> 原帖：<https://dev.to/gramli/i-vibe-coded-my-way-out-of-angular-upgrades-4fkh>
> 指标：reactions=90 · 评论=64 · reading_time=3
> 作者：Daniel Balcarek　|　发布：2026-10-15T07:10:18Z
> 项目链接：<https://angular.dev/update-guide>
> 采集：2026-10-26T09:53:38+08:00　|　id：`8237951271bb0076`

## 正文

Do you also hate upgrading Angular versions? Because I do. I maintain a few open-source projects, and upgrading Angular is probably my least favorite maintenance task. That's also why my frontend updates often get postponed for far too long.

But we have AI now, right? It should be able to handle this with some instructions. So I decided to create (or rather vibe-code) an **Angular Update Skill for Codex**.

## Creating the skill

Upgrading Angular isn't just about running `ng update`. There are several things I normally have to take care of, so I created a prompt describing what the skill should do:

- Follow the official [Angular Update Guide](https://angular.dev/update-guide).
- Create a separate Git branch for the upgrade.
- Handle migrations and dependency updates.
- Validate that everything still builds and works.
- Follow the same good practices I would use when upgrading Angular manually.

(Updating NuGet packages in .NET feels so much simpler.)

Codex generated the first version of the skill, and surprisingly, it worked!

Well... locally.

### First problem: npm ci

After pushing my changes to GitHub, the CI pipeline failed with:

```plaintext
npm ci can only install packages when your package.json and package-lock.json are in sync.
```

Classic "works on my machine" problem. The skill had managed to update Angular, but it hadn't properly validated that a clean installation would work. So I added another validation step: run `npm ci` before considering the upgrade complete. This way, the agent can catch problems with the lock file before they reach CI.

### Second problem: npm publishing

Then I ran into another issue when trying to publish my Angular library to npm:

```plaintext
npm error code E404
npm error 404 Not Found - PUT https://registry.npmjs.org/gramli-angular-mydatepicker - Not found
```

At first, the error wasn't particularly helpful. After some investigation, I found that my publishing environment was using Node.js 22 with npm 10.

However, according to the [npm trusted publishing documentation](https://docs.npmjs.com/trusted-publishers), trusted publishing requires:

- Node.js 22.14.0 or higher
- npm 11.5.1 or higher

So I updated the skill again to prefer the latest Node.js LTS version compatible with the target Angular version, while also making sure the npm version meets any publishing requirements.

### Third problem: the skill was getting too big

After all these improvements, the skill was becoming quite large. That might not matter much with generous token limits, but I also wanted it to be usable by people working with more limited AI budgets. So I shortened the instructions, removed unnecessary repetition, and kept the important validation steps. The main skill went from 1,252 words to 701 words, with the complete bundle becoming approximately 40% shorter.

## Testing it on real projects

Of course, generating a skill is one thing. Actually using it is another. So far, I've used the current version on three of my open-source projects:

- **Angular 21 → 22:** [angular-mydatepicker PR #12](https://github.com/Gramli/angular-mydatepicker/pull/12)
- **Angular 19 → 22:** [FileApi PR #13](https://github.com/Gramli/FileApi/pull/13)
- **Angular 21 → 22:** [AuthApi PR #113](https://github.com/Gramli/AuthApi/pull/113)

The Angular 19 → 22 upgrade was especially interesting because it required migrations across three major versions. In the AuthApi project, the upgrade also involved replacing PrimeNG with Optimus UI because of the PrimeNG licensing changes.

All three upgrades have now been merged.

## Three Projects Later

The current version works pretty well, at least on my smaller projects. It's not perfect, though. Some Angular projects are much more complicated than mine, so the skill would probably need to be adapted for them. But it already helped me upgrade three projects, and I learned a few things along the way.

The best part? I finally updated my Angular projects in just ONE WEEK instead of postponing them again. 😁

I wanted to share this with the community because it might help someone else. If you want to try the skill or improve it, you can find it here:

**[Angular Update Skill on GitHub](https://github.com/Gramli/Gramli.Framework/tree/main/src/angular-skills/angular-update)**

## 评论（60/64）

> **Sylwia Laskowska** · 2026-10-15T07:42:48Z　
> Oh, this is something I should probably send to the team maintaining the Angular component library we're forced to use! 😂 Upgrading Angular itself is already a pain in the ass, but upgrading that library is a whole new level of nightmare! I swear, sometimes I think they assume nobody ever upgrades it, because they make changes like renaming (close) to (closeDialog) between versions, only to rename it back to (close) in the next one. 😂 So yeah, let them give it a try and burn some tokens! 😁

---

> **Daniel Balcarek** · 2026-10-15T08:17:09Z　
> Nice, (close) to (closeDialog) and then back to (close)? That sounds like pure evil! 😂😂😂
>
> So what you actually need is a separate skill for upgrading that specific library?! 🤣

---

> **Sylwia Laskowska** · 2026-10-15T12:10:16Z　
> Exactly! 😂 Every time we upgrade that library, we joke that they're doing it on purpose, just to make sure we'll have jobs for the rest of our lives! 🤣

---

> **Sina Rezaei** · 2026-10-15T08:35:10Z　
> The npm ci failure is the part that makes this interesting. An AI agent can migrate Angular APIs correctly and still miss the contract between the lockfile, peer dependencies, and the publishing environment.
>
> For example, in a library migrating from Angular 17 to 18, updating @angular/core and @angular/compiler-cli isn't enough if @angular-devkit/build-angular, the TypeScript version, and the library's peerDependencies still target incompatible ranges. The app may compile locally because of an existing node_modules tree, then fail in CI with a clean install or break consumers installing the published package. I'd make the skill validate those dependency constraints, run npm ci from a clean checkout, build the library in production mode, and test the packed tarball in a separate Angular consumer project. That last step catches problems a successful workspace build can easily miss.

---

> **Daniel Balcarek** · 2026-10-15T09:17:23Z　
> Good points. Actually, that first npm ci failure is exactly why I added clean-install validation to the skill. It creates a fresh temporary copy without node_modules, so it doesn't rely on existing dependencies.
>
> I also tested it on a published Angular library with its own demo application. The skill upgraded Angular, I tested the demo, and then published the updated library.
>
> Testing the packed package in a separate consumer project makes sense for library release validation, but I'd say that's beyond the scope of a general Angular upgrade skill. 😅

---

> **Sina Rezaei** · 2026-10-15T11:06:55Z　
> That makes sense. Testing the demo app is a much better signal than just checking whether the library builds after the upgrade. One edge case I'd still watch for is Angular's partial-Ivy compatibility and peer dependency ranges. For example, a library can work perfectly in its own demo while its published peerDependencies accidentally exclude an Angular version that should be supported, or while its packaging configuration omits a secondary entry point. Those are release-contract issues rather than upgrade failures, though, so I agree they don't necessarily belong in the core skill. Keeping the upgrade workflow focused and leaving deeper package-release checks as an optional step sounds like the right boundary.

---

> **Daniel Balcarek** · 2026-10-15T11:25:17Z　
> Yes, I agree, thanks for the detailed feedback and suggestions.

---

> **Web Developer Hyper** · 2026-10-15T11:06:28Z　
> Great post about agent skills! You are a great developer who succeeded in updating Angular using skills. 👍 I am using my handmade skills and keep updating it to write my AI Avatar README, but it always fails even though AI Avatar is already at v25. 🤣

---

> **Daniel Balcarek** · 2026-10-15T11:21:18Z　
> Thanks! 😁 Haha, sounds like your README skill is giving you more trouble than my Angular upgrades! 🤣

---

> **Jyanthi** · 2026-10-21T07:26:26Z　
> Haha, fair enough! 🤣 At least both teach us patience and keep us humble. Thanks for the fun discussion, and best of luck with your next upgrade! 😁

---

> **Jyanthi** · 2026-10-15T13:22:41Z　
> Haha, the struggle of keeping AI skills up to date is real! 😂🚀 Turning a repetitive Angular upgrade into a one-week achievement is genuinely impressive. It’s fascinating how the right skills can transform AI from a coding assistant into a reliable workflow partner. Now I’m curious—what do you think made the biggest difference: the skill’s instructions, the workflow, or the way you guided the agent? 🤔👏

---

> **Daniel Balcarek** · 2026-10-15T14:40:40Z　
> Thanks! I'd say the workflow, especially the validation steps. Clear instructions are important, but they don't guarantee the agent will get everything right. The first version looked promising, but then npm ci failed in CI. That's when I realized the skill needed better validation.
>
> So I think the biggest difference came from testing it on real projects, finding what failed, and improving the skill along the way.

---

> **xulingfeng** · 2026-10-15T11:09:22Z　
> Great job!

---

> **Daniel Balcarek** · 2026-10-15T11:39:23Z　
> 🤣🤣

---

> **Daniel Balcarek** · 2026-10-15T11:41:00Z　
> 🤣🤣

---

> **𝐓𝐡𝐞 𝐋𝐚𝐳𝐲 𝐆𝐢𝐫𝐥 ** · 2026-10-15T12:04:52Z　
> Of course @sylwia-lask 😅

---

> **Sylwia Laskowska** · 2026-10-15T12:10:44Z　
> hahahahahahahha 😂😂😂

---

> **Daniel Balcarek** · 2026-10-15T12:57:31Z　
> Okay, you were right. There's definitely at least one pro here! 😂😂

---

> **Glen Allen** · 2026-10-15T11:35:27Z　
> The most valuable part of this workflow is that the skill improved after each real failure. I’d take that one step further by making the validation environment reproducible: pin the Node.js and npm versions, start from a clean checkout, and run the same checks locally and in CI. Otherwise, the agent may fix the symptom in one environment without identifying the underlying version mismatch. It could also record which checks passed and which remain unverified, so “upgrade complete” means more than a successful build. That turns the skill from a migration script into a repeatable maintenance process that can be trusted across projects.

---

> **Daniel Balcarek** · 2026-10-15T11:48:35Z　
> Thanks for the ideas! That's actually how I approached it. The skill prefers the latest Node.js LTS compatible with the target Angular version and project requirements, rather than pinning a specific version for every project.
>
> It also checks the CI configuration for the npm version, runs npm ci in a fresh temporary directory without node_modules, and reports which validation steps passed or couldn't be verified.

---

> **Matt Busel** · 2026-10-15T13:41:30Z　
> The part I'd steal is that each fix came from a real failure. The part I'd worry about is the trim from 1,252 to 701 words.
>
> When I've cut agent instructions down, the line that goes first is usually the one that looks redundant but was there because of one specific bad day. Something like "run npm ci before calling it done" reads like filler six weeks later.
>
> Do you keep the three failures (lockfile drift, the npm version for trusted publishing, the big migration jump) as a checklist the skill has to pass after every edit? Otherwise the next "make it shorter" pass might quietly delete one of them.

---

> **Daniel Balcarek** · 2026-10-15T14:43:55Z　
> Good question. Actually, both frontend upgrades were done using the final, shorter version of the skill:
>
> -
> Angular 19 → 22: FileApi PR #13
>
> -
> Angular 21 → 22: AuthApi PR #113
>
> The library upgrade, angular-mydatepicker PR #12, was done before I shortened the instructions. That was actually the project where I originally built and refined the skill based on those failures.
>
> So the shorter version has been tested on real projects, but you're right that this doesn't guarantee every original edge case is still covered. Keeping a regression checklist for future changes is actually a good idea.

---

> **Matt Busel** · 2026-10-15T16:41:24Z　
> That's a better test than my worry: two real upgrades on the short version. If a third one ever breaks, the regression checklist doubles as a record of what the trim dropped, which is the part I'd most want to see. Nice PRs.

---

> **makayis** · 2026-10-15T14:18:45Z　
> I would recommend you to check Codecook a Vscode addon for these kind of issue and it will fix it, provided it will use token compression methods to save cost

---

> **pang** · 2026-10-15T15:20:36Z　
> 学到了

---

> **Yoshiyuku** · 2026-10-16T09:44:22Z　
> The “improve the skill from each real failure” loop is the best part of this post, and the comments already cover clean installs, consumer testing, and regression checklists well. One angle I didn’t see yet is supply chain safety when an agent touches dependencies:
>
> Dependency swaps need a human gate. You mention replacing PrimeNG with Optimus UI. Agents sometimes suggest packages that don’t exist or are lookalikes, so I’d have the skill list any new or removed packages and wait for approval, instead of installing them on its own.
>
> Review the lockfile diff, not just the build. Changed registry URLs, unexpected new transitive packages, or integrity hash changes are worth a quick look. npm audit and npm audit signatures add a cheap automated check.
>
> Keep publish credentials away from the agent. Since you already use trusted publishing, the agent should never see an npm token. It prepares the branch and PR, and CI with OIDC does the release.
>
> Run installs with --ignore-scripts during validation where possible, so a surprise lifecycle script in a new dependency can’t run on your machine while the agent experiments.
>
> Did the skill ask you before the PrimeNG replacement, or was that a manual decision?

---

> **Daniel Balcarek** · 2026-10-17T08:11:09Z　
> Good points!
>
> The agent actually asked me what I wanted to do: stay on the existing PrimeNG version or upgrade to the paid one. That's when I told it I'd rather switch to Optimus UI. So the replacement was my decision, not something the agent did on its own.
>
> The skill already includes lockfile validation, but I like your suggestion about npm audit signatures. That's something worth considering for future improvements.
>
> Thanks for the detailed feedback.

---

> **Krlz** · 2026-10-16T19:46:39Z　
> We are in a situation were it became hard to move on, from Angular 8 to latest version of Angular in the company is a long long trip people doesnt want to endure anymore 🫥

---

> **Daniel Balcarek** · 2026-10-17T08:14:55Z　
> Ouch, Angular 8 to the latest version? That sounds more like an archaeological expedition than an upgrade 🤣🤣
>
> I can imagine why nobody wants to touch it, and in that particular scenario, I definitely wouldn't recommend the current version of my skill 😅

---

> **Denis Ostapenko** · 2026-10-17T16:13:37Z　
> Does the skill stop for approval before a change like replacing PrimeNG? That feels like a product decision, even when it helps the upgrade pass.

---

> **Daniel Balcarek** · 2026-10-17T16:38:17Z　
> The agent actually stopped and asked whether I wanted to stay on the existing PrimeNG version or upgrade to the paid one. That's when I decided to switch to Optimus UI instead.
>
> So it was my decision, not something the agent did automatically. And I agree, that's definitely a product decision.

---

> **Denis Ostapenko** · 2026-10-17T20:21:49Z　
> Thanks, Daniel. That's the pause I was asking about: the agent surfaced the paid upgrade and left the library choice to you.

---

> **Marcus Kim** · 2026-10-17T19:03:54Z　
> The npm ci failure and the later publishing failure look like two separate acceptance checks worth keeping after the skill was shortened. I'd run the clean install and build with the same Node/npm versions as CI, then inspect a packed library in a small consumer project before calling the upgrade done. That checks what a user actually installs without making a real release. It would also make the three-major-version migration a useful regression fixture for future edits to the skill.

---

> **Ascendra Ventures** · 2026-10-18T02:40:38Z　
> The npm ci step is the part I would underline. "Works locally" was the agent's definition of done, and CI had a stricter one. Once the clean install became part of the skill, the upgrade had a finish line that matched reality.
>
> I think that is the general lesson for handing upgrades to an agent. The task is small enough to state in one line, Angular N to N+1, but done needs to be written as checks: clean install passes, build passes, tests pass, publish works on the target Node and npm versions. Without that list the agent stops at the first green signal it sees.
>
> Trimming the skill from 1,252 to 701 words while keeping the validation steps is a nice touch too. For the 19 to 22 jump, did you run it as one pass or step through each major version with its own checks?

---

> **Daniel Balcarek** · 2026-10-18T09:38:40Z　
> Agreed. For the 19 → 22 upgrade, I let the agent handle the whole process automatically, without manually stopping to verify each major version.
>
> But that’s actually a good idea. Adding validation checkpoints after each major version would be safer, especially for bigger version jumps.

---

> **SkepAgent** · 2026-10-18T03:11:22Z　
> One validation I'd add from bitter experience with ng update: after the migration schematics run, git diff --stat alone hides which schematics actually fired. I've had a schematic silently not apply because a version gate was missed, and the diff just looked 'fine' until runtime. I now make agents record the executed migrations (a small log on the upgrade branch works) so the reviewer sees 'which codemods ran', not just the resulting diff. Pairs well with your clean-install check — one verifies the environment, the other verifies the migration actually happened.

---

> **Daniel Balcarek** · 2026-10-18T10:23:25Z　
> Good point. The skill already tracks migration commands and milestones during the upgrade and includes migration evidence in the final report.
>
> But you’re right, that’s not necessarily the same as recording exactly which schematics were executed. Having that information available for PR reviews could be really useful, especially when upgrading across multiple Angular versions.
>
> Thanks for the suggestion!

---

> **Kashika Agrawal** · 2026-10-18T08:55:31Z　
> Great article! Learning digital marketing can open up exciting career opportunities and help individuals develop practical skills in SEO, social media marketing, content creation, and online branding. If you are looking for a digital marketing course in Raipur, DigiUnits is a creative digital marketing agency worth exploring for insights into digital marketing and online business growth.

---

> **Adam Lewis** · 2026-10-18T09:25:13Z　
> What did the upgrade cost you before the vibe coding, and did it stay fixed on a second run? I want the numbers, because an upgrade that passes once and then fails on the next run is worse than the upgrade you were avoiding. If the generated migration gets you across but you can't say why it worked, the next version puts you back in the same chair. I will read where it gave up and you went back to doing it by hand, because that boundary tells me more than a clean run does.

---

> **Daniel Balcarek** · 2026-10-18T10:56:04Z　
> That’s actually what most of the article is about.
>
> I maintain four small open-source projects: two Angular libraries and two full-stack applications. Angular upgrades were always a pain and usually took more than an hour, depending on what went wrong.
>
> With the improved skill, I managed to complete an upgrade in around 30 minutes, including code review and manual testing.
>
> We’ll see how it goes with future Angular versions, but I’ve already successfully used the skill across three different PRs, so I’d say the results are promising.

---

> ** Generatoren** · 2026-10-18T17:08:36Z　
> Great article! What I find particularly interesting is how AI can simplify repetitive development tasks and save so much time. The important part is making sure everything works properly after the changes. Thanks for sharing your experience!

---

> **Alpha_King06** · 2026-10-18T20:29:03Z　
> Completely agree. The real value isn't in the AI prompt itself, but in the lessons learned from real-world failures and the validation steps added afterward. Upgrading is the easy part; making sure everything works reliably in production is where the challenge begins. Great example of using AI as an accelerator rather than a replacement for engineering discipline

---

> **Mudassir Khan** · 2026-10-19T06:32:09Z　
> making npm ci a hard gate before the agent can say done is the best move in here. most agent upgrade failures i have seen are the agent grading its own work on a dev server that is already warm. a clean install plus a production build in a fresh container catches lockfile drift, peer dep conflicts and node version mismatches in one shot.
>
> the 1,252 to 701 word trim tracks with what we saw too, the long instructions were mostly hedging and the validation steps were the part that survived.
>
> did the skill ever stall on the 19 to 22 jump, or did it step one major at a time?

---

> **Daniel Balcarek** · 2026-10-19T12:33:12Z　
> For the 19 → 22 upgrade, I let the agent handle the process automatically. The skill is designed to upgrade one major version at a time, completing the required migrations and validation before advancing.
>
> I didn't manually verify each intermediate version myself, though.

---

> **Mudassir Khan** · 2026-10-21T06:23:35Z　
> one major at a time with validation between each hop is the right shape. the failure i would watch for is a schematic that silently skips on hop two while the build stays green, so hop three inherits the gap. we log which migrations actually ran per hop so a reviewer can see it.
>
> did the 19 to 22 run leave you a per hop record, or only the final report?

---

> **Mohsen jr** · 2026-10-19T06:42:13Z　
> The interesting part is that the upgrade itself wasn’t the hardest problem. It was catching the things that only show up outside the local environment. Adding npm ci as a validation step seems like a small change, but it can save a lot of debugging later.

---

> **Harald Nezbeda** · 2026-10-19T07:51:13Z　
> Have you also tried doing the upgrade in combination with the MCP for the CLI? angular.dev/ai/mcp

---

> **Daniel Balcarek** · 2026-10-19T16:19:59Z　
> Nope, I haven't tried that yet, but thanks for the tip.

---

> **Anas Issath** · 2026-10-19T07:52:59Z　
> Love that every fix came from a real failure instead of guessing upfront. “Works locally” being the agent’s idea of done is so relatable 😅 Curious how the skill holds up when Angular 23 drops, since that’ll be the real test. Bookmarking this for my next upgrade!

---

> **Geo** · 2026-10-19T16:15:30Z　
> good

---

> **MD Mashiur** · 2026-10-19T16:22:17Z　
> sites.google.com/d/1vEkn4k_C1zLubc...

---

> **MD Mashiur** · 2026-10-19T16:29:48Z　
> **_
>
>  `
>
> {% embed 😀 %}
>
> `
>
> _**

---

> **Shirley** · 2026-10-19T21:47:35Z　
> Nice practical write-up. Automating the parts of ng update that usually get postponed is a solid use of a skill.
>
> The iterative fixes are the interesting part: catching npm ci lockfile drift before CI, and accounting for the Node/npm versions required by trusted publishing, are the kinds of “works on my machine” gaps that pure upgrade scripts often miss. Compressing the skill from ~1,250 words to ~700 while keeping the validation steps is also a good reminder that longer instructions aren’t always better, especially under tighter token budgets.
>
> Useful that it handled a 19 → 22 jump and a PrimeNG → Optimus UI swap in one of the projects. Curious how it behaves on larger apps with more custom schematics or peer-dependency conflicts — those tend to be where the remaining edge cases live.

---

> **PixQuill** · 2026-10-20T02:27:02Z　
> It illustrates a big pain point for AI agent workflows: local success means nothing. You must simulate clean CI‑like environments to catch dependency and lock‑file issues before code lands on main.

---

> **Serhii Lyzun** · 2026-10-20T09:56:40Z　
> "Follow the official Angular Update Guide" is the step I'd want to check. Did Codex actually fetch the guide for 21 → 22, or work from what it remembered? Angular 22 is probably newer than most models' training data.
>
> Next.js 16 approaches this with an AGENTS.md rule telling the agent to read the docs bundled in node_modules/next/dist/docs/ instead of trusting its memory. On my Next 16 project that matters, since params and cookies() are async-only now and the old sync code still looks perfectly valid to a model.

---

> **Daniel Balcarek** · 2026-10-20T14:15:31Z　
> Good question. That's actually why the skill has a dedicated step for retrieving the official Angular Update Guide. It instructs Codex to use the latest official documentation for each version transition. If the interactive guide isn't accessible, it should fall back to other official Angular sources and migration information. I can't confirm from the PR alone exactly which source Codex retrieved during that particular run, though.
>
> And I agree, relying on model memory for framework upgrades would be pretty risky.

---

> **xxxn3m3s1sxxx** · 2026-10-20T16:28:27Z　
> The npm ci step as part of the skill's definition-of-done is the real fix here - you moved the failure from CI (after the push) into the agent's loop (before the push). That pattern generalizes: anything that currently only runs in CI should be runnable locally by the agent, otherwise "works on my machine" just becomes "the agent says it works on my machine".
>
> One addition that has helped me with toolchain-dependent failures: pin the environment explicitly (.nvmrc plus engines and engine-strict=true), so a Node/npm version mismatch surfaces as a clear preflight error instead of an opaque E404 from trusted publishing.
>
> Also +1 on trimming the skill to 701 words - it is cheaper, but the bigger win is that shorter instructions leave less room for the model to paraphrase a validation step into something weaker.

---

> **Daniel Balcarek** · 2026-10-21T06:25:40Z　
> Thanks! I like the idea of catching version mismatches early. But since the skill is meant to work across different Angular projects, I'd rather have it respect each project's existing Node/npm requirements than enforce specific version pins automatically.

---

> **xxxn3m3s1sxxx** · 2026-10-21T16:08:11Z　
> @gramli Fair - and I would narrow my claim: the skill should not enforce its own pins, but it can enforce the project's declared requirement. Read engines / .nvmrc / packageManager from the repo, check the running Node/npm against it as a preflight, and fail with "this project requires Node X, you have Y". No pin injection, but the constraint is read from the project and surfaced early. That was the actual point of engine-strict: it turns an opaque E404 from trusted publishing into a named, early failure - and the version mismatch stops being a supply-chain mystery.

---

> **Daniel Balcarek** · 2026-10-21T16:48:20Z　
> Ah, I see what you mean now. The skill already checks the project's Node/npm requirements, but making version mismatches an explicit preflight failure with a clear error message is a good point.
>
> Thanks for clarifying!

## 关联链接

- https://docs.npmjs.com/trusted-publishers
- https://github.com/Gramli/AuthApi/pull/113
- https://github.com/Gramli/FileApi/pull/13
- https://github.com/Gramli/Gramli.Framework/tree/main/src/angular-skills/angular-update
- https://github.com/Gramli/angular-mydatepicker/pull/12
- https://registry.npmjs.org/gramli-angular-mydatepicker

## 导航

- 项目页：[[10-项目/angular.dev_cb8f3161]]
- 渠道页：[[50-渠道/devto]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
