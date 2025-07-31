# Check Even or Odd: Write a program to check if a given number is even or odd.
try:

   num = int (input ("Enter a number:"))
    
   if num % 2 != 0:
      print("num is Odd")
   else:
      print("num is Even")
except ValueError:
   print("Enter only integer!!")



 


 