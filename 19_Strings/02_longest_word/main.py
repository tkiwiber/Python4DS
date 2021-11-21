user_list = sorted(input('Введите строку: ')
                   .split(), key=len, reverse=True)

print('Самое длинное слово: "{0}", его длина: {1} символов'
      .format(user_list[0], len(user_list[0])))
