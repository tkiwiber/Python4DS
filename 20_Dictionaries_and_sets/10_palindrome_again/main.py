def is_sym(word):
    char_dict = {}

    for char in word:
        char_dict[char] = char_dict.get(char, 0) + 1
    odd_char = 0
    for val in char_dict.values():
        odd_char += 1 if val % 2 != 0 else 0

    return odd_char <= 1


def main():
    while True:
        word = input('Введите строку ("end" - для выхода): ').lower()

        if word.lower() == 'end':
            return
        if is_sym(word):
            print('Можно сделать палиндромом')
        else:
            print('Нельзя сделать палиндромом')
        print()


main()
