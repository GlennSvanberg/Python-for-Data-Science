from math import pi


class Circle():

    def __init__(self, radius):
        self.radius = radius

    def surface(self):
        return pi * self.radius**2


class Cylinder(Circle):

    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def volume(self):
        return self.surface() * self.height


class Cone(Cylinder):

    def __init__(self, radius, height):
        super().__init__(radius, height)

    def volume(self):
        return (1 / 3) * super().volume()


c = Circle(4)
print("Circle: ", c.surface())

cyl = Cylinder(4, 9)
print("Cylinder: ", cyl.volume())

cone = Cone(4, 9)
print("Cone: ", cone.volume())
