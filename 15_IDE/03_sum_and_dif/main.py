
def digits_sum(number):
    result = 0
    if number <= 0:
        return 0
    while number != 0:
        result += number % 10
        number //= 10
    return result


def digits_count(number):
    result = 0
    if number <= 0:
        return 0
    while number != 0:
        result += 1
        number //= 10
    return result


def main():
    num = int(input('Введите число: '))
    if digits_sum(num):
        print('Сумма цифр:', digits_sum(num))
        print('Кол-во цифр в числе:', digits_count(num))
        print('Разность суммы и кол-ва цифр:', digits_sum(num) - digits_count(num))
    else:
        print('Введенное число не является целым положительным числом')


main()
