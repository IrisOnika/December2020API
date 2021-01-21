from beer.breweries_func import *
import re
import cerberus

#проверка схемы пивоварни
@pytest.mark.parametrize('number', ['/1', '/777'])
def test_check_breweries_schema(number):
    ap = brewer_api()
    res = ap.text_dict(path=number)
    print(res)
    schema = open_read('beer/schema_brewery.json')
    v = cerberus.Validator(schema)
    assert v.validate(res)


# проверка количества пивоварен на странице по умолчанию.
# А также проверка общего кол-ва пивоварен на текущее состояние базы
@pytest.mark.parametrize(('page_num', 'count'),
                         [
                             # кейсы для номера вызываемой страницы
                             ('0', 20),
                             ('1', 20),
                             ('401', 20),
                             # для текущего состояния базы (текущего кол-ва пивоварен)
                             ('402', 12),
                             ('403', 0)
                            ])
def test_check_brewer_page_num(page_num, count):
    ap = brewer_api()
    res = ap.text_dict(path=f'?page={page_num}')
    res_count = 0
    for item in res:
        res_count += 1
    assert res_count == count


# проверка возможности выводить разное кол-во пивоварен на странице
@pytest.mark.parametrize(('per_page', 'count'), [('0', 0),
                                      ('1', 1),
                                      ('50', 50),
                                      ('51', 50)])
def test_check_brewer_per_page(per_page, count):
    ap = brewer_api()
    res = ap.text_dict(path=f'?per_page={per_page}')
    res_count = 0
    for item in res:
        res_count += 1
    assert res_count == count


@pytest.mark.parametrize('search', ['California', 'Russia', 'Fat Orange Cat', 'Cat', 'khjkhjkh'])
def test_check_brewer_search(search):
    ap = brewer_api()
    res = ap.text_dict(path=f'{search_query}{search}')
   # print(f'res={res}')
    # Идея теста - проверять, что если пивоварня нашлась по какому-либо набору символов, то этот набор символов попадёт
    # в строку вывода(в одно из полей).
    # по факту работает не со всеми значениями ('Cat'), но, возможно, я некорректно разобралась в работе сервиса.
    for item in res:
        print(item.get("id"))
        count=0
        for i in list(item.keys()):
            # добавить проверку на некорректную обработку (если подстрока нигде не нашлась.)
            if str(item.get(i)).find(search) > -1:
                print(i)
                print(item.get(i))
                count += 1
                #print(count)
        if res != []:
            assert count > 0
        else:
            assert count == 0


# тест про схему ответа при автокомплите
# Баг (или фича). id в выводе имеет тип 'string'. id в других методах имеет тип 'integer'
@pytest.mark.parametrize('search', ['Fat Orange Cat', 'Mew'])
def test_autocomplete_schema(search):
    ap = brewer_api()
    res = ap.text_dict(path=f'{autocomplete_query}{search}')
   # print(res)
    schema = open_read('beer/schema_autocomplete.json')
   # print(schema)
    v = cerberus.Validator(schema)
    for res_item in res:
        assert v.validate(res_item)





