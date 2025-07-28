import allure
from apis.base_api import BaseAPI

class UsersAPI(BaseAPI):
    """API methods for interacting with the /users endpoints."""

    @allure.step("List users, page={page}")
    def list_users(self, page: int = 1):
        """Get a list of users with pagination."""
        return self.request("get", "/api/users", params={"page": page})

    @allure.step("Get single user, id={user_id}")
    def get_single_user(self, user_id: int):
        """Retrieve a specific user by ID."""
        return self.request("get", f"/api/users/{user_id}")

    @allure.step("Create user with name={name} and job={job}")
    def create_user(self, name: str, job: str):
        """Create a new user."""
        json_data = {"name": name, "job": job}
        return self.request("post", "/api/users", json=json_data)

    @allure.step("Update user PUT, id={user_id}")
    def update_user_put(self, user_id: int, data: dict):
        """Fully update user data (PUT)."""
        return self.request("put", f"/api/users/{user_id}", json=data)

    @allure.step("Update user PATCH, id={user_id}")
    def update_user_patch(self, user_id: int, data: dict):
        """Partially update user data (PATCH)."""
        return self.request("patch", f"/api/users/{user_id}", json=data)

    @allure.step("Delete user, id={user_id}")
    def delete_user(self, user_id: int):
        """Delete a user by ID."""
        return self.request("delete", f"/api/users/{user_id}")

    @allure.step("Delayed response with delay={delay}")
    def delayed_response(self, delay: int):
        """Simulate a delayed server response."""
        return self.request("get", "/api/users", params={"delay": delay})



