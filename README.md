# chatgpt-auto-reply

Automated reply system that uses OpenAI's GPT to generate and schedule intelligent responses. Built with Django, Celery, and Django Channels for async task processing and real-time WebSocket support.

## Features

- **AI-powered replies** — Generates context-aware responses using the OpenAI API
- **Scheduled delivery** — Celery Beat + django-celery-beat for cron-based scheduling
- **Async processing** — Django Channels + Daphne for WebSocket and async task handling
- **Redis queue** — Kombu/Redis as the Celery broker for reliable task queueing
- **JWT auth** — Secure API access via djangorestframework-simplejwt

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5, Django REST Framework |
| AI | OpenAI API (GPT) |
| Task Queue | Celery, Celery Beat, Redis |
| Async / WebSocket | Django Channels, Daphne |
| Auth | JWT (SimpleJWT) |
| Database | PostgreSQL (psycopg2) |
| Deployment | Docker, Gunicorn, Whitenoise |

## Getting Started

```bash
# Clone the repo
git clone https://github.com/Kh125/chatgpt-auto-reply.git
cd chatgpt-auto-reply

# Copy env file and set your keys
cp .env.example .env
# Add OPENAI_API_KEY, SECRET_KEY, REDIS_URL, ALLOWED_HOSTS to .env

# Run with Docker
docker build -t chatgpt-auto-reply .
docker run -p 8000:8000 chatgpt-auto-reply
```

## Environment Variables

```env
OPENAI_API_KEY=your_openai_key
OPENAI_ORGANIZATION=your_openai_org_id
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your_django_secret
DEBUG=True
```

## Architecture

```
Request
   ↓
Django REST API
   ↓
OpenAI API (GPT reply generation)
   ↓
Celery Task Queue (Redis broker)
   ↓
Celery Beat Scheduler (cron-based delivery)
   ↓
Django Channels (WebSocket real-time updates)
```


## Author

[Khant Hmue](https://khanthmue.com) — Backend & AI Engineer
