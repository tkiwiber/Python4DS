def create_list(nbr):
    new_list = []
    for j in range(nbr):
        print('Введите число №', j + 1, ': ', sep='', end='')
        nbr = int(input())
        new_list.append(nbr)
    return new_list


i = 1
draft_list = []
num1 = int(input('Введите кол-во элементов первого списка: '))
list1 = create_list(num1)
num2 = int(input('Введите кол-во элементов второго списка: '))
list2 = create_list(num2)

print()
print('Первый список:', list1)
print('Второй список:', list2)
print()

list1.extend(list2)
draft_list.append(list1[0])
print(len(list1))
while i < len(list1):
    while list1[i] not in draft_list:
        draft_list.append(list1[i])
    i += 1
list1 = draft_list

print('Новый первый список с уникальными элементами:', list1)
