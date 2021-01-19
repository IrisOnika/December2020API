from dogs.breed_list_func import *
import re

# with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'breеd_list.json'), 'r') as breeds:
#     breeds_all = breeds.read()
#     breeds_list = loads(breeds_all)


# проверка возвращаемого списка пород
def test_check_breeds_list():
    ap = dogs_api()
    res = ap.text_dict(path=list_all)
    breed_list_dict = res.get("message")
    #print(breed_list_dict)
    breed_list = list(breed_list_dict.keys())
    breeds_list = open_read('dogs/breеd_list.json')
    #print(breeds_list)
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
    i = 0
    for link in links:
        i += 1
    assert i == result


# Проверка того, что метод с указанной породой возвращает ссылки на фото собак указанной в методе породы.
@pytest.mark.parametrize("breed", ['setter'])
def test_breed_links_images(breed):
    ap = dogs_api(host1)
    res = ap.text_dict(path='/' + breed + '/images')
    links = res.get("message")
    for link in links:
        assert re.match(r"^" + random1_result + breed + r"\S+/\S+.[jpegJPEG]{3,4}$", link)



