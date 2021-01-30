from dogs.breed_list_func import *
import re


# проверка возвращаемого списка пород
def test_check_breeds_list():
    ap = dogs_api()
    res = ap.text_dict(path=list_all)
    breed_list_dict = res.get("message")
    breeds_list = open_read('dogs/breеd_list.json')
    assert breed_list_dict == breeds_list


# Проверка того, что метод random возвращает одну рандомную фотографию
def test_breed_random():
    ap = dogs_api()
    res = ap.text_dict(path=random1)
    rand1 = res.get("message")
    # Проверяем, что в message одна строка в виде "https://images.dog.ceo/breeds/{название_породы}/{номер_картинки}.jpg"
    assert re.match(r"^" + random1_result + r"\S+/\S+.[jpegJPEG]{3,4}$", rand1)


# Проверка метода множественного рандома - он работает и возвращает фотографии
@pytest.mark.parametrize("count", ['1', '11', '50', '51', '0', 's'])
def test_breed_links_random(count):
    ap = dogs_api()
    res = ap.text_dict(path=random1+'/'+count)
    links = res.get("message")
    for link in links:
        assert re.match(r"^" + random1_result + r"\S+/\S+.[jpegJPEG]{3,4}$", link)


# Проверка метода множественного рандома - он возвращает столько ссылок на фотографии,
# сколько задано , а также граничные и "некорректные" значения, передаваемые в ссылке.
@pytest.mark.parametrize(("count", "result"), [('1', 1), ('11', 11), ('50', 50), ('51', 50), ('0', 1), ('s', 1)])
def test_breed_links_count(count, result):
    ap = dogs_api()
    res = ap.text_dict(path=random1 + '/' + count)
    links = res.get("message")
    assert len(links) == result


# Проверка того, что метод с указанной породой возвращает ссылки на фото собак указанной в методе породы.
@pytest.mark.parametrize("breed", ['setter'])
def test_breed_links_images(breed):
    ap = dogs_api(host1)
    res = ap.text_dict(path='/' + breed + '/images')
    links = res.get("message")
    for link in links:
        assert re.match(r"^" + random1_result + breed + r"\S+/\S+.[jpegJPEG]{3,4}$", link)



