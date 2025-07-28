import pytest
from apis.auth_api import AuthAPI
from apis.users_api import UsersAPI
from apis.resource_api import ResourceAPI


@pytest.fixture(scope="session")
def users_api():
    """Fixture that provides an instance of UsersAPI for testing user-related endpoints."""
    return UsersAPI()


@pytest.fixture(scope="session")
def auth_api():
    """Fixture that provides an instance of AuthAPI for testing authentication endpoints."""
    return AuthAPI()


@pytest.fixture(scope="session")
def resource_api():
    """Fixture that provides an instance of ResourceAPI for testing resource-related endpoints."""
    return ResourceAPI()
