geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def filter_for_city(visit):
    for city in visit.values():
        if 'Россия' in city:
            return True
        else:
            return False


def sort_geo_logs(list_visit):
    geo_logs = list(filter(filter_for_city, list_visit))
    return geo_logs


def get_max_stats(stats):
    return max(stats, key=stats.get)


def get_sort_list_ids(ids):
    set_ids = set()
    for values in ids.values():
        for elem in values:
            set_ids.add(elem)
    return list(set_ids)


if __name__ == '__main__':
    print(sort_geo_logs(geo_logs))
    print(get_max_stats(stats))
    print(get_sort_list_ids(ids))
