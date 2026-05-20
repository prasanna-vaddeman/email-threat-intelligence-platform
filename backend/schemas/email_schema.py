from pydantic import (

    BaseModel,

    Field
)

from typing import Dict


# =========================================================
# REQUEST SCHEMA
# =========================================================

class EmailRequest(

    BaseModel
):

    """

    Input email payload.

    """

    email_text: str = Field(

        ...,

        min_length=1,

        description=(

            "Raw email text "
            "for spam prediction"
        )
    )


# =========================================================
# RESPONSE SCHEMA
# =========================================================

class EmailResponse(

    BaseModel
):

    """

    Prediction response.

    """

    prediction: str

    spam_probability: float

    threat_level: str

    features: Dict[

        str,

        float
    ]