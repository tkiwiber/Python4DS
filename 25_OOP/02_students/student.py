
class Student:
    min_mark = 1
    max_mark = 5

    def __init__(self, name, group, marks):
        self.name = ' '.join([elem.title() for elem in name.split()])
        self.group = group
        if not isinstance(group, int):
            raise TypeError('Number of group must be Integer')
        if not isinstance(marks, list):
            raise TypeError('Marks must be list of Integer between {} and {}'.
                            format(self.min_mark, self.max_mark))
        for mark in marks:
            if not (isinstance(mark, int) and self.min_mark <= mark <= self.max_mark):
                raise TypeError('Marks must be list of Integer between {} and {}'.
                                format(self.min_mark, self.max_mark))
        self.marks = marks
        self.mark = self.count_mark()

    def count_mark(self):
        marks_sum = 0
        for mark in self.marks:
            marks_sum += mark
        return marks_sum/len(self.marks)

    def info(self):
        print('Name: {}\nGroup №: {}\nMarks: [{}]\nAverage: {}\n'.format(
            self.name,
            self.group,
            ','.join([str(mark) for mark in self.marks]),
            self.mark
        ))
