---
type: "corpus"
item_id: "7b65be78e8dce92e"
title: "Show HN: Starquix – Open-source local visual Astro website builder"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50553109"
project_url: "https://github.com/Mayhopar/Starquix"
author: "mayhopar"
published_at: "2026-11-18T22:21:46Z"
captured_at: "2026-11-19T09:56:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - hn_show
  - author_mayhopar
  - story_50553109
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Starquix – Open-source local visual Astro website builder

> [!info] 一句话导读
> Visual editor for Astro websites — your folder stays a real Astro site, you edit it like a design file.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50553109>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：mayhopar　|　发布：2026-11-18T22:21:46Z
> 项目链接：<https://github.com/Mayhopar/Starquix>
> 采集：2026-11-19T09:56:08+08:00　|　id：`7b65be78e8dce92e`

## 正文

# Mayhopar/Starquix

Visual editor for Astro websites — your folder stays a real Astro site, you edit it like a design file.

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: MIT License
- Homepage: starquix.app
- Default branch: main
- Created: 2026-11-18T19:38:16Z

## Languages

- Astro
- CSS
- HTML
- JavaScript
- MDX
- Shell
- TypeScript

## Topics

- astro
- astrojs
- cms
- design-tool
- desktop-app
- electron
- local-first
- low-code
- macos
- mcp-server
- mdx
- no-code
- page-builder
- react
- seo
- tailwindcss
- typescript
- visual-editor
- vite
- website-builder

## Top Contributors

- Mayhopar (2 contributions)

---

## README

 Free visual editor for Astro websites. Mac app.

Starquix opens your Astro project folder and shows the real site on a canvas. Select an element and change it in the Design panel; the change is written to your files. The project stays a plain Astro and Tailwind folder on your computer.

## Build with agents

Run Claude Code, Codex or another CLI agent in the built-in terminal, or chat in the app with your own API key (Anthropic, OpenAI, OpenRouter or a local Ollama). Agents edit the open project through the built-in MCP server, and their changes show on the canvas.

## Edit by hand

Change text, images, colors and layout on the canvas or in the Design panel.

## Publish or export

Publish to Cloudflare or GitHub Pages, to Netlify or Vercel through your GitHub repo, or export the project folder.

## Also included

 CMS. Write blog posts and publish them as pages.
 SEO. Titles, descriptions and a score for every page.

 Variables. Change a color once and it updates everywhere.
 Local files. Your site is plain Astro files in a folder on your computer.

## Development

```bash
git clone https://github.com/Mayhopar/starquix.git
cd starquix
npm ci
npm ci --prefix preview-template
npm ci --prefix desktop
npm --prefix app run dev -- --host 127.0.0.1 --port 3061 --strictPort   # the editor the desktop app loads
```

Then, in a second terminal:

```bash
cd desktop && npm run deps && npm start      # desktop app
```

Requires Node.js 22+ and npm 10. The desktop app runs on macOS.

Tests: `cd app && npm run test:run` and `cd desktop && npm test`.

| Folder | Contents |
|---|---|
| `app/` | Editor (Vite + React) |
| `desktop/` | Electron app: runs each project's Astro dev server |
| `preview-template/` | Vite plugin and canvas bridge copied into each project |
| `mcp/` | MCP server for coding agents |
| `scripts/` | Bridge and snapshot builds |
| `fixtures/` | Sample Astro project for tests |
| `docs/` | Architecture, data flows, how-tos |

The bridge source is `app/src/bridge/parts/`. After changing it or `preview-template/`, run `npm run build:snapshot`.

Bug fixes need a regression test. Contributing: CONTRIBUTING.md.

## Privacy

Projects and API keys are stored on your computer. The app goes online to:

- count anonymous page views with Plausible (no cookies; `app/src/main.tsx`);
- check GitHub for a newer release (`desktop/src/update-check.mjs`);
- load Google Fonts when you pick a font;
- reach the AI provider and publishing services you connect, with your own keys and accounts.

Third-party code and assets: THIRD_PARTY_NOTICES.md.

## License

MIT. Third-party components keep their own licenses (THIRD_PARTY_NOTICES.md). The Starquix name and logo were created by Oleg Maykhopar and are not covered by the license; using them requires his permission.

Error fetching https://i.redd.it/5vvafm0h8g0i1.png: CRAWL_EMPTY_CONTENT

## 关联链接

- https://github.com/Mayhopar/starquix.git
- https://i.redd.it/5vvafm0h8g0i1.png:

## 导航

- 项目页：[[10-项目/github.com_2c90a3a1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
