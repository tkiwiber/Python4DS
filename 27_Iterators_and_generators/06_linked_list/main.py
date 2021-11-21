from linkedlist import LinkedList


my_list = LinkedList()
my_list.append(20)
my_list.append(10)
my_list.append('wer')
my_list.append(['this', 'is', 'to', 'delete'])
my_list.append(999)
my_list.append(0)
my_list.append('d')
elem_to_get = 2
elem_to_remove = 2
print('Текущий список:', my_list)
print('Получение элемента #{}: {}'.format(elem_to_get, my_list.get(elem_to_get)))
print('Удаление элемента #{} ({}).'.format(elem_to_remove, my_list.get(elem_to_remove)))
my_list.remove(elem_to_remove)
print('Новый список:', my_list)

print('-' * 20)
for i in my_list:
    print(i)
