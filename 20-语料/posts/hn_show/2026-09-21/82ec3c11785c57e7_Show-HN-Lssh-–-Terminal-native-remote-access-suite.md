---
type: "corpus"
item_id: "82ec3c11785c57e7"
title: "Show HN: Lssh – Terminal-native remote access suite for SSH and cloud targets"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47957567"
project_url: "https://github.com/blacknon/lssh"
author: "blacknon"
published_at: "2026-04-30T03:04:04Z"
captured_at: "2026-09-21T02:52:30+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-04-30"
tags:
  - 语料
  - hn_show
  - author_blacknon
  - story_47957567
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: Lssh – Terminal-native remote access suite for SSH and cloud targets

> [!info] 一句话导读
> A terminal-native remote access suite for SSH, cloud inventories, provider-backed connectors, parallel commands, mux workspaces, file transfer, and monitoring.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47957567>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：blacknon　|　发布：2026-04-30T03:04:04Z
> 项目链接：<https://github.com/blacknon/lssh>
> 采集：2026-09-21T02:52:30+08:00　|　id：`82ec3c11785c57e7`

## 正文

# blacknon/lssh

A terminal-native remote access suite for SSH, cloud inventories, provider-backed connectors, parallel commands, mux workspaces, file transfer, and monitoring.

- Stars: 319
- Forks: 33
- Watchers: 319
- Open issues: 18
- License: MIT License
- Default branch: master
- Created: 2017-01-02T15:52:47Z

## Languages

- Dockerfile
- Go
- Makefile
- Shell

## Topics

- aws-ssm
- cloud
- devops
- golang
- mux
- port-forwarding
- remote-access
- scp
- sftp
- ssh
- sysadmin
- telnet
- terminal
- tui
- winrm

## Top Contributors

- blacknon (693 contributions)
- NaofumiUesugi (103 contributions)
- jiro4989 (19 contributions)
- dependabot[bot] (2 contributions)
- kuckjwi0928 (2 contributions)

---

## README

Go Report Card
Version
Go
Platforms
License

lssh
====

 ls + ssh = lssh

`lssh` is a terminal-native remote access suite for SSH workflows, cloud inventories, and provider-backed connectors.

It lets you select hosts from OpenSSH config, `lssh` config, or provider inventories, then operate them through native SSH or connector backends such as AWS SSM, EC2 Instance Connect Endpoint, WinRM, Telnet, and custom providers.

Use it for interactive shells, parallel commands, mux workspaces, file transfer, sync, mount, and monitoring. Connector-backed hosts expose only the operations their connector supports.

- works with your existing SSH config
- interactive host selection
- parallel command execution

## Install

### Homebrew

```bash
brew install blacknon/lssh/lssh
```

### Go

```bash
go install github.com/blacknon/lssh/cmd/lssh@latest
```

Provider-backed inventory and connector features use separate provider executables.
If you install only `cmd/lssh`, those provider binaries are not installed automatically.

For local development, install the bundled providers with:

```bash
mise run provider_install
```

For release builds, either install the all-in-one `lssh-complete_*` archive or add the matching `lssh-providers_*` archive from GitHub Releases.

For more installation details, including other options and platform-specific notes, see docs/install.md.

## Quick start

Already using `~/.ssh/config`?

Just run:

```bash
lssh
```

Want to generate an `lssh` config from your existing SSH config?

```bash
lssh --generate-lssh-conf > ~/.lssh.toml
```

## Basic workflow

lssh is built for a simple workflow:

1. list hosts from SSH config
2. pick one or more hosts
3. open a shell or run a command

## Examples

 Interactive host picker
 lssh
 Select one or more hosts from the TUI.

 Parallel command execution
 lssh -p tail -f /var/log/syslog
 Pick hosts and run the same command across them.

 Mux workflow
 lssh -P
 Open the multi-pane terminal workflow.

 Mux workflow with command
 lssh -P 'htop'
 Start the mux UI and launch a command immediately.

You can still target a single host directly when you already know where to connect:

```bash
lssh -H my-server
```

For more details about config formats and settings, see cmd/lssh/README.md.

## Demo

Want to try `lssh` quickly with a ready-to-run local playground?
Start with `demo/README.md`.
For the telnet connector + multi-hop provider flow, use `demo-telnet-provider/README.md`.

## OpenSSH config and lssh config

`lssh` supports both your existing OpenSSH config and its own config format.

If you want to get started quickly, you can keep using `~/.ssh/config` as-is. If you want richer host metadata and workflow-oriented settings, you can move to an `lssh` config instead.

You can also generate an `lssh` config from your existing SSH config:

```bash
lssh --generate-lssh-conf > ~/.lssh.toml
```

Even after moving to `lssh` config, you can still point it at your existing OpenSSH config and load hosts from there:

```toml
[sshconfig.default]
path = "~/.ssh/config"
```

For more details about config formats and settings, see docs/configuration.md.

## Providers

`lssh` can work with more than static SSH config entries.
Providers let it pull hosts from external inventory sources, resolve secrets just before connect, and use non-SSH connection backends such as cloud-managed connectors.

In `v0.10.0`, provider-backed inventory and secret workflows are best treated as `beta`.
Connector-backed access beyond native SSH is still `experimental`, especially for cloud-managed runtimes and non-SSH backends.

If you want to try provider-oriented flows locally, start from these demos:

- demo/README.md: core SSH, proxy chains, and general multi-host workflow examples
- demo-telnet-provider/README.md: provider-managed telnet connector flow, including direct telnet access and telnet behind a double SSH hop

For the provider architecture and protocol overview, start with provider/README.md.
Category details are also documented under inventory, connector, secret, and mixed.

### Bundled providers

These provider implementations are currently bundled in this repository.

#### Inventory

 provider-inventory-proxmox
 Build host entries from Proxmox inventory.

#### Connector

 provider-connector-openssh
 Use OpenSSH-compatible connection handling as a provider-backed connector.

 provider-connector-telnet
 Reach telnet targets through the connector interface.

 provider-connector-winrm
 Run command execution workflows against WinRM targets. Interactive shell support is not available in v0.10.0.

#### Mixed

 provider-mixed-aws-ec2
 Combine EC2 inventory with AWS SSM and EC2 Instance Connect Endpoint connectors. Native SSH-adjacent flows are usable, while connector-specific behavior remains experimental.

 provider-mixed-azure-compute
 Build Azure Compute inventory with connector-aware access settings.

 provider-mixed-gcp-compute
 Build Google Compute Engine inventory with connector-aware access settings.

#### Secret

 provider-secret-bitwarden
 Resolve secret references from Bitwarden.

 provider-secret-onepassword
 Resolve secret references from 1Password.

 provider-secret-custom-script
 Resolve secret references through custom local scripts.

 provider-secret-os-keychain
 Resolve secret references from the local OS keychain.

## Tools in the lssh suite

The `lssh` project includes multiple tools for SSH-centered workflows.

 lssh
 core / stable
 Interactive SSH access, parallel commands, and forwarding modes.

 lscp
 transfer / stable
 SCP-style copy over SSH/SFTP, including remote-to-remote transfers.

 lsftp
 transfer / stable
 Interactive SFTP shell for browsing and transferring files.

 lsshell
 sysadmin / beta
 Parallel interactive shell with broadcast and targeted commands.

 lsmux
 sysadmin / beta
 Pane-based SSH workspace for multi-host terminal workflows.

 lsmon
 monitor / beta
 Multi-host monitoring UI over SSH without extra remote agents.

 lssync
 transfer / beta
 Tree sync over SSH/SFTP with daemon and bidirectional modes.

 lsdiff
 sysadmin / beta
 Compare remote files from multiple hosts in a synchronized TUI.

 lspipe
 sysadmin / alpha
 Persistent host sessions reusable from local pipelines and automation.

 lsshfs
 transfer / beta
 Mount a remote directory through `FUSE on Linux` or `NFS on macOS`.

## Docs

- docs/README.md: documentation index
- cmd/lssh/README.md: `lssh` command details, forwarding, and local rc usage
- cmd/README.md: command overview
- CONTRIBUTING.md: development and contribution guidelines

## Related projects

- go-sshlib: Go library for SSH connections, command execution, and interactive shells
- tvxterm: tvxterm provides terminal widgets for tview
- boco: Bash Shell Function's Fuzzy Finder.

## Alternatives

If you are evaluating `lssh`, these projects are also worth a look.
They overlap with parts of the suite, but each usually covers a narrower slice of the overall workflow.

| Project | Closest `lssh` command(s) | Main focus | How it differs from `lssh` |
| --- | --- | --- | --- |
| `sshs` | `lssh` | TUI-based SSH host picker | Similar in spirit to a focused host picker, but `lssh` also covers parallel execution, forwarding, mux workflows, and provider/connector-backed targets. |
| `ClusterSSH (cssh)` | `lssh -P`, `lsmux`, `lsshell` | Multi-host interactive administration | Strong for broadcast typing into multiple terminals; `lsshell` and `lsmux` are a closer fit when you want synchronized shell workflows inside one suite. |
| `pssh` | `lssh -p`, `lscp`, `lssync` | Parallel command execution and transfer tools | A good fit for parallel CLI jobs, while `lssh` adds TUI host selection, interactive workflows, and a more integrated multi-command toolset. |
| `tmuxinator` | `lssh -P`, `lsmux` | tmux session layout management | Great for predefined tmux workspaces, but it is not an SSH host picker or transfer tool by itself. `lsmux` is SSH-oriented from the start. |

### How the `lssh` suite is different

- `lssh` combines host selection, interactive SSH, parallel command execution, forwarding, and connector/provider-backed targets.
- `lsshell` focuses on parallel interactive shell workflows instead of just launching many terminals.
- `lscp`, `lsftp`, and `lssync` cover file transfer and synchronization as first-class commands in the same suite.
- `lsmux` provides a pane-based SSH workspace rather than only session templating.
- `lspipe` keeps selected hosts reusable from local pipelines and automation.

## License

MIT

## Author

blacknon

# TalentProof/workproof-schema

## 评论（2/2）

> **blacknon** · 2026-04-30T03:04:26.000Z　
> Hello, HN.I developed “lssh,” a terminal-native remote access suite designed for users who manage multiple SSH targets.It started about 10 years ago as an interactive SSH host selection tool, but now includes parallel command execution, mux-style SSH workspaces, file transfer/synchronization tools, provider-integrated inventory, and connectors for AWS SSM, EICE, WinRM, Telnet, Proxmox, GCP, Azure, and more.One of the features I personally wanted was the ability to use my local shell environment (including vim and tmux) on a remote host without having to copy dot files or helper scripts.Since I recently added native mux workspace support, and also add terminal to agentless monitering tool I thought it had turned into something interesting, so I decided to post it for this place.

---

> **immanuwell** · 2026-04-30T04:23:57.000Z　
> would love to know how it holds up against Boundary or just plain old ssh config + mosh for the day-to-day grind

## 导航

- 项目页：[[10-项目/github.com_4c442ff7]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
