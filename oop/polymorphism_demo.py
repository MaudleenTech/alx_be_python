import math

class Shape:
    # Base class for all shapes.
    def area(self):
        # Must be overridden by derived classes.
        raise NotImplementedError("Subclasses must implement the 'area()' method.")

class Rectangle(Shape):
    # Derived class for a rectangle.
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Overrides area() for rectangle: length * width.
        return self.length * self.width

class Circle(Shape):
    # Derived class for a circle.
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Overrides area() for circle: pi * radius^2.
        return math.pi * (self.radius ** 2)