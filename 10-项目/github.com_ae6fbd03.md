---
type: "project"
title: "inokone/go-micro-saas"
project_url: "https://github.com/inokone/go-micro-saas"
first_seen: "2026-09-20T09:36:33+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - Go
  - topic:microsaas
lang: "en"
---

# inokone/go-micro-saas

> [!info] 一句话导读
> A template for building Micro-SAAS (Software as a Service) applications in Go. See our [feature list](/docs/featureset.md) for implemented and planned capabilit…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/inokone/go-micro-saas>
> 首次收录：2026-09-20T09:36:33+08:00
> 来源渠道：GitHub 新星仓库
> 标签：Go, topic:microsaas
> 最新指标：stars=0 · forks=0 · open_issues=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:24:14+08:00 | GitHub 新星仓库 | stars=0 · forks=0 · open_issues=0 | [[20-语料/posts/github_new/2026-09-20/ae6fbd03969a3cf1_inokone-go-micro-saas]] |
| 2026-09-20T09:36:33+08:00 | GitHub 新星仓库 | stars=0 · forks=0 · open_issues=0 | [[20-语料/posts/github_new/2026-09-20/ae6fbd03969a3cf1_inokone-go-micro-saas]] |

## 摘要正文

# Go-micro-SAAS  A template for building Micro-SAAS (Software as a Service) applications in Go. See our [feature list](/docs/featureset.md) for implemented and planned capabilities.  Before getting started, make sure to review and set up the required [third-party services and API keys](PREREQUISITES.md).  ## Development Setup  ### Prerequisites  Install the following tools:  ```sh # Install Go brew install go  # Install development tools go install github.com/swaggo/swag/cmd/swag@latest    # OpenAPI spec generator go install golang.org/x/tools/cmd/goimports@latest   # Code formatting tool go install github.com/golang-migrate/migrate/v4/cmd/migrate@latest  # Database migration tool  # Install linter brew tap golangci/tap brew install golangci/tap/golangci-lint ```  Note: On macOS, if `swag` command is not found, add `~/go/bin` to your PATH.  ### Development Workflow  1. Install dependencies:  ```sh go mod download ```  2. Generate OpenAPI specification:  ```sh ~/go/bin/swag init -g cmd/app.go -o api ```  3. Run tests:  ```sh go test -v ./... ```  4. Run linter:  ```sh golangci-lint run ```  ### Running Locally  1. Start Postgres database:  ```sh docker run --name postgres --env-file…
