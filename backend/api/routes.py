"""
API Routes
"""

from fastapi import APIRouter
from fastapi import HTTPException

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

    try:

        return predict_email(

            request.email_text

        )

    except Exception as exc:

        raise HTTPException(

            status_code=500,

            detail=str(exc)

        )