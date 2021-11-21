
def check_input(number):
    return True if 1000 <= number <= 9999 else False


def check_year(year):
    for number in range(0, 10):
        count = 0
        for char in str(year):
            if str(number) == char:
                count += 1
                if count == 3:
                    return True
    return False


def print_unique_years(start_year, end_year):
    no_unique_years = True
    for year in range(start_year, end_year + 1):
        if check_year(year):
            no_unique_years = False
            print(year)
    if no_unique_years:
        print('таких нет')


def main():
    start_year = int(input('Введите первый год: '))
    end_year = int(input('Введите второй год: '))

    if check_input(start_year) and check_input(end_year):
        print('\nГода от', start_year, 'до', end_year, 'с тремя одинаковыми цифрами:')
        print_unique_years(start_year, end_year)
    else:
        print('Ошибка ввода!')


main()
