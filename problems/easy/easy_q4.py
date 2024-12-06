# Positive, Negative, or Zero: Accept a number and check if it is positive, negative, or zero.
def check_number(num):
    if num < 0: #LogicError: lesser_than -> greater_than
        print("Negative")
        exit()
    elif num > 0: ##LogicError: greater_than -> lesser_than
        print("Positive") 
        exit()
    else:
        print("Number is Zero i.e. Neither Positive nor Negative")
        exit()   
        
if __name__ == "__main__":
    num = int(input("Enter the Number : ")) #LogicError/SyntaxError: Datatype Correction
    res = check_number(num)
    print(res)
    
#the exit() is added because the function returns a None value by adding exit() this could be resolved
    
# By: Deepak K M, 24UCS121, CSE_A