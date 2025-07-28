def test_register_user_success(auth_api):
    """Verify that registering a user returns 200 and contains id and token."""
    response = auth_api.register_user("eve.holt@reqres.in", "pistol")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "token" in data

def test_login_user_success(auth_api):
    """Verify that logging in a user returns 200 and contains token."""
    response = auth_api.login_user("eve.holt@reqres.in", "cityslicka")
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

