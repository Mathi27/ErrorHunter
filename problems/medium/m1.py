'''
Create a menu to perform basic mathematical operations (addition, subtraction, multiplication, division, modulo) on two numbers.

'''
def math_operations_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            a = int(input("Enter number 1:"))
            b = int(input("Enter number 2:"))
            break
        except:
            print("Enter a number!")

    while True:
        if choice == 1:
            print("Addition:", a + b)
            break 
        elif choice == 2:
            print("Subtraction:", a - b)
            break     
        elif choice == 3:
            print("Multiplication:", a * b)
            break
        elif choice == 4:
            print("Division:", a / b)
            break     
        elif choice == 5:
            print("Modulo:", a % b)
            break   
        else:
            print("Invalid option")
math_operations_menu()