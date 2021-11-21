import ast


def my_zip(s1, s2):
    iter1 = iter(s1)
    iter2 = iter(s2)
    for _ in range(min(len(s1), len(s2))):
        yield next(iter1), next(iter2)


def print_zip(zip_list):
    for each in zip_list:
        print(each)


def convert_data(user_seq):
    try:
        result = ast.literal_eval(user_seq)
        return result
    except RecursionError:
        print('Ошибка! Введена слишком запутанная последовательность')
        return -1
    except TypeError:
        print('Ошибка! Введена не итерируемая последовательность')
        return -1
    except SyntaxError:
        print('Ошибка! Введена не итерируемая последовательность')
        return -1
    except ValueError:
        result = ast.literal_eval("\'" + user_seq + "\'")
        return result


def main():
    seq1 = input('Последовательность 1: ')
    seq2 = input('Последовательность 2: ')

    user_seq1 = convert_data(seq1)
    user_seq2 = convert_data(seq2)

    if user_seq1 != -1 and user_seq1 != -1:
        print('Результат:')
        seq = my_zip(user_seq1, user_seq2)
        print(seq)
        print_zip(seq)
    else:
        print('Генератор не создан')


main()
