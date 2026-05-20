# =========================================================
# IMPORT LIBRARIES
# =========================================================

import joblib

from pathlib import Path

from backend.services.preprocessing import (

    clean_text
)

from backend.services.vectorization import (

    vectorize_email
)

from backend.services.feature_engineering import (

    get_threat_level,

    build_manual_features
)


# =========================================================
# PROJECT PATHS
# =========================================================

BASE_DIR = (

    Path(__file__)
    .resolve()
    .parents[2]
)

MODEL_DIR = (

    BASE_DIR
    / "models"
)

ARTIFACT_DIR = (

    BASE_DIR
    / "artifacts"
)


# =========================================================
# VALIDATE DIRECTORIES
# =========================================================

if not MODEL_DIR.exists():

    raise FileNotFoundError(

        f"Models directory missing:\n"

        f"{MODEL_DIR}"
    )

if not ARTIFACT_DIR.exists():

    raise FileNotFoundError(

        f"Artifacts directory missing:\n"

        f"{ARTIFACT_DIR}"
    )


# =========================================================
# MODEL FILE PATHS
# =========================================================

MODEL_PATH = (

    MODEL_DIR

    / "advanced_xgboost_model.pkl"
)

LABEL_ENCODER_PATH = (

    ARTIFACT_DIR

    / "advanced_hybrid_label_encoder.pkl"
)


# =========================================================
# VALIDATE MODEL FILES
# =========================================================

if not MODEL_PATH.exists():

    raise FileNotFoundError(

        f"Missing model artifact:\n"

        f"{MODEL_PATH}"
    )

if not LABEL_ENCODER_PATH.exists():

    raise FileNotFoundError(

        f"Missing label encoder artifact:\n"

        f"{LABEL_ENCODER_PATH}"
    )


# =========================================================
# LOAD MODEL ARTIFACTS
# =========================================================

"""
Load artifacts once during startup.

Avoid repeated loading
during API requests.

Reduces inference latency.

Improves deployment stability.
"""

advanced_model = joblib.load(

    MODEL_PATH
)

advanced_label_encoder = joblib.load(

    LABEL_ENCODER_PATH
)


# =========================================================
# INFERENCE CONFIGURATION
# =========================================================

SPAM_THRESHOLD = 0.70


# =========================================================
# MAIN INFERENCE PIPELINE
# =========================================================

def predict_email(

    email_text: str

) -> dict:

    """

    Predict email threat.

    Pipeline:

    1. Clean text

    2. Feature engineering

    3. Vectorization

    4. Probability prediction

    5. Threshold decision

    6. Threat scoring

    7. Response generation

    Args:

        email_text (str)

    Returns:

        dict

    """

    # =====================================================
    # INPUT PROTECTION
    # =====================================================

    email_text = (

        email_text

        if email_text

        else ""
    )

    # =====================================================
    # CLEAN EMAIL
    # =====================================================

    cleaned_email = (

        clean_text(

            email_text
        )
    )

    # =====================================================
    # FEATURE VECTOR
    # =====================================================

    features = (

        vectorize_email(

            cleaned_email,

            email_text
        )
    )

    # =====================================================
    # MODEL INFERENCE
    # =====================================================

    try:

        spam_probability = float(

            advanced_model

            .predict_proba(

                features

            )[0][1]
        )

    except Exception as error:

        raise RuntimeError(

            f"Model inference failed: "

            f"{str(error)}"

        ) from error

    # =====================================================
    # THRESHOLD DECISION
    # =====================================================

    prediction = (

        1

        if spam_probability

        >= SPAM_THRESHOLD

        else 0
    )

    # =====================================================
    # LABEL DECODING
    # =====================================================

    label = (

        advanced_label_encoder

        .inverse_transform(

            [prediction]

        )[0]
    )

    # =====================================================
    # THREAT LEVEL
    # =====================================================

    threat_level = (

        get_threat_level(

            spam_probability
        )
    )

    # =====================================================
    # FEATURE EXPLAINABILITY
    # =====================================================

    manual_features = (

        build_manual_features(

            email_text
        )
    )

    # =====================================================
    # RESPONSE OBJECT
    # =====================================================

    return {

        "prediction": label,

        "spam_probability": round(

            spam_probability,

            4
        ),

        "threat_level": threat_level,

        "features": {

            key:

            round(

                float(value),

                4

            )

            for key,

            value

            in manual_features

            .iloc[0]

            .items()
        }
    }