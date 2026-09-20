---
type: "corpus"
item_id: "71a256a6eb591e5b"
title: "Show HN: BitBang – Reach machines behind NAT from a browser, no account"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49123789"
project_url: "https://github.com/richlegrand/bitbang-cli"
author: "narragansett"
published_at: "2026-07-31T14:41:13Z"
captured_at: "2026-09-21T03:11:06+08:00"
lang: "en"
kind: "post"
topic: AI 工具/Agent
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_narragansett
  - story_49123789
  - show_hn
metrics: {"points": 97, "comments": 39, "engagement_velocity": 97}
comments_count: 39
comments_total: 39
discovered_via: "hn:show_hn:83d"
---

# Show HN: BitBang – Reach machines behind NAT from a browser, no account

> [!info] 一句话导读
> richlegrand/bitbang-cli

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49123789>
> 指标：点赞=97 · 评论=39 · engagement_velocity=97
> 作者：narragansett　|　发布：2026-07-31T14:41:13Z
> 项目链接：<https://github.com/richlegrand/bitbang-cli>
> 采集：2026-09-21T03:11:06+08:00　|　id：`71a256a6eb591e5b`

## 正文

# richlegrand/bitbang-cli

Proxy server that uses BitBang

- Stars: 5
- Forks: 1
- Watchers: 5
- Open issues: 4
- License: MIT License
- Default branch: main
- Created: 2026-04-23T02:19:30Z

## Languages

- Go
- HTML
- JavaScript
- Python
- Shell

## Top Contributors

- richlegrand (63 contributions)

---

## README

# BitBang CLI

BitBang CLI is a single static binary remote-access multitool: open an interactive shell, browse and transfer files, and access web apps on the remote machine's network from any browser, no port forwarding, no configuring, and no account.

Tests
License

Install bitbang, run bitbang serve, and open the printed URL in a browser to get a shell, a file browser, and a proxy to the machine's network

On the machine you want to reach:

```
curl -sSfL bitba.ng/install | sh
bitbang serve
```

`serve` prints a URL. Open it in any browser and you get a terminal, a file browser, and a proxy to that machine's network -- or connect from another terminal with `bitbang connect ` using the same binary. The connection is end-to-end encrypted and peer-to-peer; the `bitba.ng` server introduces the two ends, then steps aside.

`bitbang` is a single static Go binary. It's part of the BitBang project; this whitepaper covers the design in depth.

## Pairing with a 6-digit code

When you can't paste a URL or scan a QR code, such as when you're on the phone, or within yelling distance, `bitbang serve` also prints a short **pairing code**. The other party opens `bitba.ng/ ` (or runs `bitbang connect `), their screen shows a second 6-digit number, and they read *that* one back to you. You type it in to approve. A machine-in-the-middle can't make the two numbers match, and pairing saves the device connection credentials for next time, e.g. `bitbang connect nas1`. If you know Magic Wormhole, the shape is similar -- a spoken code that securely introduces two machines.

Server prints a 5-minute pairing code; the other party enters it at bitba.ng, their screen shows a 6-digit challenge to read aloud, and typing it back on the serving machine approves the connection

## Why?

- **Nothing to forward or configure.** Works from behind NAT, CGNAT, or a locked-down network -- no router changes, no VPN, no tunnel daemon.
- **Nothing to install on the connecting side.** A browser is enough. A CLI is there when you want scripting, pipes, and file copy.
- **Private by design.** Traffic is WebRTC/DTLS, peer-to-peer. The signaling server never sees it; if a direct path isn't possible, a TURN relay carries ciphertext only.
- **No account, no telemetry.**

### Why not just use SSH?

`bitbang` is shaped like ssh: `serve`, `connect`, and `cp` map to `sshd`, `ssh`, and `scp`, with WebRTC as the transport instead of TCP. For a machine you can already SSH into comfortably, that difference doesn't buy you much. But most of `bitbang` came out of annoyances I seem to hit more often than I should:

**Reach.** Remote SSH access needs an inbound path, and on most networks opening one isn't your call -- CGNAT (cellular, Starlink, many ISPs), corporate, university, municipal. So in practice you bolt on a second system: Tailscale, a VPN, ngrok -- another install, another account, another daemon to keep running. `bitbang serve` needs no open port and works from anywhere.

**Setup.** SSH has to be enabled and configured before it will let you in. It's disabled by default on Raspberry Pi OS, and often key-only, which means getting your public key onto the machine first. And how do you do that? Email or a USB stick are usually the most painless options. `bitbang` sets up the connection with a 6-digit code exchange instead -- something you can do safely over the phone, or call out across the room. It also runs as an ordinary user -- no root, no daemon, no config file.

**Proxying.** If you want a web app on that machine's network, SSH gives you a separate tunnel per app, named in advance. The `bitbang` proxy is generic: specify the web app's URL at connection time.

**Browser client.** SSH needs an SSH client and a key or password on the connecting side. `bitbang` needs a browser -- which means a phone, a borrowed laptop, or someone who has never opened a terminal. Hand them the URL and they get the access that you've granted them.

## Using `bitbang`

Every connection has two ends: a **listener** (`bitbang serve`, running on the machine being reached) and a **connector** (a browser, or the `bitbang` CLI, on the machine doing the reaching). One listener URL serves both kinds of connector.

### The listener: `bitbang serve`

```
bitbang serve                    # everything: shell + files + proxy on one URL
bitbang serve shell              # shell only
bitbang serve files ~/share      # files only (add -upload to allow uploads)
bitbang serve proxy              # proxy; pick the target in the browser
bitbang serve proxy localhost:8080   # ...or pin a single target
```

Each prints a QR code, URL and a pairing code.

### Connecting from a browser

Open the URL. Depending on what's served, you get:

- **Shell** -- a full terminal in the page (colors, resize, copy/paste).
- **Files** -- browse, preview, download, and upload.
- **Proxy** -- type a LAN address (`nas.local`, `192.168.1.10:8080`, `localhost:3000/admin`) and use the app as if you were local. Logins, cookies, uploads, and streaming all work.

### Connecting from the CLI

```
bitbang connect <url>                                   # interactive shell
bitbang connect <url> -- tail -f /var/log/syslog        # one-shot command
bitbang cp <url>:/var/log/app.log ./app.log             # copy files, scp-style
bitbang cp - <url>:/tmp/firmware.bin < firmware.bin     # stdin/stdout work too
```

Every successful connect or pairing is saved to `~/.bitbang/devices.json`, so from then on a short name is enough: `bitbang connect nas1`.

## Install

The one-liner detects your arch (`amd64`, `arm64`, `armv7`), downloads the binary from the latest GitHub release, verifies its SHA-256 against the release's `checksums.txt`, and installs to `~/.local/bin/bitbang`.

Pin a version, change the location, or audit the script first:

```
curl -sSfL bitba.ng/install | sh -s -- --version v0.5.0
curl -sSfL bitba.ng/install | sh -s -- --prefix /usr/local/bin

curl -sSfL bitba.ng/install -o install.sh && less install.sh && sh install.sh
```

macOS and Windows builds are coming -- issues have been created for each (macOS, windows, just react or post to show me you're insterested . **Manual install:** download the binary from Releases and place it on your PATH. **Build from source:** see below.

### How the install URL works

`bitba.ng/install` is a redirect, not a hosted script. The chain:

1. `curl` hits `https://bitba.ng/install`, which 302s to `install.sh` in this repo (on `main`).
2. The script runs in your shell, detects OS+arch, and downloads the binary asset from `https://github.com/richlegrand/bitbang-cli/releases/latest/download/bitbang-linux- `.
3. It fetches `checksums.txt` from the same release and verifies the binary's SHA-256.
4. Installs to `~/.local/bin` (overridable).

The install script lives in this repo, next to the code it installs -- so you can review it alongside the binary, and the canonical bitba.ng host owns only the short URL. Self-hosters can point their own host's `/install` at whatever script they ship: the signaling server's `INSTALL_URL` env var controls the redirect target (empty → 404).

## Security

- **Self-certifying identity.** On first run, `bitbang` generates an RSA keypair under `~/.bitbang/ /`; the device UID is derived from the public key, so impersonating a device means finding a second preimage of its UID.
- **The secret never touches the server.** The access code lives in the URL fragment (`#…`), which browsers never send -- `bitba.ng` brokers the connection without ever seeing the credential that authorizes it.
- **End-to-end encryption.** All traffic rides WebRTC's DTLS. The signaling server sees only the public key, the derived UID, and connection metadata -- never your data. A TURN relay, if one is needed, sees ciphertext only.
- **Verified pairing.** The read-aloud number in code pairing is a short authentication string (SAS), computed independently on both ends from the negotiated DTLS fingerprints and two committed nonces -- a machine-in-the-middle, whose fingerprints necessarily differ, can't make the two numbers match.
- **Optional PIN** (`--pin`) for permanent or headless setups, and **throwaway mode** (`-ephemeral`) for a fresh identity each run.

How the two ends authenticate each other without trusting the signaling server is covered in detail here: *Trustless Signaling: Authentication Without a Central Authority*.

## How it compares

| | ngrok | Cloudflare Tunnel | Tailscale | `bitbang` |
| ------------------------------- | ------------- | ----------------- | ------------------------ | ---------------- |
| Account required | Yes | Yes | Yes | **No** |
| Install on the connecting side | No | No | **Yes** | **No** (browser) |
| End-to-end encrypted | Not by default | No | Yes | **Yes** |
| Data path | Their servers | Their servers | P2P | **P2P** |
| Self-hostable server (open source) | No | No | No (Headscale is third-party) | **Yes** |
| Setup before first use | Account + authtoken | Account + DNS | Account + login on each device | **Run one command** |

## Command reference

Flags accept either form (`-pin` or `--pin`). Boolean flags default off unless noted.

```
bitbang serve [flags]                  All capabilities: shell + files + proxy on one URL
bitbang serve shell [flags]            Shell only
bitbang serve files [PATH] [flags]     Files only (PATH defaults to cwd)
bitbang serve proxy [TARGET] [flags]   HTTP/WebSocket reverse proxy (TARGET pins one host:port)
bitbang connect <target> [-- cmd …]    Client shell (interactive or one-shot)
bitbang cp <src> <dst>                 Copy files (one side is <URL>:/path, or '-')
bitbang version                        Print version (also --version)
bitbang help                           Usage (also --help, -h)
```

### `bitbang serve` -- run a listener

**Shared flags** (all four `serve` forms):

| Flag | Default | Description |
| ------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-server HOST` | `bitba.ng` | Signaling server hostname |
| `-pin PIN` | (none) | Require this PIN for connections |
| `-ephemeral` | off | Temporary identity (a fresh URL each run) |
| `-nocode` | off | Disable code-exchange pairing -- no 6-digit code is issued; the URL still works. Use for headless/non-TTY listeners that can't complete the SAS prompt. |
| `-program NAME` | `bitbang` | Identity name; keypair stored at `~/.bitbang/ /identity.pem` |
| `-target HOST:PORT` | (dynamic) | Fixed proxy target (proxy mode); empty = pick the target in the browser. `serve proxy host:port` is shorthand for this. |
| `-v` | off | Verbose logging (adds the browser `!debug` overlay) |

**Shell flags** (`serve` and `serve shell`):

| Flag | Default | Description |
| ----------------------- | --------------------- | --------------------------------------------- |
| `-shell-cmd CMD` | `$SHELL` or `/bin/sh` | Shell to spawn |
| `-shell-max-sessions N` | `1` | Max concurrent shell sessions (0 = unlimited) |
| `-shell-mirror` | on | Mirror shell output to the listener's console |

**Files flags:**

| Form | Path | Upload flag |
| -------------------------- | ------------------------------- | --------------- |
| `serve` (all capabilities) | `-files PATH` (default cwd) | `-files-upload` |
| `serve files [PATH]` | positional `PATH` (default cwd) | `-upload` |

*(Advanced: `-video-fd N` passes an inherited socketpair FD to an external video helper; for internal/embedding use.)*

### `bitbang connect [-- command …]` -- client shell

` ` may be any of:

- a **saved name** -- e.g. `nas1`; resolved from the known-hosts table (see below)
- a **6-digit pair code** -- e.g. `482731`; runs the pairing flow, then connects
- a **URL** -- `https://bitba.ng/ # `, `bitba.ng/ # `, or bare ` # `

With no `-- command`, opens an interactive shell (a PTY when stdin is a terminal). With `-- command args…`, runs that single command non-interactively and exits with its status (signal exits report 128).

| Flag | Default | Description |
| -------------- | ---------- | ----------------------------------------------------------------------------------------------------------- |
| `-name NAME` | (auto) | Remember this host under NAME (new hosts only; auto-assigns `device ` if omitted) |
| `-relay` | off | Request a TURN relay up front instead of only on fallback (ICE still prefers a direct path if one succeeds) |
| `-pin PIN` | (prompt) | PIN to send if the listener requires one (skips the interactive prompt) |
| `-timeout DUR` | `30s` | Dial timeout (e.g. `45s`, `1m`) |
| `-server HOST` | `bitba.ng` | Signaling server -- **pair-code mode only**; the URL form carries its own host |
| `-v` | off | Verbose logging |

### `bitbang cp ` -- copy files

Exactly one of ` ` / ` ` is remote, written `:/path` (URL in any form accepted by `connect`). `-` means stdin/stdout, so `cp:/f -` streams to stdout and `cp -:/f` uploads from stdin. A trailing `/` or `.` on the local side keeps the remote basename (scp-style).

| Flag | Default | Description |
| -------------- | -------- | ----------------------------------------------- |
| `-relay` | off | Request a TURN relay up front (as in `connect`) |
| `-pin PIN` | (prompt) | PIN to send if required |
| `-timeout DUR` | `30s` | Dial timeout |
| `-v` | off | Verbose logging |

### Device names & the known-hosts table

Every successful connect or pairing is remembered in `~/.bitbang/devices.json` (mode `0600`), so you can reconnect by a short name instead of a URL or code:

```
bitbang connect 482731 -name nas1     # pair once, save it as "nas1"
bitbang connect nas1                  # thereafter, just the name
```

- **`-name NAME`** chooses the name; it applies only to a *new* host. Without it, an auto name (`device1`, `device2`, …) is assigned and printed (`Saved as "device1".`).
- **Naming rules:** a name must start with a letter and contain only letters, digits, `-`, or `_`. That guarantees it can never be mistaken for a 6-digit code or a URL. Lookups and uniqueness are case-insensitive.
- **No renaming via connect:** `bitbang connect nas1 -name nas2` is rejected -- `-name` is for first-time saves only.
- **When it's saved:** a pairing is recorded as soon as the SAS is verified (so a flaky reconnect doesn't lose it); a URL connect is recorded once connected.
- Each entry stores `{name, uid, access_code, server, paired_at}`. Reconnecting a known host (by name or URL) refreshes it in place and keeps the name.

## Building from source

Requires Go 1.25+. Pure Go, statically linked (`CGO_ENABLED=0`) -- trivial cross-compilation, no runtime dependencies.

```
go build ./cmd/bitbang/

# cross-compile:
GOOS=linux   GOARCH=arm64        go build -o bitbang-arm64 ./cmd/bitbang/
GOOS=linux   GOARCH=arm GOARM=7  go build -o bitbang-armv7 ./cmd/bitbang/
GOOS=windows GOARCH=amd64        go build -o bitbang.exe   ./cmd/bitbang/
GOOS=darwin  GOARCH=arm64        go build -o bitbang-macos ./cmd/bitbang/
```
## Diagrams

## Roadmap

Shipping today: **shell, files, and proxy**, reachable from the browser or the CLI, plus scp-style file copy and **ad-hoc pairing** with a saved device table. Designed and on the way:

- **Serial bridging** -- drive a remote `/dev/ttyUSB0` from a local virtual port (e.g. run Arduino IDE over the internet). An issue has been opened here.
- **TCP port forwarding** -- `-L 5432:db.internal:5432` to reach LAN-only services. And issue has been opened here.
- **Remote desktop** -- screen over a WebRTC video track, keyboard/mouse over the data channel.

## License

MIT -- see LICENSE.

## Contributing

Issues and PRs welcome.

# Bhavya6187/tandem

## 评论（39/39）

> **narragansett** · 2026-07-31T14:42:07.000Z　
> It's a single Go binary, shaped like ssh. The main difference is the transport -- WebRTC instead of TCP -- so it doesn't need the machine to be reachable in the first place. Run "bitbang serve" and it prints a URL. Open it in a browser and you get a terminal, a file browser, and a proxy to web apps on that machine's network -- or connect from another terminal. There's nothing to install on the connecting side, no account, no port forwarding.The trick to having no accounts: a device's identity is the hash of its public key, so browser and device verify each other directly. The server keeps no registry, authorizes nothing, and isn't in the data path -- it brokers the introduction and steps aside. About 75% of connections go direct P2P. The rest fall back to a TURN relay that only sees ciphertext. The server is open source and self-hostable -- and since it's out of the data path, cheap to run.BitBang started on an ESP32, as the networking for a tiny telepresence robot. Embedded development is difficult and slow, so this CLI is where I've beaten the security model into shape. The embedded version is next. :)

---

> **Sean-Der** · 2026-07-31T18:22:38.000Z　
> Fantastic work on this. This idea has so much promise, I hope this is the project that makes it take off.Self-hosting is pretty these days with docker. Exposing it to the internet is the annoying part. I do Jellyfin via netbird, but that means I don't really share it with my friends. I hope something like this getting baked into self-hosting flows is killer.My other pet peeve is that people use 'Cloud Services' for File transfer. Sometimes when they are in the same LAN!Nice work again and I hope it catches on/people understand how great this really is :)

---

> **apitman** · 2026-07-31T19:53:24.000Z　
> Would love to have this on https://github.com/anderspitman/awesome-tunneling as soon as it hits 100 stars.

---

> **peter_d_sherman** · 2026-07-31T20:08:43.000Z　
> So I read a whole bunch of text trying to figure out what this thing is...Then I see the following line in the 'How it compares' section:"Self-hostable server (open source)": ngrok->No, Cloudflare Tunnel->No, Tailscale->No, Bitbang->Yes...and I'm like, "It's Open Source Tailscale!"And now I "get it"! (you know, epiphany, profound enlightenment and all that!) :-)(Well, it's an open source alternative to Tailscale, to be more precise, and an excellent one at that!)Great work, Rich LeGrand!(Another step forward for open source!)

---

> **fmarasho** · 2026-07-31T21:10:15.000Z　
> Looks like https://www.iroh.computer, can you explain how this approach is similar/different?

---

> **CrimsonCape** · 2026-07-31T23:32:33.000Z　
> So i can see my use case like this: I ssh from my phone to my home raspberry pi through tailscale. i type an alias that causes the RPi to run bitbang serve and prints the connection number through stdout so i see it on my phone ssh session.Now on an untrusted PC i can bingbang into my home network, do stuff with a real keyboard, and then run another command to shutdown bitbang.Does that sound feasible?

---

> **ValdikSS** · 2026-08-01T00:04:44.000Z　
> Will shamelessly promote my thing: https://ssh-j.comNo applications except regular ssh client. Needs an SSH connection on the client as well though.

---

> **Bnjoroge** · 2026-08-01T02:10:09.000Z　
> how's this different from iroh?

---

> **Arshad-Talpur** · 2026-08-01T10:28:50.000Z　
> I like the idea but product seems to be unfinished or at least still not usable considering the problem it is solving

---

> **eqvinox** · 2026-08-01T12:30:35.000Z　
> IPv6.(Let's skip the discussion, I don't feel like watching groundhog day today.)

---

> **ebb_earl_co** · 2026-08-01T15:17:53.000Z　
> This seems simple and utile! Reading though the white paper on GitHub, there is a malformed Markdown table in the “Why WebRTC?” section [1] that probably just needs one more | somewhere.[1] https://github.com/richlegrand/bitbang/blob/main/whitepaper....

---

> **gtoubassi** · 2026-07-31T17:12:48.000Z　
> Its really clever and minimal approach to getting (for my use case at least) the moral equivalent of a cloudflare tunnel without actually depending on CF. Super cool.

---

> **owaiswiz** · 2026-07-31T18:30:20.000Z　
> In case a direct p2p connection is not possible and it goes through the relay, is that for all traffic (even if encrypted
> )?And who bears the cost for that (or does it have some FUP) (bandwidth cant be free/unlimited?)

---

> **cure_42** · 2026-08-01T04:29:28.000Z　
> I'm thrown off because you use so many em dashes, but the text surrounding them generally seems human.Not judging or brigading, just personally don't want to add a new tool to my toolbelt knowing it's made with ai right now. Is bitbang made with ai?

---

> **gigatexal** · 2026-08-02T17:47:30.000Z　
> Sounds like all I need to do is get this onto a machine and find a way to open the url click exploit or something and I get a RAT

---

> **narragansett** · 2026-07-31T18:46:58.000Z　
> Thank you -- and if you're the Sean who wrote Pion, this is built on your work, so that means a lot. :)The friends case is exactly the gap I kept running into. A mesh VPN is fine for my own devices and hopeless the moment someone else needs in, because now they're installing a client and making an account to look at one thing. Here they get a link.Baking it into self-hosting flows is the right instinct and I'd love help figuring out where it fits. There's already an OctoPrint plugin; Jellyfin seems like the obvious next one.

---

> **narragansett** · 2026-07-31T20:25:42.000Z　
> here's hoping! :)

---

> **narragansett** · 2026-07-31T20:35:21.000Z　
> Remote access lacks a certain amount of sex appeal -- thanks for reading the through the techno-babble and not giving up :)And yes -- open source and self-hostable is a big part it. The other half is that the connecting side can be a browser, so there's no client to install on whatever you happen to be sitting at. Tailscale is a network you join, this is closer to a link you hand someone.Also taking "read a whole bunch of text first" as a hint. That comparison probably belongs higher up the README.

---

> **narragansett** · 2026-08-01T02:03:33.000Z　
> Yes, that should work. "serve" prints the URL and the 6-digit pairing code to stdout, so your ssh session sees them, and shutting it down is just killing the process.One suggestion for the untrusted-PC part: bitbang serve -ephemeral. That uses a throwaway identity that dies with the process, so the URL is dead the moment you kill it -- rather than persisting and still working later from whatever browser history it's sitting in. --pin adds a second factor if you want one.The pairing code is possibly handy too. If you'd rather not type a long URL on an unfamiliar machine, go to bitba.ng, enter the 6-digit code, and confirm the number it shows you back on the Pi.

---

> **TheSkyHasEyes** · 2026-08-01T15:05:38.000Z　
> Hey there, neat offering.I see you posted it before. https://news.ycombinator.com/item?id=26500128If you want this to have more traction engage with those of us who have/had questions. Please consider an example section once connected to ssh-j.comThanks.

---

> **narragansett** · 2026-08-01T13:09:51.000Z　
> Pls see reply above.

---

> **narragansett** · 2026-08-01T12:46:13.000Z　
> You actually bring up a good point. v6 genuinely helps here. It gives every device a routable address, so no nat, but it doesn't open a hole through the firewall, which still defaults to blocking inbound, and it doesn't address authentication. You'd still need something to introduce the peers and verify identity. What v6 changes is that hole punching gets easier and more connections go direct. v6 does kill CGNAT specifically, which is the worst case for hole punching. I would really like to see CGNAT go away, which would happen in a 100% ipv6 world. Weirdly, v6 still isn't close to 100%... v6 good for BitBang and doesn't replace, which I assume was the point you were making.

---

> **narragansett** · 2026-08-01T16:43:55.000Z　
> thanks for the catch :)

---

> **tadasv** · 2026-07-31T17:58:00.000Z　
> It is minimal and somewhat neat. It claims to be P2P, but it still needs to bootstrap the connection via central server. I think that always might be a limitation of P2P.I had a similar idea but for wireguard only, where you would allow people to join a vpn through a "shared" jumpbox. To get started with wg is very simple, the problem is the same you need public IP address to scaffold everything.Out of the two options I probably would prefer going wg route, just because it generalizes better. But this is a pretty cool demo of webrtc.

---

> **narragansett** · 2026-07-31T18:56:56.000Z　
> Yes -- if direct P2P fails, everything rides the TURN relay that gets inserted automatically -- it's DTLS end-to-end so the relay only sees ciphertext, never plaintext or the access code.On cost: I pay for it on bitba.ng and it's capped right now at 10 minutes per connection (mostly to prevent people from connecting and walking away). But you're not stuck with mine -- the signaling server is open source, so you can self-host and point it at your own TURN. The Python library supports "bring your own TURN" by specifying (--turn-url, --turn-user, --turn-credential); adding the same flags to the CLI is a small gap I need to close. There are TURN providers that have reasonably generous free tiers.

---

> **dingensundso** · 2026-08-01T08:23:51.000Z　
> There are several Coauthored by Claude commits. So at least partially LLM generated.

---

> **narragansett** · 2026-08-01T12:19:37.000Z　
> Yes, I started using AI for coding (Claude Code) after much consternation -- it's been really good at boosting my productivity. This is a passion project I tackle in my spare time, I like coding, but I don't like much of the coding. Much of it is drudgery-- AI is great for that. But there is no substitute for code review.

---

> **NWoodsman** · 2026-08-01T07:00:40.000Z　
> I'm so ready for this and jellyfin, just need you to fix the cli args so i can run the server on Cloudflare TURN.

---

> **ValdikSS** · 2026-08-01T16:14:20.000Z　
> It has an example on both the website and in SSH.

---

> **eqvinox** · 2026-08-01T13:59:28.000Z　
> UPnP is the standard way to get CPE firewalls to allow a port.Other than that, discussing IPv6 on HN is… draining at best. It's all been argued a million times at this point. People hate it. People love it. People love to hate it. People hate to love it. I'm done :-)

---

> **narragansett** · 2026-07-31T18:04:41.000Z　
> Right, bootstrapping needs a rendezvous point -- that's true of any P2P system, including the wg version. The difference is what the rendezvous knows and costs. Here it holds no accounts, no registry, and nothing that grants access, so it's a phonebook rather than a keyring, and it's out of the data path so it's cheap to run and you can self-host it.On generalizing: wg wins for "put these machines on one network." WebRTC wins on reach, because the connecting side can be a browser -- a phone, a borrowed laptop, a machine you don't administer -- with nothing installed. A wg jumpbox still needs a client on both ends and a public IP for the box. Different tradeoff rather than a strictly better one.

---

> **spl757** · 2026-07-31T18:26:07.000Z　
> If you are running this stuff on a cheap VPS with limited bandwidth, you will not want all of your traffic being routed as ingress and egress as that could easily eat your monthly bandwidth limit depending on the size of files and frequency.

---

> **nighthawk454** · 2026-07-31T19:20:17.000Z　
> > it still needs to bootstrap the connection via central server. I think that always might be a limitation of P2PI think Iroh has a way of doing it using either DNS or BitTorrent DHT. Not perfect but fairly decentralized

---

> **ranger_danger** · 2026-07-31T20:29:18.000Z　
> > There are TURN providers that have reasonably generous free tiers.Could you provide a list of ones you know? Last I looked I wasn't able to find anything fast or reliable.

---

> **cure_42** · 2026-08-08T05:31:44.000Z　
> Gotcha. Thanks for the reply and I wish you success.

---

> **narragansett** · 2026-08-01T12:05:11.000Z　
> This is a really useful feature and on the top of my todo list
> https://github.com/richlegrand/bitbang-cli/issues/9

---

> **narragansett** · 2026-07-31T19:41:18.000Z　
> Iroh's discovery is genuinely neat, and node-IDs-as-public-keys is similar to bitbang.A browser can't join a DHT though because of no UDP sockets, so the connecting side would need a native client, which is the thing bitbang avoids. And DHT lets you locate the peer, but you still need somewhere to trade SDP and ICE candidates, so the rendezvous stays either way I think.What I can do is keep the broker small enough that self-hosting is realistic, which is where it is now -- no accounts, no registry, nothing that grants access, only a simple broker.

---

> **tyingq** · 2026-07-31T22:00:22.000Z　
> Cloudflare's is $0.05 per GB if your traffic exceeds the 1,000 GB free threshold.

---

> **nighthawk454** · 2026-08-01T00:57:24.000Z　
> Ah good point, no udp. I was looking at webtorrent but it does share the same limitation, unless you’re on the nodejs (non-browser) version.Looking forward to trying bitbang! Seems super neat

## 关联链接

- https://bitba.ng/
- https://bitba.ng/install`,
- https://github.com/richlegrand/bitbang-cli/releases/latest/download/bitbang-linux-

## 导航

- 项目页：[[10-项目/github.com_055c852f]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
