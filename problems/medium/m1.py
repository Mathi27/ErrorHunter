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
 
 
    a=int(input("Enter first numbers: "))
    b=int(input("Enter second numbers: "))

 
    if choice == 2:
        print("Subtraction:", a - b)   
    elif choice == 1:
        print("Addition:", a + b)   
 
    if choice == 1:
 
        print(f"Addition of {a} and {b} : {a + b}")   
 
        print("Addition:", a + b)   
    elif choice == 2:
        print("Subtration:", a - b)   
    elif choice == 3:
        print("Multiplication:", a * b)   
    elif choice == 4:
        print("Division:", a / b)   
    elif choice == 5:
        print("Modulo:", a // b)   
    else:
        print("Invalid option")

math_operations_menu()
 

    if choice == 2:
        print("Subtraction:", a - b)   
    elif choice == 1:
        print("Addition:", a + b)   
 
    elif choice == 4:
        print("Division:", a / b)   
    elif choice == 3:
        print("Multiplication:", a * b)   
 
    if choice == 1:
        print(f"Subtraction of {a} and {b}:{a - b}")   
 
    elif choice == 2:
        print(f"Subtraction of {a} and {b} : {a - b}")   
    elif choice == 3:
        print(f"Division of {a} and {b} : {a / b}")   
    elif choice == 4:
 
        print(f"Multiplication of {a} and {b} : {a * b}")   
    elif choice == 5:
        print(f"Modulus of {a} and {b} : {a % b}")   
 
        print(f"Multiplication of {a} and {b}:{a * b}")   
     elif choice == 5:
        print(f"Modulus of {a} and {b}:{a // b}")   
     elif choice == 6:
        print(f"{a} to the power of {b} : {a**b}")
    else:
        print("Invalid option")
 

math_operations_menu()
 
math_operations_menu()
 
        print("Invalid option!!!")
print("-------------Mathematical operation menu---------------")
 
print("1. Subtract")
print("2. Add")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponential")
=======
 
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
 
print("6. Exponential")

# Get user's choice for operation
try:
    choice = int(input("Enter your choice: "))
    math_operations_menu(choice)
except ValueError:
    print("Invalid choice! Please enter a number between 1 and 6.")

print("-------------------------------------------------------")
 
print("6. Expontential")
 
choice = int(input("Enter your choice: "))
math_operations_menu(choice)
print("-------------------------------------------------------")
 
 
 
 
