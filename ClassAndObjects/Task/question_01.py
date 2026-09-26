class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"Length: {self.length} | Width: {self.width}"

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"The length of rectangle is: {self.length}")
        print(f"The width of rectangle is: {self.width}")
        print(f"Perimeter of rectangle: {self.perimeter()}")
        print(f"Area of rectangle: {self.area()}")

rec1 = Rectangle(3, 5)
rec1.display()
