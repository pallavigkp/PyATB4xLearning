"""if we want to print odd number
we will use continue statement
it will print the previous statement
which is false"""

for number in range(0, 20, 1):
    if number % 2 == 00:
        continue
    else:
        print(number)
# variable |  condition     |  output
#   0   |number%2==0     | true---continue skip no output
#   1   |number%2==0     | false
#   2   |number%2==0     | true---continue skip no output
#   3   |number%2==0     | false
#   4   |number%2==0     | true---continue skip no output
#   5   |number%2==0     | false
#   6   |number%2==0     | true---continue skip no output
#   7   |number%2==0     | false
#   8   |number%2==0     | true---continue skip no output
