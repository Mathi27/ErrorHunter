# Sum of Digits: Write a program to calculate the sum of digits of a number using a while loop.
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10  
    return total

if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    res=sum_of_digits(num)
    print(res)
