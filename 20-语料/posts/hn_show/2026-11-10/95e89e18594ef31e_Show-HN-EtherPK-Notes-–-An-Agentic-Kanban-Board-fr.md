---
type: "corpus"
item_id: "95e89e18594ef31e"
title: "Show HN: EtherPK Notes – An Agentic Kanban Board from Your Markdown Tasks [video]"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50431256"
author: "gb2d_hn"
published_at: "2026-11-09T20:12:16Z"
captured_at: "2026-11-10T09:49:42+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - hn_show
  - author_gb2d_hn
  - story_50431256
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: EtherPK Notes – An Agentic Kanban Board from Your Markdown Tasks [video]

> [!info] 一句话导读
> Author: Gareth Brown

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50431256>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：gb2d_hn　|　发布：2026-11-09T20:12:16Z
> 项目链接：—
> 采集：2026-11-10T09:49:42+08:00　|　id：`95e89e18594ef31e`

## 正文

Author: Gareth Brown

EtherPK is at its core a markdown and Wikileakbased editor with rich functionality to help you manage information and projects. EtherPK tasks are plain markdown. But the EtherPK client has built powerful functionality on top of markdown tasks, integrating a cananban board, an MCP server to allow you to manage your work in your notes and easily hand off with instruction and full task context to your AI agent, for example, Claude Code. This demonstration shows you using the tasks you have added to your notes in EtherPK to hand off with context to an AI agent. Using EtherPK, the agent knows how and where to find task context, and you can even link to additional documents in your graph, making your graph an extension of the context available to the agent. The cards on this board are representations of task lines in plain markdown notes. Claude code is running in the terminal, and it's updating the markdown, which modifies the cards as it works. Here we see Claude code connected to a synced EtherPK graph. We show handing Claude code a task from the board and later a whole lane of tasks for autonomous working. A board shows the tasks that belong to one concept. Here the watering app page. It has six lanes, one for each task state, and each lane is split by priority. Drag a card to doing and the board writes the state into the task line. The board keeps no copy of the tasks, so a card moves whenever its line changes, whoever changed it. Select a card to open it in the task editor. The description is whatever is nested under the task, so it can hold links, pictures, and subtasks. This task has three subtasks and it links to the page with the watering schedule which the agent will need. Notes in a synced graph are encrypted before they reach the sync server. So the server has nothing an agent could read. The agent reaches the graph through the EtherPK headless client which runs on this computer and signs in as one of your devices. The steps are on the agents tab in settings. Create an agent setup code. Copy the login command and run it in a terminal. The code works once and expires after 10 minutes. EtherPK then asks you to approve a new device. Check that the code in the browser matches the code in the terminal. Approve it in EPK and press Y in the terminal. The second step tells the agent about this graph. Choose Claude code. Copy the command and run it. Claude Code can then use this graph from any folder. Inside Claude Code, the /mcp command shows the server connected with its tools. To hand over a task, select the copy button on its card. It copies an agent instruction, the graph's name, the task's words, a reference to the task, and which tools to use. Paste it into Claude code and say what you want done. The instruction tells the agent to change the task status only if it's asked to. So this request asks for that. The agent reads the task with read task, moves the card to doing, and reads the schedule page the task links to. The count on the card goes up as each subtask is ticked. Nobody is touching this browser. The changes reach it the same way an edit from another device does. When the tests pass, the card moves to test. The agent's note is in the tasks comments. It's an ordinary bullet under the task in the document, so you can edit it like anything else you wrote. Run the command to check the result, then drag the card to done. To hand over a whole lane, rightclick its header and choose copy agent instruction. The agent lists the lane when it reads the instruction. So tasks you move in after copying are included. This request is a triage against the goal written on the project page. The agent reads the page, sets the priorities, and the cards move into their sections. The headless client never holds the key to a protected document. An agent asking for one gets the same answer as for a name that doesn't exist. Low tool deletes a document, although an edit can empty one, and the agents token can't approve another device or delete a graph. The access tokens page lists it as agent on then the devices name. Revoke it there and that device loses sync access at once. The same steps work with codecs, cursor, and VS code. A local graph is simpler. It's a folder of markdown files. So the MCP server needs no signin. The steps are on the agents tab in settings and in the docs at docs.ek.com.

# EliotAndres/iphone-use-app

## 导航

- 项目页：[[10-项目/Show-HN-EtherPK-Notes-–-An-Agentic-Kanban-Board_95e89e18]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
