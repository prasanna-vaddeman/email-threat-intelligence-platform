"""
WhyLogs + WhyLabs
"""

import whylogs as why
import pandas as pd
import logging

from pathlib import Path
from datetime import datetime

from monitoring.whylabs_config import (
    WHYLABS_API_KEY,
    WHYLABS_ORG_ID,
    WHYLABS_DATASET_ID
)

LOGGER = logging.getLogger(__name__)

LOG_DIR = (
    Path(__file__)
    .resolve()
    .parent
    / "logs"
    / "profiles"
)

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True
)

# Initialize writer only if credentials are available
writer = None
try:
    from whylabs_client import WhyLabsWriter

    if WHYLABS_API_KEY and WHYLABS_ORG_ID and WHYLABS_DATASET_ID:
        writer = WhyLabsWriter(
            api_key=WHYLABS_API_KEY,
            org_id=WHYLABS_ORG_ID,
            dataset_id=WHYLABS_DATASET_ID
        )
except ImportError:
    LOGGER.warning("WhyLabsWriter not available, monitoring will save locally only")


def log_prediction(prediction_data: dict):
    """
    Log prediction data to WhyLogs and optionally to WhyLabs
    """
    try:
        dataframe = pd.DataFrame([prediction_data])
        profile = why.log(dataframe)

        timestamp = (
            datetime.now()
            .strftime("%Y%m%d_%H%M%S_%f")
        )

        profile_path = (
            LOG_DIR / f"profile_{timestamp}.bin"
        )

        # Save profile locally
        profile.write(str(profile_path))
        LOGGER.info(f"Profile saved locally: {profile_path}")

        # Upload to WhyLabs if writer is available
        if writer is not None:
            try:
                profile.view().write(writer)
                LOGGER.info("Profile uploaded to WhyLabs")
            except Exception as e:
                LOGGER.error(f"Failed to upload to WhyLabs: {e}")
        else:
            LOGGER.debug("WhyLabs writer not configured, skipping upload")

    except Exception as e:
        LOGGER.error(f"Error logging prediction: {e}")