"""ask user what is the type"""
user_type = input("Enter the user type,admin,manager,guest\n")
match user_type:
    case "admin" | "manager":
        print("hello sir")
    case "guest":
        print("hello guest")
    case _:
        print("hello who is there!")
