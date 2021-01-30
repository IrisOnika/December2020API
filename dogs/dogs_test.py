from dogs.breed_list_func import *
import re


def test_check_breeds_list():
    """проверка возвращаемого списка пород"""
    ap = dogs_api()
    res = ap.text_dict(path=list_all)
    breed_list_dict = res.get("message")
    breeds_list = open_read('dogs/breеd_list.json')
    assert breed_list_dict == breeds_list


def test_breed_random():
    """проверка метода random - возвращает одну рандомную фотографию"""
    ap = dogs_api()
    res = ap.text_dict(path=random1)
    rand1 = res.get("message")
    # Проверяем, что в message одна строка в виде "https://images.dog.ceo/breeds/{название_породы}/{номер_картинки}.jpg"
    assert re.match(r"^" + random1_result + r"\S+/\S+.[jpegJPEG]{3,4}$", rand1)


@pytest.mark.parametrize("count", ['1', '11', '50', '51', '0', 's'])
def test_breed_links_random(count):
    """проверка множественного random'а - каждая возвращённая строка - именно фотография"""
    ap = dogs_api()
    res = ap.text_dict(path=random1+'/'+count)
    links = res.get("message")
    for link in links:
        assert re.match(r"^" + random1_result + r"\S+/\S+.[jpegJPEG]{3,4}$", link)


@pytest.mark.parametrize(("count", "result"), [('1', 1), ('11', 11), ('50', 50), ('51', 50), ('0', 1), ('s', 1)])
def test_breed_links_count(count, result):
    """проверка множественного random'а - возвращает заданное кол-во ссылок + граничные и "некорректные" значения"""
    ap = dogs_api()
    res = ap.text_dict(path=random1 + '/' + count)
    links = res.get("message")
    assert len(links) == result


@pytest.mark.parametrize("breed", ['setter'])
def test_breed_links_images(breed):
    """проверка метода с указанием породы"""
    ap = dogs_api(host1)
    res = ap.text_dict(path='/' + breed + '/images')
    links = res.get("message")
    for link in links:
        assert re.match(r"^" + random1_result + breed + r"\S+/\S+.[jpegJPEG]{3,4}$", link)
