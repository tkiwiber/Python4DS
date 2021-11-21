from _collections_abc import Iterable


class QHofstadter:
    """" Class iterator to count Hofstadter Q sequence """

    def __init__(self, seq: list) -> None:
        self.seq = seq[:]
        self.stop = False
        if seq[0] == 1 and seq[1] == 2 and len(seq) == 2:
            self.stop = True

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> int:
            if self.stop:
                raise StopIteration
            try:
                q = self.seq[-self.seq[-1]] + self.seq[-self.seq[-2]]
                self.seq.append(q)
                return q
            except IndexError as err:
                print(err)
                raise StopIteration

    def __str__(self):
        return ' '.join([str(item) for item in self.seq])


Q = QHofstadter([1, 2])

for _ in range(20):
    try:
        next(Q)
    except StopIteration:
        break
print(Q)

Q = QHofstadter([1, 1])

for _ in range(20):
    try:
        next(Q)
    except StopIteration:
        break
print(Q)
