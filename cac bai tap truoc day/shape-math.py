# tính chu vi và diện tích hình tam giác
import math
print("This is a program to calculate the perimeter and area of a triangle")
a = int(input("First side: "))
b = int(input("Second side: "))
c = int(input("Third side: "))
print("Perimeter of the triangle =", a+b+c)
s = (a+b+c)/2
area = round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)
print("Area of the triangle =", area)
print()

# tính tuổi
from datetime import date
year = int(input("Please input your birth year: "))
current_year = date.today().year
print("Your age is:",current_year - year)
print()

# tính diện tích hình tròn
import math
r = int(input("Input the radius: "))
c_area = math.pi * pow(r,2)
print(round(c_area,2))
print()