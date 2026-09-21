---
type: "project"
title: "Show HN: Koi Editor Alpha"
project_url: "https://koieditor.com/"
first_seen: "2026-09-21T21:59:52+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_hackermanai
  - story_49756627
  - show_hn
lang: "en"
---

# Show HN: Koi Editor Alpha

> [!info] 一句话导读
> A fast, minimal, local-first, scriptable code editor for macOS

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://koieditor.com/>
> 首次收录：2026-09-21T21:59:52+08:00
> 来源渠道：HN Show HN
> 标签：author_hackermanai, story_49756627, show_hn
> 最新指标：点赞=5 · 评论=2 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/59afc4bf9a96ab4c_Show-HN-Koi-Editor-Alpha]] |
| 2026-09-20T09:36:38+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/59afc4bf9a96ab4c_Show-HN-Koi-Editor-Alpha]] |
| 2026-09-20T14:02:20+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/59afc4bf9a96ab4c_Show-HN-Koi-Editor-Alpha]] |
| 2026-09-20T14:57:50+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/59afc4bf9a96ab4c_Show-HN-Koi-Editor-Alpha]] |
| 2026-09-21T21:59:52+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/59afc4bf9a96ab4c_Show-HN-Koi-Editor-Alpha]] |

## 摘要正文

k oi . Your text editor  for code A fast, minimal, local-first, scriptable code editor for macOS Download for Mac Pricing v0.1.0-b210  · Apple Silicon  · macOS 13.2+  · Changelog koi.py 22960 # EditorContainer : _on_tab_label_clicked  22961 @func_trace  22962 def _on_tab_label_clicked ( self ):  22963 editor = ensure_not_deleted ( self .main_editor.editor)  22964 if editor is not None :  22965 safe_focus (editor)  22966  22967 # EditorContainer : _on_tab_label_toggle  22968 @func_trace  22969 def _on_tab_label_toggle ( self ):  22970 window = ensure_not_deleted ( self .window)  22971 if window is None :  22972 return  22973  22974 buffer = self .buffer  22975 if buffer is None :  22976 return  22977  22978 window.buffer_manager. toggle_active (buffer)  22979  22980 # EditorContainer : _on_tab_label_exclusive  22981 @func_trace  22982 def _on_tab_label_exclusive ( self ):  22983 window = ensure_not_deleted ( self .window)  22984 if window is None :  22985 return  22986  22987 buffer = self .buffer  22988 if buffer is None :  22989 return  22990  22991 window.buffer_manager. set_as_active_tab (buffer)  22992  22993 # EditorContainer : _file_changed  22994 @func_trace  22995 def _file…
