import os


def parse_chart(score_str, chart_list):
    new = dict()

    try:
        min_score = int(score_str)
    except ValueError:
        print('ParseError. Check score in line [1]!')
        return -1

    ln = 1
    for each in chart_list:
        ln += 1
        line = each.split()
        try:
            score = int(line[2])
        except ValueError:
            print('ParseError. Check score value in line [{}]!'.format(ln))
            return None
        except IndexError:
            print('ParseError. Check file structure!')
            return None
        new[' '.join(line[0:2])] = score

    return min_score, dict(sorted(new.items(), key=lambda item: item[1], reverse=True))


def save_next_tour(score, first_tour):
    new = open('second_tour.txt', 'w')

    lines_to_save = list()
    ln = 0
    for key, value in first_tour.items():
        name = key.split()
        ln += 1

        if value > score:
            lines_to_save.append('{line}) {name}. {surname} {score}'.format(
                line=ln,
                name=name[1][0],
                surname=name[0],
                score=str(value)
            ))
        else:
            break

    new.write(''.join([str(len(lines_to_save)), '\n']))
    with new:
        [new.write(f'{ln}\n') for ln in lines_to_save]
    new.close()

    return 0


def main():
    if not os.path.exists('first_tour.txt'):
        print("Error. File doesn't exist")
        return -1

    file = open('first_tour.txt', 'r')
    chart = file.readlines()

    chart_info = parse_chart(chart[0], chart[1:])
    if chart_info is None:
        return -1

    save_next_tour(chart_info[0], chart_info[1])
    return 0


main()
