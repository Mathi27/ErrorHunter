# Factorial of a Number: Write a program to calculate the factorial of a given number using a while loop.
def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n += 1   
    return result

if __name__ == "__main__":
    num = int(input("Enter the Number :"))
    factorial(num*7)
    print(num)
factorial(num)
    
