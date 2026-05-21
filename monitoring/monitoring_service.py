"""
Monitoring Service
"""

from monitoring.whylogs_logger import (

    log_prediction

)

import logging


LOGGER = logging.getLogger(

    __name__

)


def monitor_inference(

    prediction: str,

    threat_score: int,

    confidence: float,

    features: dict

) -> None:

    payload = {

        "prediction":

            prediction,

        "threat_score":

            threat_score,

        "confidence":

            confidence,

        **features

    }

    LOGGER.info(

        "Monitoring payload created"

    )

    log_prediction(

        payload

    )

    LOGGER.info(

        "WhyLogs profile saved"

    )