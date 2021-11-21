
def validate(data):

    if len(data) != 3:
        raise BaseException('IndexError')

    name = data[0]
    mail = data[1]
    try:
        age = int(data[2])
    except ValueError:
        raise BaseException('AnotherError')

    if not 10 <= age <= 99:
        raise BaseException('ValueError')
    if not name.isalpha():
        raise BaseException('NameError')
    if not ('.' in mail and '@' in mail):
        raise BaseException('SyntaxError')

    return True


def main(f_name):
    try:
        with open(f_name, 'r') as reg_file, \
            open('registrations_good.log', 'w') as good_log, \
                open('registrations_bad.log', 'w') as bad_log:
            for line in reg_file:
                try:
                    if validate(line.split()):
                        good_log.write(line)
                except BaseException as err:
                    bad_log.write(''.join([line[:-1], ' ', str(err), '\n']))
    except IOError as err:
        print('Ошибка ввода/вывода, проверьте файлы!')
        return 1

    return 0


main('registrations.txt')
