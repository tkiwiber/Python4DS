from random import randint


def mutate_tuple(user_tuple, elem):
    new_list = list(user_tuple)

    start = end = -1
    for index, value in enumerate(user_tuple):
        if value == elem and start > -1 and end == -1:
            end = index + 1
        if value == elem and start == -1:
            start = index
    return tuple(new_list[start if start > -1 else None:
                          end if start > -1 and end > -1 else None])


my_tuple = ('1', '2', '3', '2', '5', '2', '5', '7', '1')
random_elem = str(randint(1, 5))

print('Base tuple:', my_tuple)
print("Random element: '{0}'".format(random_elem))
print()
print(mutate_tuple(my_tuple, random_elem))
