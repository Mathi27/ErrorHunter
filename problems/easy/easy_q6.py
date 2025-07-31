# Print Numbers from 1 to N using while loop

def print_numbers(num):
    i = 1
    while i <= num:
        print(i)
        i += 1

if __name__ == "__main__":
    num = int(input("Enter the Number: "))
    print_numbers(num)
