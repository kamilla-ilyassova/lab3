import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Example:
p1 = Point(1, 2)
p2 = Point(4, 6)
p1.show()         
p2.show()
print(p1.dist(p2)) 
p1.move(3, 3)
p1.show()        
