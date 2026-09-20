---
type: "corpus"
item_id: "d14dcdf85940dd5d"
title: "Enterprise-DNA-OS/ai-app-idea-generator"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/Enterprise-DNA-OS/ai-app-idea-generator"
project_url: "https://enterprisedna.co/"
author: "Enterprise-DNA-OS"
published_at: "2026-04-10T05:13:21Z"
captured_at: "2026-09-20T09:36:29+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-04-10"
tags:
  - 语料
  - github_new
  - TypeScript
  - topic:indie-hacker
metrics: {"stars": 3, "forks": 0, "open_issues": 0}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# Enterprise-DNA-OS/ai-app-idea-generator

> [!info] 一句话导读
> <img src="public/logo.svg" alt="AI App Idea Generator" width="80" height="80" />

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/Enterprise-DNA-OS/ai-app-idea-generator>
> 指标：stars=3 · forks=0 · open_issues=0
> 作者：Enterprise-DNA-OS　|　发布：2026-04-10T05:13:21Z
> 项目链接：<https://enterprisedna.co/>
> 采集：2026-09-20T09:36:29+08:00　|　id：`d14dcdf85940dd5d`

## 正文

AI App Idea Generator

  The open-source AI tool that turns raw app ideas into build-ready product specs.

  Created by Enterprise DNA -- a leading data and AI education company.

  What is it? &bull;
  Built with AI &bull;
  Features &bull;
  Tech Stack &bull;
  Quick Start &bull;
  Self-Hosting &bull;
  Architecture &bull;
  Dev with AI &bull;
  Contributing &bull;
  License

---

## What is AI App Idea Generator?

AI App Idea Generator is an open-source web app that takes a rough idea -- a few sentences describing what you want to build -- and uses AI to produce a complete, build-ready product specification. It's the fastest way to go from "I have an idea" to "I have a plan I can actually hand to a developer (or AI coding agent)."

Think of it as an **AI product manager in a box**: describe the problem, pick your industry and function, and the app generates:

- A clear project title and pitch
- A full questionnaire walkthrough that sharpens the concept
- A detailed outline document
- Functional requirements
- Tech stack recommendations
- Frontend guidelines
- Backend structure
- File structure
- Implementation plan and task breakdown

All generated content is saved to your own Supabase project, so you can revisit, edit, and export later.

### Why another idea tool?

Most "startup idea generators" give you a sentence and walk away. AI App Idea Generator is different:

- **Full product specs, not hype** -- You get a PRD, tech stack, file structure, and tasks. Not just a tagline.
- **Questionnaire-driven** -- The app asks smart follow-up questions to tighten the scope before generating docs.
- **Industry- and function-aware** -- Ideas are tailored to your vertical (Healthcare, Finance, Retail, etc.) and business function (Sales, Operations, HR, etc.)
- **17 specialized AI endpoints** -- Each document type (outline, tech stack, tasks, etc.) has its own dedicated Supabase Edge Function with a tuned prompt.
- **Self-hostable** -- Bring your own OpenAI API key, run it on your own Supabase project, own every generated artifact.
- **Built to be handed to AI coders** -- The output format is designed so you can paste it straight into Claude Code, Cursor, or any other AI coding tool and start building.

---

## Built with AI

> **This entire application was built using AI-assisted development tools.** Enterprise DNA believes in the future of AI-augmented software development, and this project is a reference for what's possible. Every layer -- from the Supabase edge functions to the React UI -- was written collaboratively with AI coding agents.

### AI Development Tools Used

| Tool | Role |
|------|------|
| **[Claude Code](https://claude.ai/claude-code)** by Anthropic | Primary development tool. Claude Code acted as the AI coding agent, building features end-to-end across the full stack -- from Supabase edge functions to React components to page layouts. |
| **[Cursor](https://cursor.com)** | AI-powered IDE used throughout development for code navigation, inline edits, and rapid iteration. |
| **[GitHub Copilot](https://github.com/features/copilot)** | AI pair programming assistant for code completion and pattern matching. |

Enterprise DNA is committed to demonstrating that AI tools are not just productivity boosters -- they are a new way to build software. This project serves as a reference implementation for AI-assisted full-stack development.

---

## Features

### Idea Capture
- Free-form app idea textarea on the landing page
- Guided inspiration flow: pick industry + business function + describe your daily tasks, get tailored idea suggestions
- Pre-made templates by industry (Healthcare, Education, Finance, Retail, Manufacturing, Technology, Real Estate, Transportation, Hospitality)
- AI-generated project titles from free-form descriptions

### Smart Questionnaire
- Dynamic AI-generated questions that adapt to your idea
- Follow-up question generation based on previous answers
- Saves all responses to your Supabase project tied to each user

### Document Generation
Seventeen specialized Supabase Edge Functions, one for each document type:

| Function | What it produces |
|---|---|
| `generate-title` | A concise project title from a description |
| `generate-idea` | A sharpened idea pitch based on industry + function + daily tasks |
| `generate-questions` | Dynamic follow-up questions for the questionnaire |
| `generate-answer` | AI-drafted answers for review |
| `generate-app-ideas` | Multiple app idea suggestions for an industry + function pair |
| `generate-app-outline` | Full app outline from a template |
| `generate-app-flow` | User flows and interaction map |
| `generate-requirements` | Functional and non-functional requirements |
| `generate-tech-stack` | Recommended tech stack with reasoning |
| `generate-frontend-guidelines` | Frontend design and component guidelines |
| `generate-backend-structure` | Backend architecture and data model |
| `generate-file-structure` | Recommended project file/folder layout |
| `generate-implementation-plan` | Step-by-step build plan |
| `generate-tasks` | Individual developer tasks |
| `generate-document` | Combine generated sections into a polished doc |
| `analyze-submission` | Sanity-check user input before generation |

### Project Management
- Save every generated project to the **Projects** page
- Drill into any project to see its full document set
- Access Details view with deep links to each generated section
- Update and delete projects you own

### Authentication
- Email + password via Supabase Auth
- Google OAuth support (optional -- configure in your Supabase dashboard)
- Password reset flow with email confirmation
- Protected routes for logged-in users
- Profile page with account information

### UI / UX
- Enterprise DNA gradient brand colors throughout
- Responsive design (mobile-friendly from day one)
- Dark mode ready via `next-themes`
- Rich form controls powered by shadcn/ui + Radix
- Toast notifications via Sonner
- Smooth transitions and micro-interactions via Tailwind animations

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | [Vite](https://vitejs.dev/) + [React 18](https://react.dev/) |
| Language | [TypeScript 5](https://www.typescriptlang.org/) |
| UI Library | [shadcn/ui](https://ui.shadcn.com/) + [Radix UI](https://www.radix-ui.com/) |
| Styling | [Tailwind CSS 3](https://tailwindcss.com/) |
| Icons | [Lucide React](https://lucide.dev/) |
| Database | [Supabase](https://supabase.com/) (PostgreSQL + Row Level Security) |
| Auth | Supabase Auth (email/password + OAuth) |
| AI Runtime | Supabase Edge Functions (Deno) |
| AI Provider | [OpenAI API](https://platform.openai.com/) (GPT-4o-mini by default) |
| State | [Zustand](https://github.com/pmndrs/zustand) + [TanStack Query](https://tanstack.com/query) |
| Forms | [React Hook Form](https://react-hook-form.com/) + [Zod](https://zod.dev/) |
| Routing | [React Router DOM](https://reactrouter.com/) |
| Deployment | [Netlify](https://netlify.com/) (frontend) + Supabase (backend) |

---

## Quick Start

### Prerequisites
- **Node.js 18+** and npm (or bun)
- A **[Supabase](https://supabase.com/)** account (free tier works)
- An **[OpenAI API key](https://platform.openai.com/api-keys)** (pay-as-you-go)

### Step 1: Clone and Install

```bash
git clone https://github.com/Enterprise-DNA-OS/ai-app-idea-generator.git
cd ai-app-idea-generator
npm install
```

### Step 2: Create Your Supabase Project

1. Sign in at [supabase.com](https://supabase.com/) and click **New Project**
2. Wait for the project to provision (~2 minutes)
3. From **Settings → API**, copy:
   - **Project URL** → `VITE_SUPABASE_URL`
   - **anon / public key** → `VITE_SUPABASE_ANON_KEY`

### Step 3: Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your Supabase credentials:

```bash
VITE_SUPABASE_URL=https://your-project-id.supabase.co
VITE_SUPABASE_ANON_KEY=your-supabase-anon-key
```

### Step 4: Deploy Edge Functions

Install the Supabase CLI and link your project:

```bash
npm install -g supabase
npx supabase login
npx supabase link --project-ref your-project-id
```

Deploy all 17 generation functions:

```bash
npx supabase functions deploy
```

### Step 5: Set Supabase Secrets

AI API keys live in Supabase secrets (not in `.env`). Set your OpenAI key:

```bash
npx supabase secrets set OPENAI_API_KEY=sk-your-openai-key
```

### Step 6: Apply Database Schema

Create the tables the app uses. In your Supabase dashboard, open the SQL editor and create these tables (see [Database Schema](#database-schema) below), or run:

```bash
npx supabase db push
```

### Step 7: Run Locally

```bash
npm run dev
```

Open [http://localhost:8080](http://localhost:8080) and sign up for an account. Describe your first app idea and watch the AI generate the full spec.

---

## Self-Hosting

AI App Idea Generator can be deployed anywhere that hosts a static Vite build.

### Netlify (recommended)

The repo already includes a `netlify.toml`. Push to a GitHub repo and connect it to Netlify. Set the environment variables in Netlify's dashboard under **Site settings → Environment variables**.

```bash
npm run build
netlify deploy --prod
```

### Vercel

```bash
npm run build
vercel deploy --prod
```

Set `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY` in the Vercel project settings.

### Static hosting

`npm run build` produces a `dist/` folder you can host anywhere:
- Cloudflare Pages
- GitHub Pages
- Any S3 + CloudFront setup

### Production Deployment Checklist

1. **Update environment variables** in your hosting platform
2. **Supabase Auth settings** -- Add your production domain to the allowed redirect URLs
3. **Google OAuth** (if using) -- Add your production URL to the authorized redirect URIs in Google Cloud Console
4. **Enable HTTPS** -- required for Supabase Auth to work correctly
5. **Monitor edge function logs** in your Supabase dashboard

---

## Architecture

### Project Structure

```
src/
  App.tsx                  Root with providers and routing
  main.tsx                 Entry point
  components/
    auth/                  Auth form and modal
    home/                  Landing page sections (Hero, HowItWorks, Templates, etc.)
    ui/                    shadcn/ui primitives
    ProtectedRoute.tsx     Auth gate for private pages
    Navbar.tsx             Top navigation
    Footer.tsx             Footer
  contexts/
    UserContext.tsx        Current user + loading state from Supabase
  hooks/                   Custom React hooks
  integrations/
    supabase/              Supabase client + generated types
  pages/
    Index.tsx              Landing page
    Auth.tsx               Login page
    Register.tsx           Signup page
    Questionnaire.tsx      Guided questionnaire flow
    Projects.tsx           User project list
    ProjectDetails.tsx     Individual project view
    GenerateDocuments.tsx  Document generation page
    Profile.tsx            Account info
  lib/                     Utilities
  utils/                   Helper functions
  types/                   Shared TypeScript types
supabase/
  config.toml              Function configuration
  functions/
    _shared/               Shared OpenAI config + CORS helpers
    generate-*/            17 AI generation edge functions
    analyze-submission/    Input validation
```

### AI Flow

```
User input
  → React form submission
    → Supabase Edge Function (Deno runtime)
      → OpenAI API (GPT-4o-mini)
    ← Structured response
  ← JSON rendered in the UI + saved to Supabase
```

All AI calls go through Supabase Edge Functions. Your OpenAI API key lives in Supabase secrets -- it never touches the browser.

### Database Schema

The app uses a small set of Postgres tables in Supabase:

- **`user_projects`** -- One row per generated project. Stores title, description, status, and ownership (`user_id` FK to `auth.users`)
- **`questionnaire_responses`** -- Stores user answers to the guided questionnaire, tied to a project
- **`generated_documents`** -- Stores AI-generated document sections (outlines, requirements, etc.) per project

Row Level Security (RLS) is enforced on every user-facing table so users only ever see their own data.

---

## Developing with AI Tools

This project is designed to work well with AI development tools. Two files make this explicit:

- **`CLAUDE.md`** -- Project-wide instructions, conventions, and architecture overview. Claude Code reads this automatically.
- **`AGENTS.md`** -- Defines specialist agents with clear ownership boundaries.

### Using Claude Code

Open the project folder in Claude Code. The agent will pick up `CLAUDE.md` and `AGENTS.md` automatically and follow the conventions.

### Using Cursor

Open the project in Cursor. The `CLAUDE.md` file serves as context for Cursor's AI features. Use inline edit (Cmd+K) for quick changes and the chat panel for larger refactors.

### Using GitHub Copilot

Copilot picks up patterns from the existing codebase (Supabase client usage, auth checks, Tailwind conventions). The consistent conventions in `CLAUDE.md` make Copilot suggestions more accurate.

### Contributing with AI Tools

We encourage contributors to use AI tools. If you submit a PR:

1. Mention which AI tools you used -- we see it as a positive
2. Follow the conventions in `CLAUDE.md`
3. Use the specialist agent boundaries in `AGENTS.md`
4. Run `npx tsc --noEmit` and `npm run build` before submitting

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

**TL;DR:**

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes (AI tools welcome)
4. Run `npx tsc --noEmit` and `npm run build` to verify
5. Commit with a descriptive message
6. Push to your fork and open a PR

---

## License

[MIT](LICENSE) -- use it however you want.

---

## Acknowledgments

- Built with [Claude Code](https://claude.ai/claude-code) by Anthropic
- Developed in [Cursor](https://cursor.com) -- the AI-powered IDE
- AI pair programming by [GitHub Copilot](https://github.com/features/copilot)
- AI generation powered by [OpenAI](https://openai.com)
- Database, auth, and edge functions by [Supabase](https://supabase.com)
- UI components from [shadcn/ui](https://ui.shadcn.com/) and [Radix UI](https://www.radix-ui.com/)
- Originally released as **App Idea Engine** by Omni Intelligence

---

  Built with pride by Enterprise DNA

  Powered by AI-assisted development with Claude Code, Cursor, and GitHub Copilot

## 关联链接

- http://localhost:8080
- https://claude.ai/claude-code
- https://cursor.com
- https://github.com/Enterprise-DNA-OS/ai-app-idea-generator.git
- https://github.com/features/copilot
- https://github.com/pmndrs/zustand
- https://img.shields.io/badge/License-MIT-yellow?style=flat-square
- https://img.shields.io/badge/React-18-61dafb?style=flat-square
- https://img.shields.io/badge/Supabase-PostgreSQL-3ecf8e?style=flat-square
- https://img.shields.io/badge/Tailwind-3-38bdf8?style=flat-square
- https://img.shields.io/badge/TypeScript-5-3178c6?style=flat-square
- https://img.shields.io/badge/Vite-5-646cff?style=flat-square
- https://lucide.dev/
- https://netlify.com/
- https://openai.com
- https://platform.openai.com/
- https://platform.openai.com/api-keys
- https://react-hook-form.com/
- https://react.dev/
- https://reactrouter.com/
- https://supabase.com
- https://supabase.com/
- https://tailwindcss.com/
- https://tanstack.com/query
- https://ui.shadcn.com/

## 导航

- 项目页：[[10-项目/enterprisedna.co_fe0cae1f]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
