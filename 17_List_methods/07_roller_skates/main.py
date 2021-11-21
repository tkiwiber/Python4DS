
def create_list(text1, text2, text3):
    new_list = []
    print(text1, end='')
    nbr = int(input())
    for j in range(nbr):
        print(text2, j + 1, text3, sep='', end='')
        nbr = int(input())
        new_list.append(nbr)
    return new_list


def give_out_at_once(skates, people):
    new_list = skates.copy()
    count = 0
    for everybody in people:
        try:
            new_list.remove(everybody)
            count += 1
        except ValueError:
            continue
    return count


skates_list = create_list('Кол-во коньков: ', 'Размер ', ' пары: ')
print()
people_list = create_list('Кол-во людей: ', 'Размер ноги ', ' человека: ')

print()
print('Наибольшее кол-во людей, которые могут взять ролики:', give_out_at_once(skates_list, people_list))

