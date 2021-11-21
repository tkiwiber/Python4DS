violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


def add_dur(user_list, elem):
    for item in user_list:
        if item[0] == elem:
            return item[1]
    return 0


nbr = int(input('Сколько песен выбрать? '))
duration = 0

for i in range(nbr):
    print('Название', i + 1, 'песни: ', end='')
    song = input()
    duration += add_dur(violator_songs, song)

print('\nОбщее время звучания песен: ', round(duration, 2), ' минут')
