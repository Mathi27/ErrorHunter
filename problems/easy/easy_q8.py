 # Reverse a Number: Accept a number and print its reverse using a while loop.
try:
    num = int(input("Enter num : "))
    rev = 0
    while num != 0:
       digit = num % 10
       rev = rev*10 + digit   
       num //= 10
    print("The Reversed number is:", rev)
except ValueError:
    print("Enter only integer number!!")
 
 
 
  