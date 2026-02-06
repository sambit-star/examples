from datetime import datetime, timezone

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_current_time_returns_200():
    response = client.get("/current-time")
    assert response.status_code == 200


def test_get_current_time_has_current_time_key():
    response = client.get("/current-time")
    data = response.json()
    assert "current_time" in data


def test_get_current_time_returns_valid_iso_format():
    response = client.get("/current-time")
    data = response.json()
    parsed = datetime.fromisoformat(data["current_time"])
    assert parsed.tzinfo is not None


def test_get_current_time_is_recent():
    before = datetime.now(timezone.utc)
    response = client.get("/current-time")
    after = datetime.now(timezone.utc)
    data = response.json()
    returned_time = datetime.fromisoformat(data["current_time"])
    assert before <= returned_time <= after
