# Deployment Guide

## Frontend Deployment

Platform:

- Streamlit Cloud

Live URL:

https://email-threat-intelligence-platform-ai.streamlit.app/

---

## Backend Deployment

Platform:

- Railway

Live URL:

https://email-threat-intelligence-platform-production.up.railway.app/

API Documentation:

https://email-threat-intelligence-platform-production.up.railway.app/docs

---

## Environment Variables

Required:

```env
DATABASE_URL=
SUPABASE_URL=
SUPABASE_KEY=
```

---

## Deployment Workflow

GitHub Push

↓

Railway Auto Deploy

↓

FastAPI Service Restart

↓

Application Available
