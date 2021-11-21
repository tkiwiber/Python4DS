def my_sum(*argv):
    s = 0

    for elem in argv:
        if not isinstance(elem, list):
            s += elem
        else:
            for x in elem:
                s += my_sum(x)

    return s


a = [1, 2, [3, 4]]
b = 1
c = 2
d = [1, [1, [1, [1]]]]

print(my_sum(a, b, c, d))
