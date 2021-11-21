while True:
    password = input('Придумайте пароль: ')
    capital = 0
    numeric = 0
    for each in password:
        if each.lower().isalpha() or each.isdigit():
            capital += 1 if each.isupper() else 0
            numeric += 1 if each.isdigit() else 0
        else:
            print('Используйте латинский алфавит')
            break
    if len(password) >= 8 and capital >= 1 and numeric >= 3:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
