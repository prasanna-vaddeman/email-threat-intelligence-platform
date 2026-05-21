"""
FastAPI Entry Point
"""

from fastapi import FastAPI

from backend.api.routes import router


app = FastAPI(

    title=(

        "Email Threat Intelligence API"

    ),

    version="2.0.0"

)


@app.get(

    "/"

)

def root():

    return {

        "message":

        "API Running"

    }


@app.get(

    "/health"

)

def health():

    return {

        "status":

        "healthy"

    }


app.include_router(

    router

)