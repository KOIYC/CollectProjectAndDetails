---
type: "corpus"
item_id: "8a9fd97b1b95b95f"
title: "Show HN: Web server that lets you build iOS & Android offline apps like BitChat"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49900344"
project_url: "https://github.com/Qbix/webserver/tree/main"
author: "EGreg"
published_at: "2026-09-29T20:53:28Z"
captured_at: "2026-09-30T18:57:07+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-30"
pub_day: "2026-09-29"
tags:
  - 语料
  - hn_show
  - author_EGreg
  - story_49900344
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Web server that lets you build iOS & Android offline apps like BitChat

> [!info] 一句话导读
> Published: 2026-07-20

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49900344>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：EGreg　|　发布：2026-09-29T20:53:28Z
> 项目链接：<https://github.com/Qbix/webserver/tree/main>
> 采集：2026-09-30T18:57:07+08:00　|　id：`8a9fd97b1b95b95f`

## 正文

Published: 2026-07-20
Author: Qbix

GitHub - Qbix/webserver: Pure-PHP Web Server. No NGinX or PHP-FPM needed. Handle over 100x more traffic instead! · GitHub

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| .github/ workflows | .github/ workflows | | |
| bin | bin | | |
| docs | docs | | |
| examples | examples | | |
| mobile | mobile | | |
| service | service | | |
| src | src | | |
| tests | tests | | |
| web | web | | |
| .gitignore | .gitignore | | |
| COMPATIBILITY.md | COMPATIBILITY.md | | |
| LICENSE | LICENSE | | |
| README.md | README.md | | |
| RELEASE_NOTES.md | RELEASE_NOTES.md | | |
| build-app.php | build-app.php | | |
| build-binary.sh | build-binary.sh | | |
| build-phar.php | build-phar.php | | |
| composer.json | composer.json | | |
| plan.md | plan.md | | |
| qbixserver.php | qbixserver.php | | |
| site-index.html | site-index.html | | |
| View all files | | | |

# ⚡ Qbix Server v2

https://qbixserver.com is an all-in-one server that handles everything for you. Drop files in folders. Get real-time applications that can handle millions of users. Produce and distribute standalone binaries that run on Linux, Mac, Windows, and now iOS and Android too. Qbix Server v2 lets you build secure decentralized apps that can even work offline, over WiFi and Bluetooth.

When serving millions of people, safety becomes very important. Learn why the server is written in PHP. Today's PHP ecosystem has also produced thousands of useful web frameworks including OwnCloud, WordPress, Magento, Drupal, Symfony, Laravel, and more. Qbix Server can run them all, unmodified. It also gives you a dashboard and visual control panel to manage all your apps, domains, certificates, etc. in one place.

### What it replaces

| | nginx + php-fpm | Qbix Server |
| --- | --- | --- |
| 💾 Memory per worker | 30–60MB (duplicated) | ~120KB (COW, measured) |
| 👥 Concurrent PHP (1GB) | ~24 workers | ~5,000 (typical) |
| 🔒 Isolation | Statics leak between requests | OS-enforced: separate address space per request |
| 🚀 Throughput (I/O, same RAM) | 78 req/s (fpm/Swoole 4w) | 1,060 req/s (100w) |
| 🌐 WebSocket | Needs a separate server | Built in, same port |
| 🖼️ Image resize | Needs image_filter module + config | `?w=300` on any image URL, auto AVIF/WebP |
| 🔗 Peer-to-peer | Not possible | Encrypted mesh over BLE + Wi-Fi |
| 📱 Mobile | Not possible | iOS + Android with background persistence |
| 🔄 Data sync | Not possible | Bloom filters + prolly trees between peers |
| ⚙️ Setup | nginx + fpm pools + sockets | `php qbixserver.php` |

See BENCHMARKS.md for full methodology and reset.md for what gets restored between requests.

### What a "real-time PHP app" used to require

nginx for reverse proxy and static files. php-fpm to run PHP. Node.js for a Socket.IO server. Redis for pub/sub between fpm and Node. supervisor to keep it all running. Docker to make it deployable. Six processes, three languages, two runtimes.

Qbix Server replaces all six with one process. HTTP, WebSocket (with Socket.IO protocol), SSE, sessions, uploads, static files, image resizing, .htaccess — same port, same file. No Redis, no Node, no pub/sub glue.

In v2.0, the same server also discovers nearby devices over Bluetooth and Wi-Fi, establishes ECDH-encrypted sessions, routes messages through multi-hop mesh, and synchronizes data peer-to-peer with Bloom filters and prolly trees. It runs on iOS and Android alongside Linux, macOS, and Windows. A classroom of phones running the same PHP app, syncing data with no internet, no central server — one `php qbixserver.php`.

You can also package your entire app — code, assets, SQLite database — into a single binary and distribute it as a single file. Double-click on Windows, `./myapp --open` on Mac or Linux, the browser opens and the app is there. No PHP to install, no web server to configure, no database to set up. How it works →

## 📑 Table of Contents

- Documentation
- Quick Start
- Use With Your Existing Codebase
- Performance
- vs FrankenPHP and Swoole
- Features
- Server Headers
- For PHP Developers
- Configuration
- Platform Support
- Three Ways to Run
- Building
- Examples
- Migrating from another server
- Single-Binary Distribution
- Mesh Networking
- Mobile
- With Qbix Platform
- Architecture
- HTTP/2 Support
- Why PHP
- License

## Documentation

| | Topic | What it covers |
| --- | --- | --- |
| 🏎️ | Why Not php-fpm? | COW memory model, comparison with Swoole and FrankenPHP |
| 🔒 | Server Headers | Cache-Control, X-Cache-Tree, X-Accel-Redirect, ETag |
| 🗂️ | Static Files | ETag/304, compression, precompression cache |
| 🖼️ | Image Processing | Resize with `?w=`, AVIF/WebP negotiation, Save-Data, disk cache, limits |
| 🌐 | HTTP | Fork-per-request mode, request lifecycle |
| 🔌 | WebSocket & Rooms | Process per connection, rooms, Socket.IO, SSE, chat example |
| 🛤️ | Routing | Clean URLs, .htaccess, DirectoryIndex |
| 📂 | PHP Framework | The micro-framework: handlers, events, Q classes |
| ⚙️ | Configuration | JSON config, CLI options, presets |
| 📦 | Running & Building | Source, phar, binary. Building static binaries. Requirements |
| 📀 | Binaries & Signing | Pack apps, manage like zip, ECDSA M-of-N signing, Rekor, platform signing |
| 🏗️ | Architecture | Persistent workers, COW, execution model, mental model, benchmarks |
| 📊 | Dashboard & Panel | Live stats, control panel tabs |
| 🚀 | Deploy & Federation | Rsync deploy, cluster replication, inter-server trust |
| 🔍 | API Discovery | OpenAPI, MCP, qbix.json, HTTP/2 |
| 🧩 | Compatibility | Running Laravel, Symfony, WordPress, Drupal unmodified: what gets rewritten and why |
| 🏢 | Frameworks | All 13 supported frameworks, presets, boot adapters |
| 🧬 | --app Mode & SAPI Internals | SAPI emulation, class ownership, test suites |
| 🌐 | Mesh Protocol | Identity, handshake, routing, encryption |
| 🔄 | Data Sync | Bloom filters, prolly trees, conflict resolution, current limits |
| 📱 | iOS & Android | Running on phones, transports, permissions |
| 📈 | Benchmarks | Full methodology and numbers |
| 🔄 | State Reset | What gets restored between requests |
| 🔀 | Migrate from nginx | Server blocks, try_files, proxy_pass, gzip |
| 🔀 | Migrate from Apache | .htaccess unchanged, VirtualHost mapping |
| 🔀 | Migrate from Caddy | Automatic HTTPS, on-demand TLS → autohost |
| ✅ | Test Results | 140 end-to-end tests |
| 🗺️ | Roadmap | What's next |
| 📄 | License | MIT |

## Quick Start

```
git clone https://github.com/Qbix/webserver
cd webserver
php qbixserver.php
```

Or grab a self-contained binary (PHP bundled, nothing to install):

```
# Linux
curl -LO https://github.com/Qbix/webserver/releases/latest/download/qbixserver-linux-x86_64
chmod +x qbixserver-linux-x86_64
./qbixserver-linux-x86_64

# macOS (Apple Silicon)
curl -LO https://github.com/Qbix/webserver/releases/latest/download/qbixserver-macos-arm64
chmod +x qbixserver-macos-arm64
./qbixserver-macos-arm64

# Windows
curl -LO https://github.com/Qbix/webserver/releases/latest/download/qbixserver-windows-x64.exe
qbixserver-windows-x64.exe
```

Or use the PHAR (single file, no extensions to compile):

```
php bin/qbixserver.phar --root=./public --port=8080
```

## Use With Your Existing Codebase

If you already have a PHP app running on nginx + php-fpm, switching is one command. The server reads your `.htaccess`, rewrites URLs to your front controller, and runs your code with 27 functions shimmed so static variables, sessions, and headers work correctly between requests.

Laravel:

```
cd my-laravel-app
php /path/to/qbixserver.php --root=public --preset=laravel --port=8080
```

Symfony:

```
cd my-symfony-app
php /path/to/qbixserver.php --root=public --preset=symfony --port=8080
```

WordPress:

```
cd my-wordpress-site
php /path/to/qbixserver.php --root=. --preset=wordpress --port=8080
```

Drupal:

```
cd my-drupal-site
php /path/to/qbixserver.php --root=web --preset=drupal --port=8080
```

Any PHP app with a front controller:

```
php /path/to/qbixserver.php --root=public --port=8080
```

If the root directory has an `index.php`, all clean URLs automatically route to it (the same behavior as `try_files $uri $uri/ /index.php` in nginx). If there's a `.htaccess`, its `RewriteRule` and `RewriteCond` directives are applied.

### What `--preset` does

Each preset sets framework-appropriate defaults: the front controller path, upload limits, memory limits, and session GC settings. You can override any of these in a JSON config file. The preset is a convenience — without it, the server still works if your `.htaccess` handles routing.

### What gets shimmed

The server intercepts 27 PHP functions (`header()`, `session_start()`, `setcookie()`, `ini_set()`, etc.) via source transformation at include time. Your code calls `header()` and it works — the server captures it. Between requests, all static properties are restored from a snapshot in 0.03ms. See Compatibility for the full list.

### Supported Frameworks

Qbix Server ships presets and boot adapters for 13 frameworks. Every framework runs unmodified — no plugins or code changes needed.

| Framework | Preset | Speedup vs php-builtin |
| --- | --- | --- |
| Laravel | `--preset=laravel` | 3.4× |
| Symfony | `--preset=symfony` | — |
| WordPress | `--preset=wordpress` | — |
| Drupal | `--preset=drupal` | 4.0× |
| CakePHP | `--preset=cakephp` | 2.0× |
| CodeIgniter | `--preset=codeigniter` | — |
| Yii | `--preset=yii` | — |
| Mezzio | `--preset=mezzio` | 1.5× |
| Slim | `--preset=slim` | — |
| Joomla | `--preset=joomla` | — |
| Magento | `--preset=magento` | — |
| Nextcloud | `--preset=nextcloud` | — |
| ownCloud | `--preset=owncloud` | — |

"—" = not benchmarked or no significant speedup on CPU-bound "hello world". Real-world I/O-bound workloads see much larger gains from the COW memory model (see Benchmarks).

See FRAMEWORKS.md for full details, preset reference, and boot adapter documentation. See BENCHMARKS.md for full benchmark methodology and per-framework numbers.

### What to watch for

Most apps work immediately. A few things to be aware of:

- `define()` constants persist between requests in persistent workers. If a plugin defines a constant conditionally, the second request sees it already defined. Rare in practice.
- `stream_wrapper_register()` persists. Uncommon outside testing frameworks.
- Long-running scripts (migrations, imports) should use `--workers=1` or run via CLI directly.
- Extensions that store C-level state (e.g. some custom PECL modules) won't reset between requests. Standard extensions (PDO, curl, mbstring) are fine.

## 📊 Performance

Benchmarked against nginx on the same single-core container, PHP 8.3, Ubuntu 24. 13KB static file, best-of-3 runs, warm caches.

| Scenario | nginx | Qbix Server | Ratio |
| --- | --- | --- | --- |
| Sequential (c=1) | 10,154 req/s | 6,376 req/s | 63% |
| Concurrent (c=10) | 12,300 req/s | 6,876 req/s | 56% |
| High concurrency (c=50) | 12,919 req/s | 7,253 req/s | 56% |
| Keep-alive (c=10) | 26,858 req/s | 19,700 req/s | 73% |
| Keep-alive (c=50) | 30,158 req/s | 20,369 req/s | 67% |

Zero failed requests across 50,000+ requests at concurrency 50. Server never crashed.

> For context: 20K req/s means the server handles 1,000 simultaneous page loads per second (assuming ~20 static assets per page), all from a single PHP process.

For PHP application workloads, the story flips — the memory and bootstrap savings matter more than static file throughput:

- nginx + php-fpm: 0.1ms static file + 30ms PHP bootstrap + 5ms actual work = 35ms
- Qbix Server: 0.15ms static file + 0ms bootstrap + 5ms actual work = 5ms

See BENCHMARKS.md for full methodology, and the framework benchmarks for per-framework numbers.

> 💡 You can always put nginx, a reverse proxy, or a CDN (Cloudflare, CloudFront) in front of this for faster HTTPS and edge caching. Qbix Server handles the PHP execution, access control, and intelligent caching behind it.

## ⚖️ vs FrankenPHP and Swoole

If you're looking beyond php-fpm, you've probably seen FrankenPHP and Swoole. Here's how they compare:

| | FrankenPHP | Swoole | Qbix Server |
| --- | --- | --- | --- |
| Language | Go + C (embeds PHP) | C extension for PHP | Pure PHP |
| Install | Download Go binary or Docker | `pecl install swoole` (compiles C) | `php qbixserver.php` — nothing to install |
| Architecture | Worker mode (persistent) | Coroutine-based (persistent) | Shared-nothing with fork-after-preload |
| State leaks | ⚠️ Possible — workers persist between requests | ⚠️ Possible — must manage globals carefully | ✅ Impossible — each request gets a clean fork |
| PHP compatibility | Most code works, some edge cases | Many extensions incompatible, blocking I/O breaks coroutines | ✅ 100% — standard PHP, nothing unusual |
| Memory safety | Go runtime + PHP = complex interaction | C extension = segfault risk | PHP only = memory-safe by default |
| Access control | No X-Accel-Redirect equivalent | Manual implementation | ✅ Built-in X-Accel-Redirect |
| Component cache | No | No | ✅ X-Cache-Tree — sub-page invalidation |
| Early hints / 103 | ✅ Yes | No | Via amphp |
| HTTP/2 | ✅ Built-in (Caddy) | ✅ Built-in | ✅ Via amphp |
| WebSocket | Via Mercure | ✅ Built-in | ✅ Built-in |

### The shared-nothing advantage

FrankenPHP and Swoole keep PHP workers alive across requests. This is fast, but it means global state, static variables, database connections, and in-memory caches persist between unrelated requests. This causes subtle bugs:

```
// This leaks between requests in FrankenPHP/Swoole:
class UserService {
    private static ?User $cached = null;
    
    public static function current(): User {
        if (!self::$cached) {
            self::$cached = User::fromSession();
        }
        return self::$cached; // Returns previous user's data!
    }
}
```

Every PHP framework, library, and snippet that uses static variables, singletons, or global state becomes a potential security hole. You have to audit everything.

Qbix Server avoids this entirely. Workers fork from a preloaded parent, so they inherit loaded classes and parsed config (read-only, shared via copy-on-write). But each request runs in its own process — when it's done, everything is gone. No state leaks. No audit needed. Your existing PHP code works exactly as it does on php-fpm.

### The "just PHP" advantage

FrankenPHP requires Go tooling to build or a pre-built binary that bundles Caddy. Swoole requires compiling a C extension, which can conflict with other extensions and doesn't work on all hosting environments.

Qbix Server is a PHP file. If you can run `php -v`, you can run the server. It uses standard PHP extensions (`sockets`, `pcntl`) that come pre-installed on most systems. There's no compilation step, no foreign runtime, no binary compatibility issues.

```
# FrankenPHP
docker pull dunglas/frankenphp  # 150MB+ image, or build from Go source

# Swoole
pecl install swoole             # compiles C, may fail on some systems
# Then edit php.ini, restart php...

# Qbix Server
php qbixserver.php --port=8080  # done
```

### When to choose what

Choose FrankenPHP if you want Caddy's ecosystem (automatic HTTPS, HTTP/3) and don't mind Go as a dependency. Good for Laravel projects that already use Octane.

Choose Swoole if you need coroutines for high-concurrency I/O (thousands of simultaneous HTTP client requests, database queries). Good for async-heavy microservices.

Choose Qbix Server if you want shared-nothing safety, zero-install deployment, access-controlled file serving, component-level cache invalidation, and full compatibility with existing PHP code. Good for apps that serve pages (not just APIs), need fine-grained caching, and want the simplest possible deployment.

## ✨ Features

| Category | What you get |
| --- | --- |
| Static files | ETag, 304 Not Modified, Last-Modified, MIME type detection, in-memory response cache |
| Keep-alive | HTTP/1.0 and 1.1, TCP_NODELAY, configurable limits |
| HTTP/2 | Via amphp — multiplexed streams, header compression, TLS (optional) |
| PHP execution | `.php` files in document root run in-process or via pre-fork worker pool |
| Compression | On-the-fly gzip/brotli + pre-compressed `.gz`/`.br` siblings |
| WebSocket | RFC 6455 upgrade on any path |
| Dashboard | Live stats at `/Q/dashboard` — request rates, memory, status codes |
| Health check | JSON at `/Q/health` — for load balancers and monitoring |
| Control panel | Password-protected at `/Q/panel` — manage apps and scripts |
| Rate limiting | Per-IP with configurable windows and burst limits |
| Security | Path traversal blocked, dotfiles blocked, 431 for oversized headers, 400 for malformed requests |
| Graceful shutdown | SIGTERM/SIGINT drain in-flight requests before closing |
| TLS | Optional HTTPS with auto-certbot or manual certs |
| Logging | Colored terminal output + file-based access logs |
| Access control | X-Accel-Redirect support — PHP enforces access, server serves the file |
| Component cache | X-Cache-Tree headers — invalidate parts of a page, not the whole thing |
| Image processing | Resize with `?w=`, automatic AVIF/WebP negotiation, disk cache |
| Framework presets | Built-in presets for 13 frameworks — Laravel, Symfony, WordPress, Drupal, and more |
| Mesh networking | Encrypted P2P over BLE + Wi-Fi with multi-hop routing |
| Data sync | Bloom filter + prolly tree sync between peers |

## 🔒 Server Headers — What Your PHP Can Send

Qbix Server understands special response headers from your PHP scripts. These are the same headers nginx understands (like `X-Accel-Redirect`) plus new ones for component-level caching. Your PHP sends them with `header()`, the server acts on them.

### Quick reference

| Header | What it does | Example |
| --- | --- | --- |
| `Cache-Control` | Server caches the response, serves without running PHP | `header('Cache-Control: public, max-age=300');` |
| `X-Accel-Redirect` | Server streams a file after PHP checks access | `header('X-Accel-Redirect: /uploads/private/doc.pdf');` |
| `X-Cache-Tree` | Registers page components with content hashes | `header('X-Cache-Tree: ' . json_encode([...]));` |
| `X-Cache-Deps` | Maps components to data dependency keys | `header('X-Cache-Deps: ' . json_encode([...]));` |
| `X-Cache-Invalidate` | Marks dependency keys as stale | `header('X-Cache-Invalidate: ' . json_encode([...]));` |
| `X-Cache-Stale` | Marks specific components as needing re-render | `header('X-Cache-Stale: feed,sidebar');` |

All of these are standard PHP `header()` calls. No SDK, no framework needed. The server strips them before sending the response to the client.

### Access-controlled static files

With a typical server, your uploaded files sit at public URLs. Anyone with the link can access them — and share the link with others. The usual workaround is "unguessable" URLs, which are just security through obscurity.

`X-Accel-Redirect` lets your PHP check access, then tells the server to serve the file directly — fast, streamed, with no public URL exposed:

```
<?php
// web/download.php — access-controlled file serving
session_start();

$fileId = $_GET['id'] ?? '';
$userId = $_SESSION['user_id'] ?? null;

// Your access control logic
if (!$userId || !userCanAccess($userId, $fileId)) {
    http_response_code(403);
    echo 'Access denied';
    exit;
}

// Tell the server to serve the file directly.
// The client never sees the real path.
header("X-Accel-Redirect: /uploads/private/{$fileId}");
header("Content-Disposition: attachment; filename=\"document.pdf\"");

// The server takes over from here — streams the file
// with correct Content-Type, ETag, compression, etc.
// Your PHP process is already done.
```

No public URL for the file. No redirect the user can bookmark. The server streams the file after your PHP has verified access and exited.

### Component-level cache invalidation

Most caching systems cache whole pages. When anything changes, you throw away the entire page and re-render everything. Qbix Server can cache individual components and only re-render what changed.

Step 1: Register components when rendering a page

```
<?php
// web/community.php — a page with three components

$feedHtml    = renderFeed($communityId);
$sidebarHtml = renderSidebar($communityId);
$membersHtml = renderMembers($communityId);

// Tell the server about the component tree and what data each depends on
header('X-Cache-Tree: ' . json_encode([
    'l' => [
        'feed'    => md5($feedHtml),
        'sidebar' => md5($sidebarHtml),
        'members' => md5($membersHtml),
    ]
]));

header('X-Cache-Deps: ' . json_encode([
    'feed'    => ["community/{$communityId}/feed"],
    'sidebar' => ["community/{$communityId}/about"],
    'members' => ["community/{$communityId}/participants"],
]));

header('Cache-Control: public, max-age=300');
echo $feedHtml . $sidebarHtml . $membersHtml;
```

Step 2: Invalidate when data changes

```
<?php
// web/post.php — user posts to the feed
saveNewPost($communityId, $content);

// Tell the server which dependency key changed
header('X-Cache-Invalidate: ' . json_encode([
    "community/{$communityId}/feed"
]));

// The server walks its dependency graph:
//   community/123/feed → page /community/123 component 'feed'
// Only 'feed' is stale. Sidebar, members = still cached.
// Next request re-renders only the feed component.

echo json_encode(['ok' => true]);
```

The server maintains a Merkle tree of component hashes. When a dependency key is invalidated, it walks the tree to find exactly which components on which pages are affected. Everything else is served from the in-memory cache.

## 📂 For PHP Developers — The Micro-Framework

Qbix Server isn't just a static file server with PHP bolted on. It's a micro-framework where you drop files into conventional directories and things just work — classes autoload, events fire handlers, views render templates. No configuration needed for the basics.

### Project layout

```
myproject/
├── qbixserver.php              ← server entry point (or use the PHAR)
├── config/
│   └── server.json             ← server + app configuration
├── web/                        ← document root (publicly accessible)
│   ├── index.html              ← static files served directly
│   ├── style.css
│   ├── api.php                 ← PHP scripts executed on request
│   └── uploads/
├── classes/                    ← your PHP classes (autoloaded when first used)
│   ├── MyApp/
│   │   ├── User.php            ← MyApp\User or MyApp_User
│   │   ├── Feed.php
│   │   └── Auth.php
│   └── vendor/
│       └── autoload.php        ← Composer autoloader (optional)
├── handlers/                   ← event handlers (loaded on demand)
│   └── MyApp/
│       └── feed/
│           ├── post.php        ← handles "MyApp/feed/post" event
│           └── validate.php    ← handles "MyApp/feed/validate" event
└── views/                      ← PHP templates for Q::view()
    └── MyApp/
        └── feed/
            ├── page.php
            └── item.php

```

Only `web/` is accessible via HTTP. Everything else is server-side only.

Your PHP scripts don't need to `require` or `include` anything. The server has already loaded the `Q` class, the autoloader, and the event system before your script runs. Classes from `classes/`, events via `Q::event()`, views via `Q::view()` — all available immediately:

```
<?php
// web/api.php — no require, no include, no bootstrap
use MyApp\User;

$user = User::find($_GET['id']);
$feed = Q::event('MyApp/feed/get', ['userId' => $user->id]);

header('Content-Type: application/json');
echo json_encode($feed);
```

### The `Q` class — available in every script

| Method | What it does |
| --- | --- |
| `Q::event($name, $params)` | Fire an event — runs the handler from `handlers/` |
| `Q::canHandle($name)` | Check if a handler exists for an event |
| `Q::view($name, $params)` | Render a PHP template from `views/` |
| `Q::ifset($arr, 'key1', 'key2', $default)` | Safe nested array/object access without isset chains |
| `Q::getObject($data, ['path', 'to', 'key'], $default)` | Deep access into nested arrays/objects |
| `Q::setObject(['path', 'to', 'key'], $value, $data)` | Deep set into nested arrays, creating intermediates |
| `Q::json_encode($value)` | `json_encode` with unescaped slashes |
| `Q::json_decode($json, true)` | `json_decode` wrapper |
| `Q_Config::get('section', 'key', $default)` | Read from `config/server.json` |
| `Q_Config::set('section', 'key', $value)` | Set a config value at runtime |
| `Q_Config::expect('section', 'key')` | Read config or throw if missing |

### Handlers — event-driven dispatch

Drop a file in `handlers/` and it's available as an event:

```
<?php
// handlers/MyApp/feed/post.php
function MyApp_feed_post(&$params, &$result) {
    $title = $params['title'] ?? 'Untitled';
    $userId = $params['userId'] ?? null;
    $id = saveFeedPost($userId, $title);
    $result = ['id' => $id, 'title' => $title, 'saved' => true];
    return $result;
}
```

```
<?php
// web/api.php — fire it from anywhere
$result = Q::event('MyApp/feed/post', [
    'title'  => $_POST['title'],
    'userId' => $_SESSION['user_id'],
]);
header('Content-Type: application/json');
echo json_encode($result);
```

The handler file is `include`'d the first time the event fires, then the function stays in memory. If the event never fires, the file is never loaded.

Before/after hooks via config — useful for validation, logging, access control:

```
{
    "Q": {
        "handlersBeforeEvent": {
            "MyApp/feed/post": ["MyApp/feed/validate"]
        },
        "handlersAfterEvent": {
            "MyApp/feed/post": ["MyApp/feed/notify"]
        }
    }
}
```

Any before hook returning `false` stops the chain. Handlers can also be URLs — the server POSTs event parameters as JSON to remote endpoints, giving you webhooks built into the event system.

### The philosophy

| | Loaded when | Lives in | Purpose |
| --- | --- | --- | --- |
| Classes | Startup (preloaded) | `classes/` | Models, services, utilities — your core code |
| Handlers | First event fire (on demand) | `handlers/` | Actions, hooks, webhooks — code that responds to events |
| Views | When rendered | `views/` | Templates — HTML with PHP |
| Scripts | When requested via HTTP | `web/` | Entry points — the "controller" layer |
| Config | Startup | `config/` | Settings, handler hooks, preload lists |

Classes are eager. Handlers are lazy. Scripts are per-request. Views are on-demand. This gives you the right loading strategy for each kind of code without thinking about it — just put files in the right directory.

When your project outgrows the micro-framework and you need user accounts, real-time streams, access control, payments, or a plugin system, switch to `--app` mode and everything you've written keeps working. See With Qbix Platform.

## ⚙️ Configuration

Create `config/server.json` next to your `web/` directory, or pass `--config=path/to/config.json`:

```
{
    "Q": {
        "webserver": {
            "keepAlive": {
                "max": 100,
                "timeout": 15
            },
            "maxConnections": 1024,
            "fileCache": {
                "maxSize": 67108864,
                "maxFile": 1048576,
                "checkInterval": 1
            },
            "rateLimit": {
                "enabled": true,
                "requests": 100,
                "window": 60
            }
        }
    }
}
```

| Key | Default | What it does |
| --- | --- | --- |
| `keepAlive.max` | 100 | Max requests per keep-alive connection |
| `keepAlive.timeout` | 15 | Seconds before closing idle connection |
| `maxConnections` | 1024 | Max simultaneous connections |
| `fileCache.maxSize` | 64MB | Total memory for cached file responses |
| `fileCache.maxFile` | 1MB | Largest file to cache in memory |
| `fileCache.checkInterval` | 1 | Seconds between file modification checks |
| `rateLimit.enabled` | false | Enable per-IP rate limiting |
| `rateLimit.requests` | 100 | Requests per window |
| `rateLimit.window` | 60 | Window in seconds |

See Configuration for the full reference.

## Platform Support

| Platform | Workers | COW | Transport |
| --- | --- | --- | --- |
| Linux x86_64, aarch64 | pcntl_fork | Yes — 120KB per worker | TCP, mDNS |
| macOS Intel, Apple Silicon | pcntl_fork | Yes | TCP, mDNS |
| FreeBSD / OpenBSD / NetBSD | pcntl_fork | Yes | TCP, mDNS |
| Windows x64 | qbix_fork.dll (FFI) or php-cgi | Yes (FFI) / No (php-cgi) | TCP |
| iOS arm64 | NativePHP / php-ios | — | TCP, MultipeerConnectivity, BLE GATT |
| Android arm64 | Phphone / NativePHP | — | TCP, BLE GATT, NSD |

On Linux, macOS and BSD, the server runs thousands of COW-forked workers at ~120KB each. On Windows, the server ships `qbix_fork.dll` which uses `RtlCloneUserProcess` via PHP's FFI extension to give full COW fork semantics — same memory efficiency as POSIX platforms. If FFI or the DLL isn't available, the server falls back to `php-cgi` subprocesses (no COW, higher memory per worker, but fully functional). On iOS and Android, the PHP runtime is embedded in a native app shell; the TransportManager handles peer discovery and transport negotiation automatically.

PHP 8.6+ (epoll/kqueue): The server auto-detects PHP 8.6's native `Io\Poll` API and uses `epoll` on Linux or `kqueue` on macOS for event notification — no PECL extensions needed. On older PHP versions, the server uses `stream_select` (which works fine, just O(n) per tick instead of O(1)). Revolt is also supported if installed.

GitHub Actions CI builds and tests on Linux x86_64, Linux aarch64, macOS arm64, Windows x64, FreeBSD 14, plus experimental Android and iOS targets. 464 tests, 0 failures.

### Requirements

Linux / macOS (recommended):

- PHP 8.1 or later
- Extensions: `sockets`, `pcntl` (for signals + workers), `openssl` (for HTTPS)

```
# Check
php -m | grep -E 'sockets|pcntl|openssl'

# Install on Ubuntu/Debian
sudo apt install php-cli php-sockets
```

For the static binary: Nothing. The PHP runtime is included.

Windows: The server runs in single-threaded mode (`--workers=0` only) unless `qbix_fork.dll` + FFI is available. Static files, PHP scripts, WebSocket, caching, compression, access control — everything works. You lose fork-per-request isolation and signal-based graceful shutdown without `pcntl`. Good for development; for production use Linux or macOS (or WSL).

### 1. From source (needs PHP 8.1+)

```
php qbixserver.php --root=./web --port=8080
```

### 2. PHAR — single file (needs PHP)

```
php bin/qbixserver.phar --root=./web --port=8080

# Or make it executable
chmod +x bin/qbixserver.phar
./bin/qbixserver.phar --port=8080
```

### 3. Static binary — no PHP needed

```
# Download from GitHub Releases
chmod +x qbixserver-linux-x86_64
./qbixserver-linux-x86_64 --root=./web --port=8080
```

The binary bundles PHP 8.3 + extensions into a single ~15MB executable. Copy it to any Linux or macOS machine and run. No dependencies.

### Build the PHAR

```
php -d phar.readonly=0 build-phar.php
# Output: bin/qbixserver.phar
```

### Build the static binary

```
# With Docker (easiest):
./build-binary.sh --docker

# With static-php-cli installed locally:
./build-binary.sh

# Output: bin/qbixserver (~15MB)
```

The binary is built using static-php-cli, which compiles PHP + extensions into a statically linked binary.

GitHub Actions automatically builds binaries for Linux x86_64, Linux ARM64, macOS x86_64, and macOS Apple Silicon on every tagged release.

## Examples

Six example apps are included in `examples/`:

| App | What it demonstrates |
| --- | --- |
| todo | SQLite CRUD, REST API, static HTML |
| counter | SQLite persistence, GET/POST |
| chat | WebSocket rooms, Socket.IO, 8 handler files |
| stream | Server-Sent Events, AI token streaming |
| swarm | Q::event() dispatch, cluster replication |
| collab | Collaborative editing |

```
php qbixserver.php --root=examples/todo/web --port=8080
```

## Migrating from another server

Already running nginx, Apache, or Caddy? These guides show the config mapping:

- Migrating from nginx — server blocks, try_files, proxy_pass, gzip
- Migrating from Apache — .htaccess works unchanged, VirtualHost → domains config
- Migrating from Caddy — automatic HTTPS, on-demand TLS → autohost

## Single-Binary Distribution

Package your app into one executable file — PHP runtime, web server, and all your code. The binary includes SQLite auto-provisioning: if your app bundles a `.sqlite` file, the server copies it to the data directory on first run and writes the framework config to point at it. No external database needed.

Supported out of the box: Qbix (detects plugins, writes `local/app.json` with per-plugin prefixes), Laravel (`.env`), Symfony (`.env`), WordPress (`wp-config.php` + wp-sqlite-db), Craft CMS, and Drupal.

Sign binaries with ECDSA P-256 keys (M-of-N threshold), publish to Sigstore Rekor for independent verification, and customize by editing the binary as a zip file.

- Building and distributing binaries — pack, sign, verify, customize, platform code signing

## Mesh Networking

Every Qbix Server instance has a cryptographic identity (ECDSA P-256, same security model as Ethereum). When two servers discover each other — over Bluetooth, Wi-Fi, or TCP — they perform an ECDH handshake and establish an AES-256-GCM encrypted session. All traffic is encrypted end-to-end, even through relay nodes.

```
// Talk to a nearby server (transport is automatic)
$response = Q::handleUsingRemote('qbix-peer://' . $peerId . '/api/data');

// React to peers
Q_WebServer_Transport::onPeerOnline(function ($peer) {
    // Sync data, exchange messages, coordinate
});
```

Multi-hop routing extends range beyond direct connections. The router uses distance-vector routing with HELLO/BYE/HEARTBEAT propagation, TTL limits, and deduplication. Intermediate nodes relay encrypted payloads they cannot read.

Data sync runs automatically when peers connect: Bloom filter exchange identifies what's different, then only the missing records transfer. For large datasets (10,000+ records), the protocol switches to prolly tree comparison — a deterministic content-addressed tree where identical subtrees are skipped entirely.

See docs/Mesh.md for the full protocol specification, edge cases, and security analysis.

## Mobile

Qbix Server runs on iOS and Android as a native app. A Swift (iOS) or Kotlin (Android) shell starts the embedded PHP server on `127.0.0.1`, points a WebView at it, and handles peer-to-peer transport. The PHP process runs your Qbix app exactly as it would on a desktop or VPS — no Cordova, no Capacitor, no JavaScript bridge.

The native TransportManager discovers nearby peers over every available channel and picks the best transport automatically:

| Priority | Transport | Bandwidth | Platforms |
| --- | --- | --- | --- |
| 1 | TCP (LAN) | 100+ Mbps | iOS + Android |
| 2 | MultipeerConnectivity | 2–25 Mbps | iOS only |
| 3 | BLE GATT | ~2 Mbps | iOS + Android |

If Wi-Fi drops, traffic falls back to BLE seamlessly. The PHP server sees HTTP on localhost regardless of transport.

Background persistence: iOS uses a silent AVAudioEngine session (App Store precedent: PocketServer, BitChat). Android uses a Foreground Service with `START_STICKY`.

### Preparing a mobile project

In the control panel, select your app and click Prepare with the iOS or Android platform selected. This generates a native project scaffold under `apps/YourApp/mobile/ios/` or `apps/YourApp/mobile/android/` with all the Swift/Kotlin source files, manifest, build config, and a `Server/` (iOS) or `assets/` (Android) directory where you place the PHP binary or phar.

### Building for iOS

1. Get the `qbixserver-ios-arm64` micro binary from the CI release artifacts, or build it locally with static-php-cli. For Simulator testing, just place `qbixserver.phar` in the Server directory — PhpBridge falls back to the system PHP on macOS.
2. Generate the Xcode project: `cd apps/YourApp/mobile/ios && xcodegen generate`
3. Open the `.xcodeproj`, set your signing team, and build.

For distribution, archive in Xcode and upload to App Store Connect via the Organizer or `xcodebuild -exportArchive`. See mobile/iOS.md for the full walkthrough including signing, TestFlight, and App Store submission.

### Building for Android

1. Get the `qbixserver-android-arm64` micro binary from the CI release artifacts, or cross-compile it locally with static-php-cli and the Android NDK. For debug testing, `qbixserver.phar` also works.
2. Place the binary (or phar) in `app/src/main/assets/`.
3. Build: `cd apps/YourApp/mobile/android && ./gradlew assembleDebug` (or `bundleRelease` for Play Store).

For distribution, sign the release AAB and upload to the Google Play Console. See mobile/Android.md for the full walkthrough including keystore setup, signing, and Play Store submission.

### More details

- mobile/README.md — transport layer architecture, BLE GATT service definition, chunking protocol, platform requirements
- mobile/iOS.md — PhpBridge, xcodegen, background persistence, signing, TestFlight, App Store
- mobile/Android.md — PhpBridge, Gradle, Foreground Service, signing, Play Store

## 🔌 With Qbix Platform

Qbix Server is extracted from the Qbix Platform — a full-stack framework for building social apps with real-time streams, user management, and plugin architecture.

When you have a Qbix app, the server uses the full framework:

```
php qbixserver.php --app=/path/to/myapp --port=8080
```

In this mode:

- Requests route through `Q_Dispatcher` — the full Qbix event pipeline
- Plugins load automatically (Users, Streams, Assets, etc.)
- Clean URLs work (`/community/123` → module routing)
- Static files still use the fast path (no framework overhead)
- The dashboard shows Qbix-specific stats

The standalone mode (without `--app`) runs as a plain web server — no framework, no plugins. PHP files execute directly, static files serve from memory. Use this for simple sites, APIs, or any project that doesn't need the full Qbix stack.

See --app Mode & SAPI Internals for details.

## 🏗️ Architecture

```
                    ┌──────────────────┐
 HTTP request ────→ │  Event Loop      │ stream_select (zero deps)
                    │  (single thread) │ or amphp/revolt (optional)
                    └────────┬─────────┘
                             │
             ┌───────────────┼───────────────┐
             │               │               │
        ┌────▼─────┐   ┌────▼─────┐   ┌────▼─────┐
        │  Static  │   │   PHP    │   │ WebSocket │
        │  Files   │   │ Dispatch │   │  Upgrade  │
        │          │   │          │   │           │
        │ In-memory│   │ In-proc  │   │ RFC 6455  │
        │ response │   │ or fork  │   │ frames    │
        │ cache    │   │ pool     │   │           │
        └──────────┘   └──────────┘   └──────────┘

```

Static files are served from an in-memory response cache. The full HTTP response (headers + body) is pre-built and sent in a single `fwrite()` call. The cache is mtime-validated with configurable check intervals. Combined with `TCP_NODELAY`, this delivers sub-millisecond response times.

PHP scripts run in-process (single-threaded, suitable for lightweight APIs) or in a pre-fork worker pool (`--workers=N`) for concurrent PHP execution. Workers are forked after class preloading, so they share the base memory footprint via copy-on-write pages.

The remaining gap versus nginx (55–73%) is inherent: nginx uses `sendfile()` (kernel-space file→socket copy), `epoll` (O(1) event notification), and compiled C. PHP's `stream_select` is `select(2)`, file serving goes through userspace, and every operation has interpreter overhead. Getting to 55–73% of C performance from pure interpreted PHP is about as good as it gets.

## 🌐 HTTP/2 Support

The built-in event loop uses `stream_select` — zero dependencies, works ever

# lost

## 关联链接

- https://github.com/Qbix/webserver
- https://github.com/Qbix/webserver/releases/latest/download/qbixserver-linux-x86_64
- https://github.com/Qbix/webserver/releases/latest/download/qbixserver-macos-arm64
- https://github.com/Qbix/webserver/releases/latest/download/qbixserver-windows-x64.exe
- https://qbixserver.com

## 导航

- 项目页：[[10-项目/github.com_64761782]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
