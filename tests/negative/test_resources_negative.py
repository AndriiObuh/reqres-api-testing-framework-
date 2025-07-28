def test_get_single_resource_not_found(resource_api):
    """Verify that requesting a non-existent resource returns 404."""
    response = resource_api.get_single_resource(9999)
    assert response.status_code == 404