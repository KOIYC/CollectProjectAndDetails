---
type: "project"
title: "[送码] 的一些问题以及解决方案"
project_url: "https://chromewebstore.google.com/detail/nocamfkfejlkimolcededcllhokjhlgg"
first_seen: "2026-11-16T10:06:32+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# [送码] 的一些问题以及解决方案

> [!info] 一句话导读
> v 站有很多独立开发者，看到了很多送码帖子里面的痛点，于是做了这个插件解决这个问题

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://chromewebstore.google.com/detail/nocamfkfejlkimolcededcllhokjhlgg>
> 首次收录：2026-11-16T10:06:32+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-16T10:06:32+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-16/c80158268b8e1b68_送码-的一些问题以及解决方案]] |

## 摘要正文

v 站有很多独立开发者，看到了很多送码帖子里面的痛点，于是做了这个插件解决这个问题   # 问题  问题 1：兑换码用了，不说，还需要用户一个一个的去尝试  问题 2：兑换码有可能被脚本爬了，用了  问题 3：找不到兑换入口  问题 4：找 OP 要，需要留邮箱，虽然 base64 加密了，但是也有隐私泄露给其他人的风险  问题 5：如果不能及时看消息，OP 发的新的兑换码本来是给 100 楼的，结果被其他人用了  问题 N......    ![](  )   ![](  )   ![](  )       # 解决方案原理：    领取人和发放人都需要安装这个插件，这个插件自动获取 V2EX 的公开信息（ https://www.v2ex.com/api/members/show.json?username=Livid ） 进行登录，一个 V2EX 账号领取一个码，当然，如果简简单单的用这个 username 进行肤浅的判断，那肯定是行不通的，所以，在领取的时候，还需要根据 V2EX 官方令牌进行真正的校验是本人 V2EX 官方 API （ https://edge.v2ex.com/help/api#my-profile ） , 我在这里承落 ，不存储所有人的令牌，令牌插件本地存储，（如果担心，可以用完就删掉令牌）      # 插件下载地址：    https://chromewebstore.google.com/detail/nocamfkfejlkimolcededcllhokjhlgg?utm_source=item-share-cb      # 最后的话  目前插件昨天晚上刚审核通过，有遇到问题可以在评论区留言，我进行修复，不玻璃心 ，插件刚上线，没什么数据，哪位开发者做第一只吃螃蟹的人呢？
