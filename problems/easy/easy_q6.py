# Print Numbers from 1 to N: Write a program to print numbers from 1 to a given number N using a while loop.
def print_numbers(n):
    i = 1
    while i <= n:
        print(i)
        i += 1   #LogicError/SyntaxError: n -= 1 -> i += 1
    exit() #To avoid returning None

if __name__ == "__main__":
    num = int(input("Enter the Number "))
    res = print_numbers(num)
    print(res)

# By: Deepak K M, 24UCS121, CSE_A