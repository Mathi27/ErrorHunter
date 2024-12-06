# Factorial of a Number: Write a program to calculate the factorial of a given number using a while loop.
def factorial(n):
    if n == 1 or n == 0:
       return 1
    elif n < 1:
       print("Factorial is not defied for negative Numbers")
    else:
      return n * factorial(n-1)

if __name__ == "__main__":
    num = int(input("Enter the Number :"))
    print("The Factorail of the number is:",factorial(num))
    
# By: Deepak K M, 24UCS121, CSE_A