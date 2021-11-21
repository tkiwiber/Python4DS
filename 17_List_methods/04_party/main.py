guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
answer = ''


def add_guest(u_list, g_name):
    if len(u_list) == 6:
        return False
    u_list.append(g_name)
    return True


def remove_guest(u_list, g_name):
    try:
        u_list.remove(g_name)
        return True
    except ValueError:
        return False


while answer.lower() != 'пора спать':
    print('Сейчас на вечеринке ', len(guests), ' человек:', guests)
    answer = input('Гость пришел или ушел? ')
    if answer.lower() == 'пришел':
        name = input('Имя гостя: ')
        if add_guest(guests, name):
            print('Привет, ', name, '!', sep='')
        else:
            print('Прости, ', name, ', но мест нет.', sep='')
    elif answer.lower() == 'ушел':
        name = input('Имя гостя: ')
        if remove_guest(guests, name):
            print('Пока, ', name, '!', sep='')
        else:
            print('У нас нет таких!', sep='')
    print()

print('Вечеринка закончилась, все легли спать.')
