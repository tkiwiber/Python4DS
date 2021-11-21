def group_by_pizza(o_dict, name):
    print('\n{0}: '.format(name))
    pizza_dict = {item[1] for item in o_dict.values() if item[0] == name}
    for pizza in sorted(pizza_dict):
        count = 0
        for item in o_dict.values():
            if item[0] == name and item[1] == pizza:
                count += int(item[2])
        print('\t{p}: {c}'.format(p=pizza, c=count))


while True:
    try:
        N = int(input('Введите кол-во заказов: '))
        break
    except ValueError:
        print('Ошибка: должно быть введено число!')

order_dict = dict()
for i in range(1, N + 1):
    print('{} заказ: '.format(i), end='')
    order_list = input().split()
    order_dict[i] = order_list

# order_dict = {
#     1: 'Иванов Пепперони 1'.split(),
#     2: 'Петров Де-Люкс 2'.split(),
#     3: 'Иванов Мясная 3'.split(),
#     4: 'Иванов Мексиканская 2'.split(),
#     5: 'Иванов Пепперони 2'.split(),
#     6: 'Петров Интересная 5'.split()
# }

print()
print(order_dict)
client = {v[0] for v in order_dict.values()}

for each in sorted(client):
    group_by_pizza(order_dict, each)
