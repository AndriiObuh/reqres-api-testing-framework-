import time
import pytest


def test_list_users(users_api):
    """Test list of users for status 200 and valid data."""
    response = users_api.list_users(2)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert data["page"] == 2

def test_get_single_user(users_api):
    """"Test getting single user by ID returns correct user."""
    response = users_api.get_single_user(2)
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2

def test_create_user(users_api):
    """Test creating user returns status 201 and contains correct fields."""
    response = users_api.create_user("Thierry Henry", "Forward")
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Thierry Henry"
    assert data["job"] == "Forward"
    assert "id" in data
    assert "createdAt" in data

def test_update_user_put(users_api):
    """Test full update (PUT) of user returns updated data."""
    response = users_api.update_user_put(2, {"name": "Patrick Vieira", "job": "Captain"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Patrick Vieira"
    assert data["job"] == "Captain"

def test_update_user_patch(users_api):
    """Test partial update (PATCH) of user updates only specific fields."""
    response = users_api.update_user_patch(2, {"job": "Midfielder"})
    assert response.status_code == 200
    data = response.json()
    assert data["job"] == "Midfielder"


def test_delete_user(users_api):
    """Test deleting a user returns status 204 (No Content)."""
    response = users_api.delete_user(2)
    assert response.status_code == 204
    assert response.content == b""


def test_delayed_response(users_api):
    """Test delayed response returns data and status 200."""
    start = time.time()
    response = users_api.delayed_response(3)
    end = time.time()
    duration = end - start
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    # Check the response was delayed for at least 3 seconds (with a margin)
    assert duration >= 3, f"Expected delay >= 3, but got {duration:.2f}s"






