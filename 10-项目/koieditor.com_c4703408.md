---
type: "project"
title: "Show HN: Koi Editor Alpha"
project_url: "https://koieditor.com/"
first_seen: "2026-09-20T14:57:50+08:00"
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
> 首次收录：2026-09-20T14:57:50+08:00
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

## 摘要正文

EN JP CN   Report a problem →   koi.  # Your text editor  for code  A fast, minimal, local-first, scriptable code editor for macOS   Download for Mac Pricing Join Discord for Alpha access →  Apple Silicon · macOS 13.2+ · Releases· Changelog· Discord  timer.py Untitled · timer.py 3  ```  1     2    > How does rumps work in python? Give a small example  3     4    rumps (Ridiculously Uncomplicated Mac os x Python Statusbar) creates macOS menu bar apps.  5     6    Here's a small example:  7      8    import rumps  9    10    class MyApp(rumps.App): 11        def __init__(self): 12            super().__init__("MyApp", icon="icon.png") 13            self.menu = ["Preferences", "About", rumps.separator, "Quit"] 14    15        @rumps.clicked("Preferences") 16        def prefs(self, _): 17            rumps.alert("Preferences clicked!") 18    19        @rumps.clicked("About") 20        def about(self, _): 21            rumps.alert("This is my app!") 22    23        @rumps.clicked("Quit") 24        def quit_app(self, _): 25            rumps.quit_application() 26     27    if __name__ == "__main__": 28        MyApp().run() 29     30      ```  ```  1    # tray timer using rumps  2    import …
