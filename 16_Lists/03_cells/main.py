
def fill_list(n):
    cells_list = []

    for i in range(n):
        print('Эффективность', i + 1, 'клетки: ', end='')
        x = int(input())
        cells_list.append(x)
    return cells_list


def print_list(cells_list):
    count = 0
    print('\n\nНеподходящие значения:', end=' ')
    for _ in cells_list:
        if cells_list[count] < count:
            print(cells_list[count], end=' ')
        count += 1


def main():

    n = int(input('Кол-во клеток: '))
    cells_list = fill_list(n)
    print_list(cells_list)


main()
