---
type: "corpus"
item_id: "c9bf7619fb0ffa9d"
title: "Show HN: C# based Kubernetes Operator to deploy SurrealDB"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47945217"
project_url: "https://github.com/stevefan1999-personal/surrealdb-operator"
author: "stevefan1999"
published_at: "2026-04-29T07:35:18Z"
captured_at: "2026-09-21T02:52:40+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_stevefan1999
  - story_47945217
  - show_hn
metrics: {"points": 8, "comments": 2, "engagement_velocity": 8}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:174d"
---

# Show HN: C# based Kubernetes Operator to deploy SurrealDB

> [!info] 一句话导读
> stevefan1999-personal/surrealdb-operator

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47945217>
> 指标：点赞=8 · 评论=2 · engagement_velocity=8
> 作者：stevefan1999　|　发布：2026-04-29T07:35:18Z
> 项目链接：<https://github.com/stevefan1999-personal/surrealdb-operator>
> 采集：2026-09-21T02:52:40+08:00　|　id：`c9bf7619fb0ffa9d`

## 正文

# stevefan1999-personal/surrealdb-operator

- Stars: 4
- Forks: 0
- Watchers: 4
- Open issues: 0
- Default branch: master
- Created: 2026-04-29T05:39:20Z

## Languages

- C#
- Just

## Top Contributors

- stevefan1999-personal (248 contributions)

---

## README

# SurrealDB Operator

A Kubernetes operator for managing SurrealDB clusters, built with KubeOps (.NET 10).

## Overview

The SurrealDB Operator manages the full lifecycle of SurrealDB clusters on Kubernetes: deployment, storage backend provisioning (TiKV, RocksDB, or in-memory), scaling, TLS via cert-manager, and automated backups via Velero.

```
┌──────────────────────────────────────────────────────────┐
│                    Kubernetes Cluster                     │
│                                                          │
│  ┌───────────────────────┐   ┌────────────────────────┐  │
│  │  SurrealDB Operator   │   │   TiDB Operator (ext)  │  │
│  │  ┌─────────────────┐  │   │   Manages TiKV/PD      │  │
│  │  │  Cluster Ctrl   │──┼───►   StatefulSets         │  │
│  │  ├─────────────────┤  │   └────────────────────────┘  │
│  │  │  Backup Ctrl    │──┼──►                            │
│  │  └─────────────────┘  │   ┌────────────────────────┐  │
│  └───────────────────────┘   │   Velero (ext)         │  │
│                              │   Backup / Schedule /  │  │
│                              │   Restore / BSL        │  │
│  ┌───────────┐ ┌───────────┐ └────────────────────────┘  │
│  │ SurrealDB │ │ SurrealDB │                              │
│  │ Pod       │ │ Pod       │  tikv://pd:2379             │
│  └─────┬─────┘ └─────┬─────┘                             │
│        └──────┬───────┘                                  │
│  ┌────────────▼───────────────────────┐                  │
│  │  PD StatefulSet + TiKV StatefulSet │                  │
│  └────────────────────────────────────┘                  │
└──────────────────────────────────────────────────────────┘
```

## Features

- **Declarative SurrealDB clusters** — one CR manages Deployment, Service, and ServiceAccount
- **Multiple storage backends** — `memory` (dev/test), `tikv` (production), `rocksdb` (single-node)
- **TiKV coordination** — creates and manages `Cluster`, `PDGroup`, and `TiKVGroup` CRs via TiDB Operator v2
- **Horizontal scaling** — update `spec.surrealdb.replicas` to scale SurrealDB nodes
- **Automated backups** — Velero-backed `BackupDestination` / `Backup` / `BackupSchedule` / `Restore` CRDs with GFS retention and live data round-trip
- **Ingress support** — optional Ingress creation with TLS
- **Health status** — Kubernetes-standard conditions (`Ready`, `Synchronizing`, `Complete`, `DataVerified`, `Failed`)
- **Admission webhooks** — dependency pre-checks deny invalid resources at admission time (missing TiDB Operator, Velero, cert-manager, or secrets) with clear error messages
- **Multi-arch container** — `linux/amd64` and `linux/arm64` images published to GHCR

## Prerequisites

| Component | Version | Required? |
|-----------|---------|-----------|
| Kubernetes | 1.28+ | Yes |
| TiDB Operator | 2.0+ | For `tikv` backend |
| Velero | 1.18+ | For backups (`Backup` / `BackupSchedule` / `Restore`); install with `just velero-install` |
| cert-manager | 1.13+ | For managed TLS certificates (`spec.tls.issuerRef`) |
| just | 1.0+ | For development task runner |

## Installation

### 1. Install CRDs

```bash
kubectl apply -f https://github.com/stevefan1999-personal/surrealdb-operator/releases/latest/download/surrealdbcluster-crd.yaml
```

Or from a local clone:

```bash
kubectl apply -f deploy/crds/surrealdbcluster-crd.yaml
```

### 2. Deploy the operator

```bash
# Development (single replica, minimal resources)
kubectl apply -k deploy/kustomize/base

# Production (2 replicas, higher resource limits)
kubectl apply -k deploy/kustomize/overlays/production
```

### 3. Create a SurrealDbCluster

```bash
kubectl apply -f - <<'EOF'
apiVersion: surrealdb.io/v1alpha1
kind: SurrealDbCluster
metadata:
  name: my-cluster
  namespace: default
spec:
  surrealdb:
    replicas: 1
    image:
      repository: surrealdb/surrealdb
      tag: v3.0.5
    port: 8000
    logLevel: info
    auth:
      rootUsername: root
      rootPasswordSecretRef:
        name: surrealdb-root-password
        key: password
  storage:
    backend: memory
  service:
    type: ClusterIP
    port: 8000
EOF
```

## Usage Examples

### Production cluster with TiKV

```yaml
apiVersion: surrealdb.io/v1alpha1
kind: SurrealDbCluster
metadata:
  name: prod-cluster
  namespace: surrealdb
spec:
  surrealdb:
    replicas: 3
    image:
      repository: surrealdb/surrealdb
      tag: v3.0.5
    logLevel: warn
    auth:
      rootUsername: root
      rootPasswordSecretRef:
        name: surrealdb-root-password
        key: password
    resources:
      requests:
        cpu: 500m
        memory: 512Mi
      limits:
        cpu: "2"
        memory: 2Gi

  storage:
    backend: tikv
    tikv:
      pdReplicas: 3
      tikvReplicas: 3
      pdStorage:
        storageClassName: fast-ssd
        size: 1Gi
      tikvStorage:
        storageClassName: fast-ssd
        size: 50Gi

  service:
    type: ClusterIP
    port: 8000
```

Backups are configured separately via `BackupDestination` and `BackupSchedule` CRDs — see
Backup System below.

### Check cluster status

```bash
kubectl get surrealdbcluster my-cluster
kubectl describe surrealdbcluster my-cluster
```

## Configuration Reference

### `spec.surrealdb`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `replicas` | integer | `1` | Number of SurrealDB pods |
| `image.repository` | string | `surrealdb/surrealdb` | Container image repository |
| `image.tag` | string | `v3.0.5` | Container image tag |
| `image.pullPolicy` | string | `IfNotPresent` | Image pull policy |
| `port` | integer | `8000` | SurrealDB listen port |
| `logLevel` | string | `info` | Log level (`none`/`error`/`warn`/`info`/`debug`/`trace`) |
| `auth.rootUsername` | string | `root` | SurrealDB root username |
| `auth.rootPasswordSecretRef` | object | — | Secret reference for root password. **Optional** — if omitted, the operator auto-generates a `{cluster}-auth` Secret |
| `resources` | object | — | CPU/memory requests and limits |

#### Auto-generated root credentials

`spec.surrealdb.auth.rootPasswordSecretRef` is **optional**. When omitted, the operator
automatically creates a Secret named `{cluster}-auth` containing a cryptographically random
32-character password. This follows the same pattern used by CloudNativePG: credentials are
generated once on first reconcile and never rotated by the operator.

The auto-generated Secret has two keys:

| Key | Value |
|-----|-------|
| `username` | `root` |
| `password` | random 32-char alphanumeric string |

To retrieve the generated password:

```bash
kubectl get secret my-cluster-auth -o jsonpath='{.data.password}' | base64 -d
```

The secret name is also recorded in the cluster status for discovery:

```bash
kubectl get surrealdbcluster my-cluster -o jsonpath='{.status.auth.generatedSecretName}'
```

### `spec.storage`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `backend` | string | `memory` | Storage backend: `memory`, `tikv`, or `rocksdb` |
| `tikv.pdReplicas` | integer | `3` | PD replicas (TiKV backend) |
| `tikv.tikvReplicas` | integer | `3` | TiKV replicas |
| `tikv.pdStorage.size` | string | `1Gi` | PD persistent volume size |
| `tikv.tikvStorage.size` | string | `10Gi` | TiKV persistent volume size |
| `persistence.enabled` | boolean | `false` | Enable PVC for rocksdb backend |
| `persistence.size` | string | `10Gi` | PVC size for rocksdb backend |

### `spec.service`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `type` | string | `ClusterIP` | Kubernetes Service type: `ClusterIP`, `NodePort`, or `LoadBalancer` |
| `port` | integer | `8000` | Service port (forwards to SurrealDB container port) |

Use `ClusterIP` for internal access (expose via Ingress or `kubectl port-forward`).
Use `NodePort` for dev/test clusters without a load-balancer controller.
Use `LoadBalancer` on cloud clusters with a cloud load-balancer provider.

### `spec.ingress`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `enabled` | boolean | `false` | Create an Ingress resource |
| `className` | string | — | `ingressClassName` (e.g. `nginx`, `traefik`) |
| `hosts[*].host` | string | — | Virtual hostname |
| `hosts[*].paths[*].path` | string | `/` | URL path prefix |
| `hosts[*].paths[*].pathType` | string | `Prefix` | Path match type (`Prefix` or `Exact`) |
| `tls[*].secretName` | string | — | TLS Secret name for this host group |
| `tls[*].hosts` | array | — | Hostnames covered by the TLS certificate |

The operator updates the Ingress on every reconcile to reflect spec changes.
Both Service and Ingress carry owner references and are garbage-collected when the cluster is deleted.

### `spec.tls`

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `enabled` | boolean | `false` | Enable TLS for the SurrealDB port |
| `issuerRef.name` | string | — | Name of the cert-manager Issuer or ClusterIssuer |
| `issuerRef.kind` | string | `ClusterIssuer` | `Issuer` (namespaced) or `ClusterIssuer` (cluster-wide) |
| `secretName` | string | `{cluster}-tls` | Secret containing `tls.crt` / `tls.key`. Auto-generated by cert-manager when `issuerRef` is set; pre-existing in BYO mode |
| `dnsNames` | array | `[{cluster}-surrealdb.{ns}.svc.cluster.local]` | DNS SANs for the Certificate CR |

When `issuerRef` is set the operator creates a cert-manager `Certificate` CR owned by the cluster. When it is absent the operator expects the Secret to already exist (BYO mode).

When TLS is enabled, `--web-crt` and `--web-key` are automatically added to the SurrealDB start arguments and the TLS Secret is mounted at `/etc/surrealdb/tls/` in the pod.

When both TLS and Ingress are enabled with a `ClusterIssuer`, the annotation `cert-manager.io/cluster-issuer` is automatically added to the Ingress.

#### TLS setup example

```bash
# 1. Install cert-manager (if not already installed)
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml

# 2. Create a self-signed ClusterIssuer (for development / testing)
kubectl apply -f - <<'EOF'
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: selfsigned-issuer
spec:
  selfSigned: {}
EOF

# 3. Create a SurrealDbCluster with TLS enabled
kubectl apply -f - <<'EOF'
apiVersion: surrealdb.io/v1alpha1
kind: SurrealDbCluster
metadata:
  name: my-cluster
  namespace: default
spec:
  surrealdb:
    replicas: 1
  storage:
    backend: memory
  tls:
    enabled: true
    issuerRef:
      name: selfsigned-issuer
      kind: ClusterIssuer
EOF
```

### Backup System

Backups are configured via three independent CRDs rather than `spec.backup` on the cluster:

**`BackupDestination`** — wraps a Velero `BackupStorageLocation`:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `spec.provider` | string | `aws` | Velero object-store provider (works for any S3-compatible endpoint) |
| `spec.bucket` | string | — | S3 bucket name (required) |
| `spec.prefix` | string | — | Optional key prefix inside the bucket |
| `spec.config` | map | — | Provider config (e.g. `region`, `s3ForcePathStyle`, `s3Url`) |
| `spec.credentialSecretRef.name` | string | — | Secret containing the AWS-style credentials file |
| `spec.credentialSecretRef.key` | string | — | Key inside the Secret holding the credentials body |
| `spec.backupSyncPeriod` | string | `1m` | Velero BSL sync cadence (Go duration) |

**`Backup`** — a single backup instance:

| Field | Type | Description |
|-------|------|-------------|
| `spec.clusterRef.name` | string | Name of the `SurrealDbCluster` to back up |
| `spec.destinationRef.name` | string | Name of the `BackupDestination` |
| `spec.expiresAt` | datetime | When this backup expires (null = keep forever) |
| `spec.retentionPolicy` | string | `soft` (GFS-managed) or `hard` (kept until `expiresAt`) |
| `status.phase` | string | `Waiting` → `InProgress` → `Active` → `Expired` \| `Failed` |

**`BackupSchedule`** — cron-based trigger with GFS retention:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `spec.clusterRef.name` | string | — | `SurrealDbCluster` to back up |
| `spec.destinationRef.name` | string | — | Target `BackupDestination` |
| `spec.schedule` | string | `0 2 * * *` | Cron expression (UTC) |
| `spec.retain.last` | integer | — | Always keep last N backups |
| `spec.retain.daily` | integer | — | Keep one per day for N days |
| `spec.retain.weekly` | integer | — | Keep one per week for N weeks |
| `spec.retain.monthly` | integer | — | Keep one per month for N months |
| `spec.retain.yearly` | integer | — | Keep one per year for N years |
| `spec.hardRetentionLimit` | integer | `50` | Absolute max total Backup CRs; triggers GC |

See `samples/deploy/examples/10-backup-destination-s3.yaml`,
`11-backup-manual.yaml`, and
`12-backup-schedule-multi-tier.yaml` for complete examples.

### Admission Webhooks

The operator registers four `ValidatingAdmissionWebhook` endpoints that run **before** any
resource is admitted to the cluster. This provides fast, clear feedback when a prerequisite
is missing rather than leaving a resource stuck in a failed reconcile loop.

| What you try to create | Missing dependency | Error you'll see |
|------------------------|--------------------|------------------|
| `SurrealDbCluster` with `storage.backend: tikv` | TiDB Operator v2 not installed | `TiDB Operator v2 is not installed. Install tidb-operator v2 before using storage.backend=tikv.` |
| `SurrealDbCluster` with `tls.issuerRef` set | cert-manager not installed | `cert-manager is not installed. Install cert-manager before using spec.tls.issuerRef.` |
| `Backup` / `BackupSchedule` / `Restore` | Velero not installed | `Velero is not installed. Run 'just velero-install' before creating backup CRs.` |
| `Backup` | `BackupDestination` not ready | `BackupDestination 'my-dest' is not ready.` |
| `Backup` with `storage.backend: memory` | — | `Cannot backup memory backend.` |
| `BackupDestination` | Credential secret missing | `Secret 'my-creds' not found in namespace 'default'.` |
| `BackupDestination` | `spec.bucket` empty | `spec.bucket is required.` |

> **Note:** The webhooks require HTTPS. KubeOps generates a self-signed TLS certificate
> for the webhook server automatically — no cert-manager installation is needed for the
> webhook TLS itself.

## Development

### Prerequisites

- .NET 10 SDK
- just task runner
- Docker (for container publish)
- kubectl + a local Kubernetes cluster (k0s, kind, or minikube)

### Available recipes

```
$ just --list
Available recipes:
    build                 # Build the operator
    clean                 # Clean build artifacts
    demo endpoint username password # Run the demo console app
    deploy                # Deploy operator via kustomize base
    deploy-crds           # Apply CRD manifests to the cluster
    deploy-local          # Deploy operator via local overlay (for local development)
    gen-crds              # Generate CRD YAML via KubeOps CLI; keeps only our CRD, discards external stubs
    lint                  # Run code formatting/analyzer lint checks
    publish tag           # Publish operator container image for a single arch (amd64)
    publish-multiarch tag # Publish multi-arch operator image (amd64 + arm64 manifest)
    restore               # Restore NuGet packages
    run                   # Run the operator locally against the k0s cluster
    test                  # Run all tests (unit + integration + e2e)
    test-e2e              # Run backup/restore e2e tests against the local k0s cluster
    test-integration      # Run operator integration tests against the local k0s cluster
    test-operator         # Alias for test-integration
    test-unit             # Run all unit tests
```

### Build and test

```bash
just restore    # restore NuGet packages
just lint       # verify dotnet formatting/analyzers
just build      # compile
just test-unit  # unit tests (no cluster needed)
just test       # all tests including integration/e2e (requires k0s/k3s + dependencies)
```

### Regenerate CRDs

After modifying `SurrealDbCluster.cs` schema fields, regenerate the CRD manifest:

```bash
just gen-crds
```

This restores the KubeOps CLI tool, invokes `dotnet kubeops generate crds`, and copies the result to `deploy/crds/surrealdbcluster-crd.yaml`.

### Publish container image locally

```bash
just publish dev
```

The container is published using `dotnet publish` with `EnableSdkContainerSupport` — no Dockerfile required.

### Run against a cluster

```bash
just run   # uses KUBECONFIG=/var/lib/k0s/pki/admin.conf
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Make changes following the conventions in CLAUDE.md
4. Run lint and tests: `just lint && just test-unit`
5. Commit with conventional commits (`feat:`, `fix:`, `refactor:`, etc.)
6. Open a pull request

See ARCHITECTURE.md and DESIGN.md for architectural context.

# raws-labs/tigris

## 评论（2/2）

> **benterix** · 2026-04-29T07:51:01.000Z　
> I have so many questions! Why did you decide to use C# instead of Go? How does the C# Operator SDK compare to the Operator SDK or Kubebuilder?

---

> **stevefan1999** · 2026-04-29T08:32:30.000Z　
> While I'm both fluent in Rust, Golang and C#, I just don't think Golang is a good choice for Kubernetes operator, the code is simply too terse and verbose, and I can't enjoy a lot of good things such as DI and IoC in Golang, where I think C#/Kotlin's approach by using primary constructor is very intuitive for me, and it is really a game changer for the coding mindset, especially when you have LLM, without DI there will be a lot of spagetti code entanglement. I use DI to facilitate functional separation and modularization of code.It is not like I don't know that Golang's interface could do that. It's just C# simply did better. I do enjoy using Golang for writing network application such as network protocols and IO intensive workload, which is where Golang really shine through Goroutines, but if you want a generalist that is famiilar and did all-rounds, I would still consider C#/Java/Kotlin for that purpose.

## 关联链接

- https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml
- https://github.com/stevefan1999-personal/surrealdb-operator/releases/latest/download/surrealdbcluster-crd.yaml

## 导航

- 项目页：[[10-项目/github.com_f1ef313e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
