# protocol = {
#     1: ['69485', 'Jack'],
#     2: ['95715', 'qwerty'],
#     3: ['95715', 'Alex'],
#     4: ['83647', 'M'],
#     5: ['197128', 'qwerty'],
#     6: ['95715', 'Jack'],
#     7: ['93289', 'Alex'],
#     8: ['95715', 'Alex'],
#     9: ['95715', 'M']
# }

def create_protocol(n):
    record_dict = dict()
    for i in range(1, n + 1):
        print(i, 'запись: ', end='')
        record = input().split()
        record_dict[i] = record
    return record_dict


def leaderboard(record):
    players = set([value[1] for value in protocol.values()])
    board = dict()

    for each in players:
        for key, value in protocol.items():
            if value[1] == each:
                if board.get(each) is None:
                    board[each] = [value[0], key]
                else:
                    if int(value[0]) > int(board[each][0]):
                        board[each][0] = value[0]
                        board[each][1] = key
    return board


def find_best(board):
    best_score = 0
    best_time = 0
    best_name = ''
    for name, value in board.items():
        if int(value[0]) > best_score:
            best_score = int(value[0])
            best_name = name
            best_time = int(value[1])
        elif int(value[0]) == best_score:
            if value[1] < best_time:
                best_score = int(value[0])
                best_name = name
                best_time = int(value[1])
    return best_name, best_score


def show_board(board, top):
    print()
    print('Итоги соревнований:')

    for i in range(1, top + 1):
        best_name, best_score = find_best(board)
        print('{} место. {} ({})'.format(i, best_name, best_score))
        board.pop(best_name)


num = int(input('Сколько записей вносится в протокол? '))
protocol = create_protocol(num)
leaders = leaderboard(protocol)
show_board(leaders, 3)
