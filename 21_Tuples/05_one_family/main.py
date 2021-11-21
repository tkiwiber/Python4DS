families = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Петров', 'Витя'): 20,
    ('Моргунов', 'Иван'): 23,
    ('Моргунова', 'Лера'): 23,
    ('Петров', 'Иван'): 44,
    ('Иванова', 'Лидия'): 29,
    ('Иванов', 'Сергей'): 34,
}

surname = input('Введите фамилию: ').lower()

print()
for person, age in families.items():
    to_print = False
    for each in person:
        if surname in each.lower():
            to_print = True
    if to_print:
        print(' '.join([each for each in person]), age)


