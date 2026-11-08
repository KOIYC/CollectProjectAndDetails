---
type: "project"
title: "Ran my first playtest here is what I learned"
project_url: "https://v.redd.it/kvg3p666m4yh1"
first_seen: "2026-11-08T12:52:11+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/buildinpublic
lang: "en"
---

# Ran my first playtest here is what I learned

> [!info] 一句话导读
> I finally got about 20 people together to test Poached last week

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://v.redd.it/kvg3p666m4yh1>
> 首次收录：2026-11-08T12:52:11+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/buildinpublic
> 最新指标：得分=6 · 评论=12 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-08T12:52:11+08:00 | Reddit 独立开发版块 | 得分=6 · 评论=12 · 赞踩比=1 | [[20-语料/posts/reddit/2026-11-08/ddb482011eaab069_Ran-my-first-playtest-here-is-what-I-learned]] |

## 摘要正文

I finally got about 20 people together to test Poached last week  & halfway through, everyone started freezing and jumping around. soooo my first playtest failed(ish)  Poached is the biggest game I’ve attempted for EggVerse so far. Think MOBA (League/DOTA) x capture the flag (Fat Princess) typa game. 12 v 12 with matches aiming to run around 12-15 minutes  The matches started fine, which made the lag even more confusing. Turns out, every time the server saved the match, it stopped sending updates to the players until the save finished. The longer the match went on, the longer the saves took… & the worse it got  I rebuilt how rooms handle traffic and load-tested it with bots. In those tests, frame freezes went from 7 to 0, and worst-case ping dropped from about 150 ms to about 70 ms. Promising, but bots aren’t people, so the next playtest will be the real check  But the good part? People actually enjoyed the game & the only feedback i got was pretty much "cosmetic"  * They didn’t know they could break trees/rocks, so I’m adding outlines around things you can break * They couldn’t tell when they were being targeted by the towers, so I’m adding a red outline * The map was confusing, s…
