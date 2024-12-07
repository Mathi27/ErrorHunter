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
 
    a, b = map(int, input("Enter two numbers(separated by commas): ").split(sep=","))

 
    a=int(input("Enter a num1:"))
    b=int(input("Enter a num2:"))
 

 
    if choice == 1:
        print("Addition:", a + b) 
    elif choice == 2:
        print("Subtraction:", a - b)   
    elif choice == 3:
        print("Multiplication:", a * b)
    elif choice == 4:
        print("Division:", a / b)   
    elif choice == 5:
        print("Modulo:", a // b)   
    else:
        print("Invalid option")
 
math_operations_menu()
  
 
