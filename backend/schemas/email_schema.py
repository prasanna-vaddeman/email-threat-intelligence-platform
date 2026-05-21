"""
Email API Schemas
"""

from pydantic import BaseModel
from pydantic import Field
from typing import Dict


class EmailRequest(BaseModel):

    """
    Request payload
    """

    email_text: str = Field(

        ...,

        min_length=1

    )


class EmailResponse(BaseModel):

    """
    Prediction response
    """

    prediction: str

    spam_probability: float

    threat_score: int

    confidence: float

    inference_ms: float

    threat_level: str

    features: Dict[str, float]