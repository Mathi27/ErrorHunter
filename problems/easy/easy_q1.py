# Check Even or Odd: Write a program to check if a given number is even or odd.
num = int (input ("Enter a number:"))
try:
    
   if num % 2 != 0:
      print("num is Odd")
   else:
      print("num is Even")
except ValueError:
      print("Enter only integer number")

 


 