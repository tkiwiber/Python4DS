def main():
    first_str = input('Первая строка: ')
    second_str = input('Вторая строка: ')
    string_len = len(first_str)
    data = ''.join([first_str, first_str])
    pos = data.find(second_str)

    if pos == -1:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
    elif pos == 0:
        print('Строки равны, смещать не надо!')
    else:
        print('Первая строка получается из второй со сдвигом {}.'.format(abs(pos - string_len)))


main()
