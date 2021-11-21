def input_num():
    while True:
        try:
            num = int(input('Введите число: '))
            break
        except ValueError:
            print('(-) это не целое число!')
    return num


n = int(input('Введите число (N): '))
numbers = [input_num() for _ in range(n)]
new_num = [x for x in numbers if x != 0]
zeroes = [x for x in numbers if x == 0]
new_num.extend(zeroes)

print(new_num)
