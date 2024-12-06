 # Reverse a Number: Accept a number and print its reverse using a while loop.
def reverse_number(num):
 
    rev = ""
    while num != 0:
        digit = num % 10    #digit = 123%10 = 3  12%10
        rev = rev + str(digit)   #rev = 3
        num //= 10      # num//= 10 = 12
    return rev   
 
    rev = ''
    while num != 0:
        digit = num % 10
 
        rev = rev*10+ digit   
        num //= 10
    return rev 
 
        rev = rev + str(digit)   
        num //= 10
    return int(rev)   
 
 
if __name__ == "__main__":
    num = int(input("Enter num : "))    #123
    res = reverse_number(num)
    print(res)

 
