
def create_list(text1, text2):
    n_list = []
    print(text1, end='')
    nbr = int(input())
    for j in range(nbr):
        print(text2, sep='', end='')
        nbr = int(input())
        n_list.append(nbr)
    return n_list


def print_list(text, friend_list):
    print(text, end='')
    for each in friend_list:
        print(each, end=' ')
    print()


def is_symmetric(user_list):
    ci = len(user_list) // 2
    sh = 1 if len(user_list) % 2 == 0 else 1
    if user_list[:ci:] == user_list[:-(ci + sh):-1]:
        return True
    else:
        return False


def main():
    numbers = create_list('Кол-во чисел: ', 'Число: ')

    for i in range(len(numbers) + 1):
        new_part = []
        new_list = numbers.copy()
        new_part.extend(numbers[i::-1])
        new_list.extend(new_part)
        if is_symmetric(new_list):
            print()
            print_list('Последовательность: ', numbers)
            print('Нужно приписать чисел:', len(new_part))
            print_list('Сами числа: ', new_part)
            break


main()
