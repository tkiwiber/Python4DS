import os


def str_count_in_file(file: str) -> int:
    num = 0
    if file.endswith('.py'):
        with open(file, 'r') as f:
            for line in f:
                if line.rstrip().lstrip() != '' and line.lstrip()[0] != '#':
                    num += 1
        f.close()
        return num
    else:
        return 0


def str_count(start_path: str) -> str:
    for elem in os.listdir(start_path):
        new_path = os.path.join(start_path, elem)
        if os.path.isfile(new_path):
            yield str_count_in_file(new_path)
        else:
            yield from str_count(start_path=new_path)
    else:
        return


def main() -> int:
    path = input('Введите путь до каталога: ')
    # path = '/Users/aaon/Documents/Project.Academy/Skillbox/PythonModule/27_Iterators_and_generators'

    if not os.path.exists(path):
        print('Ошибка! Указан несуществующий путь!')
        return -1
    if not os.path.isdir(path):
        print('Ошибка! Необходимо указать путь к каталогу, а не файлу!')
        return -1

    print()

    py_files = str_count(start_path=os.path.abspath(path))
    number = 0
    for str_num in py_files:
        number += str_num
    print('Numbers of strings in all .py files here are', number)

    print()
    return 0


main()
