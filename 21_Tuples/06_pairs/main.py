from random import randint


nums = [randint(0, 9) for i in range(10)]
new_nums = [(nums[i], nums[i + 1]) for i in range(0, 9, 2)]

print('Оригинальный список: ', nums)
print('Новый список:', new_nums)
