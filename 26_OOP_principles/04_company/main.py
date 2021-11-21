
class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def __str__(self):
        return ''. join([self.get_surname().title(), ' ', self.get_surname()[0].upper(), '.'])



class Employee(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def calc_salary(self):
        pass


class Manager(Employee):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def calc_salary(self):
        return 13000


class Agent(Employee):

    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.__sales = sales

    def calc_salary(self):
        return 5000 + 0.05 * self.__sales


class Worker(Employee):

    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.__hours = hours

    def calc_salary(self):
        return 100 * self.__hours


employees = [
    Manager('alex', 'romanov', 30),
    Manager('alex', 'gorbunov', 30),
    Manager('alex', 'lopatov', 30),
    Agent('amx', 'greg', 30, 30000),
    Agent('max', 'rompittanov', 30, 40000),
    Agent('fiat', 'duke', 30, 45000),
    Worker('rita', 'poroff', 30, 60),
    Worker('cole', 'duma', 30, 68),
    Worker('nadine', 'rigly', 30, 40),
]


for each in employees:
    print(each, 'salary =', each.calc_salary())
