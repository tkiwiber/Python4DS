from random import randint
import time


def selection_sort(u_list):
    for i in range(len(u_list) - 1):
        m = i
        j = i + 1
        while j < len(u_list):
            if u_list[j] < u_list[m]:
                m = j
            j = j + 1
        u_list[i], u_list[m] = u_list[m], u_list[i]


def main():
    a = []
    selection_sort_time = 0

    for i in range(9999):
        a.append(randint(1, 99))

    b = a.copy()
    c = a.copy()
    print('Изначальный список:', a)
    start_time = time.time()
    selection_sort(b)
    selection_sort_time = time.time() - start_time
    print('\nОтсортированный список:', b)
    print('Время сортировки выбором:', selection_sort_time)
    start_time = time.time()
    c.sort()
    python_sort_time = time.time() - start_time
    print('\nОтсортированный список:', b)
    print('Время сортировки функцией Python:', python_sort_time)

    if python_sort_time < selection_sort_time:
        print('\nPython быстрее на', selection_sort_time - python_sort_time, ' сек.')
    else:
        print('\nPython медленнее на', selection_sort_time - python_sort_time, ' сек.')


main()

