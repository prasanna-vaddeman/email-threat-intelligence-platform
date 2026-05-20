# =========================================================
# IMPORT LIBRARIES
# =========================================================

from fastapi import (

    APIRouter,

    HTTPException
)

from backend.schemas.email_schema import (

    EmailRequest,

    EmailResponse
)

from backend.services.inference import (

    predict_email
)


# =========================================================
# API ROUTER
# =========================================================

router = APIRouter(

    prefix="/email",

    tags=[

        "Email Threat Intelligence"
    ]
)


# =========================================================
# HEALTH CHECK ENDPOINT
# =========================================================

@router.get(

    "/health",

    status_code=200
)

def health_check() -> dict:

    """

    Verify backend availability.

    Used for:

    - Deployment checks

    - Monitoring

    - Service validation

    Returns:

        dict

    """

    return {

        "status": "healthy"
    }


# =========================================================
# EMAIL PREDICTION ENDPOINT
# =========================================================

@router.post(

    "/predict",

    response_model=EmailResponse
)

def predict_email_endpoint(

    request: EmailRequest

) -> EmailResponse:

    """

    Predict email spam threat.

    Args:

        request (EmailRequest)

            Raw email payload.

    Returns:

        EmailResponse

            Prediction result.

    Raises:

        HTTPException

            Internal prediction failure.

    """

    try:

        return predict_email(

            request.email_text
        )

    except Exception as exc:

        raise HTTPException(

            status_code=500,

            detail=(

                "Internal prediction error"
            )

        ) from exc