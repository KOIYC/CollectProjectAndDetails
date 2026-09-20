---
type: "corpus"
item_id: "2ca8cae4193f1e78"
title: "Show HN: A CLI that'll prevent you from half-assing Auth"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47954041"
project_url: "https://github.com/COD434/create-authenik8-app"
author: "TheSBD"
published_at: "2026-04-29T20:22:18Z"
captured_at: "2026-09-21T02:52:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_TheSBD
  - story_47954041
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: A CLI that'll prevent you from half-assing Auth

> [!info] 一句话导读
> COD434/create-authenik8-app

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47954041>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：TheSBD　|　发布：2026-04-29T20:22:18Z
> 项目链接：<https://github.com/COD434/create-authenik8-app>
> 采集：2026-09-21T02:52:32+08:00　|　id：`2ca8cae4193f1e78`

## 正文

# COD434/create-authenik8-app

A lightweight authentication infrastructure generator powered by an internal Identity Engine.

- Stars: 6
- Forks: 2
- Watchers: 6
- Open issues: 0
- License: MIT License
- Homepage: https://authenik8.vercel.app/
- Default branch: main
- Created: 2026-04-13T16:39:02Z

## Languages

- JavaScript
- TypeScript

## Topics

- auth-starter
- authentication
- boilerplate
- cli
- expressjs
- identity-management
- jwt
- nodejs
- rbac
- security
- typescript

## Top Contributors

- COD434 (197 contributions)
- dependabot[bot] (9 contributions)
- step-security-bot (1 contributions)
- alceops (1 contributions)

---

## README

█████╗ █████╗
██╔══██╗ ██╔══██╗
███████║ ╚█████╔╝
██╔══██║ ██╔══██╗
██║ ██║ ╚█████╔╝
╚═╝ ╚═╝ ╚════╝

 create-authenik8-app

 Launch secure, production-ready authentication in seconds.

 If this saved you time, a ⭐ helps a lot

 A lightweight authentication infrastructure generator powered by an internal Identity Engine.

NPM Downloads
OpenSSF Scorecard
CI
Coverage

subtitle

 Demo

**See a real generated example → create-authenik8-app-example**

---

## Usage

Create a new project:

```bash
npx create-authenik8-app my-app

cd my-app

npm run prisma:migrate

redis-server --daemonize yes

npm run dev
```
Your production-ready auth backend will be ready in 50 seconds.

---

## What you get instantly

• A fully working Express authentication starter with:

• JWT authentication (access + refresh tokens) with secure rotation

• Secure refresh token rotation

• Redis-based token storage

• Role-Based Access Control (RBAC)

• TypeScript setup

• Express server preconfigured

• Clean scalable folder structure

• .env file generated automatically

• Production extras (PM2 cluster, Helmet, rate limiting, memory guards)

---

## Why create-authenik8-app

Most developers waste days (or weeks) on:

• Manual JWT setup

• Secure refresh token handling

• Redis session configuration

• Proper access control

Authenik8 provides all of this out of the box so you can start building your API immediately.

---

## Requirements

• Node.js 18+

• Redis (required for refresh tokens & security features)

Redis (Local)
```
Bash

redis-server --daemonize yes
```

---

## Environment Variables

Generated automatically:

The CLI generates these automatically:

```
DATABASE_URL=file:./dev.db
JWT_SECRET=your-secret
REFRESH_SECRET=your-refresh-secret
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
```

For Full Auth (Password + OAuth), also set:

```bash
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
GOOGLE_REDIRECT_URI=http://localhost:3000/auth/google/callback
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret
GITHUB_REDIRECT_URI=http://localhost:3000/auth/github/callback
```

---

## RBAC Example

Example of a protected route:
```
app.get("/admin", auth.requireAdmin, (req, res) => {
  res.json({ message: "Admin only route" });
});
```

---

### Testing

- Full test suite with ``80%`` coverage (actively improving)

- CI runs tests + coverage on every push and PR

---

## How It Works (Key Concept)

Authenik8 is not just another auth library.
It is an auth system generator.
At its core is the Identity Engine ``(authenik8-core)`` that treats authentication as an

# identity resolution problem:

• Unifies credentials (email/password) + OAuth providers

• Prevents duplicate identities

• Handles account linking intelligently

• Normalizes data across providers

This design makes future additions (MFA, WebAuthn, etc.) much cleaner.

---
## Powered by

authenik8-core (v1.0.38) identity & token engine(beta)

---

## How authenik8-core works in generated apps

Generated projects call:

```ts
const auth = await createAuthenik8({
  jwtSecret: requiredSecret("JWT_SECRET"),
  refreshSecret: requiredSecret("REFRESH_SECRET"),
  oauth: {
    google: {
      clientId: requiredEnv("GOOGLE_CLIENT_ID"),
      clientSecret: requiredEnv("GOOGLE_CLIENT_SECRET"),
      redirectUri: requiredEnv("GOOGLE_REDIRECT_URI"),
    },
    github: {
      clientId: requiredEnv("GITHUB_CLIENT_ID"),
      clientSecret: requiredEnv("GITHUB_CLIENT_SECRET"),
      redirectUri: requiredEnv("GITHUB_REDIRECT_URI"),
    },
  },
});
```

That factory returns one auth object used by the generated routes:

• `signToken(payload)` creates access tokens.

• `verifyToken(token)` verifies access tokens.

• `generateRefreshToken(payload)` creates stateful refresh tokens.

• `refreshToken(refreshToken)` rotates refresh tokens and returns a new access/refresh pair.

• `helmet`, `rateLimit`, and `ipWhitelist` are Express middleware.

• `requireAdmin` protects admin-only routes by checking `role: "admin"`.

• `oauth.google` and `oauth.github` provide redirect and callback handlers.

• `issueTokensFromProfile(profile)` turns a verified OAuth profile into app tokens through the Identity Engine.

### Redis-backed token lifecycle

Authenik8-core intentionally makes JWT auth stateful:

1. Access tokens are signed with `JWT_SECRET`.
2. Refresh tokens are signed with `REFRESH_SECRET` and include a unique `jti`.
3. The current valid refresh token is stored in Redis under `refresh: `.
4. Refresh calls acquire a Redis lock with `lock: `.
5. The submitted refresh token must match the Redis value.
6. A new access token and refresh token are issued.
7. The new refresh token atomically replaces the old one.
8. Reusing the old refresh token fails.

This is why Redis is required. It enables refresh-token replay protection, concurrent refresh protection, and server-side session control.

### OAuth identity resolution

OAuth is not handled as separate unrelated Passport-style strategies. Provider callbacks are normalized into this profile shape:

```ts
{
  email: "user@example.com",
  name: "User Name",
  provider: "google",
  providerId: "provider-user-id",
  email_verified: true
}
```

The Identity Engine then decides:

• Existing provider login: provider is already linked, so tokens are issued.

• New user creation: no matching identity exists, so a new user identity is created.

• Link required: an email match exists but policy requires explicit account linking.

• Link provider: an authenticated user links Google or GitHub to their existing account.

OAuth state is stored in Redis for five minutes under `oauth:state: `, and Redis-backed identity records use:

```text
oauth:v1:user:<userId>
oauth:v1:email:<email>
oauth:v1:provider:<provider>:<providerId>
```

### Security middleware

Generated apps use the middleware returned by core:

```ts
app.use(auth.helmet);
app.use(auth.rateLimit);
```

`helmet` applies secure HTTP headers. `rateLimit` is Redis-backed and defaults to 100 requests per 60 seconds with a 300-second block. `ipWhitelist` is available for stricter APIs and allows localhost by default.

### Common core errors

• `MissingTokenError`: no refresh token was sent.

• `InvalidTokenError`: refresh token is invalid, expired, reused, or replaced.

• `Concurrent refresh detected`: two refresh requests tried to rotate the same token at once.

• `OAuthError:Invalid or expired state`: OAuth callback state is missing from Redis.

• `OAuth profile email must be verified before issuing tokens`: provider email was not verified.

• `Provider already linked to another user`: account linking tried to attach an already-owned provider.

---

## Threat Model

Generated apps include a `THREAT_MODEL.md` file. It explains:

• what the generated app protects,

• what `authenik8-core` handles with Redis-backed token state,

• what threats remain your responsibility,

• and what must be configured before production.

Key protections include refresh-token replay detection, concurrent refresh locking, OAuth state validation, verified-email OAuth token issuance, Redis-backed rate limiting, secure headers, session tracking, and admin-route checks.

Key non-goals include frontend XSS protection, CSRF for cookie-based auth, object-level authorization, MFA/WebAuthn, password reset, provider dashboard security, and protection from leaked secrets.

Before production, replace generated secrets, keep Redis private, use HTTPS, review CORS, configure exact OAuth callback URLs, and add business-level authorization checks to your own routes.

---

## Production Enhancements

• PM2 cluster mode + auto-restart

• Memory usage guardrails

• Security middleware (Helmet, rate limiting, etc.)

---

## The Identity Engine

At the heart of Authenik8 is the **Identity Engine** , a unified authentication core built into `authenik8-core`.

---

### Why a dedicated Identity Engine?

Traditional auth systems treat login as separate, isolated flows:

• Email/password goes one way

• Google OAuth another way

• GitHub yet another

This leads to duplicate accounts, inconsistent data, fragile linking logic, and security gaps.

The **Identity Engine** solves this by treating authentication as an **identity resolution problem** instead of just credential validation.

---

### What the Identity Engine does

• **Unified Identity Resolution**
 It intelligently resolves any login method (credentials, OAuth, or future strategies) into a single, consistent user identity in your system.

• **Smart Account Linking**
 Automatically detects when a user already exists (via email or other signals) and offers secure linking instead of creating duplicates.

• **Profile Normalization**
 Converts provider-specific data (Google profile, GitHub profile, etc.) into your app’s clean, unified user schema.

• **Secure Token Lifecycle Management**
 Handles JWT access + refresh tokens with rotation, JTI-based replay protection, and Redis-backed stateful control.

- **Consistent Security Layer**
 Applies the same high-security rules (rate limiting, IP awareness, session controls) across all authentication methods.

---

### OAuth Through the Identity Engine

OAuth (Google, GitHub, and more coming) is **not** implemented as direct Passport.js-style routes. Instead:

1. The provider callback is received

2. The Identity Engine resolves/normalizes the profile

3. It decides: login existing user, link to existing account, or create new identity

4. Returns consistent tokens and user data

This design makes adding new providers or authentication methods much cleaner and more secure.

---

## Authenik8 vs Passport.js

| Aspect | **Authenik8** | **Passport.js** |
|---------------------------|----------------------------------------------------|------------------------------------------|
| **Purpose** | Full auth system generator | Authentication middleware |
| **Setup Time** | \~30 seconds (complete project) | Hours to days |
| **JWT + Refresh Tokens** | Secure rotation + replay protection built-in | Manual implementation required |
| **OAuth** | Unified via Identity Engine (smart linking) | Separate strategies per provider |
| **RBAC** | Built-in middleware | Not included |
| **Production Features** | PM2, Helmet, rate limiting, memory guards | None (you add them) |
| **Identity Management** | Centralized Identity Engine | None |
| **Flexibility** | Medium (opinionated & extensible) | Very high |
| **Best For** | Fast, secure, consistent backends | Maximum customization |

Passport.js is a great flexible tool, but it leaves you to build secure JWT, refresh logic, OAuth linking, and RBAC yourself.
Authenik8 gives you a complete, production-ready authentication system from day one.

---

### Benefits for you

• No more duplicate user headaches

• Consistent security behavior across all login methods

• Easier future-proofing (MFA, WebAuthn, enterprise SSO, etc.)

• Cleaner, more maintainable codebase in your generated project

The Identity Engine is what makes Authenik8 feel like a coherent **authentication system** rather than a collection of routes and middleware.

---

## Notes

• This generates a starter project, not a full framework

• Redis is mandatory for security features

• authenik8-core is closed-source for security reasons (implementation details)

---

## Roadmap

• Advanced RBAC (custom roles/permissions)

• webAuthn

• MFA

• Production presets

# hsaghir/looplet

## 关联链接

- http://localhost:3000/auth/github/callback
- http://localhost:3000/auth/google/callback
- https://authenik8.vercel.app/

## 导航

- 项目页：[[10-项目/github.com_f6dc3f28]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
