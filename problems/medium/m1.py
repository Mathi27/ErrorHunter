def math_operations_menu(choice):
    try:
        a, b = map(int, input("Enter two numbers (separated by a comma): ").split(sep=","))
        
        # Perform the operation based on user's choice
        if choice == 1:
            print(f"Addition of {a} and {b}: {a + b}")   
        elif choice == 2:
            print(f"Subtraction of {a} and {b}: {a - b}")   
        elif choice == 3:
            print(f"Multiplication of {a} and {b}: {a * b}")   
        elif choice == 4:
            if b == 0:
                print("Error! Division by zero is not allowed.")
            else:
                print(f"Division of {a} and {b}: {a / b}")   
        elif choice == 5:
            if b == 0:
                print("Error! Modulo by zero is not allowed.")
            else:
                print(f"Modulus of {a} and {b}: {a % b}")   
        elif choice == 6:
            print(f"{a} to the power of {b}: {a ** b}")
        else:
            print("Invalid option!!!")
    except ValueError:
        print("Invalid input! Please enter two valid numbers separated by a comma.")

 
# Menu for mathematical operations
print("-------------Mathematical Operation Menu---------------")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponential")

try:
    choice = int(input("Enter your choice: "))
    math_operations_menu(choice)
except ValueError:
    print("Invalid choice! Please enter a number between 1 and 6.")



 

    
