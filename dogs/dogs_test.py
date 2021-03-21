from dogs.breed_list_func import *
from conftest import open_read
import pytest
import re


def test_check_breeds_list(dogs_api):
    """проверка возвращаемого списка пород"""
    res = dogs_api.text_dict(path=list_all)
    breed_list_dict = res.get("message")
    breeds_list = open_read('dogs/breеd_list.json')
    assert breed_list_dict == breeds_list


def test_breed_rand(dogs_api):
    """проверка метода random - возвращает одну рандомную фотографию"""
    res = dogs_api.text_dict(path=random1)
    rand1 = res.get("message")
    # Проверяем, что в message одна строка в виде "https://images.dog.ceo/breeds/{название_породы}/{номер_картинки}.jpg"
    assert re.match(r"^" + random1_result + r"\S+/\S+.[jpegJPEG]{3,4}$", rand1)


@pytest.mark.parametrize("count", ['1', '11', '50', '51', '0', 's'])
def test_breed_links_random(dogs_api, count):
    """проверка множественного random'а - каждая возвращённая строка - именно фотография"""
    res = dogs_api.text_dict(path=random1+'/'+count)
    links = res.get("message")
    for link in links:
        assert re.match(r"^" + random1_result + r"\S+/\S+.[jpegJPEG]{3,4}$", link)


@pytest.mark.parametrize(("count", "result"), [('1', 1), ('11', 11), ('50', 50), ('51', 50), ('0', 1), ('s', 1)])
def test_breed_links_count(dogs_api, count, result):
    """проверка множественного random'а - возвращает заданное кол-во ссылок + граничные и "некорректные" значения"""
    res = dogs_api.text_dict(path=random1 + '/' + count)
    links = res.get("message")
    assert len(links) == result


@pytest.mark.parametrize("breed", ['setter', 'terrier'])
def test_breed_links_images(dog_api, breed):
    """проверка метода с указанием породы"""
    res = dog_api.text_dict(path='/' + breed + '/images')
    links = res.get("message")
    for link in links:
        print(f'link={link}')
        assert re.match(r"^" + random1_result + breed + r"\S+/\S+.[jpegJPEGn]{3,4}$", link)