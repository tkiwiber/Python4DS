from sys import maxsize


def count_chars(string):
    return {ch: string.count(ch)
            for ch in set(string.lower())
            if ch.isalpha()
            }


zen_file = open('../02_zen_of_python/zen.txt', 'r')
stat = {
    'lines': 0,
    'chars': 0,
    'words': 0,
    'letter': ''
        }


for line in zen_file:
    stat['lines'] += 1
    stat['words'] += len(line.split())
    for ch in line:
        if ch.isalpha():
            stat['chars'] += 1

zen_file.seek(0)
data = zen_file.read()
ch_dict = count_chars(data)

min_v = maxsize
min_ch = ''
for key, value in ch_dict.items():
    if value < min_v:
        min_v = value
        min_ch = key

stat['letter'] = min_ch

for key, value in stat.items():
    print('{}: {}'.format(key, value))

zen_file.close()
