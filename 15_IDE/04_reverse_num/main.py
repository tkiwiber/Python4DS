

def int_part_reverse(number):
    return int(str(int(number))[::-1])


def fra_part_reverse(number):
    result = ''
    for i in str(number)[::-1]:
        if i == '.':
            break
        else:
            result += i
    return int(result)


def digits_count(number):
    result = 0
    if number <= 0:
        return 0
    while number != 0:
        result += 1
        number //= 10
    return result


def num_reverse(number):
    return int_part_reverse(number) + fra_part_reverse(number) / (pow(10, digits_count(fra_part_reverse(number))))


def main():
    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))

    print('\nПервое число наоборот:', num_reverse(num1))
    print('Второе число наоборот:', num_reverse(num2))
    print('Сумма:', num_reverse(num1) + num_reverse(num2))


main()
