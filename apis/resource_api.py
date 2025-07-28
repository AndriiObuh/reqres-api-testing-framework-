import allure
from apis.base_api import BaseAPI


class ResourceAPI(BaseAPI):
    """Encapsulate API method for working with resources (list and single resource)."""

    @allure.step("List resources")
    def list_resources(self):
        """Retrieve a list of all available resources."""
        return self.request("get", "/api/unknown")

    @allure.step("Get single resource, id={resource_id}")
    def get_single_resource(self, resource_id: int):
        """Retrieve a specific resource by ID."""
        return self.request("get", f"/api/unknown/{resource_id}")
