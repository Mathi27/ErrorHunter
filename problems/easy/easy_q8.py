 # Reverse a Number: Accept a number and print its reverse using a while loop.
def reverse_number(num):
    #accepts the input and returns its revere value if the input is a integer else it prints the error essage about the ValueError
    return num[::-1] if num.isnumeric() else ValueError
if __name__ == "__main__":
    #input DataType is modified for functionality
    num = input("Enter num : ")
    res = reverse_number(num)
    print(res)

 
# By: Deepak K M, 24UCS121, CSE_A