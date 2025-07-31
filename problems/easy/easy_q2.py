def largest_of_two(a, b):
    if a > b:
        return a
    else:
        return b

try:
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    result = largest_of_two(num1, num2)
    print(f"The largest number is: {result}")
except ValueError:
    print("ENTER ONLY INTEGER VALUES")
