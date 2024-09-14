"""write a program to ask the user which browser he want to run automation"""
browser_name=input("Enter the  name of browser\n ")
#if we want to avoid case sensitivity of the program or statement
#we will use below statemnt
#variable_name=variable_name.lower()
browser_name=browser_name.lower()
match browser_name:
    case"firefox":
        #HERE we can use if else statement for specific case only
        if browser_name=="firefox":
            print("hello world")
        print("execute the firefox code")
    case"chrome":
        print("execute the chrome code")
    case"edge":
        print("execute the edge code")
    case"safari":
        print("execute the safari code")
    case _:
        print("no browser found ")
