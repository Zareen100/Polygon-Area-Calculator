import math

class Polygon:
    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def main():
    # Create instances of each polygon
    triangle = Triangle(base=10, height=5)
    rectangle = Rectangle(width=4, height=6)
    circle = Circle(radius=3)

    # Calculate and print areas
    print("Area of Triangle:", triangle.area())
    print("Area of Rectangle:", rectangle.area())
    print("Area of Circle:", circle.area())

if __name__ == "__main__":
    main()
