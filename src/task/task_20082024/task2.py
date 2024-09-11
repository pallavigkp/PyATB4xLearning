"""what does ** do in python"""
#arithmatic operator
#it gives power to the base
#2 to the power 4--->2*2*2*2----result----> 16
"""you can use ** with both integers and float
if the exponent is negative,
the result is the reciprocal of the base raised to the positive exponent.
eg---> 2**-3 is equal to 1/(2**3) which is 0.125
"""
#write a program to calculate area of square
side=int(input("Enter the length\n"))
area=side**2
print("The area of the square is",area)
side2=int(input("Enter the length\n"))
volume=side2**3
print("The volume of the cube is",volume)