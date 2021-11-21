from functools import cmp_to_key


# first values by descending order, then keys by ascending order
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
    file = open('text.txt', 'r')
    data_unnorm = file.read()
    file.close()

    data = ''.join([ch.lower()
                    for ch in data_unnorm
                    if ch.isalpha() and 'a' <= ch.lower() <= 'z']
                   )

    alphabet_dict = {x: round(data.count(x) / len(data), 3) for x in set(data)}
    sorted_dict = dict(sorted(alphabet_dict.items(), key=cmp_to_key(cmp)))

    new = open('analysis.txt', 'w')
    for key, value in sorted_dict.items():
        new.write('{char} {val}\n'.format(char=key, val=value))
    new.close()

    return 0


main()
