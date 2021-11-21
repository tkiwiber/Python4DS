import os
from time import gmtime, strftime


def main():

    n = 5
    if not os.path.exists('people.txt'):
        print("Error! File 'people.txt' not found. Stop")
        return -1

    length = 0
    i = 0

    with open('people.txt', 'r') as file:
        for line in file:
            try:
                i += 1
                length += len(line) - (1 if line.endswith('\n') else 0)
                if len(line) <= 3:
                    raise BaseException
            except BaseException:
                print('Error at line #{}. More details saved to error.log\n'.format(i))
                with open('error.log', 'a') as error:
                    error.write('{} Error! Line #{} contains less then 3 chars\n'.format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), i))
            finally:
                print('Total length of all usernames is {}'.format(length))
    return 0


main()
