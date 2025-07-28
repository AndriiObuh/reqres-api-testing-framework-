import pytest
import allure


def test_get_single_user_not_found(users_api):
    """Verify that requesting a non-existent user returns 404."""
    response = users_api.get_single_user(9999)
    assert response.status_code == 404


@pytest.mark.xfail(reason="reqres.in returns 200 instead of 404 for PUT to non-existent users")
@allure.title("Update non-existent user with PUT should return 404")
def test_update_user_put_not_found(users_api):
    """Verify that updating a non-existent user with PUT returns 404."""
    response = users_api.update_user_put(9999, {"name": "Patrick Vieira", "job": "Captain"})
    assert response.status_code == 404


@pytest.mark.xfail(reason="reqres.in returns 200 instead of 404 for PATCH to non-existent users")
@allure.title("Update non-existent user with PATCH should return 404")
def test_update_user_patch_not_found(users_api):
    """Verify that updating a non-existent user with PATCH returns 404."""
    response = users_api.update_user_patch(9999, {"job": "Midfielder"})
    assert response.status_code == 404


def test_delete_user_not_found(users_api):
    """Verify that deleting a non-existent user returns 204 (No Content)."""
    response = users_api.delete_user(9999)
    assert response.status_code == 204
