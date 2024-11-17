import pytest
from health import app #as we have filename nearby the tests we can simplify

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_status(client):
    response = client.get("/status")
    assert response.status_code in [200, 500]  # Healthy returns 200, unhealthy returns 500
    data = response.get_json()
    assert "status" in data

def test_height(client):
    response = client.get("/height")
    assert response.status_code == 200
    data = response.get_json()
    assert "geth_height" in data

def test_peers(client):
    response = client.get("/peers")
    assert response.status_code == 200
    data = response.get_json()
    assert "peer_count" in data

def test_all(client):
    response = client.get("/all")
    assert response.status_code == 200
    data = response.get_json()
    assert "geth_height" in data
    assert "lighthouse_height" in data
    assert "peer_count" in data
