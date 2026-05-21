"""
Backend Communication
"""

import os
import requests


API = os.getenv(
    "BACKEND_URL",
    "https://email-threat-intelligence-platform-production.up.railway.app"
).rstrip("/")


def predict_email(text: str):

    try:

        response = requests.post(

            f"{API}/email/predict",

            json={
                "email_text": text
            },

            timeout=60

        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        return {

            "prediction": "ERROR",

            "spam_probability": 0,

            "threat_score": 0,

            "links_found": 0,

            "html_tags": 0,

            "uppercase_ratio": 0,

            "exclamation_count": 0,

            "threat_level": "UNKNOWN",

            "error": str(e)

        }