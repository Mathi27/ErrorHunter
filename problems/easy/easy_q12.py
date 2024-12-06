# Calculator: Accept two numbers and an operator (+, -, *, /) and perform the Calculation.
def calculator(a, b, operator):
    #the operation \s for proper operations requested by the user will be done. Via assigning proper operation to proper operators
    switch = {
        '+': a + b,   
        '-': a - b,  
        '*': a * b,   
        '/': a / b    
    }
    return switch.get(operator, "Invalid Operator")

if __name__ == "__main__":
    n1 = int(input("Enter the Number 1 :"))
    n2 = int(input("Enter the Number 2 :"))
    opr  = input("Enter the Operator :")
    result = calculator(n1,n2,opr) #the order of assinment is corrected
    print(result)
    
# By: Deepak K M, 24UCS121, CSE_A