
def remove_of(val, in_list):
    while True:
        try:
            in_list.remove(val)
        except ValueError:
            break


def fill_list(vid_cards_list, n):
    for _ in range(n):
        card_number = int(input('Видеокарта: '))
        vid_cards_list.append(card_number)
    return vid_cards_list


def update_list(vid_cards_list_update, vid_cards_list):
    max_value = 0
    for i in range(len(vid_cards_list)):
        if vid_cards_list[i] > max_value:
            max_value = vid_cards_list[i]
    remove_of(max_value, vid_cards_list_update)
    return vid_cards_list_update


def main():
    vid_cards_list = []
    n = int(input('Кол-во видеокарт: '))

    vid_cards_list = fill_list(vid_cards_list, n)
    vid_cards_list_update = vid_cards_list.copy()
    vid_cards_list_update = update_list(vid_cards_list_update, vid_cards_list)
    print('\nСтарый список видеокарт: ', vid_cards_list, sep='')
    print('Новый список видеокарт: ', vid_cards_list_update, sep='')


main()
