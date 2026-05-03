
import sys
import os

# Dit à Python où trouver app.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app
import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Hello CI/CD, this is my first CI-CD" in r.data

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert b"healthy" in r.data