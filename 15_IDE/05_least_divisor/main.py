

def least_div(number):
    for x in range(2, number):
        if number % x == 0:
            return x
    else:
        return number


def check_num(number):
    return 1 if number > 1 else 0


def main():
    a = int(input('Введите натуральное число, больше 1: '))
    if check_num(a):
        print('Наименьший делитель, отличный от единицы:', least_div(a))
    else:
        print('Введено неправильное число!')


main()
