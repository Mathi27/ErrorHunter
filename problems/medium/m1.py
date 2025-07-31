 
'''
Create a menu to perform basic mathematical operations (addition, subtraction, multiplication, division, modulo) on two numbers.

'''
 
 
print("-------------Mathematical operation menu--------'1. Add' , '2. subtract' , '3. multiply' , '4.divide' , '5.modulus' , '6.expontential'")
choice = int(input("Enter your choice: "))
a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))

if choice == 1:
        add = a+b
        print("Addition:", add)
elif choice == 2:
        sub = a-b
        print("Subtraction:", sub)    
elif choice == 3:
        mul = a*b
        print("Multiplication:", mul)
elif choice == 4:
        if b!=0:
            div = a/b
            print("Division:", div)
        elif b==0:
            print("zero error")
        else:
            print("invalid")   
elif choice == 5:
        mod = a%b
        print("Modulo:", mod)
elif choice == 6:
        expo=a**b
        print("Expontential:", expo)  
else:
        print("Invalid option")




 
 