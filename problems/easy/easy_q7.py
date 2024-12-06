# Sum of Digits: Write a program to calculate the sum of digits of a number using a while loop.
def sum_of_digits(num):
    total = 0
    num = tuple(num)# while num > 0:
    for i in num:#    total += num % 10
        total += int(i)#   num = num + 10
    return total  #return total

if __name__ == "__main__":
    num = int(input("Enter the Number : "))
    res = sum_of_digits(num)
    print(res)

# By: Deepak K M, 24UCS121, CSE_A