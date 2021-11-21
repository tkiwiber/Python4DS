import random


class CalcException(Exception):
    def __init__(self, m):
        self.msg = m


def f1(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    if y == 0:
        raise CalcException('f1')

    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    if x == 0:
        raise CalcException('f2')

    return y / x


def main():
    work_file = 'coordinates.txt'

    try:
        with open(work_file, 'r') as file, open('result.txt', 'w') as file_2:
            for line in file:
                nums_list = line.split()

                res1 = f1(int(nums_list[0]), int(nums_list[1]))
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)

                my_list = sorted([res1, res2, number])
                file_2.write(' '.join([str(item) for item in my_list]) + '\n')

    except FileNotFoundError:
        print("Не найдет файл {}".format(work_file))
    except CalcException as calc:
        print("Деление на 0 при выполнении функции: {}".format(calc.msg))
    # except ZeroDivisionError as err:
    #     print("Деление на 0: {}".format(err))
    else:
        print('Успешно завершено! Результат сохранен в result.txt')


main()
