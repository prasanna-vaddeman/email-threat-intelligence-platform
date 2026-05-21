"""
Backend Communication
"""

import os
import requests


API=os.getenv(

    "BACKEND_URL",

    "http://127.0.0.1:8000"

)


def predict_email(

    text:str

):

    try:

        response=requests.post(

            f"{API}/email/predict",

            json={

                "email_text":text

            },

            timeout=30

        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        return {

            "prediction":"ERROR",

            "spam_probability":0,

            "threat_score":0,

            "links_found":0,

            "html_tags":0,

            "uppercase_ratio":0,

            "exclamation_count":0,

            "threat_level":"UNKNOWN",

            "error":str(e)

        }