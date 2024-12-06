# Check Even or Odd: Write a program to check if a given number is even or odd.

num = int(input("Enter a number: "))
if (num % 2) != 0: #LogicError: / -> %
   print(f"{num} is Odd".format(num)) #TypeError: format string syntax
else:
   print(f"{num} is Even".format(num)) #TypeError: format string syntax

# By: Deepak K M, 24UCS121, CSE_A