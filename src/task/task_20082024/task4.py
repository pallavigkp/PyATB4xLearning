import math

# Area of the circle
# formula pi*r2

radius = float(input("Enter the radius of the circle\n"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius,2)
print(f"Area of the circle is--->\n, {area:.2f}")
