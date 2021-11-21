def histogram(text):
    sym_dict = dict()
    for sym in text:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def invert_histogram(text):
    sym_dict = dict()
    values = set(text.values())
    sym_dict = {value: [key for key, v in text.items() if v == value] for value in values}

    return sym_dict


def show_dict(u_data, param):
    print('-' * 30)
    if param == 'origin':
        print('Оригинальный словарь частот:')
    elif param == 'invert':
        print('Инвертированный словарь частот:')
    for key, value in u_data.items():
        print("'{}': {}".format(key, value))
    print('-' * 30, '\n')


data = input('Введите текст: ')

hist = histogram(data)

inverted_hist = invert_histogram(hist)
show_dict(inverted_hist, 'invert')
