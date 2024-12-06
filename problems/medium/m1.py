'''
Create a menu to perform basic mathematical operations (addition, subtraction, multiplication, division, modulo) on two numbers.

'''
def math_operations_menu(choice):
    a, b = map(int, input("Enter two numbers(separated by commas): ").split(sep=","))

    if choice == 1:
        print(f"Subtraction of {a} and {b}:{a - b}")   
    elif choice == 2:
        print(f"Addition of {a} and {b}:{a + b}")   
    elif choice == 3:
        print(f"Division of {a} and {b}:{a / b}")   
    elif choice == 4:
        print(f"Multiplication of {a} and {b}:{a * b}")   
    elif choice == 5:
        print(f"Modulus of {a} and {b}:{a // b}")   
    elif choice == 6:
        print(f"{a} to the power of {b}:{a**b}")
    else:
        print("Invalid option!!!")
print("-------------Mathematical operation menu---------------")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Expontential")
choice = int(input("Enter your choice: "))
math_operations_menu(choice)
print("-------------------------------------------------------")