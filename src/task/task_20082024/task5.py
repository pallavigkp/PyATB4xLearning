"""create a program and takes two numbers as input and print whether
 the first number is grater than ,less than or equal to the 2nd number"""
num1=int(input("Enter your number 1\n"))
num2=int(input("Enter your number 2\n"))
if num1>num2:
    print("Number 1 is greater than number 2")
elif num1<num2:
    print("Number 1 is less than number 2")
else:
    print("Number 1 is equal to the number 2")