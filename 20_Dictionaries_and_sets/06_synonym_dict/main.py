
while True:
    try:
        N = int(input('Введите количество пар слов: '))
        break
    except ValueError:
        print('Ошибка: Нужно ввести число > 0 !')

count = 1
syn_dict = dict()

while count < N + 1:
    print('{} пара: '.format(count), end='')
    pair = input().lower().split(' - ')
    if len(pair) != 2:
        print('Ошибка: должна быть введена пара через разделитель " - "!')
    elif pair[0] == pair[1]:
        print('Ошибка: слова должны быть различны!')
    elif pair[0] in syn_dict or pair[1] in syn_dict:
        print('Ошибка: все слова в словаре должны быть различны!')
    else:
        syn_dict[pair[0]] = pair[1]
        count += 1

print()
while True:
    word = input('Введите слово: ').lower()
    if word in syn_dict.keys():
        print('Синоним: {}'.format(''.join(syn_dict[word])))
        break
    elif word in syn_dict.values():
        print('Синоним: {}'.format(''.join([k for k, v in syn_dict.items() if v == word])))
        break
    else:
        print('Такого слова в словаре нет.')

