from math import sin, cos, radians, degrees


class Vehicle:

    def __init__(self, pos_x, pos_y, angle):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.set_angle(angle)

    def get_pos(self):
        return self.__pos_x, self.__pos_y

    def __str__(self):
        return 'Location: ({}, {}). Angle: {}'.format(
            round(self.get_pos()[0], 2),
            round(self.get_pos()[1], 2),
            round(degrees(self.get_angle()))
        )

    def get_angle(self):
        return self.__angle

    def set_pos(self, pos_x, pos_y):
        self.__pos_x = pos_x
        self.__pos_y = pos_y

    def set_angle(self, angle):
        if not 0 <= angle <= 360:
            raise ValueError('Angle must be from 0 to 360 degree ')
        if angle == 360:
            angle = 0
        self.__angle = radians(angle)

    def move(self, distance):
        x, y = self.get_pos()
        new_x = x + distance * round(cos(self.get_angle()), 2)
        new_y = y + distance * round(sin(self.get_angle()), 2)
        self.set_pos(new_x, new_y)

    def turn_left(self, angle):
        old_angle = degrees(self.get_angle())
        if not 0 <= angle <= 180:
            raise ValueError('Angle must be from 0 to 180 degree')
        new_angle = old_angle - angle
        if new_angle < 0:
            new_angle = 360 + new_angle
        self.set_angle(new_angle)

    def turn_right(self, angle):
        old_angle = degrees(self.get_angle())
        if not 0 <= angle <= 180:
            raise ValueError('Angle must be from 0 to 180 degree')
        new_angle = old_angle + angle
        if new_angle > 360:
            new_angle = new_angle - 360
        self.set_angle(new_angle)
