from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, GitHub Actions!"}

def test_square_number():
    response = client.get("/square/5")
    assert response.status_code == 200
    assert response.json() == {"number": 5, "square": 25}
