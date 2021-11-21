def main():
    while True:
        try:
            N = int(input('Введите кол-во человек: '))
            break
        except ValueError:
            print('Ошибка: должно быть введено число!')

    gen_dict = dict()
    for i in range(1, N):
        print('{} пара: '.format(i), end='')
        order_list = input().split()
        gen_dict[i] = order_list

    # gen_dict = {
    #     1: 'Alexei Peter_I'.split(),
    #     2: 'Anna Peter_I'.split(),
    #     3: 'Elizabeth Peter_I'.split(),
    #     4: 'Peter_II Alexei'.split(),
    #     5: 'Peter_III Anna'.split(),
    #     6: 'Paul_I Peter_III'.split(),
    #     7: 'Alexander_I Paul_I'.split(),
    #     8: 'Nicholaus_I Paul_I'.split()
    # }

    parent_dict = set([item[1] for item in gen_dict.values()])
    child_dict = set([item[0] for item in gen_dict.values()])

    father = parent_dict - child_dict
    if len(father) != 1:
        print('Ошибка! Нельзя выявить родоначальника')
        return
    all_set = parent_dict | child_dict

    lvl = 0
    gen_lvl = dict()
    print()
    while any(child_dict):
        gen_lvl[lvl] = father
        child_dict -= set(father)
        father = [item[0] for item in gen_dict.values() if item[1] in father]
        lvl += 1

    for name in sorted(all_set):
        print(name, ''.join([str(lvl) for lvl, names in gen_lvl.items() if name in names]))


main()
