class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

# Example:
square = Square(5)
print(square.area())  
shape = Shape()
print(shape.area())  