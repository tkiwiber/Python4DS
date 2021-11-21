num = int(input('Кол-во стран: '))

countries_dict = {}
for i in range(1, num + 1):
    print('{} страна: '.format(i), end='')
    countries_list = input().split()
    countries_dict[countries_list[0]] = [countries_list[item] for item in range(1, len(countries_list))]

print(countries_dict)

for i in range(3):
    print('\n{0} город: '.format(i + 1), end='')
    city = input()
    for country, cities in countries_dict.items():
        if city in cities:
            print('Город {city} расположен в стране {country}.'.format(city=city, country=country))
            break
        else:
            print(f'По городу {city} данных нет.'.format(city=city))
            break
