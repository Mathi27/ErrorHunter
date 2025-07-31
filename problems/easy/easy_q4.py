try:
    num = int(input("Enter the Number: "))
    if num < 0:
        print("Negative")
    elif num > 0:
        print("Positive")
    else:
        print("Zero")
except ValueError:
    print("Please enter a valid integer.")
-4
