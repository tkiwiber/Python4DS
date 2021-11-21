def my_zip(s_str, t_tpl):
    pairs = ((s_str[i], t_tpl[i])
             for i in range(min(len(s_str), len(t_tpl))))
    return pairs


sym_str = 'abcd'
sym_tpl = (1, 2, 3)

print(sym_str.__class__)

print(sym_tpl is tuple)
result = my_zip(sym_str, sym_tpl)
print(result)
for elem in result:
    print(elem)
