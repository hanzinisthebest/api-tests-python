import pytest
from utils.jsonplaceholder_client import JSONPlaceholderClient
from utils.fakestore_client import FakeStoreClient

@pytest.fixture
def jsonplaceholder_api():
    return JSONPlaceholderClient()

@pytest.fixture
def fakestore_api():
    return FakeStoreClient() 