from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_trains():

    response = client.get("/api/trains")

    assert response.status_code == 200
