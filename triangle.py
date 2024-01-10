class Triangle:
        def __init__(self, side1, side2, side3):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        def perimeter(self):
            total = self.side1 + self.side2 + self.side3
            return total
        def area(self):
            s = self.perimeter() / 2
            area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
            return area
triangle_example = Triangle(3, 4, 5)
print("Perimeter:", triangle_example.perimeter())
print("Area:", triangle_example.area())