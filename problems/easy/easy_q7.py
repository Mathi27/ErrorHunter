# Sum of Digits: Write a program to calculate the sum of digits of a number using a while loop.
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num
        num += 1  
    print(total)

if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    sum_of_digits(num)
    
    
