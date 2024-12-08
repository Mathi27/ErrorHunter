# Factorial of a Number: Write a program to calculate the factorial of a given number using a while loop.
def factorial(num):
    result = 1
    for n in range(1,num+1):
        result=result * n
        n += 1
      
    return result

if __name__ == "__main__":
    num = int(input("Enter the Number :"))
    res = factorial(num)
    print(f"Factotial of {num} ",res)
    
