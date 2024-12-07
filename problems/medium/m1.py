'''
Create a menu to perform basic mathematical operations (addition, subtraction, multiplication, division, modulo) on two numbers.

'''
def math_operations_menu(choice):
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
  