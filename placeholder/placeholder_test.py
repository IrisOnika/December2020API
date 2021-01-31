from placeholder.placeholder_func import *
from conftest import open_read
import cerberus
import re
import pytest


@pytest.mark.parametrize("url", url_list)
def test_status(url):
    """тест на проверку статусов ответов всех страниц сервиса"""
    ap = placeholder_api()
    res = ap.status(path=url)
    assert res == '200'


@pytest.mark.parametrize(("url", "schema_file"), schema_list)
def test_schema(url, schema_file):
    """тест на проверку схем всех страниц сервиса"""
    ap = placeholder_api()
    res = ap.text_dict(path=url)
    res = [res] if type(res) != list else res
    schema = open_read(f'placeholder/schema_{schema_file}.json')
    v = cerberus.Validator(schema)
    for res_item in res:
        assert v.validate(res_item)


def test_create():
    """тест на проверку создания новой записи (метод post)"""
    pass
    # после создания не забыть удалить тестовую запись


def test_update():
    """тест на проверку обновления записи (метод patch)"""
    pass
    # после создания не забыть удалить тестовую запись


def test_delete():
    """тест на удаление записи метод delete"""
    # создание записи попытаться запихнуть в фикстуру
    pass