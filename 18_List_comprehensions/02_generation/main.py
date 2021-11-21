n = int(input('Введите число: '))

print([1 if x % 2 == 0 else x % 5 for x in range(n)])
