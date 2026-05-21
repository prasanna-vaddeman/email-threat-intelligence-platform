"""
Configuration Settings
"""

import os

from dotenv import load_dotenv


load_dotenv()


SPAM_THRESHOLD = float(

    os.getenv(

        "SPAM_THRESHOLD",

        0.70

    )

)