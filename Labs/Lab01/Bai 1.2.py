class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def perimeter(self):
        return (self.height + self.width)*2
    def area(self):
        return self.height * self.width

class circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return self.radius * 2 * 3.1415926535
    def area(self):
        return self.radius ** 2 * 3.1415926535

print("shape (rectangle/circle)")
shape = input()
if shape == "rectangle":
    height = float(input("height: "))
    width = float(input("width: "))

    Rec = Rectangle(height,width)
    print("Perimeter: \t",Rec.perimeter())
    print("Area: \t\t", Rec.area())
elif shape == "circle":
    radius = float(input("radius: "))
    cir = circle(radius)
    print("Perimeter: \t",cir.perimeter())
    print("Area: \t\t", cir.area())
else:
    print("INVALID!")