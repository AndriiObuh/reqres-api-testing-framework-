def test_list_resources(resource_api):
    """Verify that listing resources returns a list of items with status 200."""
    response = resource_api.list_resources()
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)

def test_get_single_resource(resource_api):
    """Verify that retrieving a specific resource by ID returns correct data."""
    response = resource_api.get_single_resource(2)
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == 2