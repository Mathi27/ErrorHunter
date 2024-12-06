'''
Create a menu to perform basic mathematical operations (addition, subtraction, multiplication, division, modulo) on two numbers.

'''
def math_operations_menu(choice):
    a, b = map(int, input("Enter two numbers: ").split(sep=","))

    if choice == 1:
        print("Subtraction:", a - b)   
    elif choice == 2:
        print("Addition:", a + b)   
    elif choice == 3:
        print("Multiplication:", a * b)   
    elif choice == 4:
        print("Division:", a / b)   
    elif choice == 5:
        print("Modulo:", a % b)   
    else:
        print("Invalid option")

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulo")
choice = int(input("Enter your choice: "))
math_operations_menu(choice)
