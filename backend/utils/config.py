"""
Application Configuration
"""

import os

from dotenv import load_dotenv


# Load .env

load_dotenv()


# Spam threshold

SPAM_THRESHOLD = float(

    os.getenv(

        "SPAM_THRESHOLD",

        "0.70"

    )

)