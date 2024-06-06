import pytest
from fastapi.testclient import TestClient
import hashlib
import sys
import os

# Append the path to the directory containing the app
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from main import app

client = TestClient(app)


def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "localhost"}


def test_user_hash():
    user_id = "123"
    response = client.get(f"/user_hash?user_id={user_id}")
    assert response.status_code == 200
    expected_hash = hashlib.sha1(
        (user_id + os.environ.get("USER_SALT", "")).encode()
    ).hexdigest()
    assert response.json() == expected_hash


@pytest.mark.parametrize("user_id", ["abc", "456", ""])
def test_user_hash_with_different_user_ids(user_id):
    response = client.get(f"/user_hash?user_id={user_id}")
    assert response.status_code == 200
    expected_hash = hashlib.sha1(
        (user_id + os.environ.get("USER_SALT", "")).encode()
    ).hexdigest()
    assert response.json() == expected_hash


if __name__ == "__main__":
    pytest.main()
