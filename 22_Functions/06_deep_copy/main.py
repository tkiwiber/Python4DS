import pprint
import copy

site_default = {
    'html': {
        'head': {
            'title': 'Куплю/продам {телефон} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {телефон}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def replace_placeholder(struct, new_value, key='{телефон}'):
    for id_s, val in struct.items():
        if key in val:
            struct[id_s] = val.replace(key, new_value)
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                replace_placeholder(sub_struct, new_value)


def print_sites(site_dict):
    for key, value in site_dict.items():
        print(key)
        pp = pprint.PrettyPrinter(depth=4)
        pp.pprint(value)


sites_number = int(input('Сколько сайтов: '))
sites = dict()

for i in range(sites_number):
    user_str = input('Введите название продукта для нового сайта: ')
    new_site = copy.deepcopy(site_default)
    replace_placeholder(new_site, user_str)
    sites[''.join(['Сайт для ', user_str])] = new_site
    print_sites(sites)
