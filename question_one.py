#import the abc library that provides the infrastrcture for creating abstract classes in python

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        #include the code to calculate area of a shape
        pass

    @abstractmethod
    def calculate_perimeter(self):
        #include the code to calculate perimeter of a shape
        pass


#code for the circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
    def calculate_perimeter(self):  
        return 2 * math.pi * self.radius

#code for the rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(4, 6)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter)