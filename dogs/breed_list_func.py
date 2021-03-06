from conftest import api_client_base
import pytest


host = 'https://dog.ceo/api/breeds'
host1 = 'https://dog.ceo/api/breed'
list_all = '/list/all'
random1 = '/image/random'
random1_result = 'https://images.dog.ceo/breeds/'


@pytest.fixture()
def dogs_api(path=host):
    ap = api_client_base(path)
    return ap


@pytest.fixture()
def dog_api(path=host1):
    ap = api_client_base(path)
    return ap