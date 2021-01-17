import pytest
from json import loads
from api_client import APIClient
import os.path


def api_client(requests):
    base_url = requests.config.getoption("--url")
    return APIClient(base_address=base_url)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        default="200",
        help="This is default status code"
    )
    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="This is method for execute"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def code(request):
    return request.config.getoption("--status_code")


@pytest.fixture
def site(request):
    ap = api_client(request)
    return ap