
def find_letter(some_list, letter):
    for i in range(len(some_list)):
        if some_list[i] == letter:
            return i
    else:
        return 0


string = 'daasdhasd.,.sdhdsna_hdsajk'
original_list = [x for x in string]
reversed_list = original_list[::-1]

start = find_letter(original_list, 'h') + 1
end = len(original_list) - find_letter(reversed_list, 'h') + 1
output = original_list[-start:-end:-1]
print(output)
