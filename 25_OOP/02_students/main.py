from student import Student
from random import choice
from random import randint

names = ['alex', 'ura', 'bob', 'vera', 'nika', 'lena', 'petya', 'serg']
surnames = ['petrov', 'orlov', 'ivanov', 'tomphson', 'fills']
marks = [1, 2, 3, 4, 5]

students = [Student(
    ' '.join([choice(names), choice(surnames)]),
    randint(1, 20),
    [choice(marks) for _ in range(5)]
) for _ in range(10)
]

students.sort(key=lambda x: x.mark)

for each in students:
    each.info()
