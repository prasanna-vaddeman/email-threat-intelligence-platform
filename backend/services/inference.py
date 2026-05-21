"""
Inference Pipeline
"""

import time
import joblib
import logging

from pathlib import Path

from backend.services.preprocessing import (
    clean_text
)

from backend.services.vectorization import (
    vectorize_email
)

from backend.utils.config import (
    SPAM_THRESHOLD
)

from backend.utils.threat_utils import (
    calculate_risk
)

from backend.services.feature_engineering import (

    count_urls,

    count_html_tags,

    count_special_chars,

    count_spam_keywords,

    uppercase_ratio,

    count_exclamations

)

from monitoring.monitoring_service import (

    monitor_inference

)


# ===================================================
# LOGGER
# ===================================================

LOGGER = logging.getLogger(

    __name__

)


# ===================================================
# MODEL LOADING
# ===================================================

BASE_DIR = (

    Path(__file__)

    .resolve()

    .parents[2]

)

MODEL_PATH = (

    BASE_DIR

    / "models"

    / "advanced_xgboost_model.pkl"

)


if not MODEL_PATH.exists():

    raise FileNotFoundError(

        f"Missing model:\n{MODEL_PATH}"

    )


MODEL = joblib.load(

    MODEL_PATH

)


# ===================================================
# PREDICTION PIPELINE
# ===================================================

def predict_email(

    email_text: str

) -> dict:

    """
    Predict email threat.

    Args:

        email_text:

            Raw email content.

    Returns:

        Prediction response.
    """

    start = time.time()


    # ==========================
    # EMPTY INPUT PROTECTION
    # ==========================

    email_text = (

        email_text

        or ""

    )


    # ==========================
    # PREPROCESSING
    # ==========================

    cleaned = clean_text(

        email_text

    )


    # ==========================
    # VECTORIZATION
    # ==========================

    vector = vectorize_email(

        cleaned,

        email_text

    )


    # ==========================
    # MODEL PREDICTION
    # ==========================

    probability = float(

        MODEL

        .predict_proba(

            vector

        )[0][1]

    )


    prediction = (

        "spam"

        if probability >= SPAM_THRESHOLD

        else "ham"

    )


    probability_percent = round(

        probability * 100,

        2

    )


    threat_score = int(

        probability_percent

    )


    confidence = round(

        max(

            probability,

            1 -

            probability

        ) * 100,

        2

    )


    # ==========================
    # FEATURE EXTRACTION
    # ==========================

    features = {

        "url_count":

            count_urls(

                email_text

            ),

        "html_tag_count":

            count_html_tags(

                email_text

            ),

        "uppercase_ratio":

            round(

                uppercase_ratio(

                    email_text

                ),

                4

            ),

        "special_char_count":

            count_special_chars(

                email_text

            ),

        "spam_keyword_count":

            count_spam_keywords(

                email_text

            ),

        "exclamation_count":

            count_exclamations(

                email_text

            )

    }


    # ==========================
    # LATENCY
    # ==========================

    inference_ms = round(

        (

            time.time()

            - start

        )

        * 1000,

        2

    )


    threat_level = calculate_risk(

        threat_score

    )


    # ==========================
    # MONITORING
    # ==========================

    try:

        monitor_inference(

            prediction=

                prediction,

            threat_score=

                threat_score,

            confidence=

                confidence,

            features=

                features

        )

    except Exception:

        LOGGER.exception(

            "Monitoring failure"

        )


    # ==========================
    # RESPONSE
    # ==========================

    return {

        "prediction":

            prediction,

        "spam_probability":

            probability_percent,

        "threat_score":

            threat_score,

        "confidence":

            confidence,

        "inference_ms":

            inference_ms,

        "threat_level":

            threat_level,

        "features":

            features

    }