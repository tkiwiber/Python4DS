from person import Person


class Calm:

    __calm_dict = {
        1: 'iceman',
        2: 'quite relaxed',
        3: 'very aggressive'
    }

    def __init__(self, state):
        if 1 <= state <= 3:
            self.__state = state
        else:
            raise ValueError('Calm state must be in 1..3 range')

    def get_state(self):
        return self.__calm_dict.get(self.__state)

    def change_state(self):
        if self.__state > 1:
            self.__state -= 1


class Hungry:

    __hungry_dict = {
        1: 'better to sleep',
        2: 'can eat everything',
        3: 'nothing can stop me'
    }

    def __init__(self, state):
        if 1 <= state <= 3:
            self.__state = state
        else:
            raise ValueError('Hungry state must be in 1..3 range')

    def get_state(self):
        return self.__hungry_dict.get(self.__state)

    def change_state(self):
        if self.__state > 1:
            self.__state -= 1


class Kid(Person):

    def __init__(self, parent_inst, name, age, calm, hunger):
        super().__init__(name, age)
        self.__parent = None
        self.set_parent(parent_inst)
        self.check_age()
        self.set_calm(calm)
        self.set_hunger(hunger)
        self.__parent.set_children(self)
        self.set_age(age)

    def set_parent(self, parent_inst):
        if isinstance(parent_inst, Parent):
            self.__parent = parent_inst
        else:
            raise ValueError('Expected Parent object as a parent')

    def set_calm(self, calm):
        self.__calm = Calm(calm)

    def set_hunger(self, hungry):
        self.__hungry = Hungry(hungry)

    def check_age(self):
        if (16 + self.get_age()) < self.__parent.get_age():
            pass
        else:
            raise ValueError('Too young parent. Age difference couldnt be more than 16')

    def get_hungry(self):
        return self.__hungry.get_state()

    def get_calm(self):
        return self.__calm.get_state()

    def get_parent(self):
        return self.__parent.get_name()

    def __str__(self):
        return '\tKid Name: {}, Age: {}, Parent is {} Calm: {}, Hungry: {}'.\
            format(self.get_name(), str(self.get_age()), self.get_parent(),
                   self.get_calm(), self.get_hungry())

    def get_info(self):
        print(self.__str__())

    def calm_down(self):
        self.__calm.change_state()

    def feed_kid(self):
        self.__hungry.change_state()


class Parent(Person):

    def __init__(self, name, age, children):
        super().__init__(name, age)
        self.__children = []

    def set_children(self, children):
        if isinstance(children, Kid):
                self.__children.append(children)
        else:
            raise TypeError('Children parameter must be a Kid type')

    def __str__(self):
        info = super().__str__()
        info = ''.join((
            'Adult >> ',
            info,
            ', Children: {}'.format(', '.join(each.get_name() for each in self.__children))
        ))
        return info

    def get_info(self):
        print(self.__str__())

    def calm_kid(self, kid):
        if isinstance(kid, Kid):
            kid.calm_down()
        else:
            raise TypeError('Children parameter must be a Kid type')

    def feed_kid(self, kid):
        if isinstance(kid, Kid):
            kid.feed_kid()
        else:
            raise TypeError('Children parameter must be a Kid type')


print('\nCreate Parent...\n')
vika = Parent(name='Vika', age=22, children=[])
vika.get_info()
print('\nCreate children...\n')
boby = Kid(parent_inst=vika, name='Boby', age=4, calm=3, hunger=3)
lena = Kid(parent_inst=vika, name='Lena', age=5, calm=2, hunger=3)
boby.get_info()
lena.get_info()
print('\nNew state of Parent...\n')
vika.get_info()
print('\nVika trying to calm and feed Boby few times\n')
for _ in range(3):
    vika.calm_kid(boby)
    vika.feed_kid(boby)
    boby.get_info()
    lena.get_info()
    print()
