
def count_nbr(u_list, nbr):
    count = 0
    for item in u_list:
        count += 1 if item == nbr else 0
    return count


def del_nbr_from_list(u_list, nbr):
    return [x for x in u_list if x != nbr]


list_a = [1, 5, 3]
list_b1 = [1, 5, 1, 5]
list_b2 = [1, 3, 1, 5, 3, 3]

list_a.extend(list_b1)
print('Кол-во цифр 5 при первом объединении:', count_nbr(list_a, 5))
list_a = del_nbr_from_list(list_a, 5)

list_a.extend(list_b2)
print('Кол-во цифр 3 при первом объединении:', count_nbr(list_a, 3))

print('Итоговый список:', list_a)
