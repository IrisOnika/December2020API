from conftest import api_client_base
import pytest

host = 'https://jsonplaceholder.typicode.com'
host1 = 'https://dog.ceo/api/breed'
list_all = '/list/all'
random1 = '/image/random'
random1_result = 'https://images.dog.ceo/breeds/'


def placeholder_api(path=host):
    ap = api_client_base(path)
    return ap

@pytest.fixture()
def create_placeholder(paht, bodi, )