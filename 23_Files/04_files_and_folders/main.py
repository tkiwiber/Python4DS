import os

stat = {
    'size': 0,
    'folders': 0,
    'files': 0
}


def count_stat(cur_path, path_stat):
    for elem in os.listdir(cur_path):
        new_path = os.path.join(cur_path, elem)
        if os.path.isfile(new_path):
            path_stat['files'] += 1
            path_stat['size'] += os.path.getsize(new_path)
        if os.path.isdir(new_path):
            path_stat['folders'] += 1
            count_stat(new_path, path_stat)
    else:
        return None
    return None


def main():
    path = input('Введите путь до каталога: ')

    if not os.path.exists(path):
        print('Ошибка! Указан несуществующий путь!')
        return -1
    if not os.path.isdir(path):
        print('Ошибка! Необходимо указать путь к каталогу, а не файлу!')
        return -1

    print(os.path.abspath(path))
    count_stat(os.path.abspath(path), stat)
    print()
    print('Размер каталога (в Кб): {}'.format(stat['size'] / 1024))
    print('Количество подкаталогов: {}'.format(stat['folders']))
    print('Количество файлов: {}'.format(stat['files']))


main()
