user_file = open('numbers.txt', 'r')
save_file = open('answer.txt', 'w')

result = 0

for line in user_file:
    for ch in line:
        print(ch, end='')
        if '0' <= ch <= '9':
            result += int(ch)

save_file.write(str(result))

user_file.close()
save_file.close()
