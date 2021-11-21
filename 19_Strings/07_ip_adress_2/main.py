def check_ip(ip):
    res = True
    for each in ip:
        try:
            res = 0 <= int(each) <= 255
        except ValueError:
            return False, each
    return res, 1


ip_address = input('Введите IP: ').split('.')
is_ip, err = check_ip(ip_address)
if not is_ip:
    print('{0} не является целым числом'.format(err))
elif len(ip_address) != 4:
    print('Формат ip-адреса не соответствует *.*.*.*')
else:
    print('IP-адрес введен корректно')
