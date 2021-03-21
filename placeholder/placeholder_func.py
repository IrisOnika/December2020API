from conftest import api_client_base
from conftest import open_read
import random
import pytest

rand = str(random.randint(1, 100))

host = 'https://jsonplaceholder.typicode.com'
rand_pst = f'/posts/{rand}'
posts = f'/posts/'
rand_comments = f'{rand_pst}/comments'
rand_photos = f'/albums/{rand}/photos'
rand_album = f'/users/{rand}/albums'
rand_todo = f'/users/{rand}/todos'
rand_user_posts = f'/users/{rand}/posts'
albums = f'{host}/albums/'
users = f'{host}/users/'

url_list = [rand_pst, rand_comments, rand_photos, rand_album, rand_todo, rand_user_posts]
schema_list = [(rand_pst, 'rand_pst'),
               (rand_comments, 'rand_comments'),
               (rand_photos, 'rand_photos'),
               (rand_album, 'rand_album'),
               (rand_todo, 'rand_todo'),
               (rand_user_posts, 'rand_user_posts')]

headers_create = {'Content-type': 'application/json; charset=UTF-8'}

new_placeholder = open_read(f'placeholder/new_placeholder.json')
update_placeholder = open_read(f'placeholder/update_placeholder.json')


@pytest.fixture
def placeholder_api(path=host):
    ap = api_client_base(path)
    return ap
