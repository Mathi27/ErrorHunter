def check_even_or_odd():
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")
    except ValueError:
        print("Invalid input! Please enter a valid integer number.")

# Run the function
check_even_or_odd()

 
 