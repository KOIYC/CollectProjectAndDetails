---
type: "corpus"
item_id: "a33332663f01bbdf"
title: "Show HN: UART Terminal – Web-based serial terminal using WebSerial API"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47954323"
project_url: "https://github.com/baturyilmaz/uartterminal.com"
author: "arbayi"
published_at: "2026-04-29T20:42:17Z"
captured_at: "2026-09-21T02:52:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_arbayi
  - story_47954323
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: UART Terminal – Web-based serial terminal using WebSerial API

> [!info] 一句话导读
> baturyilmaz/uartterminal.com

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47954323>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：arbayi　|　发布：2026-04-29T20:42:17Z
> 项目链接：<https://github.com/baturyilmaz/uartterminal.com>
> 采集：2026-09-21T02:52:32+08:00　|　id：`a33332663f01bbdf`

## 正文

# baturyilmaz/uartterminal.com

- Stars: 16
- Forks: 2
- Watchers: 16
- Open issues: 1
- Default branch: main
- Created: 2024-08-28T14:04:40Z

## Languages

- CSS
- HTML
- JavaScript
- TypeScript

## Top Contributors

- baturyilmaz (17 contributions)

---

## README

# UART Terminal

UART Terminal is a web-based application for serial communication. There are already some great serial terminals out there, but I wanted to create one that I could easily access and customize with my own features. This project uses the WebSerial API to make it all happen.
My hope is that this will grow into a collaborative project, bringing together different ideas and eventually becoming a user-friendly serial terminal for Chromium-based browsers. I've got some previous experience with React, so I decided to go with that for this project. I was able to build the initial skeleton pretty quickly, thanks to some help from GPT 4o.
You can access UART Terminal by visiting www.uartterminal.com, or if you prefer, you can clone the repository and run it locally.
I'm open to any and all collaboration - if you've got ideas or want to contribute, I'd really appreciate it!

Watch the video

## Features

- Connect to serial ports with customizable connection options
- Send and receive data in various formats (ASCII, Hexadecimal, Binary, Decimal)
- Auto-scrolling and manual scrolling options for received data
- Dark mode support
- Save communication logs
- Responsive design for use on different devices

I will be adding various features, with my first goal being to implement ANSI terminal capabilities similar to Hyper Terminal. Here are some other ideas (thanks again to GPT-4) that I will be considering.

- Data Visualization: Implement real-time graphing and charting capabilities for numeric data streams.
- Data Logging and Export: Enhance data logging capabilities with various export formats (CSV, JSON, etc.) and integrate cloud storage options.
- Collaborative Features: Add real-time collaboration features, allowing multiple users to view and interact with the same serial connection.(?)

## Technologies Used

- React
- TypeScript
- Tailwind CSS
- Web Serial API

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Node.js (version 12.0 or higher)
- npm (usually comes with Node.js)
- A Chromium based web browser that supports the Web Serial API (e.g., Chrome, Edge)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/baturyilmaz/uartterminal.com.git
   ```

2. Navigate to the project directory:
   ```
   cd uartterminal.com
   ```

3. Install the dependencies:
   ```
   npm install
   ```

## Usage

1. Start the development server:
   ```
   npm run dev
   ```

2. Open your web browser and navigate to `http://localhost:XXXX`

3. Configure the connection settings (baud rate, data bits, stop bits, parity)

4. Click the connect button to select a serial port

5. Once connected, you can send and receive data through the serial port

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your change
5. Push to the branch
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgements

- GPT 4o
- TypeScript
- Tailwind CSS
- Web Serial API
- Lucide Icons

## 关联链接

- http://localhost:XXXX`
- https://github.com/baturyilmaz/uartterminal.com.git

## 导航

- 项目页：[[10-项目/github.com_ebd4fd00]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
