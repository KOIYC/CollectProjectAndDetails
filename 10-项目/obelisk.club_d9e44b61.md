---
type: "project"
title: "做了几个不上传文件的浏览器小工具：去照片定位、批量改名预览、图片合并 PDF"
project_url: "https://obelisk.club/tools/batch-rename?lang=zh"
first_seen: "2026-10-25T23:34:58+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 做了几个不上传文件的浏览器小工具：去照片定位、批量改名预览、图片合并 PDF

> [!info] 一句话导读
> 我是独立开发者，平时做 Mac 和 iPhone 小应用。最近把几个常用功能做成了网页版，全部在浏览器本地运行，文件不会上传：

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://obelisk.club/tools/batch-rename?lang=zh>
> 首次收录：2026-10-25T23:34:58+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:34:58+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-25/888e940db20654bb_做了几个不上传文件的浏览器小工具-去照片定位、批量改名预览、图片合并-PDF]] |

## 摘要正文

我是独立开发者，平时做 Mac 和 iPhone 小应用。最近把几个常用功能做成了网页版，全部在浏览器本地运行，文件不会上传：  - **去除照片位置和 EXIF**：先列出照片里带了什么（ GPS 、机型、编辑记录），再下载一份干净的副本。https://obelisk.club/tools/remove-exif?lang=zh - **批量重命名规划**：粘贴文件名，选替换 / 加前缀 / 编号规则，先看每个新名字和冲突，再复制一段用 `mv -n`、绝不覆盖文件的 zsh 脚本。https://obelisk.club/tools/batch-rename?lang=zh - **图片合并成 PDF**：截图、照片按顺序放进一个 PDF ，没有水印。https://obelisk.club/tools/images-to-pdf?lang=zh  已知的不足：去 EXIF 暂不支持 HEIC ；批量改名一次只处理一个文件夹。欢迎挑错。
