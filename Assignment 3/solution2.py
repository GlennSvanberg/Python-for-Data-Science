"""
Define a class Circle () where the objects constructed from this class will be circles of various sizes.
Define the following 2 methods for this class: constructor method which uses a radius parameter and surface () method which returns the area of the circle.

Then define a class Cylinder () which is derived from the previous one. The constructor of this new class will include the two parameters radius and height.
You will define a volume() method which will return the volume of the cylinder.

Finally, define a class Cone (), which must derive this time from the class Cylinder (),
and whose constructor will also include the two parameters radius and height. This new class will have its own volume () method,
which will return the volume of the cone.
"""
from math import pi


class Circle():

    def __init__(self, radius):
        self.radius = radius

    def surface(self):
        return pi * self.radius**2


c = Circle(4)
print("Circle: ", c.surface())


class Cylinder(Circle):

    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def volume(self):
        return self.surface() * self.height


cyl = Cylinder(4, 9)
print("Cylinder: ", cyl.volume())


class Cone(Cylinder):

    def __init__(self, radius, height):
        super().__init__(radius, height)

    def volume(self):
        return (1 / 3) * pi * self.radius**2 * self.height


cone = Cone(4, 9)
print("Cone: ", cone.volume())
