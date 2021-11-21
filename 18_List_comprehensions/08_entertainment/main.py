def input_stones(i):
    st_list = []
    print('Бросок', i + 1)
    while True:
        try:
            num1 = int(input('Введите L_i: '))
            num2 = int(input('Введите R_i: '))
            for num in range(num1, num2 + 1):
                st_list.append(num)
            break
        except ValueError:
            print('(-) это не целое число!')
    return st_list


n = int(input('Кол-во палок: '))
sticks = [i for i in range(1, n + 1)]
k = int(input('Кол-во камней: '))
stones = [input_stones(i) for i in range(k)]
flat_stones = [item for sublist in stones for item in sublist]
result = [stick if stick not in flat_stones else 0 for stick in sticks]

print()
for each in result:
    if each == 0:
        print('.', end='')
    else:
        print('I', end='')
