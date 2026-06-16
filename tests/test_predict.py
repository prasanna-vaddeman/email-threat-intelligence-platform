from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_prediction():

    payload = {

        "email_text":

        """
        Congratulations!

        You won a free iPhone.

        Click now.
        """

    }

    response = client.post(

        "/email/predict",

        json=payload

    )

    assert response.status_code == 200

    data = response.json()

    assert data["prediction"] in [

        "spam",

        "ham"

    ]

    assert (

        0 <= data["spam_probability"] <= 100

    )

    assert data["threat_level"] in [

        "LOW",

        "MEDIUM",

        "HIGH",

        "CRITICAL"

    ]