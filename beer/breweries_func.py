import pytest
from conftest import api_client_base


host = 'https://api.openbrewerydb.org/breweries'
host1 = 'https://api.openbrewerydb.org/breweries?'
search_query = '/search?query='
autocomplete_query = '/autocomplete?query='


@pytest.fixture
def brewer_api(path=host):
    ap = api_client_base(path)
    return ap
