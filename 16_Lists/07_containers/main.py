
def check_value(val):
    try:
        int(val)
    except ValueError:
        return False
    return True


def input_number():
    while True:
        x = input()
        if check_value(x):
            if int(x) > 0:
                return int(x)
            else:
                print('Число д.б. больше 0. Повторите: ', end='')
        else:
            print('Число д.б. целым. Повторите: ', end='')


def fill_list(containers, x):
    flag = True
    while x > 0:
        print('Введите вес контейнера: ', end='')
        weight = input_number()
        if check_value(weight) and weight <= 200:
            if flag:
                containers.append(weight)
                x -= 1
                flag = not flag
            else:
                if weight <= (containers[-1]):
                    containers.append(weight)
                    x -= 1
                else:
                    print('Последовательность не соблюдена. Вес не может быть больше, чем:', containers[::-1])
        else:
            print('Число д.б. больше 0, меньше 200 и целым.')


def find_pos_in_list(user_list, val):
    if val > user_list[0]:
        return 1
    for pos in user_list:
        if pos < val:
            return pos + 1
    else:
        return len(user_list) + 1


def main():
    containers = []

    print('Кол-во контейнеров: ', end='')
    containers_number = input_number()
    fill_list(containers, containers_number)

    print('\n')
    print('Введите вес нового контейнера: ', end='')
    new_container = input_number()

    print('Номер, куда встанет новый контейнер: ', end='')
    print(find_pos_in_list(containers, new_container))


main()
