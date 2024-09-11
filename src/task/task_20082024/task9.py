"""write a triangle that classifies triangle based on their side
take 3 input from the user
determine if the triangle is
equilateral(all sides are equal)
isosceles(two sides are equal)
 scalene(none are equal)"""
# use if else statement
side1 = int(input("Enter the ab side of the triangle\n"))
side2 = int(input("Enter the bc side of the triangle\n"))
side3 = int(input("Enter the ca side of the triangle\n"))
if side1 == side2 == side3:
    print("This is a Equilateral triangle because its all sides are equal\n")
elif side1 == side2 or side2==side3 or side3== side1:
        print("This is a Isosceles triangle because two  sides are equal\n")
else:
    print("This is scalene triangle because its  all sides are different\n")
