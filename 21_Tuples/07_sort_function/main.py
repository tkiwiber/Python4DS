def sort_tuple(user_tuple):
    new_tuple = list(user_tuple[:])
    print(new_tuple)
    for num in user_tuple:
        if not isinstance(num, int):
            return user_tuple
    return tuple(sorted(new_tuple))


my_tuple1 = (1, 2, 10, 4, 0, 1)
my_tuple2 = (1, 2, 10, 4, 0, '1')

sorted_my_tuple = sort_tuple(my_tuple1)
print(sorted_my_tuple)
print()
sorted_my_tuple = sort_tuple(my_tuple2)
print(sorted_my_tuple)