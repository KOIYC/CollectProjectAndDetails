---
type: "corpus"
item_id: "3d1c8a8c72eaa5e0"
title: "Show HN: Bulk-harden all your GitHub repos' settings without an API token"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50416829"
project_url: "https://gist.github.com/1ch4k/ba726954db1cc509c2071d54f93b5304"
author: "1ch4k"
published_at: "2026-11-08T20:29:02Z"
captured_at: "2026-11-09T09:39:29+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-09"
pub_day: "2026-11-08"
tags:
  - 语料
  - hn_show
  - author_1ch4k
  - story_50416829
  - show_hn
metrics: {"points": 2, "comments": 1, "engagement_velocity": 2}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: Bulk-harden all your GitHub repos' settings without an API token

> [!info] 一句话导读
> Bulk-harden your GitHub repo settings

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50416829>
> 指标：点赞=2 · 评论=1 · engagement_velocity=2
> 作者：1ch4k　|　发布：2026-11-08T20:29:02Z
> 项目链接：<https://gist.github.com/1ch4k/ba726954db1cc509c2071d54f93b5304>
> 采集：2026-11-09T09:39:29+08:00　|　id：`3d1c8a8c72eaa5e0`

## 正文

# Bulk-harden your GitHub repo settings

- Owner: 1ch4k
- Created: 2026-11-08T20:23:03Z
- Public: yes
- Comments: 0
- Forks: 0

## harden_github_repos.py

Language: Python

# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright"]
# ///
"""
harden_github_repos.py: bulk-harden the settings of every public repo you own on GitHub.

For each repo it opens the settings in a real browser window and:
 * Features -> turns the Wiki off (or only restricts editing, see --wiki)
 * Advanced Security -> enables Private vulnerability reporting,
 Secret Protection and Push protection
Steps that are already done are skipped, so it is safe to re-run after creating new repos.

Why a browser and not the API? It needs no token at all: you sign in to GitHub yourself
in the window that opens, and the script only clicks the same buttons you would.

Usage (needs uv: https://docs.astral.sh/uv/):
 uv run harden_github_repos.py --dry-run # show what would change, click nothing
 uv run harden_github_repos.py # apply
Options:
 --owner NAME account to process (default: the account you sign in with)
 --wiki restrict keep wikis but only collaborators can edit (default: off)
 --no-pvr don't touch Private vulnerability reporting
 --skip a,b repo names to leave alone
 --browser PATH Chromium-based browser to drive (default: Brave/Chrome/Edge if
 installed, else Playwright's own Chromium)
 --debug save the HTML of pages where a step was skipped (they contain
 session tokens: don't share them)

Notes:
 * Only public, non-archived repos are listed (via the public API, no auth).
 * The browser uses its own profile (~/.cache/harden-github-repos), never your everyday one;
 browsers refuse automation on the default profile. Delete that folder when you're done
 so no signed-in session is left behind.
 * GitHub changes its UI from time to time. If a step says "skipped", check it by hand.
"""
import argparse
import json
import shutil
import sys
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

PROFILE = Path.home() / ".cache" / "harden-github-repos"
DEBUG_DIR = Path.cwd() / "gh-debug"
BROWSER_CANDIDATES = [
 r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
 r"C:\Program Files\Google\Chrome\Application\chrome.exe",
 r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
 "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
 "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
 "brave", "brave-browser", "google-chrome", "chromium", "microsoft-edge",
]

args = None

def parse_args():
 p = argparse.ArgumentParser(description="Bulk-harden your GitHub repo settings via the web UI.")
 p.add_argument("--owner")
 p.add_argument("--dry-run", action="store_true")
 p.add_argument("--wiki", choices=["off", "restrict"], default="off")
 p.add_argument("--no-pvr", action="store_true")
 p.add_argument("--skip", default="")
 p.add_argument("--browser")
 p.add_argument("--debug", action="store_true")
 return p.parse_args()

def find_browser():
 if args.browser:
 return args.browser
 for c in BROWSER_CANDIDATES:
 if Path(c).is_file():
 return c
 found = shutil.which(c)
 if found:
 return found
 return None # Playwright's bundled Chromium

def list_repos(owner):
 url = f"https://api.github.com/users/{owner}/repos?per_page=100&type=owner"
 with urllib.request.urlopen(url, timeout=20) as r:
 repos = json.load(r)
 skip = {s.strip() for s in args.skip.split(",") if s.strip()}
 return [x["name"] for x in repos if not x["archived"] and x["name"] not in skip]

def log(repo, msg):
 print(f" [{repo}] {msg}")

def settle(page):
 # GitHub keeps a websocket open, so "networkidle" never fires; wait for the DOM + a moment.
 try:
 page.wait_for_load_state("domcontentloaded", timeout=15000)
 except PWTimeout:
 pass
 page.wait_for_timeout(1500)

def goto(page, url):
 page.goto(url, wait_until="domcontentloaded", timeout=45000)
 settle(page)

def dump(page, repo, step):
 if not args.debug:
 return
 try:
 DEBUG_DIR.mkdir(exist_ok=True)
 f = DEBUG_DIR / f"{repo}-{step}.html"
 f.write_text(page.content(), encoding="utf-8")
 log(repo, f"(saved page to {f})")
 except Exception as e:
 log(repo, f"(could not save debug page: {e})")

def ensure_login(page):
 """Wait until signed in (GitHub sets logged_in=yes), then return the signed-in username."""
 def logged_in():
 return any(c["name"] == "logged_in" and c["value"] == "yes"
 for c in page.context.cookies("https://github.com"))
 if not logged_in():
 goto(page, "https://github.com/login")
 print("\n>>> Sign in to GitHub in the browser window (incl. 2FA). Waiting...")
 while not logged_in():
 page.wait_for_timeout(2000)
 print(">>> Signed in.\n")
 goto(page, "https://github.com/")
 meta = page.locator('meta[name="user-login"]')
 return meta.first.get_attribute("content") if meta.count() else None

def set_checkbox(page, repo, label, want, selector):
 # Select by id: get_by_label("Wikis") also matches a.
 box = page.locator(selector)
 if box.count() == 0:
 log(repo, f"'{label}' not found (skipped)")
 dump(page, repo, label.replace(" ", "_"))
 return
 box = box.first
 state = "on" if want else "off"
 if box.is_checked() == want:
 log(repo, f"'{label}' already {state}")
 return
 if args.dry_run:
 log(repo, f"would turn '{label}' {state}")
 return
 box.click()
 settle(page)
 log(repo, f"'{label}' -> {state}")

def fix_features(page, owner, repo):
 goto(page, f"https://github.com/{owner}/{repo}/settings")
 if "/settings" not in page.url:
 log(repo, "no access to settings (not yours?)")
 return
 if args.wiki == "off":
 set_checkbox(page, repo, "Wikis", False, "input#wiki-feature")
 else:
 set_checkbox(page, repo, "Wikis", True, "input#wiki-feature")
 set_checkbox(page, repo, "Restrict editing to collaborators only", True, "input#wiki-pusher-access")

def section(page, title):
 """The smallest block around `title` (heading or plain text) that contains a button."""
 return page.get_by_text(title, exact=True).first.locator("xpath=ancestor::*[.//button][1]")

def confirm_dialog(page):
 dlg = page.locator('[role="dialog"]:visible, dialog[open]')
 try:
 dlg.first.wait_for(timeout=2500)
 except PWTimeout:
 return
 btn = dlg.first.get_by_role("button", name="Enable").or_(
 dlg.first.get_by_role("button", name="Confirm")).first
 if btn.count():
 btn.click()
 settle(page)

def click_enable(page, repo, title):
 """Returns True if the feature is (now) enabled."""
 if page.get_by_text(title, exact=True).count() == 0:
 log(repo, f"'{title}' not on page (skipped)")
 dump(page, repo, title.replace(" ", "_"))
 return False
 enable = section(page, title).get_by_role("button", name="Enable", exact=True)
 if enable.count() == 0:
 log(repo, f"{title} already enabled")
 return True
 if args.dry_run:
 log(repo, f"would enable {title}")
 return False
 enable.first.click()
 confirm_dialog(page)
 settle(page)
 log(repo, f"{title} -> enabled")
 return True

def flip_toggle(page, repo, label, depends_on_previous=False):
 row = page.locator("div, li").filter(has_text=label).filter(
 has=page.locator("button[aria-pressed]")).last
 if row.count() == 0:
 if depends_on_previous:
 log(repo, f"{label} appears once Secret Protection is on (applied in the real run)")
 else:
 log(repo, f"'{label}' toggle not found (skipped)")
 dump(page, repo, label.replace(" ", "_"))
 return
 toggle = row.locator("button[aria-pressed]").first
 if toggle.get_attribute("aria-pressed") == "true":
 log(repo, f"{label} already on")
 return
 if args.dry_run:
 log(repo, f"would turn {label} on")
 return
 toggle.click()
 confirm_dialog(page)
 settle(page)
 log(repo, f"{label} -> on")

def fix_security(page, owner, repo):
 url = f"https://github.com/{owner}/{repo}/settings/security_analysis"
 goto(page, url)
 if not args.no_pvr:
 click_enable(page, repo, "Private vulnerability reporting")
 sp_on = click_enable(page, repo, "Secret Protection")
 goto(page, url) # fresh page so the Push protection toggle shows up
 flip_toggle(page, repo, "Push protection", depends_on_previous=not sp_on)

def main():
 global args
 args = parse_args()
 browser = find_browser()
 print("Browser:", browser or "Playwright's Chromium")
 with sync_playwright() as pw:
 opts = dict(headless=False, viewport=None, chromium_sandbox=True)
 if browser:
 opts["executable_path"] = browser
 try:
 ctx = pw.chromium.launch_persistent_context(str(PROFILE), **opts)
 except Exception:
 if browser:
 raise
 sys.exit("No browser found. Pass --browser PATH, or run: uv run --with playwright playwright install chromium")
 page = ctx.pages[0] if ctx.pages else ctx.new_page()
 me = ensure_login(page)
 owner = args.owner or me
 if not owner:
 sys.exit("Couldn't detect your username; pass --owner NAME.")
 repos = list_repos(owner)
 print(f"{owner}: {len(repos)} public repos")
 failed = []
 for repo in repos:
 print(f"\n== {repo}")
 try:
 fix_features(page, owner, repo)
 fix_security(page, owner, repo)
 except Exception as e: # keep going with the next repo
 log(repo, f"ERROR: {str(e).splitlines()[0]}")
 failed.append(repo)
 print("\nDone." + (f" Check these by hand: {', '.join(failed)}" if failed else ""))
 if args.dry_run:
 print("(dry run: nothing was changed)")
 print(f"Tip: delete {PROFILE} when finished so no signed-in session is left behind.")
 input("Press Enter to close the browser...")
 ctx.close()

if __name__ == "__main__":
 main()

# alam00000/bentopdf-hyper-compress

## 评论（1/1）

> **bestony** · 2026-11-08T23:07:18.000Z　
> Reading the local files of the browser is still not good enough. A better way to implement it might be through Browser Javascript, so users just need to press F12 to open Console, paste, and run.

## 关联链接

- https://api.github.com/users/{owner}/repos?per_page=100&type=owner
- https://docs.astral.sh/uv/
- https://github.com
- https://github.com/
- https://github.com/login
- https://github.com/{owner}/{repo}/settings
- https://github.com/{owner}/{repo}/settings/security_analysis

## 导航

- 项目页：[[10-项目/gist.github.com_8c19709b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
