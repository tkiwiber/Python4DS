shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
detail = input('Название детали: ')
count = 0
amount = 0

for item in shop:
    if item[0] == detail:
        count += 1
        amount += item[1]

print('Кол-во деталей -', count)
print('Общая стоимость -', amount)
