
def add_favorite(favorite, films, film_name):
    if film_name in films:
        favorite.append(film_name)
        return 1
    else:
        return 0


def main():
    films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
             'Леон', 'Богемская рапсодия', 'Город грехов',
             'Мементо', 'Отступники', 'Деревня']
    favorite = []

    while True:
        film_name = input('\nВведите название фильма (или Enter для выхода): ')
        if film_name == '':
            print('(***) До свидания!')
            break
        else:
            if not add_favorite(favorite, films, film_name):
                print('(-) Ошибка, такого фильма нет.')
            else:
                print('(+) Фильм добавлен в Избранное.')

    print('\nСписок любимых фильмов: ', favorite, sep='')

main()