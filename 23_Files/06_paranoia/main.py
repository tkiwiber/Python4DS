import os


def main():
    if not os.path.exists(os.path.join(os.path.abspath('text.txt'), 'text.txt')):
        file = open('text.txt', 'r')
    else:
        print('Error! Nothing to encrypt.')
        return -1

    new_file = open('cipher_text.txt', 'w')

    ln = 0
    for line in file:
        ln += 1
        for ch in line:
            if ch == '\n':
                new_file.write(ch)
            else:
                new_file.write(chr(ord(ch) + ln))

    file.close()
    new_file.close()


main()
