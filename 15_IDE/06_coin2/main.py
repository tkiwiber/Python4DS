
import math


def is_in_circle(x, y, radius):
    hip = math.sqrt(x**2 + y**2)
    return True if hip <= radius else False


def main():
    print('Введите координаты монетки:')
    x = float(input('X: '))
    y = float(input('Y: '))
    radius = float(input('Введите радиус: '))

    if is_in_circle(x, y, radius):
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


main()
