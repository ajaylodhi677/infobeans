'''
Assignment 4: Rectangle Calculator
 A civil engineer wants to calculate the area and perimeter of a rectangular plot.
Create a class Rectangle with the following attributes:

Length

Breadth

Create the following methods:
calculate_area() – Calculate the area.
calculate_perimeter() – Calculate the perimeter.
display_result() – Display length, breadth, area, and perimeter.

Formulas:
Area = Length × Breadth
Perimeter = 2 × (Length + Breadth)

Sample data:
Length: 15
Breadth: 8
'''

class Rectangle:
    def __init__(self):
        self.l = int(input("Enter the length OF Rectangle: "))
        self.b = int(input("Enter the Breadth OF Rectangle: "))

    def calculate_area(self):
        self.area = self.l * self.b

    def calculate_perimeter(self):
        self.parimeter = 2*(self.l + self.b)

    def display_result(self):
        print("Length:",self.l)
        print("Breadth:",self.b)
        print("Area Of rectangle:",self.area)
        print("Parimeter Of rectangle:",self.parimeter)

rec1 = Rectangle()
rec1.calculate_area()
rec1.calculate_perimeter()
rec1.display_result()