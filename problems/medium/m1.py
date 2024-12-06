'''
Create a menu to perform basic mathematical operations (addition, subtraction, multiplication, division, modulo) on two numbers.

'''
def math_operations_menu(a,b):
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Subtraction:", a - b)   
    elif choice == 2:
        print("Addition:", a + b)   
    elif choice == 3:
        print("Division:", a / b)   
    elif choice == 4:
        print("Multiplication:", a * b)   
    elif choice == 5:
        print("Modulo:", a % b)   
    else:
        print("Invalid option")
a=int(input("enter the number 1 :"))
b=int(input("enter the number 2 :"))
math_operations_menu(a,b)
