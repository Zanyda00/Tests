import pytest
from main import sort_geo_logs, get_max_stats, get_sort_list_ids


@pytest.mark.parametrize('x, expected', [
    ([{'visit4': ['Лиссабон', 'Португалия']},
      {'visit5': ['Париж', 'Франция']},
      {'visit9': ['Курск', 'Россия']}], [{'visit9': ['Курск', 'Россия']}]),
    ([{'visit7': ['Тула', 'Россия']},
      {'visit8': ['Тула', 'Россия']},
      {'visit9': ['Курск', 'Россия']},
      {'visit10': ['Архангельск', 'Россия']}],
     [{'visit7': ['Тула', 'Россия']},
      {'visit8': ['Тула', 'Россия']},
      {'visit9': ['Курск', 'Россия']},
      {'visit10': ['Архангельск', 'Россия']}]),
    ([{'visit1': ['Москва', 'Россия']}, {'visit2': ['Дели', 'Индия']}], [{'visit1': ['Москва', 'Россия']}])
])
def test_sort_geo_logs_1(x, expected):
    res = sort_geo_logs(x)
    assert res == expected
    assert isinstance(res, list)
    assert isinstance(res[0], dict)
    assert len(res) != 0


@pytest.mark.parametrize('x, expected', [
    ({'facebook': 200, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'facebook'),
    ({'facebook': 55, 'yandex': 2000, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
    ({'facebook': 55, 'yandex': 120, 'vk': 149, 'google': 99, 'email': 42, 'ok': 98}, 'vk'),
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 9052, 'email': 42, 'ok': 98}, 'google'),
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 811}, 'ok')
])
def test_get_max_stats(x, expected):
    res = get_max_stats(x)
    assert res == expected
    assert isinstance(res, str)
    assert res in x


@pytest.mark.parametrize('x, expected', [
    ({'a': [1, 1, 1, 1, 1]}, [1]),
    ({'a': [1, 2, 1, 2, 1]}, [1, 2]),
    ({'a': [1, 3, 4], 'b': [1, 2, 2], 'c': [1, 7, 0]}, [0, 1, 2, 3, 4, 7])
])
def test_get_sort_list_ids(x, expected):
    res = get_sort_list_ids(x)
    assert res == expected
    assert isinstance(res, list)
