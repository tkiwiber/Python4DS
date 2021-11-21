
class_1 = [x for x in range(160, 176 + 1, 2)]
class_2 = [x for x in range(162, 180 + 1, 3)]

class_1.extend(class_2)
class_1.sort()

print(class_1)
