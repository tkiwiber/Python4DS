def mirror_word(mes, spaces):
    w_list = []
    s_pos = 0
    is_spaces = False
    for i in range(len(mes)):
        if mes[i] not in spaces:
            if is_spaces:
                w_list.append(mes[s_pos:i])
                s_pos = i
                is_spaces = False
        else:
            if not is_spaces:
                # w_list.append(mes[s_pos:i:])
                w_list.append(mes[-len(mes) + i - 1:-len(mes) + s_pos - 1:-1])
                s_pos = i
                is_spaces = True
    return w_list


message = input('Сообщение: ')

word_list = mirror_word(message, ' :.,!?')
print(word_list)

print('\n', ''.join(each for each in word_list))
