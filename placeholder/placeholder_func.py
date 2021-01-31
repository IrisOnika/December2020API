from conftest import api_client_base
# import pytest
import random

rand = str(random.randint(1, 100))

host = 'https://jsonplaceholder.typicode.com'
rand_pst = f'/posts/{rand}'
host_ = f'{host}/posts/'
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


def placeholder_api(path=host):
    ap = api_client_base(path)
    return ap

#@pytest.fixture()
#def create_placeholder(paht, body, )