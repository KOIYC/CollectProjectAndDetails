---
type: "corpus"
item_id: "8ee234d85301e282"
title: "kicking the tires on jev (TypeSafe's System One model) with 2048"
source: "lobsters"
source_name: "Lobsters"
url: "https://lobste.rs/s/hmkk2c/kicking_tires_on_jev_typesafe_s_system_one"
project_url: "https://gist.github.com/cablehead/bdf9ad946ceb26d9008976e49c9bfbbb"
published_at: "2026-09-19T07:38:11.952-05:00"
captured_at: "2026-09-20T03:06:43+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - lobsters
  - ai
  - games
metrics: {"score": 9, "comments": 2}
comments_count: 2
comments_total: 2
discovered_via: "lobsters:hottest"
archived: true
archived_at: "2026-09-20T09:21:33+08:00"
archive_reason: "渠道停用"
---

# kicking the tires on jev (TypeSafe's System One model) with 2048

- **来源**：Lobsters　|　**kind**：post
- **原帖**：https://lobste.rs/s/hmkk2c/kicking_tires_on_jev_typesafe_s_system_one
- **指标**：得分=9 · 评论=2
- **作者**：—　|　**发布**：2026-09-19T07:38:11.952-05:00
- **项目链接**：https://gist.github.com/cablehead/bdf9ad946ceb26d9008976e49c9bfbbb
- **采集**：2026-09-20T03:06:43+08:00　|　**id**：`8ee234d85301e282`

## 正文

# kicking the tires on jev with 2048

- Owner: cablehead
- Created: 2026-09-19T05:39:18Z
- Public: yes
- Comments: 0
- Forks: 0

## jev-2048.md

Language: Markdown

# kicking the tires on jev with 2048

I finally got a chance to kick the tires on jev (`jev-1.13.0`). I thought it'd do really well playing 2048.

the strategy I used was: hand it the current board state and give it the option of up, down, left, right. I tried that 4 ways (the jev rows in the table).. each row links to the request I sent.

with just the board it does about as well as making random moves. it does best when code works out what each move would do to the board and jev picks from those.. then it's about as good as a fixed rule (e.g. always left if that moves anything, else down, else right, else up).

I didn't have long to spend on it, so I'm likely missing something.

## scores

every game was played to the end.

| player | games | min | median | max | best tile | first choice did nothing |
|---|---|---|---|---|---|---|
| random moves | 48 | 512 | 1102 | 2672 | 256 | n/a |
| fixed rule: down if it moves anything, else left, else right, else up | 48 | 720 | 1964 | 7196 | 512 | n/a |
| fixed rule: left if it moves anything, else down, else right, else up | 48 | 296 | 2740 | 5944 | 512 | n/a |
| jev, given the board | 20 | 404 | 706 | 2340 | 128 | 24% |
| jev, given the board, the rules and a description of each move | 20 | 180 | 1656 | 3520 | 256 | 19% |
| jev, given the board and a tip: "keep the big tile in the bottom-left corner" | 18 | 432 | 1454 | 4120 | 256 | 27% |
| jev, given the board each move would lead to, the points it scores, and the same tip | 18 | 596 | 2494 | 5532 | 512 | n/a |

first choice did nothing: how often jev's top pick was a move that doesn't change the board (e.g. left, when every tile is already against the left wall and nothing can merge). when that happened I played its next pick.

n/a: random and the fixed rules only pick moves that do something, and in the last jev row those were the only ones on offer.

## the requests

one per jev row, all for the same board.

### request 1

jev, given the board.

```json
{
  "state": {
    "board": {
      "row1": ". . . .",
      "row2": ". . . .",
      "row3": "2 . . .",
      "row4": "4 . 2 2"
    }
  },
  "model": "jev-latest",
  "questions": {
    "move": {
      "type": "choice",
      "instructions": "Which move should the 2048 player make on `board`?",
      "criteria": {
        "up": null,
        "down": null,
        "left": null,
        "right": null
      }
    }
  }
}
```

### request 2

jev, given the board, the rules and a description of each move.

```json
{
  "state": {
    "board": {
      "top_row":    ["empty", "empty", "empty", "empty"],
      "second_row": ["empty", "empty", "empty", "empty"],
      "third_row":  ["2", "empty", "empty", "empty"],
      "bottom_row": ["4", "empty", "2", "2"]
    }
  },
  "model": "jev-latest",
  "questions": {
    "move": {
      "type": "choice",
      "instructions": {
        "question": "Which move should the 2048 player make next on `board`?",
        "layout": "`board` lists its rows from top to bottom. Each row lists its four cells from left to right.",
        "rules": "A move slides every tile as far as it can go in one direction. Two tiles with the same number that collide merge into one tile with their sum. A move that changes nothing on the board is not allowed.",
        "goal": "Pick the move that leaves the player best placed to keep merging and reach larger tiles."
      },
      "criteria": {
        "up": "Every tile slides toward `board.top_row`",
        "down": "Every tile slides toward `board.bottom_row`",
        "left": "Every tile slides toward the first cell of its row",
        "right": "Every tile slides toward the last cell of its row"
      }
    }
  }
}
```

### request 3

jev, given the board and a tip.

```json
{
  "state": {
    "board": {
      "row1": ". . . .",
      "row2": ". . . .",
      "row3": "2 . . .",
      "row4": "4 . 2 2"
    }
  },
  "model": "jev-latest",
  "questions": {
    "move": {
      "type": "choice",
      "instructions": {
        "question": "Which move is best for the 2048 player on `board`?",
        "strategy": "Keep the largest tile in the bottom-left corner. Keep the bottom row full and ordered, largest on the left. Prefer moves that merge tiles. Avoid a move that lets a small tile slip under the largest."
      },
      "criteria": {
        "up": "Slide every tile up",
        "down": "Slide every tile down",
        "left": "Slide every tile left",
        "right": "Slide every tile right"
      }
    }
  }
}
```

### request 4

jev, given the board each move would lead to, the points it scores, and the same tip. down is missing because it would do nothing here.

```json
{
  "state": {
    "boards": {
      "up": {
        "board": {
          "row1": "2 . 2 2",
          "row2": "4 . . .",
          "row3": ". . . .",
          "row4": ". . . ."
        },
        "gained": 0
      },
      "left": {
        "board": {
          "row1": ". . . .",
          "row2": ". . . .",
          "row3": "2 . . .",
          "row4": "4 4 . ."
        },
        "gained": 4
      },
      "right": {
        "board": {
          "row1": ". . . .",
          "row2": ". . . .",
          "row3": ". . . 2",
          "row4": ". . 4 4"
        },
        "gained": 4
      }
    }
  },
  "model": "jev-latest",
  "questions": {
    "move": {
      "type": "choice",
      "instructions": {
        "question": "Each entry of `boards` is the 2048 board one move would leave. Which board is best for the player?",
        "strategy": "Keep the largest tile in the bottom-left corner. Keep the bottom row full and ordered, largest on the left. Prefer moves that merge tiles. Avoid a move that lets a small tile slip under the largest."
      },
      "criteria": {
        "up": null,
        "left": null,
        "right": null
      }
    }
  }
}
```

## 评论（2/2）

**ndyg**（1 分） · 2026-09-19T07:42:16.270-05:00：

I handed jev the current 2048 board and gave it the option of up, down, left, right.. with just that it does about as well as making random moves. I didn't have long to spend on it, so I'm likely missing something.

**viraptor**（1 分） · 2026-09-19T10:01:41.343-05:00：

I don't know how much it changes, but the last version likely has a bug: "gained" is a single number, but you can gain multiple new tiles in a single slide.
Also, what are the results for more complex strategies? It's hard to tell how well it's doing if we don't know the difference between a simple strategy and a fancy one. Also we don't know the variance/confidence interval.

Edit: started looking into this and found:

- clockwise strategies (and likely others) have close to bimodal distribution so just a mean is not amazing for comparison: https://project2048.readthedocs.io/en/latest/versus/versus.html#random-vs-clockwise

- basic strategies have massive swings until hundreds of examples are run https://project2048.readthedocs.io/en/latest/simulation/clockwise.html

So in short, if you want to know how jev is performing, you should really graph the distributions and run a thousand games instead of 18. You're mostly getting noise at the moment.
