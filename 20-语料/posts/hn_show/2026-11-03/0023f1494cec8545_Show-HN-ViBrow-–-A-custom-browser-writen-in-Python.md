---
type: "corpus"
item_id: "0023f1494cec8545"
title: "Show HN: ViBrow – A custom browser writen in Python and Zig using 35MB RAM"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50337795"
project_url: "https://github.com/HYXZKAKONHNK/ViBrow"
author: "pfehqqq"
published_at: "2026-11-02T15:06:47Z"
captured_at: "2026-11-03T09:40:36+08:00"
lang: "en"
kind: "post"
topic: "未分类"
shard: "2026-11-03"
pub_day: "2026-11-02"
tags:
  - 语料
  - hn_show
  - author_pfehqqq
  - story_50337795
  - show_hn
metrics: {"points": 2, "comments": 5, "engagement_velocity": 2}
comments_count: 5
comments_total: 5
discovered_via: "hn:show_hn:3d"
---

# Show HN: ViBrow – A custom browser writen in Python and Zig using 35MB RAM

> [!info] 一句话导读
> Author: HYXZKAKONHNK

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50337795>
> 指标：点赞=2 · 评论=5 · engagement_velocity=2
> 作者：pfehqqq　|　发布：2026-11-02T15:06:47Z
> 项目链接：<https://github.com/HYXZKAKONHNK/ViBrow>
> 采集：2026-11-03T09:40:36+08:00　|　id：`0023f1494cec8545`

## 正文

Author: HYXZKAKONHNK

GitHub - HYXZKAKONHNK/ViBrow: ViBrow — кастомный Python-браузер с собственным DOM, CSS и JS движками. Имеет многовкладвочный интерфейс, локальный кэш, cookies, встроенный поисковик и прокси-мост для обхода блокировок. Был создан 1 разработчиком, без сторонних библиотек. Потребляет 30-65МБ ОЗУ, нужен 700МГц процессор 1 ядро и 200МБ ОЗУ LPDDR1. Работает на чистом Python · GitHub

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| VIIDU | VIIDU | Add system information utility in VIIDU.py | Oct 26, 2026 |
| __pycache__ | __pycache__ | Добавление файлов кэша Python | Oct 24, 2026 |
| cache | cache | Add files via upload | Oct 25, 2026 |
| logs | logs | Log errors from viengine.py execution | Oct 24, 2026 |
| proxy | proxy | Add files via upload | Oct 24, 2026 |
| resourses | resourses | Add files via upload | Oct 25, 2026 |
| vijs_engine | vijs_engine | компилятор linux 64bit (amd, intel) | Oct 29, 2026 |
| .gitignore | .gitignore | Initial commit | Oct 24, 2026 |
| INSTRUCTIONS.md | INSTRUCTIONS.md | Fix Python version requirement in instructions | Oct 28, 2026 |
| LICENSE | LICENSE | GNU AGPL v3 | Oct 29, 2026 |
| README.md | README.md | Обновить README с новыми инструкциями и функциями | Oct 30, 2026 |
| SECURITY.md | SECURITY.md | Загружено SECURITY.md с деталями создания аккаунта | Oct 25, 2026 |
| gif_render.py | gif_render.py | Поддержка много всего | Oct 30, 2026 |
| history.py | history.py | Add files via upload | Oct 24, 2026 |
| local_cache.py | local_cache.py | Add files via upload | Oct 24, 2026 |
| oom_linux.py | oom_linux.py | Защита от OOM и проверка ОС | Oct 25, 2026 |
| oom_macos.py | oom_macos.py | Защита от OOM и проверка ОС | Oct 25, 2026 |
| oom_win32.py | oom_win32.py | Защита от OOM и проверка ОС | Oct 25, 2026 |
| os_check.py | os_check.py | Защита от OOM и проверка ОС | Oct 25, 2026 |
| requirements.txt | requirements.txt | привет | Oct 26, 2026 |
| start.bat | start.bat | Add files via upload | Oct 24, 2026 |
| viengine.py | viengine.py | Ну тоже поддержка много чего | Oct 30, 2026 |
| viengine_css.py | viengine_css.py | Enhance CSS engine with font styles and image processing | Oct 30, 2026 |
| viengine_dom.py | viengine_dom.py | Add files via upload | Oct 24, 2026 |
| viengine_js.py | viengine_js.py | Добавил поддержку нового движка | Oct 29, 2026 |
| viengine_js_else.py | viengine_js_else.py | Add files via upload | Oct 24, 2026 |
| viforge.py | viforge.py | Update print statement from 'Hello' to 'Goodbye' | Oct 30, 2026 |
| vijs_bridge.py | vijs_bridge.py | Add vijs_bridge.py for Python to JS engine integration | Oct 29, 2026 |
| View all files | | | |

# ViBrow

ViBrow – Быстрый и современный браузер, основанный на кастомном движке viengine Он написан на языке программирования Python, без каких-либо сторонних библиотек. Работает на чистом python. Весит около 44МБ распакованным

# Поддерживает операционные системы:

Windows 11 (все модификации, x64 / ARM64) — с актуальными версиями Python 3.10+ и аппаратным ускорением отрисовки окон. Windows 10 (все модификации, x64) — при условии нормальной работы диспетчера окон и отсутствия сильной фоновой нагрузки. Linux (современные дистрибутивы с легковесным окружением, например: Ubuntu 22.04 / 24.04 LTS, Debian 12, Arch Linux с XFCE, MATE или KDE Plasma) — на Linux Tkinter и сокеты работают очень шустро, а накладные расходы ОС минимальны. Работает также на устройствах типа: Raspberry Pi, Yandex Alisa, Orange Pi, Banana Pi, Radxa Zero, FPGA и прочими микрокомпьютерами macOS (версии macOS 12 Monterey, 13 Ventura, 14 Sonoma, 15 Sequoia и новее на процессорах Apple Silicon M1/M2/M3/M4) — за счет высокой производительности однопоточных вычислений процессоров Apple Silicon интерпретатор JS и отрисовка интерфейса будут работать максимально гладко.

# Работает на основе встроенных библиотек:

Tkinter, socket, ssl, threading, urllib,

# Уникальные функции

В ViBrow также присутствуют защитники от OOM (ошибки Out Of Memory), они работают в фоновых процессах и если 90% оперативной памяти занято, создают аварийный файл подкачки на 512МБ. Сначала включается фоновый процесс, который определяет операционную систему, когда он понял какая это ОС он открывает соответствующий код для этой ОС. Это очень важно для микрокомпьютеров Также в движке был реализован NaN Boxing, переход на Zig обусловлен тем, что я стремлюсь к скорости и компактности, что Zig и может дать. Переход на Zig был только в движке JavaScript (JS)

INSTRUCTIONS.md

# Лицензия

Этот проект распространяется под лицензией GNU Affero General Public License v3.0. Подробнее см. файл LICENSE.

# Упаковка файлов html в приложение

ViForge – упаковщик. Запуск как собранное приложение: python viforge.py --production Запуск как Studio (IDE): python viforge.py

## 评论（5/5）

> **asdadafa** · 2026-11-02T15:08:03.000Z　
> ViBrow

---

> **asdadafa** · 2026-11-02T15:09:07.000Z　
> ViBrow its really lifesaver for my rpi Zero

---

> **asdadafa** · 2026-11-02T15:09:14.000Z　
> ////////////////////////

---

> **asdadafa** · 2026-11-02T15:09:18.000Z　
> ////////////////////////////

---

> **asdadafa** · 2026-11-02T15:17:28.000Z　
> rtedfsrfgbhngbfvdc

## 导航

- 项目页：[[10-项目/github.com_916b05a1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`未分类`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
