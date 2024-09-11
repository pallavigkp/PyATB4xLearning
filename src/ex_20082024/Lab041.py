"""write a program to calculate and display the letter grade for given numerical value"""
# A,B,C,D,(F
# A:90-100
# B:80-89
# C:70-79
# D:60-69
# F:0-59

"""LOGIC BUILDING"""
# USER INPUT--> score or marks
# output-->string-->A,B,C
score = int(input("Enter your score\n"))
Grade = "F"
if score >= 90 and score <= 100:
    grade = "A"
    print("your grade is-->", grade)
elif score >= 80 and score <= 89:
    grade = "B"
    print("your grade is-->", grade)
elif score >= 70 and score <= 79:
    grade = "C"
    print("your grade is-->", grade)
elif score >= 60 and score <= 69:
    grade = "D"
    print("your grade is-->", grade)
else:
    grade = "F"
    print("you are fail,Your grade is-->", grade)
