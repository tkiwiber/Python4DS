violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

duration = 0
num = int(input('Сколько песен выбрать? '))

songs_name = []
for i in range(1, num + 1):
    print('Название {} песни: '.format(i), end='')
    songs_name.append(input())

for song in songs_name:
    duration += violator_songs.get(song) if violator_songs.get(song) is not None else 0

print('\nОбщее время звучания песен: {0:.2f} минут'.format(duration))
