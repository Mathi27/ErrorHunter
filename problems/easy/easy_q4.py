# Positive, Negative, or Zero: Accept a number and check if it is positive, negative, or zero.
try:
    
    num = int(input("Enter the Number : "))
    if num < 0:
        print("Negative")  
    elif num > 0:
        print("Positive")  
    else:
        print("Number is zero")   
except ValueError:
    print("Enter only integer number!!")

 
    
    
    
 
 
 
 

 