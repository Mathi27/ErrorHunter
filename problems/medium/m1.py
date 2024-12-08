choice=int(input("Enter no. of choice:"))
def math_operations_menu(choice):
    a, b = map(int,input("Enter two numbers(separated by commas): ").split(sep=",")) 
    if choice == 1:
        print(a + b)   
    elif choice == 2:
         print(a - b)   
    elif choice == 3:
        print(a * b)   
    elif choice == 4:
         print(a / b)   
    elif choice == 5:
        print(a % b)   
    elif choice == 6:
       print(a ** b)   

    if choice == 1:
        print(f"Addition of {a} and {b}:{a + b}")      
    elif choice == 2:
       print(f"Subtraction of {a} and {b}:{a - b}")
    elif choice == 3:
        print(f"Division of {a} and {b}:{a / b}")   
    elif choice == 4:
        print(f"Multiplication of {a} and {b}:{a * b}")   
    elif choice == 4:
        print(f"Division of {a} and {b}:{a / b}")
    elif choice == 5:
        print(f"Modulus of {a} and {b}:{a % b}")   
    elif choice == 6:
        print(f"{a} to the power of {b}:{a**b}")
    else:
        print("Invalid option")
math_operations_menu(choice)
print("-------------Mathematical operation menu---------------")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Expontential")


print("-------------------------------------------------------")
 