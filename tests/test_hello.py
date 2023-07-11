import pytest
from src.hello import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<p>Hello, World!</p>" in response.data