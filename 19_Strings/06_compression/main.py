
data = input('Введите строку: ')
zip_list = []

for i in range(len(data)):
    if i == 0:
        item = [data[i], 1]
        zip_list.append(item)
        continue
    else:
        if data[i] == data[i - 1]:
            zip_list[len(zip_list) - 1][1] += 1
        else:
            item = [data[i], 1]
            zip_list.append(item)

flat_list = [str(item) if type(item) == int else item
             for sublist in zip_list for item in sublist]

print(''.join(each for each in flat_list))
