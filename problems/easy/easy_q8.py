 # Reverse a Number: Accept a number and print its reverse using a while loop.
def reverse_number(num):
    rev = " "
    while num != 0:
        digit = num % 10
        rev = rev + str(digit)   
        num //= 10
    return rev
if __name__ == "__main__":
    num = int(input("Enter num : "))
    res = reverse_number(num)
    print(res)
reverse_number(num)
 
