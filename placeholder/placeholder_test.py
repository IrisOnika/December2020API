from placeholder.placeholder_func import *
from conftest import open_read
import cerberus
import re
import pytest


@pytest.mark.parametrize("url", url_list)
def test_status(placeholder_api, url):
    """тест на проверку статусов ответов всех страниц сервиса"""
    res = placeholder_api.status(path=url)
    assert res == '200'


@pytest.mark.parametrize(("url", "schema_file"), schema_list)
def test_schema(placeholder_api, url, schema_file):
    """тест на проверку схем всех страниц сервиса"""
    res = placeholder_api.text_dict(path=url)
    res = [res] if type(res) != list else res
    schema = open_read(f'placeholder/schema_{schema_file}.json')
    v = cerberus.Validator(schema)
    for res_item in res:
        assert v.validate(res_item)


def test_create(placeholder_api):
    """тест на проверку создания новой записи (метод post)"""
    ph_create = placeholder_api.post(path=posts, params=None, data=None, json=new_placeholder, headers=headers_create)
    res = ph_create.json()
    res_status = ph_create.status_code
    expected_res = open_read(f'placeholder/new_placeholder_result.json')
    assert res_status == 201
    assert expected_res == res


@pytest.mark.parametrize(("p_id", "stat", "exp_res"), [("0", 500, 'skip'),
                                                       ("11", 200, update_placeholder),
                                                       ("101", 500, 'skip')])
def test_update(placeholder_api, p_id, stat, exp_res):
    """тест на проверку обновления записи (метод put)"""
    ph_update = placeholder_api.update(path=f'{posts}{p_id}', params=None, data=None, json=update_placeholder)
    res_status = ph_update.status_code
    assert res_status == stat
    if res_status == 200:
        assert ph_update.json() == exp_res


def test_delete(placeholder_api):
    """тест на удаление записи метод delete"""
    ph_detete = placeholder_api.ph_delete()
    print(f'результат удаления записи: {ph_detete.json()}')
    assert ph_detete.json() == {}