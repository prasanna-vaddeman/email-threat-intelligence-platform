"""
FastAPI Entry Point
"""

from fastapi import FastAPI
from fastapi.responses import Response

from prometheus_client import (
    make_asgi_app
)

from backend.api.routes import router


app = FastAPI(

    title="Email Threat Intelligence API",

    version="2.0.0"

)


# ===================================
# PROMETHEUS METRICS
# ===================================

metrics_app = make_asgi_app()

app.mount(

    "/metrics",

    metrics_app

)


# ===================================
# ROOT
# ===================================

@app.get("/")
def root():

    return {

        "message": "API Running"

    }


# ===================================
# HEALTH
# ===================================

@app.get("/health")
def health():

    return {

        "status": "healthy",

        "service": "email-threat-intelligence-api",

        "version": "2.0.0"

    }


@app.head("/health")
def health_head():

    return Response(status_code=200)


# ===================================
# ROUTES
# ===================================

app.include_router(

    router

)