"""
Inference Pipeline
"""

import time
import joblib

from pathlib import Path

from backend.utils.logger import logger

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

from backend.storage.prediction_store import (
    save_prediction
)

from backend.monitoring.metrics import (
    PREDICTION_COUNTER,
    SPAM_COUNTER,
    ERROR_COUNTER,
    LATENCY
)

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

logger.info(
    f"Model loaded: {MODEL_PATH.name}"
)

def predict_email(
    email_text: str
) -> dict:

    start = time.time()

    logger.info(
        "Inference pipeline started"
    )

    try:

        email_text = (
            email_text
            or ""
        )

        cleaned = clean_text(
            email_text
        )

        logger.info(
            "Text preprocessing completed"
        )

        vector = vectorize_email(
            cleaned,
            email_text
        )

        logger.info(
            "Feature engineering completed"
        )

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

        logger.info(
            f"Prediction={prediction} | "
            f"Probability={probability:.4f}"
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
                1 - probability
            ) * 100,
            2
        )

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

        inference_ms = round(
            (
                time.time()
                - start
            ) * 1000,
            2
        )

        logger.info(
            f"Inference latency={inference_ms} ms"
        )

        threat_level = calculate_risk(
            threat_score
        )

        # ======================
        # PROMETHEUS
        # ======================

        PREDICTION_COUNTER.inc()

        if prediction == "spam":
            SPAM_COUNTER.inc()

        LATENCY.observe(
            inference_ms
        )

        # ======================
        # WHYLOGS
        # ======================

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

        except Exception as exc:

            logger.exception(
                f"WhyLogs monitoring failure: {exc}"
            )

        # ======================
        # DATABASE
        # ======================

        try:

            save_prediction(

                prediction=
                prediction,

                spam_probability=
                probability_percent,

                threat_score=
                threat_score,

                confidence=
                confidence,

                threat_level=
                threat_level,

                latency_ms=
                inference_ms,

                links_found=
                int(
                    features["url_count"]
                ),

                url_count=
                features["url_count"],

                html_tag_count=
                features["html_tag_count"],

                uppercase_ratio=
                features["uppercase_ratio"],

                special_char_count=
                features["special_char_count"],

                spam_keyword_count=
                features["spam_keyword_count"],

                exclamation_count=
                features["exclamation_count"]

            )

            logger.info(
                "Prediction stored in Supabase"
            )

        except Exception as exc:

            ERROR_COUNTER.inc()

            logger.exception(
                f"Database save failed: {exc}"
            )

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

    except Exception as exc:

        ERROR_COUNTER.inc()

        logger.exception(
            f"Inference pipeline failed: {exc}"
        )

        raise