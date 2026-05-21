"""
WhyLogs + WhyLabs
"""

import whylogs as why
import pandas as pd

from pathlib import Path
from datetime import datetime

from whylabs_client import WhyLabsWriter

from monitoring.whylabs_config import (

    WHYLABS_API_KEY,

    WHYLABS_ORG_ID,

    WHYLABS_DATASET_ID

)


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


writer = WhyLabsWriter(

    api_key=

        WHYLABS_API_KEY,

    org_id=

        WHYLABS_ORG_ID,

    dataset_id=

        WHYLABS_DATASET_ID

)


def log_prediction(

    prediction_data:dict

):

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

    profile.write(

        str(

            profile_path

        )

    )

    profile.view().write(

        writer

    )

    print(

        "Uploaded to WhyLabs"

    )