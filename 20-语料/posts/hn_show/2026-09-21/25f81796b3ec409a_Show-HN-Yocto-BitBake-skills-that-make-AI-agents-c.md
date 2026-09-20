---
type: "corpus"
item_id: "25f81796b3ec409a"
title: "Show HN: Yocto/BitBake skills that make AI agents check official docs"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48726866"
project_url: "https://github.com/Higangssh/yocto-agent-skills"
author: "swq115"
published_at: "2026-06-29T23:52:46Z"
captured_at: "2026-09-21T03:11:01+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-29"
tags:
  - 语料
  - hn_show
  - author_swq115
  - story_48726866
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Yocto/BitBake skills that make AI agents check official docs

> [!info] 一句话导读
> Higangssh/yocto-agent-skills

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48726866>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：swq115　|　发布：2026-06-29T23:52:46Z
> 项目链接：<https://github.com/Higangssh/yocto-agent-skills>
> 采集：2026-09-21T03:11:01+08:00　|　id：`25f81796b3ec409a`

## 正文

# Higangssh/yocto-agent-skills

Official-doc-first Yocto Project and BitBake skills for AI coding agents

- Stars: 6
- Forks: 1
- Watchers: 6
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-06-29T08:11:51Z

## Languages

- Python

## Topics

- agent-skills
- ai-agents
- bitbake
- claude-code
- codex
- embedded-linux
- openembedded
- yocto

## Top Contributors

- Higangssh (13 contributions)

---

## README

# Yocto Agent Skills

validate

Official-doc-first Yocto Project and BitBake skills for AI coding agents.

Yocto is release-sensitive, deeply configurable, and easy for general LLMs to hallucinate. This repository gives agents focused skills for routing to official documentation, debugging BitBake failures, reviewing recipes, reviewing layers, diagnosing image/rootfs problems, working through BSP/kernel issues, and handling security/SBOM workflows.

Korean documentation: README.ko.md

## Skills

- `skills/yocto-doc-router`: release-aware routing to the right Yocto, OpenEmbedded, and BitBake official documentation.
- `skills/bitbake-debug`: task/log/rootfs/package/provider debugging for BitBake build failures.
- `skills/yocto-recipe-review`: recipe, bbappend, bbclass, dependency, packaging, licensing, and override syntax review.
- `skills/yocto-layer-review`: layer.conf, layer compatibility, priority, dependency, provider, and bbappend matching review.
- `skills/yocto-image-rootfs`: image recipes, package names, `IMAGE_INSTALL`, `IMAGE_FEATURES`, `do_rootfs`, pkgdata, and package manager issues.
- `skills/yocto-bsp-kernel`: machine config, BSP layers, kernel providers, devicetree, defconfig, U-Boot, and deploy artifacts.
- `skills/yocto-security-sbom`: license metadata, CVE checks, SPDX/SBOM, archiver/copyleft flows, and compliance artifacts.

The root `SKILL.md` remains as a compatibility router for hosts that install a repository as a single skill.

## What It Helps With

- Debugging BitBake task failures: `do_fetch`, `do_unpack`, `do_patch`, `do_configure`, `do_compile`, `do_install`, `do_package`, `do_package_qa`, `do_rootfs`, `do_image`
- Writing and reviewing `.bb`, `.bbappend`, `.bbclass`, image recipes, machine config, distro config, and `layer.conf`
- Modernizing BitBake override syntax: `VAR:append`, `FILES:${PN}`, `RDEPENDS:${PN}`, task overrides, and package overrides
- Reviewing layers, bbappends, provider selection, package splitting, rootfs failures, QA messages, kernel/BSP metadata, and image composition
- Reducing common AI mistakes around `DEPENDS` vs `RDEPENDS`, recipe names vs package names, `SRCREV`, `LIC_FILES_CHKSUM`, `INSANE_SKIP`, host contamination, and sstate cleanup

## Installation

Every skill folder is self-contained: it carries the references it links to, so a skill
keeps working when installed on its own.

### Claude Code

The repository is also a Claude Code plugin. Add the marketplace and install:

```bash
/plugin marketplace add Higangssh/yocto-agent-skills
/plugin install yocto-agent-skills@yocto-skills
```

All seven skills load as `/yocto-agent-skills: `, and Claude invokes them
automatically when a task matches. To try them without installing:

```bash
claude --plugin-dir /path/to/yocto-agent-skills
```

### Codex and other collection-aware agents

Install the individual folders under `skills/`.

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
for skill in yocto-doc-router bitbake-debug yocto-recipe-review yocto-layer-review yocto-image-rootfs yocto-bsp-kernel yocto-security-sbom; do
  ln -s "$(pwd)/skills/$skill" "${CODEX_HOME:-$HOME/.codex}/skills/$skill"
done
```

For hosts that install one folder as one skill, install the repository root:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s "$(pwd)" "${CODEX_HOME:-$HOME/.codex}/skills/yocto-agent-skills"
```

## Example Prompts

```text
Use yocto-doc-router to find the current docs for this QA check on my release.
```

```text
Use bitbake-debug to diagnose this do_rootfs failure.
```

```text
Use yocto-recipe-review to review this recipe and modernize the override syntax.
```

```text
Use yocto-layer-review to explain why this bbappend is not being applied.
```

```text
Use yocto-image-rootfs to find why my package is not in the final image.
```

```text
Use yocto-bsp-kernel to debug why my devicetree is missing from deploy/images.
```

```text
Use yocto-security-sbom to review this license checksum and SBOM setup.
```

## Contents

- `SKILL.md`: root compatibility router
- `skills/*/SKILL.md`: focused installable skills
- `skills/*/references/`: generated per-skill copies that make each skill self-contained
- `.claude-plugin/`: Claude Code plugin and marketplace manifests
- `tools/sync_references.py`: regenerates the per-skill reference copies
- `tools/validate_skills.py`: validates frontmatter, links, drift, and public-repo disclosure
- `references/shared/official-doc-map.md`: official Yocto/BitBake documentation routing by problem type
- `references/shared/yocto-field-guide.md`: compact field guide for recipes, layers, tasks, QA, images, providers, and BSP/kernel work
- `references/bitbake/variables-core.md`: variables agents often confuse
- `references/bitbake/classes-core.md`: common classes and review rules
- `references/bitbake/tasks-reference.md`: task-level debugging reference
- `references/yocto/qa-errors.md`: common QA error patterns
- `references/yocto/migration.md`: release-aware migration checks
- `references/yocto/image-rootfs.md`: image and rootfs troubleshooting
- `references/yocto/bsp-kernel.md`: BSP and kernel troubleshooting
- `references/yocto/security-sbom.md`: security, license, CVE, and SBOM workflows
- `examples/`: realistic failure examples and expected answer patterns
- `evals/prompts.md`: manual forward-test prompts with pass criteria
- `evals/cases/`: eval cases and graders for `claude plugin eval`
- `agents/openai.yaml`: UI metadata for compatible skill hosts
- `.claude/CLAUDE.md`: project rules, including the security rules for this public repository
- `.github/workflows/validate.yml`: CI that runs the validator on every push and pull request

## Development

References under `references/` are the source of truth. The copies under
`skills/*/references/` are generated, so edit the source and re-run the sync script.

```bash
python tools/sync_references.py     # regenerate the per-skill reference copies
python tools/validate_skills.py     # frontmatter, links, drift, disclosure scan
claude plugin validate . --strict   # Claude Code plugin manifest
```

This is a public repository, so the validator also scans for email addresses, real
usernames, absolute local paths, and credential patterns. See
CONTRIBUTING.md and .claude/CLAUDE.md.

## License

MIT

# harveer10x/earned-vs-burned-skill

## 导航

- 项目页：[[10-项目/github.com_3d554909]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
