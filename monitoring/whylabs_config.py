"""
WhyLabs Configuration
"""

from dotenv import load_dotenv

import os


load_dotenv()


WHYLABS_API_KEY = os.getenv(

    "WHYLABS_API_KEY"

)

WHYLABS_ORG_ID = os.getenv(

    "WHYLABS_ORG_ID"

)

WHYLABS_DATASET_ID = os.getenv(

    "WHYLABS_DATASET_ID"

)