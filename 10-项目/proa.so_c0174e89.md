---
type: "project"
title: "Show HN: Proa – A Rust web framework with fast SSR and multi-target rendering"
project_url: "https://proa.so/"
first_seen: "2026-10-16T09:52:04+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_burnrate
  - story_50105467
  - show_hn
lang: "en"
---

# Show HN: Proa – A Rust web framework with fast SSR and multi-target rendering

> [!info] 一句话导读
> Proa Docs Ecosystem app Apps Products shipped on Proa

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://proa.so/>
> 首次收录：2026-10-16T09:52:04+08:00
> 来源渠道：HN Show HN
> 标签：author_burnrate, story_50105467, show_hn
> 最新指标：点赞=90 · 评论=26 · engagement_velocity=90

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-16T09:35:18+08:00 | HN Show HN | 点赞=90 · 评论=26 · engagement_velocity=90 | [[20-语料/posts/hn_show/2026-10-16/45b19dcb67eafa0c_Show-HN-Proa-–-A-Rust-web-framework-with-fast-SSR]] |
| 2026-10-16T09:52:04+08:00 | HN Show HN | 点赞=90 · 评论=26 · engagement_velocity=90 | [[20-语料/posts/hn_show/2026-10-16/45b19dcb67eafa0c_Show-HN-Proa-–-A-Rust-web-framework-with-fast-SSR]] |

## 摘要正文

Proa Docs Ecosystem app Apps Products shipped on Proa  dev Developer tools Components, adapters, and more Proa UI  Search ⌘ K The next era of web interfaces. Built in Rust.  An extremely performant , batteries-included Rust web framework built around a new programming model for composable, multi-target rendering.  Get started Watch intro One object. Every render target.  HTML, Markdown, and other render targets, from one typed component.  Watch multi-target rendering ProductCard :: new (product)  impl  MdRenderSync  for ProductCard {  fn render_md (self, cx: &mut WebContext ) -> Result <(), WriteError > {  md_sync! { r###"  # {self.product.name} { Link :: new ( "Buy now" , self.product.url) }  "###  }  . render_md (cx)  } }  md_sync! { r###"  [ {self.label} ]( {self.href} )  "### }  impl  WebRenderSync  for ProductCard {  fn render (self, cx: &mut WebContext ) -> Result <(), WriteError > {  html_sync! {   {self.product.name}  { Link :: new ( "Buy now" , self.product.url) }   }  . render (cx)  } }  html_sync! {   {self.label}  } Build fast, information-dense apps.  Explore re-creations of GitHub, Sentry, and Airbnb, built in Proa with fast server rendering and selective interactivit…
