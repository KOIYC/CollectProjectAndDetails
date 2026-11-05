---
type: "corpus"
item_id: "73d1cbae38ef1b0f"
title: "Show HN: Cassandra – free tool to check if you got affected by the Cursor hack"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50369457"
project_url: "https://ciphero.ai/cassandra/hn"
author: "skd-fs"
published_at: "2026-11-04T18:19:46Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_skd-fs
  - story_50369457
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Cassandra – free tool to check if you got affected by the Cursor hack

> [!info] 一句话导读
> Check your machine for the Claude Code backdoor.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50369457>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：skd-fs　|　发布：2026-11-04T18:19:46Z
> 项目链接：<https://ciphero.ai/cassandra/hn>
> 采集：2026-11-05T11:21:45+08:00　|　id：`73d1cbae38ef1b0f`

## 正文

Cassandra
by
How it works
 Advisories
Check your machine for the Claude Code backdoor.
One command. Read-only, no sudo, nothing sent. Yes, it is a script that looks for a script,
 so the whole thing is on this page . Read it, then run it.
macOS / Linux
curl -fsSL https://ciphero.ai/cassandra.sh | bash Copy
Windows, in PowerShell
irm https://ciphero.ai/cassandra.ps1 | iex Copy
Prefer not to pipe? curl -fsSL -o cassandra.sh https://ciphero.ai/cassandra.sh && less cassandra.sh && bash cassandra.sh
What it does
Looks for the indicators in Cursor's notice for the Claude Code 2.1.312 and 2.1.313 backdoor: the svc-telemetry SSH key and the two key fingerprints, the com.apple.sysmond LaunchAgent, the tunnel files in ~/.config , the cron line, the SysMon task and sysmon.cmd , the attacker IP. In the places the notice names, and in the places the same thing could sit under another name: shell start-up files, other LaunchAgents, units and tasks, the Run key, the process list, open connections, the code of your other extensions. 19 checks in all (13 apply on macOS, 11 on Linux, 12 on Windows). Cursor's own one-liner covers the first.
Hashes extension.js inside any installed Claude Code 2.1.312 and 2.1.313 and greps it for the attacker strings, which tells a genuine copy from the backdoored one. Greps the editor's install log and removed-extensions list for either version, for the common case: the bad build was installed on Oct 29 and an update has since replaced it.
Prints found or clear per check and ends with one of these:
■ NO TRACES None of the 13 published indicators were found on this machine.
■ BAD VERSION WAS INSTALLED In the editor's install history: cursor:anthropic.claude-code-2.1.313.
 → Treat the machine as exposed: rotate the keys and tokens it used, from another machine.
■ TRACES FOUND 2 of 13 published indicators were found on this machine.
 → Treat it as compromised. Steps, per incident: /advisories
Why more than Cursor's grep
Cursor's check is one grep: svc-telemetry in authorized_keys , and "machine not impacted" when it is absent. That settles whether the key is there now. It leaves three things open, and they are what the script was written for.
The backdoor is more than the key. By the notice's own account the tunnel failed on most machines, for want of admin rights, and the key, the persistence and the beacon went ahead regardless. The persistence is a LaunchAgent, a scheduled task or a startup script that retries the tunnel every 60 seconds, and it survives uninstalling the extension and deleting the key by hand. The script checks the persistence, the tunnel files and key, the cron line, the Run key, the process list and open connections, and the same places under other names.
Whether you ever had the bad build. Cursor auto-updates extensions. If 2.1.313 was replaced by 2.1.314 later that day, the extension folder is clean, the grep can be clean, and the beacon still went out on Oct 29 with your hostname, username, environment variable names, Git email and public IP. The notice's step 2 is to search your extension-installation telemetry; most people have none. The editor's own install log and removed-extensions list are that telemetry for one machine. The script reads them: that is the BAD VERSION WAS INSTALLED ending, and why it says rotate.
Whether an installed copy is the bad one. A version number is not the answer; the notice publishes the hash of the modified extension.js and the two strings inside it. The script hashes the file and greps it, and reports a backdoored build as such.
Then
Traces found, or the backdoored build installed: disconnect the machine, rotate SSH keys, cloud and API credentials and Git tokens from a different machine, run Cursor's remediation script. Steps on the advisory .
Bad version was installed, nothing else found: the update removed the extension, not what it did while installed. The beacon went out, and the notice says what it took does not rule out later credential access. Rotate the credentials this machine used, from another machine.
This is one incident. The script finds what has been published about it and nothing else: an extension nobody has flagged yet, a poisoned npm or pip package, a malicious MCP server or model file are all out of its reach. The full check adds Ciphero's known-malicious database and the marketplaces, which cover the extensions, and that is still the whole of it.
Nothing found: you are clear of this incident's published indicators. Update Claude Code to 2.1.314 or later if you have not.
Want the rest? The full check is this script with a real token: after you type yes, it also matches your extension ids against Ciphero's database of thousands of known-malicious ones and the marketplaces, and emails a report. That is why it asks for an address first. Free. Not needed for this incident.
Before you run it
408 lines of bash (414 of PowerShell). Everything it calls: grep , sed , awk , cut , sort , basename , uname , hostname , env , ps , crontab -l , launchctl , ssh-keygen -l , lsof or ss or netstat , sha256sum or shasum or openssl for the hash, and one curl at the very end.
This copy has YOUR-CHECK-TOKEN where a check token goes, so it exits before that curl . Nothing leaves. The full check is the same text with a real token; a spec holds the two to that one difference.
The body is one function, main , called on the last line: a truncated download runs nothing. Same bytes to curl and to a browser. sha256 of /cassandra.sh now: 2d4f03c543eac41922290d06b08798575ed49ba8133dd00bf075be60071d55b8 .
It finds published indicators, not novel implants. It reads your user's files only. A found is a name, path or string match, not proof of a working tunnel.
Every check, by operating system
Artefact macOS Linux Windows Cursor's grep
Attacker SSH key (svc-telemetry) in authorized_keys
 yes
 yes
 yes
 yes
Attacker SSH key fingerprint in authorized_keys
 yes
 yes
 yes
Fake Apple LaunchAgent com.apple.sysmond.plist
 yes
Reverse-tunnel service com.apple.sysmond loaded
 yes
Tunnel files ~/.config/.smt and ~/.config/.smtk
 yes
 yes
Staging files .stk_* in the temp directory
 yes
 yes
Cron entry running the tunnel script .config/.smt
 yes
 yes
Shell start-up file running the tunnel script
 yes
 yes
A LaunchAgent, systemd unit or autostart entry running the tunnel script under another name
 yes
 yes
The reverse-tunnel key, by fingerprint, among your SSH keys
 yes
 yes
 yes
Scheduled task SysMon
yes
Tunnel files smt.cmd and smtk in .config
yes
Startup script sysmon.cmd
yes
Staging files .stk_* in %TEMP%
yes
Run key starting the tunnel script smt.cmd
yes
A scheduled task running the tunnel script under another name
yes
Reverse SSH tunnel process to the attacker server
 yes
 yes
 yes
Live connection to the attacker server 134.209.82.225
 yes
 yes
 yes
The attacker server address inside the code of another installed extension
 yes
 yes
 yes
Also, per editor (Cursor, VS Code, VS Code Insiders, Windsurf, VSCodium, Kiro and Trae): installed extension ids and versions, the install log for a bad version an update already replaced, and the extension.js hash above. The malicious packages were built for macOS and Windows; the notice lists Linux paths too, and the script checks them.
What leaves the machine in the full check
 In this copy: nothing. In the full check, after you type yes : yes / no per check plus the name of what matched; extension ids and versions; the SHA-256 of extension.js , not the file; names of AI tools and of API-key environment variables, never values; OS, architecture, short host name. Never file contents, key material or secrets. Every fact is printed before the question, and s shows every line.
The script
cassandra.sh · 408 lines · sha256 2d4f03c543eac419… · raw
 #!/bin/bash
#
# Cassandra · malicious extension check · by Ciphero
#
# What this script does, in order:
# 1. Lists the extensions installed in your editors (VS Code, Cursor,
# Windsurf and other forks) and browsers (Chrome, Edge, Brave, Arc,
# Firefox and others), by folder name: id and version only. If a
# version an incident below names is installed, it also hashes that
# extension's main file and greps it for the published attacker
# strings: the hash and a yes / no go, never the file. That is how
# a genuine copy of the version is told from the backdoored one.
# 2. Checks a fixed list of places (below): named files and folders,
# your shell start-up files, your own crontab, your LaunchAgents,
# systemd units and autostart entries, the running process list
# and the code of your other extensions, for the traces of
# specific incidents. It records yes / no plus the name of what
# matched (a file name, an extension folder). It sends no file
# contents and no paths, only the answer.
# 3. Lists AI tool names and the NAMES (never values) of API-key variables.
# 4. Shows you every fact it will send and asks before sending.
# 5. Sends them to Ciphero over HTTPS. Ciphero matches the extensions
# against known-malicious lists and the marketplaces, and prints
# your risk level.
#
# It installs nothing, writes nothing, schedules nothing, needs no sudo.
# Run it only on a machine you own or are allowed to check. By sending
# the facts you accept Ciphero's terms (https://ciphero.ai/terms#cassandra)
# and privacy policy (https://ciphero.ai/privacy#cassandra).
# Incidents it looks for traces of:
# CSA-2026-0001 · Malicious Claude Code extensions 2.1.312 and 2.1.313 (Cursor marketplace)
# https://cursor.com/blog/claude-code-extension-security-notice
#
# The readable copy at https://ciphero.ai/cassandra.sh is this same file with
# YOUR-CHECK-TOKEN in place of a check token. Run as is, it does every
# check above, prints its own summary of the incident traces and stops
# before step 4: it has no token, so there is nothing it can send to.
#
# Everything below sits in main, called on the last line, so a download
# cut short runs nothing at all.
set -u
main() {
CASSANDRA_URL="https://ciphero.ai/cassandra/scan/YOUR-CHECK-TOKEN"
CASSANDRA_TOKEN="YOUR-CHECK-TOKEN"
CASSANDRA_VERSION="3"
OUT=""
NL='
'
fact() { local IFS="$(printf '\t')"; OUT="${OUT}$*${NL}"; }
if [ -t 1 ]; then
 B="$(printf '\033[1m')"; D="$(printf '\033[2m')"; R="$(printf '\033[0m')"
 RED="$(printf '\033[38;5;203m')"; AMB="$(printf '\033[38;5;215m')"; YEL="$(printf '\033[38;5;221m')"
 GRN="$(printf '\033[38;5;114m')"; GLD="$(printf '\033[38;5;179m')"
else
 B=""; D=""; R=""; RED=""; AMB=""; YEL=""; GRN=""; GLD=""
fi
say() { printf '%s\n' "$*"; }
row() {
 case "$2" in
 yes) say " ${RED}●${R} $1 ${RED}${B}found${R}" ;;
 no) say " ${GRN}○${R} ${D}$1${R} ${GRN}clear${R}" ;;
 na) say " ${D}· $1 n/a${R}" ;;
 *) say " ${YEL}?${R} $1 ${YEL}could not check${R}" ;;
 esac
}
say ""
say " ${GLD}${B}◆ CASSANDRA${R} ${D}malicious extension check · by Ciphero${R}"
say ""
case "$(uname -s)" in
 Darwin) OS=darwin ;;
 Linux) OS=linux ;;
 *) say " This script covers macOS and Linux. On Windows, run the PowerShell line from the Cassandra page."; exit 1 ;;
esac
fact v "$CASSANDRA_VERSION"
fact os "$OS"
fact arch "$(uname -m)"
fact host "$(hostname -s 2>/dev/null || hostname)"
TMPD="${TMPDIR:-/tmp}"
# ── Indicator checks: yes / no, plus the name of what matched ────
# Each probe sets ST (yes / no / na / err) and calls hit with the
# file or folder name behind a yes: a plist name, a key file, an
# extension folder. Never a path under the home directory, never
# contents. Globs in the path list expand here, unquoted.
ST=no; CHECK_ID=""
hit() { fact hit "$CHECK_ID" "$1"; }
contains_any() { # needle path...
 local needle="$1" p; ST=no; shift
 for p in "$@"; do
 [ -f "$p" ] || continue
 if [ -r "$p" ]; then grep -qF -- "$needle" "$p" 2>/dev/null && { ST=yes; hit "$(basename "$p")"; }; else [ "$ST" = yes ] || ST=err; fi
 done
}
fingerprint_any() { # fingerprint path...
 local needle="$1" p; ST=no; shift
 for p in "$@"; do
 [ -f "$p" ] || continue
 command -v ssh-keygen >/dev/null 2>&1 || { ST=err; continue; }
 if [ -r "$p" ]; then ssh-keygen -lf "$p" -E sha256 /dev/null | grep -qF -- "$needle" && { ST=yes; hit "$(basename "$p")"; }; else [ "$ST" = yes ] || ST=err; fi
 done
}
exists_any() { local p; ST=no; for p in "$@"; do [ -e "$p" ] && { ST=yes; hit "$(basename "$p")"; }; done; }
launchctl_has() {
 command -v launchctl >/dev/null 2>&1 || { ST=na; return; }
 launchctl list 2>/dev/null | grep -qF -- "$1" && ST=yes || ST=no
}
connected_to() {
 if command -v lsof >/dev/null 2>&1; then
 lsof -nP -iTCP 2>/dev/null | grep -qF -- "$1" && ST=yes || ST=no
 elif command -v ss >/dev/null 2>&1; then
 ss -tn 2>/dev/null | grep -qF -- "$1" && ST=yes || ST=no
 elif command -v netstat >/dev/null 2>&1; then
 netstat -an 2>/dev/null | grep -qF -- "$1" && ST=yes || ST=no
 else ST=err; fi
}
crontab_has() { # the user's own crontab; the backdoor ran as the user
 command -v crontab >/dev/null 2>&1 || { ST=na; return; }
 crontab -l 2>/dev/null | grep -qF -- "$1" && ST=yes || ST=no
}
process_has() { # a command line in the process list, our own grep excluded
 command -v ps >/dev/null 2>&1 || { ST=err; return; }
 ps -eww -o command= 2>/dev/null | grep -F -- "$1" | grep -qvF -- 'grep -F' && ST=yes || ST=no
}
# The needle inside the code of any installed extension other than
# the versions an incident already names: a re-published variant
# under another id or version. Top-level, dist/ and out/ scripts only,
# so it stays fast; the folder name is the evidence.
EXT_DIRS=""
extensions_contain() { # needle
 local id dir f rel folder nd skip; ST=no
 while IFS=' ' read -r id dir; do
 [ -n "$id" ] && [ -d "$dir" ] || continue
 for f in "$dir"/*/*.js "$dir"/*/dist/*.js "$dir"/*/out/*.js; do
 [ -f "$f" ] && [ -r "$f" ] || continue
 rel="${f#"$dir"/}"; folder="${rel%%/*}"; skip=no
 for nd in $NEEDLES; do case "$folder" in "$nd"*) skip=yes ;; esac; done
 [ "$skip" = no ] || continue
 grep -qF -- "$1" "$f" 2>/dev/null && { ST=yes; hit "$id:$folder"; }
 done
 done </dev/null && { fact hist "$1" "$nd" obsolete; note_hist "$1" "$nd"; }
 done
}
# The editor's own install log (main.log, sharedprocess.log per
# session) names the versions it installed and removed: a second
# history source, for a bad version that an update already replaced.
log_history() { # editor logs-dir
 [ -d "$2" ] || return
 local nd f
 for nd in $NEEDLES; do
 for f in "$2"/*/main.log "$2"/*/sharedprocess.log; do
 [ -r "$f" ] && grep -qF -- "$nd" "$f" 2>/dev/null && { fact hist "$1" "$nd" logs; note_hist "$1" "$nd"; break; }
 done
 done
}
sha256_of() {
 if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | awk '{print $1}'
 elif command -v shasum >/dev/null 2>&1; then shasum -a 256 "$1" | awk '{print $1}'
 else openssl dgst -sha256 "$1" 2>/dev/null | awk '{print $NF}'; fi
}
vsix_cache() { # editor dir
 [ -d "$2" ] || return
 for f in "$2"/*; do
 [ -f "$f" ] || continue
 n="$(basename "$f")"
 for nd in $NEEDLES; do
 case "$n" in "$nd"*) fact vsix "$1" "$n" "$(sha256_of "$f")" ;; esac
 done
 done
}
# The main file of an installed copy of a version an incident names:
# its SHA-256, and whether the published attacker strings are in it.
HASHED=""; BACKDOORED=""
payload_scan() { # editor dir file "needle needle" string...
 local ed="$1" dir="$2" file="$3" nds="$4" nd d n hit s; shift 4
 [ -d "$dir" ] || return
 for nd in $nds; do
 for d in "$dir/$nd"*/; do
 [ -f "$d$file" ] && [ -r "$d$file" ] || continue
 n="$(basename "$d")"; hit=no
 for s in "$@"; do grep -qF -- "$s" "$d$file" 2>/dev/null && { hit=yes; break; }; done
 [ "$hit" = yes ] && BACKDOORED="${BACKDOORED} ${n}"
 fact payload "$ed" "$n" "$file" "$(sha256_of "$d$file")" "$hit"
 HASHED="${HASHED} ${B}${n}${R} ${D}${file} hashed: the hash goes, not the file${R}${NL}"
 done
 done
}
list_exts cursor "$HOME/.cursor/extensions"
list_exts cursor "$HOME/.cursor-server/extensions"
vsix_cache cursor "$HOME/Library/Application Support/Cursor/CachedExtensionVSIXs"
vsix_cache cursor "$HOME/.config/Cursor/CachedExtensionVSIXs"
log_history cursor "$HOME/Library/Application Support/Cursor/logs"
log_history cursor "$HOME/.config/Cursor/logs"
payload_scan cursor "$HOME/.cursor/extensions" extension.js "anthropic.claude-code-2.1.312 anthropic.claude-code-2.1.313" 134.209.82.225 svc-telemetry
payload_scan cursor "$HOME/.cursor-server/extensions" extension.js "anthropic.claude-code-2.1.312 anthropic.claude-code-2.1.313" 134.209.82.225 svc-telemetry
list_exts vscode "$HOME/.vscode/extensions"
list_exts vscode "$HOME/.vscode-server/extensions"
vsix_cache vscode "$HOME/Library/Application Support/Code/CachedExtensionVSIXs"
vsix_cache vscode "$HOME/.config/Code/CachedExtensionVSIXs"
log_history vscode "$HOME/Library/Application Support/Code/logs"
log_history vscode "$HOME/.config/Code/logs"
payload_scan vscode "$HOME/.vscode/extensions" extension.js "anthropic.claude-code-2.1.312 anthropic.claude-code-2.1.313" 134.209.82.225 svc-telemetry
payload_scan vscode "$HOME/.vscode-server/extensions" extension.js "anthropic.claude-code-2.1.312 anthropic.claude-code-2.1.313" 134.209.82.225 svc-telemetry
list_exts vscode_insiders "$HOME/.vscode-insiders/extensions"
payload_scan vscode_insiders "$HOME/.vscode-insiders/extensions" extension.js "anthropic.claude-code-2.1.312 anthropic.claude-code-2.1.313" 134.209.82.225 svc-telemetry
list_exts windsurf "$HOME/.windsurf/extensions"
vsix_cache windsurf "$HOME/Library/Application Support/Windsurf/CachedExtensionVSIXs"
log_history windsurf "$HOME/Library/Application Support/Windsurf/logs"
log_history windsurf "$HOME/.config/Windsurf/logs"
payload_scan windsurf "$HOME/.windsurf/extensions" extension.js "anthropic.claude-code-2.1.312 anthropic.claude-code-2.1.313" 134.209.82.225 svc-telemetry
list_exts vscodium "$HOME/.vscode-oss/extensions"
payload_scan vscodium "$HOME/.vscode-oss/extensions" extension.js "anthropic.claude-code-2.1.312 anthropic.claude-code-2.1.313" 134.209.82.225 svc-telemetry
list_exts kiro "$HOME/.kiro/extensions"
payload_scan kiro "$HOME/.kiro/extensions" extension.js "anthropic.claude-code-2.1.312 anthropic.claude-code-2.1.313" 134.209.82.225 svc-telemetry
list_exts trae "$HOME/.trae/extensions"
payload_scan trae "$HOME/.trae/extensions" extension.js "anthropic.claude-code-2.1.312 anthropic.claude-code-2.1.313" 134.209.82.225 svc-telemetry
say " ${B}Editor extensions${R} ${D}${EXT_COUNT} found, ids and versions only${R}"
[ -n "$HASHED" ] && printf '%s' "$HASHED"
# ── Browser extensions: ids only ─────────────────────────────────
BEXT_COUNT=0
BSEEN=" "
BNAMES=""
add_bext() { # browser id version
 case "$BSEEN" in *" $1:$2 "*) return ;; esac
 BSEEN="$BSEEN$1:$2 "
 case " $BNAMES " in *" $1 "*) ;; *) BNAMES="${BNAMES:+$BNAMES }$1" ;; esac
 fact bext "$1" "$2" "$3"; BEXT_COUNT=$((BEXT_COUNT + 1))
}
list_chromium() { # browser root: //Extensions//_0
 [ -d "$2" ] || return
 for ed in "$2"/*/Extensions; do
 [ -d "$ed" ] || continue
 for idd in "$ed"/*/; do
 id="$(basename "$idd")"
 [ "${#id}" -eq 32 ] || continue
 case "$id" in *[!a-p]*) continue ;; esac
 ver=""
 for vd in "$idd"*/; do [ -d "$vd" ] && ver="$(basename "$vd")"; done
 add_bext "$1" "$id" "${ver%_*}"
 done
 done
}
list_firefox() { # browser root: //extensions/.xpi
 [ -d "$2" ] || return
 for x in "$2"/*/extensions/*.xpi; do
 [ -f "$x" ] || continue
 add_bext "$1" "$(basename "$x" .xpi)" ""
 done
}
list_chromium chrome "$HOME/Library/Application Support/Google/Chrome"
list_chromium chrome "$HOME/.config/google-chrome"
list_chromium chrome "$HOME/.var/app/com.google.Chrome/config/google-chrome"
list_chromium edge "$HOME/Library/Application Support/Microsoft Edge"
list_chromium edge "$HOME/.config/microsoft-edge"
list_chromium brave "$HOME/Library/Application Support/BraveSoftware/Brave-Browser"
list_chromium brave "$HOME/.config/BraveSoftware/Brave-Browser"
list_chromium arc "$HOME/Library/Application Support/Arc/User Data"
list_chromium dia "$HOME/Library/Application Support/Dia/User Data"
list_chromium comet "$HOME/Library/Application Support/Comet"
list_chromium vivaldi "$HOME/Library/Application Support/Vivaldi"
list_chromium vivaldi "$HOME/.config/vivaldi"
list_chromium chromium "$HOME/Library/Application Support/Chromium"
list_chromium chromium "$HOME/.config/chromium"
list_chromium chromium "$HOME/snap/chromium/common/chromium"
list_firefox firefox "$HOME/Library/Application Support/Firefox/Profiles"
list_firefox firefox "$HOME/.mozilla/firefox"
list_firefox firefox "$HOME/snap/firefox/common/.mozilla/firefox"
say " ${B}Browser extensions${R} ${D}${BEXT_COUNT} found${BNAMES:+ in $BNAMES}, ids and versions only${R}"
say ""
# ── Incident traces: yes / no, plus the name of what matched ─────
say " ${B}Claude Code 2.1.312 and 2.1.313${R} ${D}incident traces${R}"
run_check ssh_key_comment "darwin linux" "Attacker SSH key svc-telemetry in authorized_keys" contains_any "svc-telemetry" "$HOME/.ssh/authorized_keys" "$HOME/.ssh/authorized_keys2"
run_check ssh_key_fingerprint "darwin linux windows" "Attacker SSH key fingerprint in authorized_keys" fingerprint_any "SHA256:0Z6R+DF64Do2nwQic8a7kkfDLNNk4IiK+2U2Rci4htk" "$HOME/.ssh/authorized_keys" "$HOME/.ssh/authorized_keys2"
run_check mac_launch_agent "darwin" "Fake Apple LaunchAgent com.apple.sysmond.plist" exists_any "$HOME/Library/LaunchAgents/com.apple.sysmond.plist"
run_check mac_launchctl "darwin" "Reverse-tunnel service com.apple.sysmond loaded" launchctl_has "com.apple.sysmond"
run_check unix_tunnel_files "darwin linux" "Tunnel files ~/.config/.smt and ~/.config/.smtk" exists_any "$HOME/.config/.smt" "$HOME/.config/.smtk"
run_check unix_stage_files "darwin linux" "Staging files .stk_* in the temp directory" exists_any "$TMPD"/.stk_* "/tmp"/.stk_*
run_check cron_entry "darwin linux" "Cron entry running the tunnel script .config/.smt" crontab_has ".config/.smt"
run_check unix_shell_rc "darwin linux" "Shell start-up file running the tunnel script" contains_any ".config/.smt" "$HOME/.zshrc" "$HOME/.zprofile" "$HOME/.zshenv" "$HOME/.bashrc" "$HOME/.bash_profile" "$HOME/.profile" "$HOME/.config/fish/config.fish"
run_check unix_persistence_renamed "darwin linux" "A LaunchAgent systemd unit or autostart entry running the tunnel script under another name" contains_any ".config/.smt" "$HOME/Library/LaunchAgents"/*.plist "$HOME/.config/systemd/user"/*.service "$HOME/.config/autostart"/*.desktop
run_check tunnel_key_anywhere "darwin linux windows" "The reverse-tunnel key by fingerprint among your SSH keys" fingerprint_any "SHA256:KOAU57+ZG6u3MG4WwzPzPX2O5YEe9qdOC1Bl+6MVyDQ" "$HOME/.ssh"/* "$HOME/.config/.smtk"
run_check tunnel_process "darwin linux windows" "Reverse SSH tunnel process to the attacker server" process_has "tunnel@134.209.82.225"
run_check c2_connection "darwin linux windows" "Live connection to the attacker server 134.209.82.225" connected_to "134.209.82.225"
run_check ext_code_ioc "darwin linux windows" "The attacker server address inside the code of another installed extension" extensions_contain "134.209.82.225"
say ""
# ── AI tools and API-key variable NAMES (never values) ───────────
TOOLS=""
for b in claude codex cursor-agent gemini aider goose opencode amp copilot ollama lms; do
 command -v "$b" >/dev/null 2>&1 && { fact tool "$b"; TOOLS="$TOOLS $b"; }
done
if [ "$OS" = darwin ]; then
 for a in "Cursor" "Windsurf" "Claude" "ChatGPT" "Visual Studio Code" "Kiro" "Trae" "Zed" "Ollama" "LM Studio"; do
 if [ -d "/Applications/$a.app" ] || [ -d "$HOME/Applications/$a.app" ]; then fact tool "app:$a"; TOOLS="$TOOLS app:$a"; fi
 done
fi
ENV_RE='^(OPENAI|ANTHROPIC|GEMINI|GOOGLE|MISTRAL|GROQ|OPENROUTER|TOGETHER|FIREWORKS|DEEPSEEK|XAI|COHERE|HF|HUGGINGFACE|AWS|AZURE|GITHUB|GH|GITLAB|NPM|PYPI|STRIPE|SLACK|DATABRICKS|SNOWFLAKE)[A-Z0-9_]*(_API_KEY|_API_TOKEN|_ACCESS_TOKEN|_SECRET_KEY)$'
ENVS="$( { env | cut -d= -f1; grep -hoE '^\[[:space:\]]*export\[[:space:\]]+[A-Z][A-Z0-9_]*=' "$HOME/.zshrc" "$HOME/.zprofile" "$HOME/.bashrc" "$HOME/.bash_profile" "$HOME/.profile" 2>/dev/null | sed -E 's/^\[[:space:\]]*export\[[:space:\]]+//; s/=$//'; } | grep -E "$ENV_RE" | sort -u)"
for e in $ENVS; do fact env "$e"; done
say " ${B}AI tools${R} ${D}${TOOLS:- none found}${R}"
KEYN="$(echo $ENVS)"
say " ${B}Key variable names${R} ${D}${KEYN:-none found}${R}"
say ""
# ── The readable copy: no token, so nothing to send to ───────────
# Its own summary of the incident traces, then out, before the
# consent prompt. The list match needs a check (https://ciphero.ai/cassandra).
if [ "$CASSANDRA_TOKEN" = "YOUR-CHECK-TOKEN" ]; then
 if [ -n "$BACKDOORED" ]; then
 say " ${RED}${B}■ BACKDOORED BUILD${R} ${B}Installed, and its main file contains the attacker strings:${BACKDOORED}${R}"
 fi
 if [ -n "$HISTORY" ]; then
 say " ${RED}${B}■ BAD VERSION WAS INSTALLED${R} ${B}In the editor's install history:${HISTORY}.${R} An update may have removed it since; what it did while installed is not undone."
 fi
 if [ "$FOUND" -gt 0 ]; then
 say " ${RED}${B}■ TRACES FOUND${R} ${B}${FOUND} of ${CHECKS} published indicators were found on this machine.${R}"
 elif [ -z "${BACKDOORED}${HISTORY}" ]; then
 say " ${GRN}${B}■ NO TRACES${R} ${B}None of the ${CHECKS} published indicators were found on this machine.${R}"
 else
 say " ${B}None of the ${CHECKS} other published indicators were found.${R}"
 fi
 if [ "$FOUND" -gt 0 ] || [ -n "$BACKDOORED" ]; then
 say " ${GLD}→${R} Treat it as compromised. Steps, per incident: https://ciphero.ai/advisories"
 elif [ -n "$HISTORY" ]; then
 say " ${GLD}→${R} Treat the machine as exposed: rotate the keys and tokens it used, from another machine. Steps: https://ciphero.ai/advisories"
 fi
 say ""
 say " ${D}This is the readable copy of the script. It carries no check token, so nothing was sent${R}"
 say " ${D}and everything above ran here. It did not match your ${EXT_COUNT} editor and ${BEXT_COUNT} browser${R}"
 say " ${D}extensions against the known-malicious lists or the marketplaces. For that, and a${R}"
 say " ${D}written report: https://ciphero.ai/cassandra${R}"
 say ""
 exit 0
fi
# ── Consent: nothing goes until you type yes ─────────────────────
NFACTS="$(printf '%s' "$OUT" | grep -c .)"
say " ${B}Ready to send ${NFACTS} facts to Ciphero.${R} ${D}No file contents, no key values.${R}"
say " ${D}Sending accepts Ciphero's terms and privacy policy: https://ciphero.ai/terms#cassandra${R}"
ANSWER=""
while :; do
 if [ "${CASSANDRA_YES:-}" = 1 ]; then ANSWER=y
 elif (exec < /dev/tty) 2>/dev/null; then
 printf ' Send them? [y]es / [n]o / [s]how every line: ' > /dev/tty
 read -r ANSWER < /dev/tty || ANSWER=n
 else say " No terminal to ask on. Re-run with CASSANDRA_YES=1 to send without asking."; exit 1; fi
 case "$ANSWER" in
 s|S|show) printf '%s' "$OUT" | sed 's/^/ /' ;;
 n|N|no|No|NO) say " Nothing sent."; exit 0 ;;
 y|Y|yes|Yes|YES) break ;;
 *) say " ${D}Please answer y, n or s.${R}" ;;
 esac
done
RESP="$(printf '%s' "$OUT" | curl -fsS --max-time 40 -X POST -H 'Content-Type: text/plain' --data-binary @- "$CASSANDRA_URL" 2>&1)" || {
 say " ${RED}Upload failed:${R} $RESP"; exit 1; }
say ""
printf '%s\n' "$RESP" | while IFS='|' read -r level text; do
 case "$level" in
 critical) say " ${RED}${B}■ CRITICAL${R} ${B}$text${R}" ;;
 high) say " ${AMB}${B}■ HIGH${R} ${B}$text${R}" ;;
 caution) say " ${YEL}${B}■ CAUTION${R} ${B}$text${R}" ;;
 clear) say " ${GRN}${B}■ CLEAR${R} ${B}$text${R}" ;;
 step) say " ${GLD}→${R} $text" ;;
 error) say " ${RED}${B}■${R} $text" ;;
 *) say " ${D}$text${R}" ;;
 esac
done
say ""
}
main
cassandra.ps1 · 414 lines · sha256 73c8df3cdc0bcc3d… · raw
 # Cassandra - malicious extension check - by Ciphero
#
# Lists the extensions installed in your editors (VS Code, Cursor,
# Windsurf and other forks) and browsers (Chrome, Edge, Brave, Firefox
# and others) by folder name: id and version only. If a version an
# incident below names is installed, hashes that extension's main file
# and checks it for the published attacker strings (the hash and a
# yes / no go, never the file). Checks a fixed list of places (named
# files and folders, your Run keys, the scheduled tasks, the running
# processes and the code of your other extensions) for the traces of
# specific incidents: yes / no plus the name of what matched, never
# file contents. Lists AI tool names and the NAMES (never values) of
# API-key variables, shows you every fact, asks before sending, then
# prints your risk level. Ciphero matches the extensions against
# known-malicious lists and the marketplaces. Installs nothing.
# Run it only on a machine you own or are allowed to check. By sending
# the facts you accept Ciphero's terms (https://ciphero.ai/terms#cassandra)
# and privacy policy (https://ciphero.ai/privacy#cassandra).
# Incidents it looks for traces of:
# CSA-2026-0001 - Malicious Claude Code extensions 2.1.312 and 2.1.313 (Cursor marketplace)
# https://cursor.com/blog/claude-code-extension-security-notice
#
# The readable copy at https://ciphero.ai/cassandra.ps1 is this same file with
# YOUR-CHECK-TOKEN in place of a check token. Run as is, it does every
# check, prints its own summary of the incident traces and stops before
# asking to send: it has no token, so there is nothing it can send to.
#
# Cmdlets only, no .NET calls beyond strings and hashtables, so it also
# runs under Constrained Language Mode on managed machines. Its state
# lives in one hashtable ($cx) rather than in your session's variables.
& {
 $ErrorActionPreference = 'SilentlyContinue'
 $ProgressPreference = 'SilentlyContinue'
 $url = 'https://ciphero.ai/cassandra/scan/YOUR-CHECK-TOKEN'
 $token = 'YOUR-CHECK-TOKEN'
 $cx = @{ facts = @(); checkId = ''; extDirs = @(); extCount = 0; bextCount = 0; bseen = @{}; bnames = @(); checks = 0; found = 0; backdoored = @(); history = @() }
 $psNoise = @('PSPath', 'PSParentPath', 'PSChildName', 'PSDrive', 'PSProvider')
 function Add-Fact { $cx.facts += ($args -join "`t") }
 function Show-Row($label, $st) {
 switch ($st) {
 'yes' { Write-Host " * $label " -NoNewline; Write-Host 'found' -ForegroundColor Red }
 'no' { Write-Host " o $label " -NoNewline -ForegroundColor DarkGray; Write-Host 'clear' -ForegroundColor Green }
 'na' { Write-Host " . $label n/a" -ForegroundColor DarkGray }
 default { Write-Host " ? $label " -NoNewline; Write-Host 'could not check' -ForegroundColor Yellow }
 }
 }
 # A file under ProgramData that this user can't open (OpenSSH Server's
 # administrators_authorized_keys) is one that code running as this user
 # couldn't have written either: not applicable, not a failed check.
 function Test-AdminOnly($p) {
 if (-not $env:ProgramData) { return $false }
 if (-not $p.ToLowerInvariant().StartsWith($env:ProgramData.ToLowerInvariant())) { return $false }
 try { $null = Get-Content -LiteralPath $p -TotalCount 1 -ErrorAction Stop; return $false } catch { return $true }
 }
 # Each probe returns yes / no / na / err and records the name of
 # what matched (a file, a key, an extension folder): never a path
 # under the profile, never contents. A wildcard sits only in the last
 # segment of a path, so it expands as a filter inside its literal
 # parent folder; brackets elsewhere in the path stay literal.
 function Add-Hit($name) { Add-Fact 'hit' $cx.checkId $name }
 function Expand-Paths($paths) {
 $found = @()
 foreach ($p in $paths) {
 if ($p -match '[*?]') {
 $dir = Split-Path $p -Parent; $leaf = Split-Path $p -Leaf
 if ($dir -and (Test-Path -LiteralPath $dir)) {
 $found += @(Get-ChildItem -LiteralPath $dir -Filter $leaf -File -Force -ErrorAction SilentlyContinue | ForEach-Object { $_.FullName })
 }
 } elseif (Test-Path -LiteralPath $p -PathType Leaf) { $found += $p }
 }
 return $found
 }
 function Test-Contains($needle, $paths) {
 $st = 'no'; $read = $false; $skipped = $false
 foreach ($p in (Expand-Paths $paths)) {
 if (Test-AdminOnly $p) { $skipped = $true; continue }
 try {
 if (Select-String -LiteralPath $p -SimpleMatch -Pattern $needle -Quiet -ErrorAction Stop) { $st = 'yes'; Add-Hit (Split-Path $p -Leaf) }
 $read = $true
 } catch { if ($st -ne 'yes') { $st = 'err' } }
 }
 if ($st -eq 'no' -and $skipped -and -not $read) { return 'na' }
 return $st
 }
 function Test-Fingerprint($needle, $paths) {
 $st = 'no'; $read = $false; $skipped = $false
 $keygen = Get-Command ssh-keygen -ErrorAction SilentlyContinue
 foreach ($p in (Expand-Paths $paths)) {
 if (Test-AdminOnly $p) { $skipped = $true; continue }
 if (-not $keygen) { $st = 'err'; continue }
 # Empty input on stdin: ssh-keygen -l asks nothing, and if a build
 # ever did, it gets an answer instead of waiting on the terminal.
 $fp = '' | & ssh-keygen -lf $p -E sha256 2>$null
 if (-not $fp) { continue }
 if (($fp -join ' ').Contains($needle)) { $st = 'yes'; Add-Hit (Split-Path $p -Leaf) }
 $read = $true
 }
 if ($st -eq 'no' -and $skipped -and -not $read) { return 'na' }
 return $st
 }
 function Test-Any($paths) {
 $st = 'no'
 foreach ($p in $paths) {
 if ($p -match '[*?]') {
 $dir = Split-Path $p -Parent; $leaf = Split-Path $p -Leaf
 if ($dir -and (Test-Path -LiteralPath $dir)) {
 foreach ($f in @(Get-ChildItem -LiteralPath $dir -Filter $leaf -Force -ErrorAction SilentlyContinue)) { $st = 'yes'; Add-Hit $f.Name }
 }
 } elseif (Test-Path -LiteralPath $p) { $st = 'yes'; Add-Hit (Split-Path $p -Leaf) }
 }
 return $st
 }
 # The user's own Run keys: persistence the notice did not list.
 function Test-RunKey($needle) {
 $st = 'no'
 foreach ($k in 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run', 'HKCU:\Software\Microsoft\Windows\CurrentVersion\RunOnce') {
 $props = Get-ItemProperty -Path $k -ErrorAction SilentlyContinue
 if (-not $props) { continue }
 foreach ($p in $props.PSObject.Properties) {
 if ($psNoise -contains $p.Name) { continue }
 if ("$($p.Value)".Contains($needle)) { $st = 'yes'; Add-Hit $p.Name }
 }
 }
 return $st
 }
 # Any scheduled task whose action runs the needle, whatever the task is called.
 function Test-TaskAction($needle) {
 if (-not (Get-Command Get-ScheduledTask -ErrorAction SilentlyContinue)) { return 'err' }
 $st = 'no'
 foreach ($t in @(Get-ScheduledTask -ErrorAction SilentlyContinue)) {
 foreach ($a in @($t.Actions)) {
 if ("$($a.Execute) $($a.Arguments)".Contains($needle)) { $st = 'yes'; Add-Hit $t.TaskName; break }
 }
 }
 return $st
 }
 # The needle inside the code of any installed extension other than
 # the versions an incident already names. Top-level, dist and out
 # scripts only (a few MB at most), so it stays fast.
 function Test-ExtCode($needle) {
 $st = 'no'
 foreach ($pair in $cx.extDirs) {
 $editor, $dir = $pair
 foreach ($f in @(Get-ChildItem -Path "$dir\*\*.js", "$dir\*\dist\*.js", "$dir\*\out\*.js" -File -ErrorAction SilentlyContinue)) {
 if ($f.Length -gt 64MB) { continue }
 $folder = (($f.FullName.Substring($dir.Length) -replace '^[\\/]+', '') -split '[\\/]')[0]
 $named = $false
 foreach ($n in $needles) { if ($folder.StartsWith($n)) { $named = $true } }
 if ($named) { continue }
 if (Select-String -LiteralPath $f.FullName -SimpleMatch -Pattern $needle -Quiet -ErrorAction SilentlyContinue) { $st = 'yes'; Add-Hit "${editor}:$folder" }
 }
 }
 return $st
 }
 function Test-Task($name) {
 if (Get-Command Get-ScheduledTask -ErrorAction SilentlyContinue) {
 if (Get-ScheduledTask | Where-Object { $_.TaskName -eq $name }) { return 'yes' } else { return 'no' }
 }
 schtasks /Query /TN $name *> $null
 if ($LASTEXITCODE -eq 0) { return 'yes' } else { return 'no' }
 }
 function Test-Connection2($ip) {
 if (Get-Command Get-NetTCPConnection -ErrorAction SilentlyContinue) {
 if (Get-NetTCPConnection -RemoteAddress $ip -ErrorAction SilentlyContinue) { return 'yes' } else { return 'no' }
 }
 if (netstat -an | Select-String -SimpleMatch $ip) { return 'yes' } else { return 'no' }
 }
 function Test-Process($needle) {
 $procs = Get-CimInstance Win32_Process -ErrorAction SilentlyContinue
 if (-not $procs) { return 'err' }
 foreach ($p in $procs) { if ($p.CommandLine -and $p.CommandLine.Contains($needle)) { return 'yes' } }
 return 'no'
 }
 # A check's status is the last yes / no / na / err its probe
 # returned; anything else a cmdlet let slip into the pipeline is
 # ignored, and a probe that throws is 'could not check'.
 function Run-Check($id, $label, $probe) {
 $cx.checkId = $id
 $st = 'err'
 try {
 $seen = @(& $probe) | Where-Object { "$_" -in @('yes', 'no', 'na', 'err') } | Select-Object -Last 1
 if ($seen) { $st = "$seen" }
 } catch { $st = 'err' }
 Add-Fact 'check' $id $st; Show-Row $label $st
 $cx.checks += 1; if ($st -eq 'yes') { $cx.found += 1 }
 }
Write-Host ''
 Write-Host ' CASSANDRA' -ForegroundColor DarkYellow -NoNewline; Write-Host ' malicious extension check by Ciphero' -ForegroundColor DarkGray
 Write-Host ''
 $mode = "$($ExecutionContext.SessionState.LanguageMode)"
 if ($mode -and $mode -ne 'FullLanguage') {
 Write-Host " PowerShell runs in $mode here, a policy on this machine. Cassandra is written for it; anything it cannot check will say so." -ForegroundColor DarkGray
 Write-Host ''
 }
 Add-Fact 'v' '3'
 Add-Fact 'os' 'windows'
 Add-Fact 'arch' $env:PROCESSOR_ARCHITECTURE
 Add-Fact 'host' $env:COMPUTERNAME
$needles = @('anthropic.claude-code-2.1.312', 'anthropic.claude-code-2.1.313')
 function List-Exts($editor, $dir) {
 if (-not (Test-Path -LiteralPath $dir)) { return }
 $cx.extDirs += ,@($editor, (Get-Item -LiteralPath $dir).FullName)
 Get-ChildItem -LiteralPath $dir -Directory -Force | Where-Object { -not $_.Name.StartsWith('.') } | ForEach-Object {
 Add-Fact 'ext' $editor $_.Name; $cx.extCount += 1
 }
 $obs = Join-Path $dir '.obsolete'
 if (Test-Path -LiteralPath $obs) {
 $text = Get-Content -LiteralPath $obs -Raw
 foreach ($n in $needles) { if ($text -and $text.Contains($n)) { Add-Fact 'hist' $editor $n 'obsolete'; Note-Hist $editor $n } }
 }
 }
 # editor:version pairs the install history names, for the readable
 # copy's own summary (the full check's verdict gets the facts).
 function Note-Hist($editor, $n) { if ($cx.history -notcontains "${editor}:$n") { $cx.history += "${editor}:$n" } }
 # The editor's own install log names the versions it installed and
 # removed: a second history source for a version an update replaced.
 function Log-History($editor, $dir) {
 if (-not (Test-Path -LiteralPath $dir)) { return }
 $logs = @(Get-ChildItem -Path "$dir\*\main.log", "$dir\*\sharedprocess.log" -File -ErrorAction SilentlyContinue)
 foreach ($n in $needles) {
 foreach ($f in $logs) {
 if (Select-String -LiteralPath $f.FullName -SimpleMatch -Pattern $n -Quiet) { Add-Fact 'hist' $editor $n 'logs'; Note-Hist $editor $n; break }
 }
 }
 }
 function Vsix-Cache($editor, $dir) {
 if (-not (Test-Path -LiteralPath $dir)) { return }
 Get-ChildItem -LiteralPath $dir -File | ForEach-Object {
 $f = $_
 foreach ($n in $needles) {
 if ($f.Name.StartsWith($n)) { Add-Fact 'vsix' $editor $f.Name ((Get-FileHash -LiteralPath $f.FullName -Algorithm SHA256).Hash.ToLower()) }
 }
 }
 }
 # The main file of an installed copy of a version an incident names:
 # its SHA-256, and whether

## 关联链接

- https://ciphero.ai/advisories
- https://ciphero.ai/cassandra
- https://ciphero.ai/cassandra${R}
- https://ciphero.ai/cassandra.ps1
- https://ciphero.ai/cassandra.sh
- https://ciphero.ai/cassandra/scan/YOUR-CHECK-TOKEN
- https://ciphero.ai/privacy#cassandra
- https://ciphero.ai/terms#cassandra
- https://ciphero.ai/terms#cassandra${R}
- https://cursor.com/blog/claude-code-extension-security-notice

## 导航

- 项目页：[[10-项目/ciphero.ai_14b82968]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
