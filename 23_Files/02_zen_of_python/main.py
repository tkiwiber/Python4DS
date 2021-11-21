zen_file = open('zen.txt', 'r')

data = zen_file.readlines()

for line in reversed(data):
    print(line, end='')

zen_file.close()
