import allure
from apis.base_api import BaseAPI

class AuthAPI(BaseAPI):
    """Encapsulate API methods for user authentication (register and login)."""

    @allure.step("Register user with email={email}")
    def register_user(self, email: str, password: str = None):
        """Register a new user (POST)."""
        json_data = {"email": email}
        if password is not None:
            json_data["password"] = password
        return self.request("post", "/api/register", json=json_data)

    @allure.step("Login user with email={email}")
    def login_user(self, email: str, password: str = None):
        """Login existing user (POST)."""
        json_data = {"email": email}
        if password is not None:
            json_data["password"] = password
        return self.request("post", "/api/login", json=json_data)