# write a program to calculate
# area of circle given by its radius using the formula
# area=pi*r2 (take pi as 3.14
# logic building formula
# step1 Figure out the inputs and outputs
# input--> r-->data type-->float or user will give
# pi-->3.14
# power-->pow or **-->any
# o/p-->float-area,print area
# step2
# rough logic=area=3.14*pow(r,2)
# step3-write the logic
import math

radius = float(input("Enter the radius of the circle\n"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius, 2)
# *---> means multiplication
# **---> means power
area2 = 3.14 * (radius ** 2)
print("area of the circle is-->", area)
print("area of the circle is -->{area:.2f")
print("Area2--->", area2)

# it can also be written in one line
print(3.141592653589793 * (float(input("enter the radius\n")) ** 2))
