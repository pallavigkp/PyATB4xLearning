#number formatting concept
"""suppose we have a number which has large infinite decimal value
 bur we want only first 4 value of after decimal
 then we will use following formatted concept"""
number=3.14159265359
formated_number=f"{number:.4f}"
#here .4 is place value of number after decimal which we want it can be anything.
print(formated_number)
#string formatting concept
"""suppose we want to write a table of 9 in table format 
9*1=9
we will format in below manners"""
table=9
print(f"{table}*1={table}")
print(f"{table}*2={table*2}")
print(f"{table}*3={table*3}")
print(f"{table}*4={table*4}")
print(f"{table}*5={table*5}")
print(f"{table}*6={table*6}")
print(f"{table}*7={table*7}")
print(f"{table}*8={table*8}")
print(f"{table}*9={table*9}")
print(f"{table}*10={table*10}")