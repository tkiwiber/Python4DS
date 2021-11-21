
n = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке? '))
player = 1
print('Значит, выбывает каждый', k, 'человек')
people = [x for x in range(1, n + 1)]

while len(people) > 1:
    print('\nТекущий круг людей:', people)
    print('Начало счёта с номера', player)
    pos = (people.index(player) + k) % (len(people)) - 1
    player = people[pos]
    print('Выбывает человек под номером', player)
    people.remove(player)
    player = people[pos] if pos >= 0 else people[0]

print('\nОстался человек под номером', people[0])
