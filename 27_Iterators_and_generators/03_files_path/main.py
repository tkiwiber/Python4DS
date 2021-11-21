import os


def gen_files_path(start_path: str, target: str) -> str:
    if os.path.isdir(start_path):
        if os.path.split(start_path)[1] == target:
            print('\nFOUND\n')
            raise StopIteration
        else:
            for current in os.listdir(start_path):
                path = os.path.join(start_path, current)
                yield path
                yield from gen_files_path(path, target)


def main() -> int:
    path = input('Введите путь до каталога: ')
    to_find = input('Введите папку: ')
    # path = '/Users/alex/Documents/Project.Academy/Skillbox/PythonModule/27_Iterators_and_generators/'
    # to_find = '12'

    print(os.path.basename(os.path.normpath(path)), '\n')

    if not os.path.exists(path):
        print('Ошибка! Указан несуществующий путь!')
        return -1
    if not os.path.isdir(path):
        print('Ошибка! Необходимо указать путь к каталогу, а не файлу!')
        return -1

    print()

    try:
        i_files = gen_files_path(start_path=os.path.abspath(path), target=to_find)
        for i in i_files:
            print(i)
    except RuntimeError:
        pass

    print()
    return 0


main()
