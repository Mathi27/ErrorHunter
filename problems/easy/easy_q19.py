"""
A magic number is a number which satisfy the below condition:
1.The number must be an Armstrong Number
2.It must a palindrome Number 

and the number lies between 100 and 999
"""
print("Magic numbers from 100 to 999 are:")

for number in range(100, 999): 
    a = number / 100            
    b = (number % 100) / 10    
    c = number % 10

    total = a*a*a + b*b*b + c*c*c  

    if total =number:  
    if str(number) = str(number)[::-1]:  
            print(number)
