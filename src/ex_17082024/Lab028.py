#escape sequence
print("hello world") #print as it is
print("hello\nworld")#\n --->new line
print("hello\tworld") #\t ---> tab
print("hello\bworld")#\b --->back space
"""use of r-raw concept 
whenever we are using file path
we use r-concept
it will prevent the conversion of escape sequence
"""
#Use in automation,API and web automation
#suppose we are storing a directory file
#dir='C:\Pramod\n.txt' also not in "c:\pramod\n.txt"
#print(dir) #it will give error
"""so we have to use r concept"""
dir=r"c:\pramod\n.txt"
dir2=r'c:\pramod\n.txt' #concept also works with ''single qoute
print(dir)
print(dir2)

#in python we can use single or double qoute
#suppose
#name='Prince'singh'----> it will give error
name='saroj\'singh'
print(name) #if we want to print single qoute we have to pre slash
#without any interruption we can use double qoute string
name1="saroj'singh"

print(name1)
