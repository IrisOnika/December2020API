import pytest
from conftest import api_client


@pytest.fixture
def site(request):
    ap = api_client(request)
    return ap