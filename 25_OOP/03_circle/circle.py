import math


class Circle:

    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius

    def square(self):
        return math.pi * (self.radius ** 2)

    def length(self):
        return 2 * math.pi * self.radius

    def increase(self, k):
        if not isinstance(k, int):
            raise ValueError("Error! 'Circle' class method expected Integer")
        if k <= 0:
            raise ValueError("Error! 'Circle' class method value must be positive integer")
        self.radius *= k

    def intersected(self, another):
        if not isinstance(another, Circle):
            raise TypeError("Error! Class method expected 'Circle' object")
        d = math.sqrt((self.x - another.x) ** 2 + (self.y - another.y) ** 2)

        if d > (self.radius + another.radius):
            return False
        if d < abs(self.radius - another.radius):
            return False
        return True
