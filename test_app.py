import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "Hello from AWS ECS!"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_echo_endpoint():
    response = client.post("/echo", json={"msg": "DevOps Rocks"})
    assert response.status_code == 200
    assert response.json() == {"received": "DevOps Rocks"}
