
def calc_values(n1, n2, operation):

    if operation == '+':
        return n1 + n2
    elif operation == '-':
        return n1 - n2
    elif operation == '*':
        return n1 * n2
    elif operation == '/':
        return n1 / n2
    elif operation == '//':
        return n1 // n2
    elif operation == '%':
        return n1 % n2

    return 0


def calc(data):
    operators = ['+', '-', '/', '*', '//', '%']

    if len(data) != 3:
        raise Exception('Неправильный формат! Должно быть 2 операнда и операция, разделенные пробелом')

    try:
        num1 = int(data[0])
        num2 = int(data[2])
    except ValueError:
        raise Exception('Операнд не является целым числом')

    try:
        operators.index(data[1])
    except IndexError:
        raise Exception('Оператор не является арифметической операцией')

    return calc_values(num1, num2, data[1])


def main(f_name):
    result_sum = 0
    line_number = 0
    try:
        with open(f_name, 'r') as file:
            for line in file:
                line_number += 1
                try:
                    elem = calc(line.split())
                    print('Результат строки №{} (будет учтен в общей сумме): {}'.format(line_number, elem))
                    result_sum += elem
                except Exception as err:
                    print('Результат строки №{} (не будет учтен в общей сумме): {}'.format(line_number, err))
    except IOError:
        print('File <{}> not found'.format(f_name))
        return -1
    else:
        print('\n' + '\x1b[6;30;42m' + 'Общая сумма: {}'.format(result_sum) + '\x1b[0m')
    return 0


main('calc.txt')
