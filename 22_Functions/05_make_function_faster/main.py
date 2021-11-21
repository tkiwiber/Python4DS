def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num - 1)


def get_from_cache(num, cache={}):
    print('cache={}'.format(cache))
    if num in cache:
        return cache[num]
    cache[num] = result = factorial(num)
    print('res=', result)

    return result


def calculating_math_func(data):

    result = get_from_cache(data)
    result /= data ** 3
    result = result ** 10

    return result


while True:
    user_data = int(input('Введите число: '))
    if user_data == -1:
        break
    res = calculating_math_func(user_data)
    print(res)
