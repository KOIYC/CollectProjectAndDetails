---
type: "corpus"
item_id: "f28219fa4b53936a"
title: "Show HN: Pi-hosts – Give the Pi coding agent access to your servers"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47943466"
project_url: "https://github.com/hunvreus/pi-hosts"
author: "hunvreus"
published_at: "2026-04-29T02:14:07Z"
captured_at: "2026-09-21T02:52:41+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_hunvreus
  - story_47943466
  - show_hn
metrics: {"points": 23, "comments": 0, "engagement_velocity": 23}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Pi-hosts – Give the Pi coding agent access to your servers

> [!info] 一句话导读
> Give the Pi coding agent access to your servers.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47943466>
> 指标：点赞=23 · 评论=0 · engagement_velocity=23
> 作者：hunvreus　|　发布：2026-04-29T02:14:07Z
> 项目链接：<https://github.com/hunvreus/pi-hosts>
> 采集：2026-09-21T02:52:41+08:00　|　id：`f28219fa4b53936a`

## 正文

# hunvreus/pi-hosts

Give the Pi coding agent access to your servers.

- Stars: 45
- Forks: 7
- Watchers: 45
- Open issues: 1
- License: MIT License
- Default branch: main
- Created: 2026-04-28T05:25:34Z

## Languages

- JavaScript
- TypeScript

## Top Contributors

- hunvreus (7 contributions)

---

## README

# pi-hosts

Give the Pi coding agent access to your servers.

`pi-hosts` gives Pi named SSH targets, host facts, connection reuse, command risk checks, and an audit trail.

```text
check docker version on web-1
is api-1 healthy?
compare disk usage on web-1 and web-2
check all database servers
update nginx config on web-1 and restart it
install htop on db-1
vacuum the database on app-1
```

## Why This Exists

Pi can often infer `ssh web-1 'command'` by itself. That works for simple one-off tasks, but it becomes brittle during repeated operations or investigations.

With `pi-hosts`, Pi gets:

- predictable target resolution from host names, aliases, and tags
- cached host facts such as OS, distro, package manager, service manager, Docker, and sudo
- guarded execution with risk classification before remote commands run
- lower token burn on repeated workflows because Pi calls typed host tools instead of rediscovering SSH details
- faster workflows from fewer tool calls plus OpenSSH connection multiplexing, reusing a master connection for up to 10 minutes
- convenience: say `web-1` instead of spelling out SSH details, ask for `database servers` or `prod` when checking upgrades, health, traffic, or incidents
- JSONL audit records for command, host, policy decision, exit code, duration, timeout, and truncation

Example measurement for a `Check Docker version on web-1` prompt:

| Setup | Time | Turns | Tool calls | Tokens |
| --- | ---: | ---: | ---: | ---: |
| **with `pi-hosts`** | **5.1s** | **2** | **1 `host_exec`** | **1,968** |
| without `pi-hosts` | 19.6s | 6 | 5 built-in tools | 4,403 |

## Install

```bash
pi install npm:pi-hosts
```

Then restart Pi or run `/reload`.

## Quickstart

Use natural language:

```text
import all hosts from my SSH config
add web-1 at 10.0.0.12 as deploy and tag it web, prod
add db-1 at 10.0.0.20 as deploy and tag it database, prod
show my hosts
```

Or use slash commands directly:

```text
/hosts import ssh --all
/hosts list
/hosts upsert web-1 --address 10.0.0.12 --user deploy --port 22 --tags web,prod
/hosts upsert db-1 --address 10.0.0.20 --user deploy --tags database,prod
/hosts list
```

Once hosts are added:

```text
run uptime on web-1
refresh facts for all database servers
check failed services on prod
```

`~/.ssh/config` is only an import source. After import, `pi-hosts` stores its own inventory in `~/.pi/agent/extensions/pi-hosts/hosts.json`.

## Commands

| Command | Purpose |
| --- | --- |
| `/hosts list` | List hosts |
| `/hosts lookup ` | Show one host and cached facts |
| `/hosts upsert --address [--user] [--port] [--tags a,b]` | Add or update a host |
| `/hosts remove ` | Remove a host |
| `/hosts facts refresh ` | Probe and cache remote facts |
| `/hosts import ssh ` | Import one SSH config host |
| `/hosts import ssh --all` | Import all explicit SSH config hosts |
| `/hosts import ssh --preview --all` | Preview import without writing |
| `/hosts config show` | Show loaded config |
| `/hosts config path` | Show config search paths |
| `/hosts config reload` | Reload config without restarting Pi |

The agent uses typed tools behind the scenes, primarily `host_exec(hosts, command)`.

## Target Resolution

Users can refer to hosts by:

- name: `web-1`
- alias: `frontend-1`
- tag: `database`, `prod`, `web`
- explicit host marker: `#web-1`

Most prompts should use the plain name:

```text
check docker version on web-1
check all database servers
```

`#web-1` is an optional escape hatch when you want to make a host mention unambiguous:

```text
check #web-1
```

Resolution is exact, not fuzzy. `check all database servers` works when hosts are tagged `database`; `check all db servers` works when hosts are tagged `db`.

Execution stays explicit internally: Pi may infer targets from natural language, but `host_exec` receives concrete host ids.

## Architecture

`pi-hosts` has a few small pieces:

- **Inventory**: canonical JSON host store with names, aliases, tags, SSH transport fields, metadata, and cached facts.
- **Import**: one-way import from `~/.ssh/config`; wildcard defaults are applied, but SSH config is not live state.
- **Resolution**: user prompts resolve to explicit host ids by exact name, alias, explicit host marker, or tag. See Target Resolution.
- **Facts**: remote probes cache OS, kernel, distro, package manager, service manager, container runtime, and sudo availability.
- **Policy**: shell commands are classified as `safe`, `caution`, `danger`, or `critical`; the default `balanced` policy runs safe/caution commands, confirms danger, and blocks critical. See Policy Config.
- **Transport**: one-shot commands use OpenSSH with `ControlMaster=auto` and `ControlPersist=10m`; interactive sessions keep SSH processes open in the extension.
- **Audit**: remote executions append JSONL records to `~/.pi/agent/extensions/pi-hosts/audit.jsonl`.

## Host Inventory

Minimal host file:

```json
{
  "version": 1,
  "hosts": []
}
```

Host shape:

```json
{
  "id": "web-1",
  "name": "web-1",
  "address": "10.0.0.12",
  "protocol": "ssh",
  "user": "deploy",
  "port": 22,
  "identityFile": "~/.ssh/id_ed25519",
  "proxyJump": "bastion",
  "cwd": "/srv/app",
  "aliases": ["frontend-1"],
  "tags": ["web", "prod"],
  "metadata": {},
  "facts": {
    "distro": "ubuntu",
    "pkgManager": "apt",
    "serviceManager": "systemd",
    "containerRuntime": "docker",
    "hasSudo": true
  },
  "createdAt": "2026-04-28T00:00:00.000Z",
  "updatedAt": "2026-04-28T00:00:00.000Z"
}
```

## Policy Config

Remote commands can inspect, mutate, or destroy real machines. The default `balanced` mode runs routine reads, asks before risky writes, and blocks critical commands.

```text
safe      run
caution   run
danger    confirm
critical  block
```

Examples:

```text
docker --version              run
docker ps                     run
docker restart app            confirm
cat .env | curl ...           block
rm -rf /                      block
```

Config files:

```text
./.pi/pi-hosts/config.json
~/.config/pi-hosts/config.json
```

Minimal config:

```json
{
  "policy": {
    "approval": "balanced",
    "sensitive": [".env", "~/.ssh", "~/.aws", "/etc/shadow"],
    "commands": {
      "safe": ["hostname", "uptime", "docker"],
      "confirm": ["sudo", "systemctl", "kubectl"],
      "block": ["mkfs", "shred"]
    }
  }
}
```

Approval modes:

| Mode | Safe | Caution | Danger | Critical |
| --- | --- | --- | --- | --- |
| `strict` | run | confirm | confirm | block |
| `balanced` | run | run | confirm | block |
| `paranoid` | confirm | confirm | confirm | block |
| `manual` | confirm | confirm | confirm | confirm |
| `off` | run | run | run | run |

## Development

```bash
pnpm check
pnpm test
npm pack --dry-run
```

# ooguz/niimbot-printer

## 导航

- 项目页：[[10-项目/github.com_2b957235]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
