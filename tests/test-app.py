import os
import sys

# Allow Python to find app.py in the parent directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Payment application is running"


def test_version():
    client = app.test_client()

    response = client.get("/version")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "payment"
    assert "version" in data
    assert "git_commit" in data
    assert "branch" in data