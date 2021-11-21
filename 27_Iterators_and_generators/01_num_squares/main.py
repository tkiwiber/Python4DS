from _collections_abc import Iterable


class Square:
    """" Class iterator to count sequence of number's squares """

    def __init__(self, number: int) -> None:
        self.counter = 0
        self.current_value = 1
        self.number = number

    def __iter__(self) -> Iterable[int]:
        self.counter = 0
        self.current_value = 1

        return self

    def __next__(self) -> int:
        self.counter += 1
        answer = self.current_value ** 2
        if self.counter > self.number:
            raise StopIteration
        self.current_value += 1

        return answer


def square_gen(num: int) -> Iterable[int]:
    for j in range(1, num + 1):
        yield j ** 2


while True:
    try:
        n = int(input('Input number: '))
        break
    except ValueError:
        print('Value must be Integer number')
        continue


print('\nClass:')
n_square_class = Square(n)
for i in n_square_class:
    print(i)

print('\nFunction:')
n_square_func = square_gen(num=n)
for i in n_square_func:
    print(i)

print('\nExpression:')
n_square_expr = (n ** 2 for n in range(1, n + 1))
for i in n_square_expr:
    print(i)

print('\n***')
