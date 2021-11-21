
word = input('Введите слово: ')
letters = [x for x in word]
unique_letters = 0

for i in letters:
    if letters.count(i) == 1:
        unique_letters += 1

print('Кол-во уникальных букв:', unique_letters)

