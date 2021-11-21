
def is_palindrome(u_list):
    reversed_u_list = u_list.copy()
    reversed_u_list.reverse()
    if u_list == reversed_u_list:
        return True
    else:
        return False


def main():
    word = input('Введите слово: ')
    word_list = [x for x in word]
    if is_palindrome(word_list):
        print('\nСлово является палиндромом')
    else:
        print('\nСлово НЕ является палиндромом')


main()
