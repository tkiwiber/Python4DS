import os
import readchar


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

    return 0


def check_name(user):
    if user == '' or user == ' ':
        raise ValueError('>> Ошибка! Имя не может быть пустым')
    name = user.strip().split()
    if len(name) > 1:
        raise ValueError('>> Ошибка! Имя не может содержать пробел')
    if not name[0].isprintable():
        raise ValueError('>> Ошибка! В имени есть непечатные символы')
    if len(name[0]) < 3:
        raise ValueError('>> Ошибка! В имени должно быть минимум 3 символа')

    return True


def init_chat():
    while True:
        cls()
        print(bcolors.HEADER, 'Добро пожаловать в ЧАТ!', bcolors.ENDC)
        print(bcolors.HEADER, '>> Представьтесь: ', bcolors.ENDC, end='')
        name = input()
        try:
            check_name(name)
            break
        except ValueError as err:
            print(bcolors.WARNING, err, bcolors.ENDC)
            readchar.readchar()
            continue

    return name


def read_socket():
    cls()
    try:
        with open('chat.socket', 'r') as chat:
            for message in chat:
                line = message.split()
                print(bcolors.OKGREEN, '<{}> '.format(''.join(line[0:1])), bcolors.ENDC, end='')
                print(bcolors.BOLD, '\t{}'.format(' '.join(line[1:])), bcolors.ENDC)
            readchar.readchar()
    except IndexError:
        print(bcolors.WARNING, 'Ошибка! Запись повреждена', bcolors.ENDC)
        readchar.readchar()
    except FileNotFoundError:
        print(bcolors.WARNING, 'Ошибка! В чате еще нет записей. Ты первый!', bcolors.ENDC)
        readchar.readchar()


def write_socket(user):
    cls()
    print(bcolors.HEADER, 'Введите сообщение: ', bcolors.ENDC)
    message = input(' >> ')
    try:
        with open('chat.socket', 'a') as chat:
            chat.write(''.join([' '.join([user, message]), '\n']))
    except FileNotFoundError:
        try:
            with open('chat.socket', 'w') as chat:
                (''.join([' '.join([user, message]), '\n']))
        except IOError:
            print(bcolors.FAIL, 'Ошибка файловой системы!')
            raise IOError('Экстренный выход ...')


def main():
    cls()
    name = init_chat()
    while True:
        cls()
        print(bcolors.HEADER, 'ПРИВЕТ, {}. ЭТО КОМНАТА ДЛЯ ОБЩЕНИЯ'.format(name.upper()), bcolors.ENDC)
        print(bcolors.HEADER, '1 - посмотреть текущий чат', bcolors.ENDC)
        print(bcolors.HEADER, '2 - отправить сообщение', bcolors.ENDC)
        print(bcolors.HEADER, '3 - выйти из комнаты', bcolors.ENDC)
        try:
            print(bcolors.HEADER, '>> что выберешь? ', bcolors.ENDC, end='')
            choice = int(input())
            if choice == 1:
                read_socket()
            if choice == 2:
                write_socket(name)
            if choice == 3:
                cls()
                print(bcolors.HEADER, 'Ну, до скорого! :-)', bcolors.ENDC)
                break
        except ValueError:
            continue
        except IOError as err:
            print(err)
            return 0

    return 0


main()
