# Factorial of a Number: Write a program to calculate the factorial of a given number using a while loop.
n= int(input("Enter the Number :"))
fact=1
i=1
if n < 0:
    print("Factorial number caanot be negative!")
else:
        while i<=n:
              fact*=i
              i+=1 
        print(f"Factorial of {n} is {fact}")
