from vehicle import Vehicle


class Auto(Vehicle):

    def __init__(self, pos_x, pos_y, angle):
        super().__init__(pos_x, pos_y, angle)

    def __str__(self):
        return ''.join(['Type: Auto. ', super().__str__()])


class Bus(Vehicle):

    def __init__(self, pos_x, pos_y, angle, passengers):
        super().__init__(pos_x, pos_y, angle)
        self.__passengers = passengers
        self.__income = 0
        self.__max_passengers_count = 54
        self.__min_passengers_count = 0
        self.__price_per_distance = 1

    def __str__(self):
        return ''.join([
            'Type: Bus. ',
            super().__str__(),
            '. Passengers: {}. Income: {}'.format(self.get_passengers(), round(self.get_income(), 2))
        ])

    def get_income(self):
        return self.__income

    def get_passengers(self):
        return self.__passengers

    def enter_bus(self, passengers):
        if self.__passengers + passengers > self.__max_passengers_count:
            raise ValueError('Too many passengers to this bus. Value cant be more than {}'.format(
                self.__max_passengers_count
            ))
        self.__passengers += passengers

    def exit_bus(self, passengers):
        if self.__passengers - passengers < 0:
            raise ValueError('Too less passengers to exit. Value cant be less than {}'.format(
                self.__min_passengers_count
            ))
        self.__passengers -= passengers

    def move(self, distance):
        super().move(distance)
        self.__income += round(self.__passengers * self.__price_per_distance / distance, 2)


# Some simple tests with Auto

auto = Auto(pos_x=0, pos_y=0, angle=20)
print(auto)

auto.turn_left(60)
auto.move(10)
print(auto)

# Some simple tests with Bus

bus = Bus(pos_x=-1, pos_y=-1, angle=75, passengers=13)
print(bus)

bus.move(10)
print(bus)

bus.enter_bus(13)
bus.move(10)
print(bus)

bus.exit_bus(26)
bus.move(10)
print(bus)


