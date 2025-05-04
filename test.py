class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    @staticmethod
    def unit_circle():
        return Circle(1)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

c = Circle(3)
print(c.area())

u = Circle.unit_circle()
print(u.radius)

big = Circle.from_diameter(10)
print(big.radius)