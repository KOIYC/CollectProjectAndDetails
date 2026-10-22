---
type: "corpus"
item_id: "03f1d5b23be5bbc1"
title: "Show HN: TutorLoom, an open-source multi-tenant LMS (Django, React, Flutter)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50181517"
project_url: "https://github.com/pacewisdomhq/TutorLoom"
author: "madhukarah"
published_at: "2026-10-21T14:22:07Z"
captured_at: "2026-10-22T09:46:18+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - hn_show
  - author_madhukarah
  - story_50181517
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: TutorLoom, an open-source multi-tenant LMS (Django, React, Flutter)

> [!info] 一句话导读
> pacewisdomhq/TutorLoom

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50181517>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：madhukarah　|　发布：2026-10-21T14:22:07Z
> 项目链接：<https://github.com/pacewisdomhq/TutorLoom>
> 采集：2026-10-22T09:46:18+08:00　|　id：`03f1d5b23be5bbc1`

## 正文

# pacewisdomhq/TutorLoom

Self-hosted, multi-tenant learning management system (LMS) for training institutes and teams: course builder, trainer and student portals, progress tracking. Django + React. Apache-2.0.

- Stars: 33
- Forks: 10
- Watchers: 33
- Open issues: 8
- License: Apache License 2.0
- Homepage: https://www.tutorloom.io/
- Default branch: main
- Created: 2026-10-07T11:21:56Z

## Languages

- C
- C++
- CMake
- CSS
- Dart
- Dockerfile
- HTML
- JavaScript
- Jinja
- Kotlin
- Objective-C
- Python
- Ruby
- Swift
- TypeScript

## Topics

- corporate-training
- django
- edtech
- elearning
- flutter
- learning-management-system
- lms
- moodle-alternative
- multi-tenant
- open-source
- react
- self-hosted

## Top Contributors

- pacewisdomsolutions (17 contributions)
- dependabot[bot] (12 contributions)
- PKulal (10 contributions)
- Aby-Sunny (3 contributions)
- Leelanjan-s (3 contributions)
- YajneshKottary (3 contributions)
- Kruthikagowda12 (1 contributions)
- YashwithaKulal2003 (1 contributions)
- nihallsuvarna (1 contributions)

---

## README

CI
License: Apache 2.0
PRs welcome
GitHub stars

Python
Django
DRF
PostgreSQL
React
TypeScript
Flutter

**Screenshots** · **Quickstart** · **Editions** · **Architecture** · **API** · **Contributing**

**TutorLoom** is a free, self-hosted learning platform for institutes and training teams. Build structured courses, enrol learners in batches, grade their work and follow their progress, on the web and on Android and iOS.

---

## ✨ Highlights

 🏢 Multi-tenant by design
 One installation serves many organisations. Every query is scoped to the organisation, so trainers and learners only ever see their own data.

 🧱 Structured course builder
 Courses are organised into levels, chapters and steps: videos, documents, tasks and quizzes, with prerequisites and sequential unlocking.

 👥 Batches & bulk onboarding
 Group learners into time-boxed batches. Invite trainers and students one by one or in bulk from CSV / Excel.

 ✅ Grading & feedback
 Trainers review submissions in one queue, approve or reject with a score and written feedback, and export progress to Excel.

 🗺️ Guided learner roadmap
 Students follow a step-by-step roadmap on the web or the mobile app, track completion and earn points and levels.

 🔌 API-first
 A documented REST API (OpenAPI 3, Swagger UI and ReDoc) with JWT auth powers the web app, the mobile app and your own integrations.

---

## 📸 Screenshots

### 🖥️ Web app

 Institute Admin dashboard

 Course builder

 Trainer dashboard

 One account, many organisations

 Student dashboard

 My courses

 Course roadmap

 Progress & certificates

### 📱 Mobile app (Android & iOS)

---

## 🔄 How it works

---

## 📦 Editions

This repository is the **Community edition**: free, open source and self-hosted. An **Enterprise edition** adds advanced modules on top.

| Capability | 🆓 Community | 💎 Enterprise |
|---|:---:|:---:|
| Email & password login, invites, password reset | ✅ | ✅ |
| Multi-role accounts with role switching | ✅ | ✅ |
| Institute Admin portal: trainers, students, batches | ✅ | ✅ |
| Bulk upload of trainers & students (CSV / Excel) | ✅ | ✅ |
| Course builder: levels, chapters, resources, tasks, quizzes | ✅ | ✅ |
| Prerequisites & sequential unlocking | ✅ | ✅ |
| Trainer portal: dashboard, grading, learner progress | ✅ | ✅ |
| Student portal & mobile app: dashboard, roadmap, progress | ✅ | ✅ |
| Points & levels | ✅ | ✅ |
| Course completion certificates (PDF) | ✅ | ✅ |
| Branded email notifications | ✅ | ✅ |
| Google & Microsoft sign-in | — | ✅ |
| Coding questions with AI test cases & starter code | — | ✅ |
| Course import/export, quiz bulk upload, drip release | — | ✅ |
| Assessments (MCQ, task, coding) | — | ✅ |
| No-login coding interviews for candidates | — | ✅ |
| Super Admin console, audit logs, organisation branding | — | ✅ |
| Leaderboard, badges, in-app notifications, calendars | — | ✅ |

---

## 📐 Architecture

| Component | Location | Stack |
|---|---|---|
| Backend REST API | repository root | Python 3.13, Django 6, Django REST Framework, Celery |
| Web frontend | `frontend/` | React 19, TypeScript, Vite, Tailwind CSS 4 |
| Student mobile app | `student_mobile_app/` | Flutter (Android & iOS), learner-only: courses, lessons, tasks, quizzes and progress against the same API |

---

## 👤 Roles & portals

| Role | What they do | Role in code | Edition |
|---|---|---|---|
| **Institute Admin** | Runs one organisation: people, batches, courses, progress | `org_admin` | 🆓 |
| **Trainer** | Delivers assigned courses, grades work, tracks learners | `teacher` | 🆓 |
| **Student** | Follows course roadmaps, submits work, tracks progress | `student` | 🆓 |
| **Super Admin** | Platform-wide console for every organisation and user | Django superuser | 💎 |
| **External Candidate** | Takes a coding interview through a private link, no account needed | — | 💎 |

One account can hold several roles (for example a Trainer who is also an Institute Admin) and switch between portals without signing out.

---

## 🚀 Quickstart

The fastest way to run everything (Postgres, Redis, the Django API, a Celery worker and the web app) is Docker. Nothing else to install.

```bash
git clone https://github.com/pacewisdomhq/TutorLoom.git
cd TutorLoom
docker compose up --build
```

| Service | URL |
| --- | --- |
| Frontend | http://localhost:5173 |
| API docs (Swagger) | http://localhost:8010/api/docs/ |
| ReDoc | http://localhost:8010/api/redoc/ |
| Django admin | http://localhost:8010/admin/ |

Source is bind-mounted, so edits on your machine reload in the containers — no
rebuild unless dependencies change. Database migrations run automatically on
every backend start.

Create the initial organization, default batch, and Org Admin (with superuser/admin panel access) in a single command:

```bash
docker compose exec backend python manage.py create_initial_organization \
  --name "Acme Academy" --slug "acme-academy" \
  --admin-email "admin@acme.edu" --password "SecurePassword123" \
  --batch-name "Batch 1"
```

*(This automatically creates the user as an Org Admin and grants superuser/staff privileges so they can access both the LMS and `/admin/`).*

 Ports and common Docker commands

The backend is published on **8010** because 8000 is often taken by another local service. Postgres and Redis are deliberately not published, so they never clash with ones you already run. Override host ports in a `.env` file next to `docker-compose.yml`, or inline:

```bash
BACKEND_PORT=9000 FRONTEND_PORT=3000 docker compose up
```

`VITE_API_BASE_URL` follows `BACKEND_PORT` automatically.

```bash
docker compose logs -f backend     # tail a service's logs
docker compose exec backend bash   # shell into the API container
docker compose exec backend python manage.py migrate
docker compose down                # stop; add -v to also wipe the database
```

---

## 💻 Manual setup

 Run the backend and frontend without Docker

**Prerequisites:** Python 3.13, Poetry 2.x, PostgreSQL, Redis, Node.js and npm.

**1. Install**

```bash
git clone https://github.com/pacewisdomhq/TutorLoom.git
cd TutorLoom
poetry env use python3.13
poetry install
```

Prefer pip? `python3.13 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`

**2. Configure**

```bash
cp .env.example .env
```

At minimum set `SECRET_KEY`, the `DB_*` variables (or `DATABASE_URL`), `REDIS_URL` and `CELERY_BROKER_URL`. See environment variables for the full list.

**3. Create the database and first organisation**

```bash
poetry run python manage.py migrate
poetry run python manage.py create_initial_organization \
  --name "Acme Academy" --slug "acme-academy" \
  --admin-email "admin@acme.edu" --password "AdminPassword123" \
  --batch-name "Batch 1"
```

This creates the organisation, its first batch and the Institute Admin, who also gets Django admin (`/admin/`) access. Pass `--no-superuser` to skip that.

**4. Run the backend**

```bash
redis-server                                          # or: docker run -d -p 6379:6379 redis
poetry run python manage.py runserver
poetry run celery -A lms_core worker -l info          # background tasks
```

**5. Run the web app**

```bash
cd frontend
npm install
cp .env.example .env   # set VITE_API_BASE_URL, e.g. http://localhost:8000/api
npm run dev            # http://localhost:5173
```

The full frontend guide lives in `frontend/README.md`. The mobile app guide, covering Flutter setup, its one environment variable, architecture, and building and releasing, lives in `student_mobile_app/README.md`.

---

## 🔧 Configuration

All settings are read from environment variables (or a `.env` file). Copy `.env.example` to get started.

 All environment variables

| Variable | Description | Example |
|---|---|---|
| `SECRET_KEY` | Django secret key | `change-this-to-a-secure-secret-key` |
| `DEBUG` | Debug mode (default `False`) | `True` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts (default `*`) | `localhost,127.0.0.1` |
| `DATABASE_URL` | Full DB URL; overrides the `DB_*` vars | `postgres://postgres:postgres@localhost:5432/lms_db` |
| `DB_NAME` | Postgres database name | `lms_db` |
| `DB_USER` | Postgres user | `postgres` |
| `DB_PASSWORD` | Postgres password | `postgres` |
| `DB_HOST` | Postgres host (**required** unless `DATABASE_URL` is set) | `localhost` |
| `DB_PORT` | Postgres port | `5432` |
| `REDIS_URL` | Redis URL for the cache (**required**) | `redis://127.0.0.1:6379/1` |
| `CELERY_BROKER_URL` | Celery broker (**required**) | `redis://127.0.0.1:6379/0` |
| `CELERY_RESULT_BACKEND` | Celery result backend | `django-db` |
| `CELERY_TASK_ALWAYS_EAGER` | Run tasks inline, with no worker | `False` |
| `FRONTEND_URL` | Web app URL, used in emails, CORS and CSRF | `http://localhost:5173` |
| `BACKEND_PUBLIC_URL` | Public URL of this API | `http://localhost:8000` |
| `CSRF_TRUSTED_ORIGINS` | Comma-separated trusted origins | `https://app.example.com` |
| `CORS_ALLOWED_ORIGINS` | Extra comma-separated CORS origins | `https://app.example.com` |
| `CORS_ALLOW_ALL_ORIGINS` | Allow any origin | `False` |
| `DEFAULT_FROM_EMAIL` | Sender address | `no-reply@example.com` |
| `AWS_SES_ACCESS_KEY_ID` | SES key. If empty, email goes through `EMAIL_BACKEND` | *(empty)* |
| `AWS_SES_SECRET_ACCESS_KEY` | SES secret | *(empty)* |
| `AWS_SES_REGION` | SES region | `ap-south-1` |
| `EMAIL_BACKEND` | Fallback mail backend (default: console) | `django.core.mail.backends.console.EmailBackend` |
| `EMAIL_HOST` / `EMAIL_PORT` / `EMAIL_USE_TLS` | SMTP server settings | `smtp.gmail.com` / `587` / `True` |
| `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` | SMTP credentials | `user@example.com` / `app-password` |
| `USE_S3` | Store uploads on S3 instead of `./media/` | `False` |
| `AWS_S3_ACCESS_KEY_ID` / `AWS_S3_SECRET_ACCESS_KEY` | S3 credentials | `AKIA...` / `...` |
| `AWS_STORAGE_BUCKET_NAME` | S3 bucket | `lms-media` |
| `AWS_S3_REGION_NAME` | S3 region | `ap-south-1` |
| `USE_AWS_SECRETS` | Load settings from AWS Secrets Manager | `False` |
| `AWS_SECRETS_NAME` | Secret name | `lms/prod` |
| `AWS_REGION_NAME` | Secrets Manager region | `ap-south-1` |
| `TEST_IP` | *(tests only)* IP used by the test suite | `127.0.0.1` |

---

## 🔌 API

| URL | What |
|---|---|
| `/api/docs/` | Swagger UI: interactive API reference |
| `/api/redoc/` | ReDoc |
| `/api/schema/` | OpenAPI 3 schema |
| `/admin/` | Django admin |

To try authenticated endpoints in Swagger, call `POST /api/auth/login/`, click **Authorize** and paste the access token.

 Endpoint overview

All endpoints require `Authorization: Bearer ` except login, invite and password reset. Lists are paginated at 20 items per page.

| Area | Endpoints |
|---|---|
| Auth | `POST /api/auth/login/` · `refresh/` · `logout/` · `forgot-password/` · `reset-password/` · `accept-invite/` · `GET verify-invite/` |
| Profile | `GET/PATCH /api/users/me/` · `POST /api/users/ /reinvite/` |
| Roles | `/api/roles/` · `/api/user-roles/` · `update-role/` · `delete-role/` |
| Organisation | `/api/organizations/ /` · `members/` · `staff/` · `batches/` · `batches/ /students/` · `students/` · `…/bulk-upload-file/` · `…/download-template/` |
| Dashboards | `…/ /analytics/overview/` · `…/batches/ /analytics/` · `…/students/me/dashboard/` · `…/teacher-dashboard/ /` · `…/batches-overview/` |
| Course builder | `/api/organizations/ /courses/` → `modules/` → `nodes/` · `nodes/ /content/` |
| Learning | `…/courses/ /roadmap/` · `…/my-courses/` · `…/my-progress/` · `POST /api/nodes/ /complete/` |
| Submissions | `/api/nodes/ /submit/` · `task/submit/` · `task/result/` · `task/all-submissions/` · `/api/quizzes/ /submit/` |
| Grading & progress | `…/pending-evaluations/` · `…/submissions/tasks/ /review/` · `…/learner-progress/` · `…/learner-progress/export/` · `…/node-submission-details/` |

For architecture details, multi-tenancy flowcharts and the full endpoint reference, see `PROJECT_OVERVIEW.md`.

---

## 🧰 Tech stack

| Area | Technology |
|---|---|
| Backend | Python 3.13, Django 6, Django REST Framework 3.16 |
| Auth | JWT via `djangorestframework-simplejwt` (rotating refresh tokens with blacklist) |
| Database | PostgreSQL |
| Cache & jobs | Redis, Celery, `django-celery-results` |
| Storage | Local filesystem or Amazon S3 (`django-storages`) |
| Email | Amazon SES, with a fallback to any Django mail backend |
| Spreadsheets | pandas, openpyxl, xlrd (bulk uploads and Excel exports) |
| API docs | OpenAPI 3 via `drf-spectacular` (Swagger UI and ReDoc) |
| Web frontend | React 19, TypeScript, Vite, React Router, Tailwind CSS 4 |
| Mobile | Flutter (Dart 3.13), MVVM + Provider, go_router, Dio, Hive |
| Tests | pytest, pytest-django, pytest-cov (backend) · Vitest (frontend) · `flutter test` (mobile) |

 Project structure

```text
.
├── lms_core/            # Settings, root URLs, Celery app, email & storage utilities, soft-delete base model
├── accounts/            # Users (email login), JWT auth, invites, password reset, profile
├── rbac/                # Roles, role assignments, permission classes
├── organizations/       # Organisations, staff, batches, students, bulk upload, bootstrap command
├── curriculum/          # Courses, levels, chapters, steps, resources, tasks, quizzes, submissions, progress
├── analytics/           # Admin / trainer / student dashboards and daily metrics
├── gamification/        # Points & levels
├── settings/            # Shared Amazon SES client
├── frontend/            # React 19 + TypeScript + Vite web app (docs: frontend/README.md)
├── student_mobile_app/  # Flutter learner app for Android and iOS (docs: student_mobile_app/README.md)
├── Dockerfile           # Backend API image
├── docker-compose.yml   # Full local stack: Postgres, Redis, API, Celery worker, frontend
├── pyproject.toml       # Poetry dependencies + pytest / coverage config
└── requirements.txt     # pip dependencies (used by the Dockerfile)
```

Each backend app has its own `README.md` with deeper notes. The frontend is documented in `frontend/README.md` and the mobile app in `student_mobile_app/README.md`.

---

## 🧪 Testing

Backend tests need a running PostgreSQL; Redis, S3 and Celery are stubbed automatically.

```bash
poetry run pytest -p no:cacheprovider --no-cov -q    # fast run
poetry run pytest                                    # with coverage (terminal + coverage.xml)
poetry run pytest curriculum/ --no-cov -q            # a single app
```

Frontend tests and lint:

```bash
cd frontend
npm test          # Vitest
npm run lint      # ESLint
```

---

## 🚢 Deployment

```bash
docker build -t tutorloom-backend .
docker run -d -p 8000:8000 --env-file .env tutorloom-backend
```

> [!IMPORTANT]
> The image starts Django's development server. In production, run `gunicorn lms_core.wsgi:application --bind 0.0.0.0:8000` (already installed) behind a TLS-terminating proxy.

- Set `DEBUG=False`, a strong `SECRET_KEY`, and explicit `ALLOWED_HOSTS`, `FRONTEND_URL` and `CSRF_TRUSTED_ORIGINS`.
- Use `USE_S3=True` for uploads and SES credentials for email.
- Run a Celery worker next to the web process. Schedule `analytics.tasks.calculate_daily_analytics` yourself; no beat schedule ships with the project.
- The web frontend is a static Vite build (`npm run build` in `frontend/`) that you deploy separately.

---

## 🧭 Roadmap

 Planned and proposed work

**Planned (Enterprise)**

- **Master data management:** assessment types, skills, course categories, notification templates
- **Training cycle templates:** term dates, working days, holidays
- **System settings:** password policy, upload limits, email/SMS gateway, feature flags
- **Cross-organisation reports & activity feed**, with CSV/PDF export
- **Notification broadcast & maintenance mode**
- **Training structure:** departments, job roles, skills mapping
- **Institute reporting dashboard:** student performance and trainer activity
- **Organisation announcements**

**Proposed (edition not yet decided)**

| Area | Ideas |
|---|---|
| AI | AI feedback drafts for trainers · chapter-scoped AI tutor chat · code plagiarism / similarity check |
| Learning content | SCORM / xAPI import · native video hosting with watch progress · discussion threads per chapter |
| Assessment depth | Advanced proctoring · question bank with tags & random pools · rubric grading · skill-wise score breakdown |
| Reporting & compliance | Mandatory training compliance tracking · data export, account deletion & retention (GDPR / DPDP) |
| Platform | Custom subdomains & white-label email · subscription plans & usage limits · public API keys & webhooks · SAML SSO / SCIM · PWA with offline reading |
| Learner experience | Course catalogue with self-enrolment · learning paths across courses · notes & bookmarks · multi-language UI |

---

## 🤝 Contributing

Contributions are welcome, especially for the 🚧 Community items and the roadmap. Please read **CONTRIBUTING.md** and our **Code of Conduct** first.

1. Fork the repository and create a feature branch.
2. Keep code in the app that owns the feature, and scope every query to the organisation.
3. Commit migrations together with model changes (`makemigrations --check` runs in the test suite).
4. Add tests under ` /tests/` (or next to the component in `frontend/`) and make sure `poetry run pytest` and `npm test` pass.
5. Open a pull request describing the change.

Need help? See **SUPPORT.md**. Found a security issue? Please report it privately as described in **SECURITY.md**.

---

## 📄 License

Licensed under the Apache License, Version 2.0. See NOTICE for attribution details.

**TutorLoom** is built and maintained by **Pace Wisdom Solutions**

Copyright © 2026 Pace Wisdom Solutions Pvt. Ltd.

 If this project helps you, consider giving it a ⭐ on GitHub.

## 关联链接

- http://localhost:5173
- http://localhost:5173`
- http://localhost:8000/api
- http://localhost:8000`
- http://localhost:8010/admin/
- http://localhost:8010/api/docs/
- http://localhost:8010/api/redoc/
- https://app.example.com`
- https://github.com/pacewisdomhq/TutorLoom.git
- https://www.tutorloom.io/

## 导航

- 项目页：[[10-项目/github.com_70264d82]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
