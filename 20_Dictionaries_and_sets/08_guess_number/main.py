from random import randint

N = int(input('Введите максимальное число: '))

number = randint(0, N)
print(number)
base_set = set(str(i) for i in range(0, N + 1))

while True:
    print()
    guess_set = set(input('Нужное число есть среди вот этих чисел: ').lower().split())
    print(guess_set)
    if 'помогите!' in guess_set:
        print('Артём мог загадать следующие числа: {}'.format(' '.join([str(i) for i in base_set])))
        break
    if str(number) in guess_set:
        print('Ответ Артёма: Да')
        base_set.intersection_update(guess_set)
    else:
        print('Ответ Артёма: Нет')
        base_set.difference_update(guess_set)
