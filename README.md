# Siddur Guide

An audio guide for learning Jewish prayers — Hebrew text, Cyrillic transliteration, Russian translation, pronunciation audio, daily prayer times, and progress tracking.

## Demo

> Screenshots will be added after deployment.
>
> - `docs/screenshot-prayers.png` — prayer catalog with progress bar
> - `docs/screenshot-detail.png` — prayer detail view with audio player
> - `docs/screenshot-schedule.png` — daily prayer times for the selected city

## Product Context

### End users

Russian-speaking people who are new to Judaism or just starting to practice and want to learn how to correctly read Jewish prayers but struggle with Hebrew pronunciation.

### Problem

Beginners struggle to correctly pronounce Hebrew prayers. There is no simple audio guide that pairs the original text with a Cyrillic transliteration, a plain-language explanation, and the actual prayer times for where the user lives.

### Solution

A web app that lets a user:

1. Browse a catalog of core Jewish prayers (Shema, Amidah, blessings, Shabbat liturgy).
2. See each prayer in three forms side-by-side — Hebrew, Cyrillic transliteration, Russian translation.
3. Listen to an audio track of the correct pronunciation.
4. Mark prayers as "learned" and track progress across sessions.
5. Check today's prayer times (Shacharit, Mincha, Maariv, sunrise, sunset) for a chosen city, computed locally from latitude/longitude using the KosherJava zmanim algorithm — no external API needed.

## Features

### Implemented (Version 2)

- Prayer catalog with 7 core prayers across 3 categories (Daily, Blessings, Shabbat)
- Per-prayer view with Hebrew text, Cyrillic transliteration, Russian translation, description
- Audio playback of correct pronunciation
- Icons / visual markers for every prayer
- Category filter (All / Daily / Blessings / Shabbat)
- User progress tracking (mark as learned, progress bar, persisted per user)
- Daily prayer times (Zmanim) computed locally via the KosherJava zmanim algorithm for 10 cities including Jerusalem, Tel Aviv, Moscow, New York, and Innopolis — fully offline, no external API
- REST API with health, prayers, progress, zmanim, and categories endpoints
- Dockerized backend, database, and frontend; single `docker compose up` starts the whole stack
- PostgreSQL persistence for prayers and user progress

### Not yet implemented

- Recording high-quality audio for every prayer (currently placeholders)
- Full-text search across prayers
- Multi-language UI (currently English UI with Russian/Hebrew content)
- Favorites / bookmarks
- Push notifications for prayer times
- Mobile native app (PWA-ready but not installed)

## Usage

After deployment, open the web app in a browser.

1. **Prayers tab** — browse the catalog. Filter by category using the pill buttons. Click a card to open the detail view.
2. **Prayer detail** — read Hebrew, transliteration, and translation. Tap **▶ Play Audio** to hear the pronunciation. Tap **Mark as learned** to track progress. Use **← Back** to return.
3. **Times tab** — pick your city from the dropdown. See today's Shacharit, Mincha, Maariv, plus sunrise and sunset. The selection is remembered.

Your progress and city selection are stored server-side tied to a random user id that lives in `localStorage`, so clearing browser storage resets progress for that browser.

## Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  React SPA   │ ──▶ │   FastAPI    │ ──▶ │  PostgreSQL  │
│  (nginx:80)  │     │  (uvicorn)   │     │              │
└──────────────┘     └──────┬───────┘     └──────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │  HebCal API  │
                     │ (zmanim.com) │
                     └──────────────┘
```

- **Frontend**: React 18 + Vite, built into static assets served by nginx. Nginx also reverse-proxies `/api/` and `/audio/` to the backend.
- **Backend**: FastAPI (Python 3.12) with SQLAlchemy ORM and Pydantic schemas. Uses the `zmanim` Python library (port of KosherJava) to compute prayer times locally.
- **Database**: PostgreSQL 16. Tables: `prayers`, `user_progress`. Seeded on first boot.

### API endpoints

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/health` | Health check |
| GET | `/api/prayers` | List prayers (optional `?category=`) |
| GET | `/api/prayers/{id}` | Get one prayer |
| GET | `/api/categories` | List categories |
| GET | `/api/cities` | List supported cities |
| GET | `/api/zmanim?city=Jerusalem` | Today's prayer times |
| GET | `/api/progress/{user_id}` | User's learned prayer ids |
| POST | `/api/progress` | Mark a prayer as learned |
| DELETE | `/api/progress?user_id=&prayer_id=` | Unmark |

## Deployment

### Target environment

- **OS**: Ubuntu 24.04 LTS (as on Innopolis University VMs)
- **CPU / RAM**: 1 vCPU / 1 GB RAM is enough
- **Ports**: 3000 (frontend), 8000 (backend), 5432 (Postgres, optional external)

### Prerequisites on the VM

Install Docker Engine and Docker Compose:

```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin git
sudo systemctl enable --now docker
sudo usermod -aG docker $USER  # re-login after this
```

### Step-by-step deployment

```bash
# 1. Clone the repo
git clone https://github.com/Farcimin/se-toolkit-hackathon.git
# (old URL https://github.com/Farcimin/PrayPrayPray still works as GitHub auto-redirects)
cd se-toolkit-hackathon

# 2. Build and start all services
docker compose up --build -d

# 3. Verify
curl http://localhost:8000/api/health
# {"status":"ok","version":"2.0"}

# 4. Open the app
# http://<your-vm-ip>:3000
```

The first boot will:

1. Pull/build Postgres, backend, and frontend images.
2. Wait for Postgres healthcheck to pass.
3. Start the backend, which creates tables and seeds the prayer catalog.
4. Start the frontend (nginx) which proxies API calls to the backend.

### Stopping / updating

```bash
docker compose down            # stop
docker compose down -v         # stop and wipe DB volume
git pull && docker compose up --build -d  # pull latest and restart
```

### Notes

- The Docker images pull base images from `harbor.pg.innopolis.university/docker-hub-cache/`. If deploying outside the university network, replace these prefixes with plain `python:3.12-slim`, `node:20-alpine`, `nginx:alpine`, and `postgres:16-alpine` in the three Dockerfiles and `docker-compose.yml`.
- Audio files live in `./audio` and are mounted into the backend container. Replace the placeholder `.mp3` files with real recordings without rebuilding.
- Prayer times are computed locally — no external network is required at runtime beyond what Docker already needs for image pulls.

## License

MIT — see [LICENSE](LICENSE).
