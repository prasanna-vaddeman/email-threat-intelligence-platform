from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_metrics():

    response = client.get(
        "/metrics"
    )

    assert response.status_code == 200

    assert (
        "email_predictions_total"
        in response.text
    )