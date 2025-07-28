def test_register_user_missing_password(auth_api):
    """Verify that registering without a password returns 400 and proper error message."""
    response = auth_api.register_user("sydney@fife")
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert data["error"] == "Missing password"

def test_login_user_missing_password(auth_api):
    """Verify that logging in without a password returns 400 and proper error message."""
    res = auth_api.login_user("peter@klaven")
    assert res.status_code == 400
    data = res.json()
    assert "error" in data
    assert data["error"] == "Missing password"