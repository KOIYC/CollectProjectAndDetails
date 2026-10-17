---
type: "corpus"
item_id: "efa7755fe9a5975d"
title: "Show HN: MacVisor Runs VMs with VLANs and Firewall on Apple Silicon"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50119018"
project_url: "https://scaleninja.com/macvisor"
author: "onzr"
published_at: "2026-10-16T14:46:38Z"
captured_at: "2026-10-17T13:35:15+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-17"
pub_day: "2026-10-16"
tags:
  - 语料
  - hn_show
  - author_onzr
  - story_50119018
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: MacVisor Runs VMs with VLANs and Firewall on Apple Silicon

> [!info] 一句话导读
> Run macOS and Linux VMs natively on Apple Silicon, now with Windows 11 (Tech Preview): snapshots, templates, networking, and CLI automation.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50119018>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：onzr　|　发布：2026-10-16T14:46:38Z
> 项目链接：<https://scaleninja.com/macvisor>
> 采集：2026-10-17T13:35:15+08:00　|　id：`efa7755fe9a5975d`

## 正文

MacVisor
Run macOS and Linux VMs natively on Apple Silicon, now with Windows 11 (Tech Preview): snapshots, templates, networking, and CLI automation.
 Now available
Get MacVisor (Beta) →
Home
Products
 Main Products
MacVisor Beta Run macOS and Linux VMs on your Mac, and Windows 11 and AI sandboxes as Tech Previews. A complete virtualization platform. DeltaSnap APFS snapshot manager for Mac. List, label, diff, and restore snapshots on any volume.
 Utilities
DriveSync App Store CLI Sync a folder with Google Drive, one reviewed change at a time. Noject App Store Keep your external drives mounted. DeltaSync Free Compare and sync folders on Mac.
Resources
 Documentation
Guides, references, and quickstarts for each product.
 YouTube
Videos, walkthroughs, and behind-the-build clips.
 Support
Email us, file an issue, or browse the docs.
 About
Who we are, what we have shipped, and the work behind it.
Blog
Contact
Access Purchases
Home Main Products
 MacVisor DeltaSnap
 Utilities
 DriveSync Noject DeltaSync
 Resources
 Documentation YouTube ↗ Support Contact us More
 Blog About
MacVisor Beta
Free 30-day trial
Run macOS, Linux & Windows VMs, natively on Apple Silicon
Native VM management with snapshots, templates, flexible
 storage, advanced networking, guest tools, and CLI automation for Macs.
 Operate as desktop virtualization, hypervisor or headless CI
 automation. Designed for Mac as Infrastructure. Windows 11 on ARM
 and AI sandboxes are Tech Previews.
Run AI agents safely in a disposable Linux or macOS VM ( AI sandboxes, Tech Preview ). Your keys and your code stay on the Mac, and you review every change before it lands.
Developers
 Creators
 Power Users
 Server Macs and Homelabs
Free 30-day trial · macOS 27 · Secured by Polar
Download Beta
 Buy License Price $39 one-time
Launch price until GA, when the price goes up. Same license, every 27.x update.
For teams: MacVisor Business, $99 per Mac per year at launch, priority support →
Running 10 or more Macs? 24x7 support with an SLA →
 Linux & macOS Guest Support · Windows 11 (Tech Preview) · AI Sandboxes (Tech Preview) · Compare Licenses · EULA · Changelog
Watch the 2-min overview
Read the docs
Pricing & Licensing
Mac and macOS are trademarks of Apple Inc. Linux distribution logos are trademarks of their respective owners.
Install with Homebrew
Copy
$ brew tap scaleninja/tap && brew trust --tap scaleninja/tap $ brew install --cask macvisor
AI Sandboxes
Tech Preview
Give AI agents a VM of their own.
Coding agents like Claude Code and Codex do their best work when they can run commands without asking you
 first. On your Mac that is risky: they can reach your files, your keys and your network. MacVisor runs each
 agent in its own VM instead, and you check what it changed before anything touches your project.
An agent on your Mac
 The same agent in a sandbox
Can read your SSH keys, passwords and other projects.
 Sees one copy of one project, and nothing else from your Mac.
Needs your API keys in its environment.
 Never gets a key. MacVisor adds it to each request on the way out.
Can reach the internet, your network and the apps on your Mac.
 Reaches only the sites you allow. Your Mac and your network are off limits.
Changes your files directly.
 You see a diff first, and apply it when you are happy with it.
How it works
 Your keys, your code and your models stay on the Mac
Models Internet Your code
Five steps
 01 · Create mvz sandbox create ~/src/app --agent claude Makes a Linux or macOS VM, copies your project in and installs the agent.
02 · Run mvz sandbox run app-1 -- "fix the failing test" The agent works on its own. Watch it, or open a shell next to it.
03 · Review mvz sandbox diff app-1 See every changed file. Scripts, hooks and CI files are flagged.
04 · Apply mvz sandbox apply app-1 Bring the changes into your project, or onto a new branch.
05 · Clean up mvz sandbox discard app-1 Throw the VM away, or roll back to a checkpoint and try again.
Prefer the app? Click New AI Sandbox... next to + in the sidebar.
 The sandbox's Overview has buttons to run the agent, review its changes and apply them.
Local models
 Use Ollama, LM Studio, oMLX or llama.cpp on your Mac. The model gets the Mac’s GPU and memory, and every sandbox shares it.
 Cloud models
 Use Claude, GPT or OpenRouter models. Your API keys stay in the Mac’s Keychain.
 Five agents, ready to go
 Claude Code, Codex, Goose, Aider and OpenCode are installed and set up for you. Or bring your own.
 A short list for the internet
 npm, PyPI, GitHub and your distribution’s mirrors are allowed. Add or remove sites at any time.
 Undo in seconds
 Checkpoints save the whole VM, memory included. Roll back when an agent goes off track.
 Works with your tools
 An MCP server lets agents on your Mac use sandboxes too, with screenshots and clicks in a macOS one.
New in 27.0.0 beta 5, as a Tech Preview. AI sandboxes are tested in every build,
 but commands and defaults may still change. Models run on your Mac rather than in the VM, where they get the full GPU and memory.
Read the guide
Built-in feature set
More than start and stop.
MacVisor brings desktop VM ergonomics and virtualization-platform
 controls into one native app. These features reflect the current
 beta implementation, not roadmap items.
MacVisor 27 requires macOS 27. Some features additionally depend on supported Apple Silicon hardware.
Guests
 Linux dev VMs from a signed catalogue of cloud images: Ubuntu, Debian, Fedora, Rocky, AlmaLinux, Oracle Linux, CentOS Stream, openSUSE Leap, Alpine
 cloud-init sets up your account and SSH keys and the guest agent, plus, when you ask, a container runtime (containerd, Docker, Podman, k3s) and your home folder at the same path
 Native macOS VMs from a catalogue installer (macOS 27, 26, 15, 14) or your own IPSW
 macOS 27 guests skip Setup Assistant and get the MacVisor Agent installed for you
 ARM64 Linux VMs installed from ISO
 Rosetta 2 sharing for x86_64 Linux applications
 Tech Preview: Windows 11 on ARM from Microsoft's ISO, installed unattended with your account, Remote Desktop, and the MacVisor agent
 AI sandboxes (Tech Preview)
 A Linux or macOS 27 VM for each project and coding agent: Claude Code, Codex, Goose, Aider or OpenCode, set up for you
 Models from your Mac (Ollama, LM Studio, oMLX, llama.cpp) or the cloud (Claude, GPT), with API keys kept in the Keychain, never in the VM
 No direct internet: only the sites you allow
 Review the changes on your Mac, then apply them or make a branch; checkpoints to roll back
 An MCP server, so agents on your Mac can use sandboxes too
 Virtual hardware
 Dynamic displays for macOS and Linux VMs; Remote Desktop through Microsoft's Windows App for Windows VMs
 Accelerated Graphics (shared GPU) for macOS
 Mac keyboard, trackpad, audio, and input capture
 Virtio or NVMe disks, hot-plug USB disks and ISO media
 Nested KVM for supported Linux guests
 USB device passthrough and runtime device capture
 Snapshots
 Instant Disk-only and Live (disk and memory) snapshots
 Safety snapshots before rollback (revert)
 Create VM or export from any snapshot
 Reusable templates, copy-on-write clones, and instant linked clones
 Plain-words recovery when a saved session will not restore: Try Again or Start from Disk
 Advanced Networking
 Default NAT plus named shared-NAT and host-only networks
 Every VM reachable by name as .mvz; host.mvz.internal inside cloud-image Linux guests
 Automatic TCP and UDP port forwarding for cloud-image VMs, plus manual per-VM forwards
 Host 802.1Q VLAN creation and physical or VLAN bridge uplinks
 Per-network DHCP and stable MAC/IP address reservations
 TCP/UDP NAT forwarding and visual network topology
 Individual DHCP, DNS proxy, NAT44, NAT66, and IPv6 RA controls
 Host-enforced per-network IPv4 firewall policy, from the app or the CLI
 Flexible Storage
 ASIF sparse disks throughout, with in-place conversion of legacy raw disks
 Cloud images downloaded once, verified against the vendor checksum, kept as templates; resumable downloads
 Multiple internal or external storage locations
 Cold migration for stopped VMs and templates
 Warm migration for running VMs
 Portable VM import and export workflows
 Storage browser with logical, physical, and private sizes per location
 Integration and operations
 mvz shell and exec: an SSH shell in any VM over the guest agent, as your own account
 A Docker socket and docker context per VM; kubeconfig for k3s VMs
 Drag-and-drop files between macOS host and guests
 Bidirectional files, clipboard, and port forwarding tunnels powered by guest tools
 VirtioFS shared folders for macOS and Linux
 Autostart, metrics, task progress, and runner health
 The mvz CLI, serial console, and headless operation
The MacVisor Architecture
A control plane, not a window that happens to run VMs.
MacVisor separates management, clients, and VM execution. An always-running
 control plane owns orchestration and policy. The native GUI and
 mvz
CLI act as independent clients, while every VM runs in its own isolated process.
 That same architecture works as a desktop app, a persistent local host, or a
 CLI-driven virtualization platform.
MacVisor process model
One host, independent lifecycles
Always Online
01 Separate lifecycles
 Restart the GUI, close a display, or run only the CLI without making those client lifecycles the VM lifecycle.
 02 Crash isolation
 Each VM has a dedicated runtime owner, so one runner failure does not take down every workload or the control plane.
 03 One source of truth
 GUI and CLI issue the same typed requests and receive the same state events from the service.
 04 Service recovery
 After a control-plane restart, MacVisor reconciles live runner records and removes stale processes from its registry.
One architecture, three operating modes
Use it like a desktop app or operate it like a platform.
The same VM can move between interactive and unattended workflows without
 moving to a different runtime or management stack.
Interactive
 Native desktop virtualization
Open a VM in its own Mac window with dynamic display sizing, input capture,
 clipboard, shared folders, file transfer, audio, and USB passthrough.
Best for development, OS testing, and hands-on lab work.
Persistent
 A local virtualization host
Start VMs headlessly, keep them running after windows close, enable login
 autostart, and connect services through named networks and port forwards.
Best for always-on services, clusters, and multi-VM environments.
Programmable
 CLI-driven infrastructure
Create a Linux dev VM from a cloud image in one command, open a shell
 in it, and script lifecycle, snapshots, networks, port forwards,
 autostart, and serial-console access through the bundled
 mvz CLI.
Best for repeatable environments, automation, and local CI workflows.
Platform capabilities
The operational tools around the VM matter.
MacVisor combines native Apple Silicon virtualization with the controls
 needed to build, protect, connect, and operate a local VM fleet.
01
 Lifecycle and saved state
 Start, pause, resume, restart, shut down, power off, suspend to disk, or reopen a hidden display without changing runtime ownership.
 Interactive and headless control
 02
 APFS-native snapshots
 Capture disk-only or live memory-and-disk checkpoints, then safely revert, resume, export, or clone a new VM from a snapshot.
 Copy-on-write storage
 03
 Cloud images, templates and storage
 Make Linux VMs from a signed catalogue of distribution cloud images, each a linked clone of a verified template set up by cloud-init; promote your own VMs into templates, use multiple storage locations, and perform warm or cold migrations.
 Repeatable environments
 04
 Lab networking
 Reach every VM as .mvz. Build named shared-NAT or host-only segments, create 802.1Q VLAN bridges, reserve guest addresses, forward TCP/UDP ports, customise gateway services, and apply an IPv4 firewall.
 Addressed and policy-controlled segments
 05
 Guest integration
 macOS, Linux and Windows guest agents (installed for you on cloud-image, macOS 27 and Windows VMs) carry clipboard sync, bidirectional file transfer, port tunnels, and live guest information over vsock; on macOS and Linux also mvz shell, the per-VM Docker socket, and the snapshot filesystem flush.
 No guest network dependency
 06
 Operations and visibility
 Track VM state, CPU, memory, disk, GPU, and network activity while the service manages autostart, tasks, and runner health.
 Fleet-level awareness
Screenshots
One window for the whole fleet.
Linux VM
 Account, containers, shared folders, guest tools, and live readings on one Overview tab.
 macOS 27 guest
 Installed from Apple's image, signed in, with MacVisor Agent running.
 New VM
 Pick a cloud image or installer; everything else has a default.
 Templates
 Linux Cloud Images, macOS Installers, and your own custom VM templates.
 Storage
 Every bundle with its logical, on-disk, and private size.
 Networks
 Firewall, Port groups, VLANs, and who is attached where.
Further reading
Why we built MacVisor.
Notes from the team behind MacVisor: why a Mac makes a good virtualization host, how the app is
 built around a background service, and what the public beta can do today.
All posts → Documentation → Changelog →
Product Oct 16, 2026
 MacVisor: run your Mac like a virtualization host
 Why we built MacVisor, how it runs macOS, Linux and Windows VMs on Apple Silicon, and what the public beta can do today.
 Rohit Yadav
Read →
Compare macOS Virtualization
Pick the tool that matches the workload.
MacVisor is not a cross-architecture emulator, and its Windows 11 support is a Tech Preview rather than a Windows desktop product with accelerated graphics. See where it fits against desktop hypervisors, native macOS VM apps, and CI-focused runtimes.
View all comparisons
vs. UTM
 Desktop virtualization and emulation
vs. Parallels
 Commercial desktop virtualization
vs. Fusion
 Desktop virtualization
vs. VirtualBuddy
 Native macOS virtualization
vs. Tart
 CLI-first VM automation
vs. Orka Desktop
 Local macOS VM testing
Public beta
Get MacVisor updates.
Join the list for release notes, platform notes, and what's coming next.
Website
Join MacVisor list
By subscribing, you agree to our
 Privacy Policy
and
 Terms .
Enterprise
Running Macs as infrastructure?
MacVisor Enterprise starts at $49 per Mac per month, billed annually for 10 or more Macs, and is
 quoted for your deployment. It includes a yearly license for every Mac, always on the latest MacVisor,
 with 24x7 support and an SLA: help with CI/CD pipelines and unattended build Macs, firewall policy and
 custom networks, and remote and headless access. Smaller team? MacVisor Business is
$99 per Mac per year at launch, locked in for as long as you renew, with priority email support. Every feature is the same in every license.
24x7 priority support with an SLA
 Deployment help with your MDM
 CI/CD and build-farm guidance
 Firewall, VLAN, and network design help
 Purchase orders and invoices
Contact sales
 Compare licenses
Privacy
Your VMs stay on your Mac.
MacVisor has no analytics and no telemetry. On its own it connects for two things only:
 checking your license with ScaleNinja's licensing server, and checking whether a new version exists. Cloud images
 and macOS installers are downloaded when you ask, from the vendor, and verified. Disks,
 snapshots, and your guests' traffic never pass through us.
Legal
 Privacy Policy
Exactly what MacVisor sends, when, and what never leaves your Mac.
Read policy Docs
 Licensing
The free trial, MacVisor 27 Pro, Business, and Enterprise compared. How activation and the weekly check work.
Compare licenses Legal
 EULA
The end user license agreement you accept when you first run MacVisor.
Read agreement
Build VM labs that survive experiments.
Snapshot the full machine, integrate with guests through the MacVisor Agent,
 and build labs with VLAN bridges, named shared or host-only networks, address reservations, and host-enforced firewall policy.
Download MacVisor
 Beta
Buy License
Read the docs
Contact sales
Website
By subscribing, you agree to our
 Privacy Policy
and
 Terms .
Company
 About
 Media kit
 Contact us
Products
MacVisor
 Beta
DeltaSnap
DriveSync
Noject
DeltaSync
Consulting
 CloudStack
 Public Health
Resources
 Blog
 Documentation
 Support
Legal
 Terms
 Privacy Policy
 Security
Compare
MacVisor
 MacVisor vs UTM
 MacVisor vs Parallels Desktop
 MacVisor vs VMware Fusion
 MacVisor vs VirtualBuddy
 MacVisor vs Tart
 MacVisor vs MacStadium Orka Desktop
DeltaSnap
 DeltaSnap vs Carbon Copy Cloner
 DeltaSnap vs Keeply
 DeltaSnap vs TechTool Pro
 DeltaSnap vs Snappy
 DeltaSnap vs BackupLoupe
 DeltaSnap vs Time Machine
DriveSync
 DriveSync vs rclone
 DriveSync vs Insync
 DriveSync vs GoogleDriveSync
 DriveSync vs RaiDrive
Noject
 Noject vs Mountain
 Noject vs Ejectify
 Noject vs Jettison
 Noject vs AutoMounter
© 2014-2026 ScaleNinja Software LLP. All rights reserved.
Brewed in Gurugram & Mumbai 3.0
Mac and macOS are trademarks of Apple Inc.

## 导航

- 项目页：[[10-项目/scaleninja.com_eea7d6df]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
