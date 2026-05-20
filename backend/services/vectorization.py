# =========================================================
# IMPORT LIBRARIES
# =========================================================

import joblib

from pathlib import Path

from scipy.sparse import (

    hstack,

    csr_matrix
)

from backend.services.feature_engineering import (

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

ARTIFACT_DIR = (

    BASE_DIR
    / "artifacts"
)


# =========================================================
# VALIDATE ARTIFACT DIRECTORY
# =========================================================

if not ARTIFACT_DIR.exists():

    raise FileNotFoundError(

        f"Artifact directory missing:\n"

        f"{ARTIFACT_DIR}"
    )


# =========================================================
# ARTIFACT FILE PATHS
# =========================================================

VECTORIZER_PATH = (

    ARTIFACT_DIR

    / "advanced_hybrid_tfidf_vectorizer.pkl"
)

SCALER_PATH = (

    ARTIFACT_DIR

    / "advanced_manual_feature_scaler.pkl"
)


# =========================================================
# VALIDATE ARTIFACT FILES
# =========================================================

if not VECTORIZER_PATH.exists():

    raise FileNotFoundError(

        f"Missing vectorizer artifact:\n"

        f"{VECTORIZER_PATH}"
    )

if not SCALER_PATH.exists():

    raise FileNotFoundError(

        f"Missing scaler artifact:\n"

        f"{SCALER_PATH}"
    )


# =========================================================
# LOAD ARTIFACTS
# =========================================================

"""
Load artifacts once during startup.

Avoid loading during
every API request.

Improves API latency.

Startup loading prevents
repeated disk access.
"""

advanced_vectorizer = joblib.load(

    VECTORIZER_PATH
)

advanced_scaler = joblib.load(

    SCALER_PATH
)


# =========================================================
# EMAIL VECTORIZATION PIPELINE
# =========================================================

def vectorize_email(

    cleaned_text: str,

    raw_email: str

) -> csr_matrix:

    """

    Converts email into
    model-ready sparse matrix.

    Pipeline:

    1. TF-IDF transform

    2. Manual feature extraction

    3. Feature scaling

    4. Sparse matrix combine

    Args:

        cleaned_text (str)

            NLP cleaned email

        raw_email (str)

            Original email

    Returns:

        csr_matrix

            Final feature vector

    """

    # =====================================================
    # EMPTY INPUT PROTECTION
    # =====================================================

    cleaned_text = (

        cleaned_text

        if cleaned_text

        else ""
    )

    raw_email = (

        raw_email

        if raw_email

        else ""
    )

    # =====================================================
    # TF-IDF FEATURES
    # =====================================================

    text_vector = (

        advanced_vectorizer
        .transform(

            [cleaned_text]
        )
    )

    # =====================================================
    # MANUAL FEATURES
    # =====================================================

    manual_features = (

        build_manual_features(

            raw_email
        )
    )

    # =====================================================
    # SCALE FEATURES
    # =====================================================

    scaled_manual = (

        advanced_scaler
        .transform(

            manual_features
        )
    )

    # =====================================================
    # COMBINE FEATURES
    # =====================================================

    combined_features = hstack(

        [

            text_vector,

            scaled_manual

        ],

        format="csr"

    )

    # =====================================================
    # RETURN FINAL VECTOR
    # =====================================================

    return combined_features