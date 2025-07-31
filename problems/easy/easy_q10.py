def pal(num):
    return num == num[::-1]

# Main program
number = input("Enter a number: ")

if pal(number):
    print("Palindrome")
else:
    print("Not a Palindrome")
