#syntax
#if condition1:
#print("do1")
#elif condition2:
#print("do2")
#elif condition3:
#print("do3")
#else:
#print("do4")
num1=int(input("Enter your num1\n"))
num2=int(input("Enter your num2\n"))
num3=int(input("Enter your num3\n"))
num4=int(input("Enter your num4\n"))

if num1>num2 and num1>num3:
    print(f"Number 1 is maximum {num1}\n")
elif num2>num1 and num2>num3:
    print(f"Number 2 is maximum{num2}\n")
elif num3>num1 and num3>num2:
    print(f"Number 3 is maximum{num3}\n")
else:
    print("Number 4 is maximum in all")

result=max(num1,num2,num3,num4)
print(result)



