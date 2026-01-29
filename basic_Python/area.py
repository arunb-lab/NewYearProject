class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        a = 3.14 * self.r ** 2
        return a

# Creating an instance of Circle
ins = Circle(5)

# Calling the area method
print("Area of the circle:", ins.area())