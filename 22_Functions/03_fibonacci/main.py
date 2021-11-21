def fib_row(stop, count, value=[0, 1]):
    if stop < 1:
        print('Число: {}'.format(0))
        return
    if count == stop:
        print('Число: {}'.format(value[0]))
        return
    tmp = value
    value = [tmp[1], tmp[0] + tmp[1]]
    count += 1
    fib_row(stop, count, value)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
fib_row(num_pos, 0)
