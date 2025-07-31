 
'''
Create a menu to perform basic mathematical operations (addition, subtraction, multiplication, division, modulo) on two numbers.

'''
 
 
def math_operations_menu(a,b,operator):
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
 
 
    choice = int(input("Enter your choice: "))
 

    a, b = map(int, input("Enter two numbers: ").split(sep=","))

 
    if choice == 1:
        print("Addition:", a + b)   
    elif choice == 2:
        print("Subtraction:", a - b)   
 
 
 
 
    a=int(input("enter a number1:"))
    b=int(input("enter a number2:"))
 
 
    if choice == 2:
        print("Subtraction:", a - b)   
    elif choice == 1:
        print("Addition:", a + b)   
    elif choice == 4:
 
        print("Division:", a / b)   
 
        print("Division:", a / b)   
 
        if b==0:
            print("zero error")
        else:
            print("Division:", a / b)   
 
 
 
    elif choice == 3:
        print("Multiplication:", a * b)   
    elif choice == 4:
        print("Divide:", a / b)   
    elif choice == 5:
 
        print(f"Modulus of {a} and {b}:{a // b}")   
    elif choice == 6:
        print(f"{a} to the power of {b}:{a**b}")
    else:
        print("Invalid option!!!")
print("-------------Mathematical operation menu--------------------")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Expontential")