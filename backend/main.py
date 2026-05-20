# =========================================================
# IMPORT LIBRARIES
# =========================================================

from fastapi import (

    FastAPI
)

from backend.api.routes import (

    router
)


# =========================================================
# FASTAPI APPLICATION
# =========================================================

app = FastAPI(

    title=(

        "Email Threat Intelligence API"
    ),

    description=(

        "Spam email detection API "
        "powered by machine learning."
    ),

    version="1.0.0",

    docs_url="/docs",

    redoc_url="/redoc"
)


# =========================================================
# REGISTER API ROUTES
# =========================================================

app.include_router(

    router
)


# =========================================================
# ROOT ENDPOINT
# =========================================================

@app.get(

    "/",

    status_code=200
)

def root() -> dict:

    """

    Verify API availability.

    Returns:

        dict

    """

    return {

        "message":

        "Email Threat Intelligence API is running."
    }