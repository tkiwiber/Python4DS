
def modify_text(ch, sh):
    try:
        if alphabet_low.index(ch.lower()) + shift <= 31:
            return alphabet_low[alphabet_low.index(ch.lower()) + sh] \
                if ch.islower() else alphabet_upp[alphabet_low.index(ch.lower()) + sh]
        else:
            return alphabet_low[(alphabet_low.index(ch.lower()) + sh) % 32] \
                if ch.islower() else alphabet_upp[(alphabet_low.index(ch.lower()) + sh) % 32]
    except ValueError:
        return ' '


print()
text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

alphabet_low = [chr(ord('а') + i) for i in range(32)]
alphabet_upp = [chr(ord('А') + i) for i in range(32)]
caesar_text = [modify_text(char, shift) for char in text]
print(''.join(caesar_text))
