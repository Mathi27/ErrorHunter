'''Write a program to check if a number is an Armstrong number (e.g., 153  = 1^3 + 5^3 + 3^3 ) .'''
def count_digits(n):
    i = 0
    while n > 0:  
        n //= 10  
        i += 1    
    return i

def calculate_sum(n):
    original = n  
    i = count_digits(n)
    s = 0
    while n > 0:
        digit = n % 10  
        s += pow(digit, i)  
        n //= 10  
    return s


number = int(input("Enter a number: "))
print("Sum of digits raised to the power of count:", calculate_sum(number))
