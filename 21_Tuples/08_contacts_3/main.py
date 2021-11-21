import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def wait():
    print()
    os.system('pause' if os.name == 'nt' else
              'read -s -n 1 -p "Press any key to continue..."')


def menu():
    cls()
    print('Меню телефонной книги\n'.upper())
    print('1 - добавить контакт\n'
          '2 - поиск контакта\n'
          '3 - показать список контактов\n'
          '4 - выйти')
    choice = str(input('\nВведите действие: '))
    if choice == '1':
        return 1
    elif choice == '2':
        return 2
    elif choice == '3':
        return 3
    elif choice == '4':
        return 4
    else:
        return 0


def add_contact(pb):
    cls()
    print('Добавить контакт\n'.upper())

    name = input('Введите имя и фамилию: ').split()
    if len(name) == 0:
        print('\nОшибка! Контакт не добавлен')
        input('Нажмите любую клавишу для продолжения ...')
        return

    num = input('Введите номер телефона: ')
    for ch in num:
        if ch not in '0123456789':
            print('\nОшибка! Контакт не добавлен')
            input('Нажмите любую клавишу для продолжения ...')
            return

    pb[tuple(name)] = ''.join([ch for ch in num])
    print('\nКонтакт добавлен')
    wait()


def search_contact(pb):
    is_any = False
    cls()
    print('Поиск контакта\n'.upper())
    surname = input('Введите фамилию: ').lower()
    print()

    for person, age in pb.items():
        to_print = False
        for each in person:
            if surname in each.lower():
                to_print = True
                is_any = True
        if to_print:
            print(' '.join([each for each in person]), age)
    if not is_any:
        print('Нет контактов с такой фамилией')
    wait()


def show_phonebook(pb):
    cls()
    print('Список контактов\n'.upper())
    for contact, number in pb.items():
        print(' '.join([each for each in contact]), number)
    wait()


def main():
    phonebook = {
        ('Petrov', 'Petr'): 89001005040,
        ('Petrova', 'Zhenya'): 89001005042
    }

    while True:
        action = menu()
        if action == 1:
            add_contact(phonebook)
        elif action == 2:
            search_contact(phonebook)
        elif action == 3:
            show_phonebook(phonebook)
        elif action == 4:
            break


main()
