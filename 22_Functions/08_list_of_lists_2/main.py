def flatten_list(user_list, new_list=[]):
    for each in user_list:
        if isinstance(each, list):
            flatten_list(each)
        else:
            new_list.append(each)
    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
flat_list = flatten_list(nice_list)
print(flat_list)
