import os


def create_path(u_path):
    r_path = ''
    if u_path[0][0] != '.':
        for each in u_path:
            r_path = os.path.join(r_path, each)
    return os.path.join(os.path.sep, r_path)


def validate_path(u_path):
    if not os.path.exists(u_path):
        print('Ошибка! Указан несуществующий путь!')
        return None
    if not os.path.isdir(u_path):
        print('Ошибка! Необходимо указать путь к каталогу, а не файлу!')
        return None
    return u_path


def main():
    print()
    data = input('Введите строку: ')
    # path_str = 'Users aaon Documents Project.Academy Skillbox PythonModule 23_Files 01_nums_sum_2'.split()
    print()
    print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
    path_str = input().split()
    user_path = create_path(path_str)
    path = validate_path(user_path)
    if path is None:
        return -1

    while True:
        print()
        file_name = input('Введите имя файла: ')
        file_name = file_name + '.txt'
        if os.path.exists(os.path.join(path, file_name)):
            mode = ''
            while True:
                print('Файл существует. Точно хотите перезаписать (1 - перезаписать, 0 - отмена)? ', end='')
                answer = input()
                if answer == '1':
                    mode = 'w'
                    break
                elif answer == '0':
                    break
            if mode == 'w':
                break
        else:
            break

    file = open(os.path.join(path, file_name), 'w')

    file.write(data)
    file.close()
    print('Файл успешно сохранён!')

    return 0


main()
