# Factorial of a Number using while loop

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    i = 1

    while i <= n:
        result *= i
        i += 1

    return result

if __name__ == "__main__":
    num = int(input("Enter the Number: "))
    print("Factorial:", factorial(num))
