"""
WhyLogs Monitoring
"""

import whylogs as why
import pandas as pd
import logging

from pathlib import Path
from datetime import datetime


LOGGER = logging.getLogger(__name__)


# ===================================
# PROFILE STORAGE LOCATION
# ===================================

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


# ===================================
# LOG PREDICTION
# ===================================

def log_prediction(

    prediction_data: dict

):

    """
    Store monitoring profile locally.

    WhyLogs captures inference
    metadata for monitoring.

    """

    try:

        dataframe = pd.DataFrame(

            [prediction_data]

        )

        profile = why.log(

            dataframe

        )

        timestamp = (

            datetime.now()

            .strftime(

                "%Y%m%d_%H%M%S_%f"

            )

        )

        profile_path = (

            LOG_DIR

            /

            f"profile_{timestamp}.bin"

        )

        # Save monitoring profile

        profile.write(

            str(profile_path)

        )

        LOGGER.info(

            f"Profile saved: {profile_path}"

        )

    except Exception as e:

        LOGGER.exception(

            f"Monitoring failed: {e}"

        )