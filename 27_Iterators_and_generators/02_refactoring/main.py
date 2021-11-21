
def find(list1: list, list2: list, stop: int) -> int:
    for x in list1:
        for y in list2:
            yield x * y
            if x * y == stop:
                print("Found! x = {}, y = {}".format(x, y))
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

seq = find(list_1, list_2, to_find)
for i in seq:
    print(i)

# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break

# TODO провести рефакторинг кода
