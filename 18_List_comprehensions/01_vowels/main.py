
vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

text = input('Введите текст: ')
print('\nСписок гласных букв:', [letter for letter in text if letter in vowel])
print('Длина списка:', len([letter for letter in text if letter in vowel]))
