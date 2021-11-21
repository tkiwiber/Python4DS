
def create_list(nbr, text1):
    new_list = []
    for j in range(nbr):
        print('\n', j + 1, text1, sep='')
        bond_list = []
        bond_to = int(input('Кому: '))
        bond_list.append(bond_to)
        bond_from = int(input('От кого: '))
        bond_list.append(bond_from)
        bond_sum = int(input('Сколько: '))
        bond_list.append(bond_sum)
        new_list.append(bond_list)
    return new_list


def count_balance(friend_list, bonds_list):
    for each in friend_list:
        for bond in bonds_list:
            if each[0] == bond[0]:
                each[1] -= bond[2]
            elif each[0] == bond[1]:
                each[1] += bond[2]


def print_balance(friend_list):
    print('\nБаланс друзей:')
    for each in friend_list:
        print(each[0], ':', each[1])


n = int(input('Кол-во друзей: '))
k = int(input('Долговых расписок: '))

friends = [[x, 0] for x in range(1, n + 1)]
bonds = create_list(k, ' расписка')

count_balance(friends, bonds)
print_balance(friends)
