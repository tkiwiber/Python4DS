
class Person:
    __count = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Person.__count += 1

    def set_age(self, age):
        if isinstance(age, int):
            if age >= 0:
                self.__age = age
            else:
                raise Exception('Incorrect age. Must be in positive integer')
        else:
            raise Exception('Incorrect age. Must be an integer value')

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception('Incorrect name. Must be string value')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_count(self):
        return self.__count

    def __str__(self):
        return 'Name: {}, Age: {}'.\
            format(self.get_name(), str(self.get_age()))
