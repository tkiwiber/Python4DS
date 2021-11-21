import os
import time

towers = dict()
answer = list()


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def return_size(user_list, index):
    try:
        return user_list[index - 1]
    except IndexError:
        return 0


def draw_pyramids(height):
    cls()
    offset = 15
    size = 2
    for i in range(height + 1):
        f = return_size(towers[1], i)
        s = return_size(towers[2], i)
        t = return_size(towers[3], i)
        if i == 0:
            print(' ' * offset, '1', ' ' * offset * 2, '2', ' ' * offset * 2, '3')
            print()
        else:
            print(' ' * (offset - (size * f // 2)), '=' * (size * f), ' ' * (offset - (size * f // 2)),
                  ' ' * (offset - (size * s // 2)), '=' * (size * s), ' ' * (offset - (size * s // 2)),
                  ' ' * (offset - (size * t // 2)), '=' * (size * t), ' ' * (offset - (size * t // 2)))
    print()


def action(string):
    for ch in string:
        if not ('0' < ch < '9'):
            print('ERROR', ch)
            input()
            return None
    if len(string) != 3:
        print('ERROR', len(string))
        input()
        return None
    return int(string[0]), int(string[1]), int(string[2])


def search_disk_from(tower_number, disk_pos):
    try:
        return towers[tower_number].index(disk_pos)
    except IndexError:
        return None
    except ValueError:
        return None


def search_disk_to(tower_number, disk):
    pos = -1
    for i in range(len(towers[tower_number])):
        if towers[tower_number][i] == 0:
            pos = i
        else:
            if towers[tower_number][i] < disk:
                return None
            return pos
    else:
        return None if pos == -1 else pos


def move_man(n, x, y):
    disk_from = search_disk_from(x, n)
    disk_to = search_disk_to(y, n)
    if disk_from is not None and disk_to is not None:
        towers[x][disk_from] = 0
        towers[y][disk_to] = n
        answer.append(''.join([str(n), str(x), str(y)]))
    else:
        return


def move(src, dst):
    disk_from = -1
    disk_to = -1
    for i in range(len(towers[src])):
        if towers[src][i] != 0:
            disk_from = i
            break
    for i in range(len(towers[dst])):
        if towers[dst][i] == 0:
            disk_to = i
        else:
            break
    buf = towers[src][disk_from]
    towers[src][disk_from] = 0
    towers[dst][disk_to] = buf
    answer.append(''.join([str(buf), str(src), str(dst)]))


def hanoi(n, src, dst, buf, h):
    if n >= 1:
        hanoi(n - 1, src, buf, dst, h)
        move(src, dst)
        draw_pyramids(h)
        time.sleep(0.32)
        hanoi(n - 1, buf, dst, src, h)


def main():
    cls()

    quantity = int(input('Введите количество дисков: '))
    towers[1] = [x for x in range(1, quantity + 1)]
    towers[2] = [0 for x in range(1, quantity + 1)]
    towers[3] = [0 for x in range(1, quantity + 1)]

    while True:
        cls()
        mode = input('Введите режим (interactive - для симуляции, manual - для самостоятельного решения): ')
        if mode == 'manual' or mode == 'interactive':
            break

    if mode == 'interactive':
        draw_pyramids(quantity)
        hanoi(quantity, 1, 3, 2, quantity)
        return 1

    elif mode == 'manual':
        while True:
            draw_pyramids(quantity)
            param = input('Переместите диск (формат nxy) или end для выхода: ')

            if param == 'end':
                return 0
            if action(param) is not None:
                a, b, c = action(param)
                move_man(a, b, c)
            if set(towers[3]) == set(x for x in range(1, quantity + 1)):
                return 1

    return 0


win = main()
if win:
    print('You WON !!!')
    for turn in answer:
        print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'
              .format(turn[0], turn[1], turn[2]))
else:
    print('You LOSE :-(')
