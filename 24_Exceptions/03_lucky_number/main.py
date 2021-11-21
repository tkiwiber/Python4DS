import random


def main():
    num_sum = 0

    while num_sum < 777:
        try:
            x = int(input('Введите число: '))
            num_sum += x
        except ValueError:
            print('\tОшибка! Введено не число, повторите ввод')
        except KeyboardInterrupt:
            print('\nНадоело? Пока ...')
            break

        if random.randint(1, 13) == 1:
            raise random.choice([FloatingPointError, ValueError, TypeError, Exception, IndexError, InterruptedError])

    return 0


main()
