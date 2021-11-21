
import os
import time


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def shift_list_left(u_list):
    s_list = u_list.copy()
    s_list[0] = u_list[-1]
    for i in range(1, len(u_list)):
        s_list[i] = u_list[i - 1]
    u_list = s_list.copy()
    return u_list


def main():
    given_list = [x for x in range(10)]
    shifted_list = given_list.copy()
    k = 30
    cls()

    for i in range(k):
        shifted_list = shift_list_left(shifted_list)
        cls()
        print('Сдвиг: ', k, ' (', k - i, ')', sep='')
        print('Изначальный список:', given_list)
        print('Сдвинутый список:', shifted_list)
        time.sleep(0.3)


main()

