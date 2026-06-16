"""
API Routes
"""

from fastapi import APIRouter
from fastapi import HTTPException

from backend.utils.logger import logger

from backend.schemas.email_schema import (
    EmailRequest,
    EmailResponse
)

from backend.services.inference import (
    predict_email
)

router = APIRouter(

    prefix="/email",

    tags=[

        "Threat Detection"

    ]

)


@router.get(
    "/health"
)
def router_health():

    logger.info(
        "Health check requested"
    )

    return {

        "status":

        "healthy"

    }


@router.post(
    "/predict",
    response_model=EmailResponse
)
def predict_endpoint(
    request: EmailRequest
):

    logger.info(
        f"Prediction request received | "
        f"Length={len(request.email_text or '')}"
    )

    try:

        result = predict_email(
            request.email_text
        )

        logger.info(
            f"Prediction completed | "
            f"Label={result['prediction']} | "
            f"Threat={result['threat_level']}"
        )

        return result

    except Exception as exc:

        logger.exception(
            f"Prediction failed: {exc}"
        )

        raise HTTPException(

            status_code=500,

            detail=str(exc)

        )