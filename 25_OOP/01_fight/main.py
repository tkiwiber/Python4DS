from warrior import WarriorsRaw

warriors = WarriorsRaw(2)

round_num = 0
while True:
    round_num += 1
    print('ROUND {}.'.format(round_num))
    warriors.random_attack()
    if warriors.someone_dead():
        warriors.show_winners()
        break
