 # Reverse a Number: Accept a number and print its reverse using a while loop.
def reverse_number(num):
 
    rev = ""
    while num != 0:
        digit = num % 10
        rev = rev + digit   
        num //= 10
    return num   
if __name__ == "__main__":
    num = int(input("Enter num : "))    #123
    res = reverse_number(num)
    print(res)

 
