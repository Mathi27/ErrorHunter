# Check Even or Odd: Write a program to check if a given number is even or odd.
 
try:
   num = int(input("Enter a number: "))
   if num % 2 != 0:
      print(f"{num} is Odd")
   else:
      print(f"{num} is Even")
except ValueError:
   print("Enter only INTEGER that is ONLY NUMBER")