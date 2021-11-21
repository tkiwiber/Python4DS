import io
import zipfile
import os
from functools import cmp_to_key


def cmp(item1, item2):
    if item1[1] < item2[1]:
        return 1
    if item1[1] > item2[1]:
        return -1

    if item1[0] > item2[0]:
        return 1
    if item1[0] < item2[0]:
        return -1

    return 0


def main():

    if not os.path.exists('voyna-i-mir.zip'):
        print("Error! File 'voyna-i-mir.zip' not found. Stop")
        return -1

    if not zipfile.is_zipfile('voyna-i-mir.zip'):
        print("Error! Not a valid zip file. Stop")
        return -1

    with zipfile.ZipFile('voyna-i-mir.zip', 'r') as my_zip:
        try:
            my_zip.extract('voyna-i-mir.txt')
            file = open('voyna-i-mir.txt', 'r', encoding='utf8')
            draft = file.read()
        except FileNotFoundError:
            print("Error! Can't found 'voyna-i-mir.txt' in archive. Stop")
            return -1
        except IOError:
            print("Error! I/O problem. Stop")
            return -1

    os.remove('voyna-i-mir.txt')
    file.close()
    my_zip.close()

    data = \
        ''.join([ch for ch in draft if ch.isalpha()])

    alphabet_dict = {x: data.count(x) for x in set(data)}
    sorted_dict = dict(sorted(alphabet_dict.items(), key=cmp_to_key(cmp)))

    new = open('answer.txt', 'w')
    for letter, freq in sorted_dict.items():
        new.write("'{letter}': {freq:,}\n".format(letter=letter, freq=freq))
    new.close()

    return 0


main()
