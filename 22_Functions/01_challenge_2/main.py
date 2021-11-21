def print_nums(n):
    if n == 0:
        return
    print_nums(n - 1)
    print(n, end=' ')
    return


num = int(input('Введите число: '))
print_nums(num)
