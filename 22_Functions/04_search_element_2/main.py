site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац',
            'new': {
                'a1': 1,
                'a2': 2
            }
        }
    }
}


def find_key(key, struct, lvl, curr_lvl=0):
    if key in struct:
        return struct[key]
    if lvl == curr_lvl:
        return None
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            curr_lvl += 1
            result = find_key(key, sub_struct, lvl, curr_lvl)
            if result:
                break
    else:
        result = None
    return result


user_key = input('Какой ключ ищем? ')
print('Введите глубину вложенности для поиска (1 - первый уровень, 2 - второй и т.д.). \nEnter для поиска по всей '
      'структуре:')
level_str = input('Где ищем? ')
try:
    level = int(level_str)
    level = -1 if level < 1 else level
except ValueError:
    level = -1

value = find_key(user_key, site, level)
if value:
    print("Значение ключа '{}' равно '{}'".format(user_key, value))
else:
    print('Такого ключа в структуре нет')
