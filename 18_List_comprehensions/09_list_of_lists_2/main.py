nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

flat_list = [item for sublist in nice_list for item in sublist]
flat_list = [item for sublist in flat_list for item in sublist]
print(flat_list)