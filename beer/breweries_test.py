import cerberus
from conftest import open_read
from beer.breweries_func import *


@pytest.mark.parametrize('number', ['/8044', '/8047'], ids=["brewery_No8044", "brewery_No8047"])
def test_check_breweries_schema(brewer_api, number):
    """проверка схемы пивоварни"""
    res = brewer_api.text_dict(path=number)
    print(res)
    schema = open_read('beer/schema_brewery.json')
    v = cerberus.Validator(schema)
    assert v.validate(res)


@pytest.mark.parametrize(('page_num', 'count'),
                         [
                             # кейсы для номера вызываемой страницы
                             ('0', 20),
                             ('1', 20),
                             ('393', 20),
                             # для текущего состояния базы (текущего кол-ва пивоварен)
                             ('394', 2),
                             ('395', 0)
                         ])
def test_check_brewer_page_num(brewer_api, page_num, count):
    """проверка кол-ва пивоварен на странице+общее кол-во пивоварен на текущее состояние базы"""
    res = brewer_api.text_dict(path=f'?page={page_num}')
    assert len(res) == count


# проверка возможности выводить разное кол-во пивоварен на странице
@pytest.mark.parametrize(('per_page', 'count'), [('0', 0),
                                                 ('1', 1),
                                                 ('50', 50),
                                                 ('51', 50)])
def test_check_brewer_per_page(brewer_api, per_page, count):
    """проверка возможности вывыодить разное кол-во пивоварен на странице"""
    res = brewer_api.text_dict(path=f'?per_page={per_page}')
    assert len(res) == count


@pytest.mark.parametrize('search', ['California',
                                    'Russia',
                                    'Fat Orange Cat',
                                    pytest.param('Cat',
                                                 marks=pytest.mark.xfail(
                                                     reason='bug? can not find cat in one of returned string')),
                                    'should not get result'])
def test_check_brewer_search(brewer_api, search):
    """проверка: если пивоварня нашлась по набору символов, то этот набор попадёт в одно из полей строки вывода"""
    res = brewer_api.text_dict(path=f'{search_query}{search}')
    for item in res:
        print(item.get("id"))
        count = 0
        for i in list(item.keys()):
            if str(item.get(i)).find(search) > -1:
                # print(i)
                # print(item.get(i))
                count += 1
            else:
                print(f'there is no {search} in brewery with id {i}')
        if res:
            assert count > 0
        else:
            assert count == 0


# тест про схему ответа при автокомплите
# Баг (или фича). id в выводе имеет тип 'string'. id в других методах имеет тип 'integer'
@pytest.mark.parametrize('search', ['Fat Orange Cat', 'Mew'])
def test_autocomplete_schema(brewer_api, search):
    """"""
    res = brewer_api.text_dict(path=f'{autocomplete_query}{search}')
    schema = open_read('beer/schema_autocomplete.json')
    v = cerberus.Validator(schema)
    for res_item in res:
        assert v.validate(res_item)
