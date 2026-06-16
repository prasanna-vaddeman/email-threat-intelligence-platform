from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_invalid_request():

    response = client.post(

        "/email/predict",

        json={}

    )

    assert response.status_code == 422