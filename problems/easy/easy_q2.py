# Find the Largest Number: Accept two numbers and print the larger one.
def largest_of_two(a, b):
    if a > b:
        return a   #LogicError: return b -> return a
    else:
        return b    #LogicError: return a -> return b
if __name__ == "__main__":
    num1 = int(input("Enter the First Number :"))
    num2 = int(input("Enter the Second Number :"))
    res = largest_of_two(num1,num2) #SyntaxError: Assignment num1,num1 -> num1,num2
    print(f"The Largest Number among {num1} and {num2} is ",res) #Context of the result added

# By: Deepak K M, 24UCS121, CSE_A