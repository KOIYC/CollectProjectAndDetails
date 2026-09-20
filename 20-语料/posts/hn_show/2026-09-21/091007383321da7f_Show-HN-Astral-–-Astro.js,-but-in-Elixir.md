---
type: "corpus"
item_id: "091007383321da7f"
title: "Show HN: Astral – Astro.js, but in Elixir"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49508900"
project_url: "https://github.com/elixir-volt/astral"
author: "dannote"
published_at: "2026-08-31T12:32:30Z"
captured_at: "2026-09-21T03:11:23+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_dannote
  - story_49508900
  - show_hn
metrics: {"points": 10, "comments": 3, "engagement_velocity": 10}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:52d"
---

# Show HN: Astral – Astro.js, but in Elixir

> [!info] 一句话导读
> Volt-powered static site generator for Elixir applications.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49508900>
> 指标：点赞=10 · 评论=3 · engagement_velocity=10
> 作者：dannote　|　发布：2026-08-31T12:32:30Z
> 项目链接：<https://github.com/elixir-volt/astral>
> 采集：2026-09-21T03:11:23+08:00　|　id：`091007383321da7f`

## 正文

# elixir-volt/astral

Volt-powered static site generator for Elixir applications.

- Stars: 28
- Forks: 0
- Watchers: 28
- Open issues: 1
- License: MIT License
- Homepage: https://hexdocs.pm/astral/readme.html
- Default branch: master
- Created: 2026-06-25T14:02:03Z

## Languages

- Elixir
- Svelte
- TypeScript

## Topics

- eex
- elixir
- hmr
- markdown
- mdex
- no-nodejs
- ssg
- static-site-generator
- typescript
- volt

## Top Contributors

- dannote (115 contributions)

---

## README

# Astral ✨

Hex.pm Documentation

Static site generation for Elixir. Astral gives you Astro-class site features — pages, Markdown, layouts, content collections, pagination, feeds, sitemaps, and component templates — while Volt handles TypeScript, CSS, assets, dev serving, and HMR.

```bash
mix igniter.install astral
mix astral.dev
mix astral.build
```

Build docs, blogs, marketing pages, and content sites with Elixir config and templates. No JavaScript site config, no separate bundler process, no Node.js requirement for the default toolchain.

## Why Astral

Most static site generators put your content model, routing, and build configuration in JavaScript. Astral keeps the site layer in Elixir and delegates frontend assets to Volt.

You get the pieces expected from a modern static site framework:

- File-based static pages from Markdown, HTML, and `.astral` templates.
- Markdown content with HEEx-style local components through MDEx.
- Dynamic file routes such as `pages/blog/[slug].astral` and `pages/docs/[...path].md`.
- HEEx-first `.astral` pages, layouts, and local components.
- Schema-backed content collections with Ecto-style fields, JSONSpec maps, or Zoi schemas.
- Static pagination and generated routes for blogs, docs, and indexes.
- Built-in feed and sitemap plugins.
- Stable Markdown heading anchors for table-of-contents layouts.
- Optimized build-time images with `<.image>`, `<.picture>`, and `<.figure>` components.
- Client-only islands for Volt-powered framework components.
- Public files copied as-is.
- TypeScript, CSS, imported assets, browser environment variables, dev serving, and HMR through Volt.
- Plug/Bandit dev server with full reloads for pages, layouts, components, and public files.
- Igniter-powered starter scaffolding.

Astral is early but usable for small static sites, documentation prototypes, and blogs. See the roadmap for planned work.

## Elixir site config

`astral.config.exs` is ordinary Elixir:

```elixir
import Astral.Config

layouts do
  default "site.astral"
end

assets do
  entry "app.ts"
  url_prefix "/assets"
end
```

See the Getting Started guide and Configuration cheatsheet.

## HEEx-first static templates

`.astral` templates use Phoenix HEEx syntax but render static HTML:

```astral
---
assigns = assign(assigns, :title, "Home")
---

<h1>{@title}</h1>
<.pill :for={feature <- @features}>{feature}</.pill>
```

Local components and slots use HEEx conventions:

```astral
<!-- components/card.astral -->
<article class="card">
  {render_slot(@inner_block)}
</article>
```

Browser assets inside `.astral` templates are extracted into Volt's asset graph:

```astral




```

Markdown can use the same local components:

```md
# Project

<.card>
  Rendered inside Markdown by MDEx and HEEx.
</.card>
```

See the `.astral` Templates guide and Pages and Layouts guide.

## Content collections

Define typed content collections in Elixir:

```elixir
collection :posts, "content/posts" do
  permalink "/blog/:slug/"
  layout "post.html"

  schema do
    field :title, :string, required: true
    field :date, :date, required: true
    field :draft, :boolean, default: false
    field :tags, {:array, :string}, default: []
    field :cover, :image
  end
end
```

Image fields resolve relative to their entry file, expose dimensions and format, and can be passed directly to `<.image>`, `<.picture>`, or `<.figure>`.

Allow trusted remote image optimization with URL-shaped policies:

```elixir
image do
  allow_remote "https://images.example.com/**"
end
```

Use validated data from layouts and templates:

```eex
<%= for post <- @collections.posts do %>
  <a href={post.route_path}><%= post.data.title %></a>
<% end %>
```

Collection-backed dynamic file routes let page templates own the detail page HTML:

```text
content/posts/hello.md
pages/blog/[slug].astral
```

See the Content Collections guide and Pages and Layouts guide.

## Pagination, feeds, and sitemaps

Build common site routes with plugins:

```elixir
plugin Astral.Plugin.CollectionPages,
  collection: :posts,
  pattern: "/blog/*page",
  page_size: 10,
  layout: "blog.html"

plugin Astral.Plugin.Feed,
  site_url: "https://example.com",
  title: "My Blog",
  author: "Me",
  collection: :posts

plugin Astral.Plugin.Sitemap,
  site_url: "https://example.com"
```

Add one-off generated files directly in config with Phoenix-shaped `get` routes:

```elixir
get "/robots.txt", content_type: "text/plain" do
  "User-agent: *\nAllow: /\n"
end

get "/search-index.json", content_type: "application/json" do
  Jason.encode!(MySite.Search.index(site))
end
```

Use Astral plugins for site semantics and Volt plugins for browser asset integrations. See Pagination and Generated Routes, Feeds and Sitemaps, and Plugins and Integrations.

## Optimized images and Volt-powered assets

Render optimized images from `.astral` pages or component-aware Markdown:

```astral
<.image src="images/hero.jpg" alt="Hero" width={1200} format={:webp} />

<.picture
  src="images/hero.jpg"
  alt="Hero"
  widths={[480, 768, 1200]}
  formats={[:webp, :avif]}
/>

<.figure src="images/hero.jpg" alt="Hero" caption="Product hero" width={1200} />
```

Astral writes compressed, content-hashed variants to `dist/assets/` during static builds. Local Markdown image syntax is optimized too:

```md
Hero
```

Include trusted local SVG files inline when you need definitions, masks, or hand-authored SVG markup:

```astral
<.svg src="@/icons/clip-paths.svg" class="sr-only" />
```

Reference source frontend assets from layouts:

```eex


```

In development this points to Volt's dev server. In static builds it resolves through Volt's manifest to content-hashed output files.

See the Assets guide, Editor Setup and TypeScript guide, Environment Variables guide, and the Volt documentation for frontend tooling details.

## Icons

Render Iconify icons server-side with PhoenixIconify; Astral prepares the icon manifest during build/dev rendering:

```astral
<.icon name="ri:external-link-fill" class="inline-block" width="12" height="12" />
```

## Client islands

Mount a browser component from your Volt assets:

```astral
<.vue
  component="islands/Gallery.vue"
  client={:visible}
  props={%{images: @images}}
>
  <div class="thumbnail-strip">Static HEEx children become the default framework slot.</div>
</.vue>
```

Astral provides framework-specific island components for every framework Volt supports: `<.vue>`, `<.svelte>`, `<.react>`, and `<.solid>`. Multiple framework island types may be mixed on the same page, repeated, nested inside another island's slot, and given different client directives. Production island entries are emitted as ES modules so Volt can share common runtime/framework chunks across repeated islands when the installed Volt version supports multi-entry shared chunks. All adapters are enabled by default; configure `islands do adapter :vue end` only if you want to restrict the allowed set. Client directives include `:load`, `:idle`, `:visible`, and `:media` with a media query string. The current island milestone is client-only: Astral renders a container, static slot template, and generated entry module, while Volt compiles the imported framework component.

Nested islands can cross framework boundaries. The child island is rendered into the parent's static slot HTML, then hydrates after the parent framework has mounted:

```astral
<.react component="islands/Shell.jsx" client={:load}>
  <.svelte component="islands/NestedButton.svelte" client={:load} props={%{label: "Buy"}} />
</.react>
```

## Development and builds

```bash
mix astral.dev --open
mix astral.build
```

`mix astral.dev` serves routes, public files, Volt assets, HMR, and useful HTML error pages. `mix astral.build` writes static files to `dist/` for any static host or CDN.

See the Development Server guide and Static Builds guide.

## Example site

A runnable example lives in `examples/basic`:

```bash
cd examples/basic
mix deps.get
mix astral.dev
mix astral.build
mix check
```

It demonstrates Markdown, HTML pages, `.astral` pages/layouts/components, public files, Volt TypeScript/CSS assets, feeds, sitemaps, and Volt JS/TS formatting/linting.

## Documentation

Full documentation, guides, and cheatsheets are available on HexDocs.

## Development

```bash
mix deps.get
mix ci
```

## License

MIT © 2026 Danila Poyarkov

# alexellis/glm-5.3-flash-4x-dgx-spark-switchless

## 评论（3/3）

> **recursivegirth** · 2026-08-31T13:51:18.000Z　
> Any major differentiators between this and Phoenix? I have been getting more into Elixir lately coming from Laravel and React projects. Been having a blast.

---

> **DylanMerigaud** · 2026-08-31T14:03:15.000Z　
> Congrats on shipping this.

---

> **dannote** · 2026-08-31T14:39:54.000Z　
> The main difference is that Astral is a static site generator. It also doesn’t require Node.js (or a compatible runtime), because it’s built on Volt [1], which in turn uses the QuickBEAM runtime [2].[1] https://github.com/elixir-volt/volt[2] https://github.com/elixir-volt/quickbeam

## 关联链接

- https://example.com
- https://hexdocs.pm/astral/readme.html
- https://images.example.com/**

## 导航

- 项目页：[[10-项目/github.com_4c76cb34]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
