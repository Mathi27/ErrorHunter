# Check Palindrome Number: Use a do-while loop to determine if a given number is a palindrome
def is_palindrome(num):
    original = num
    reverse = ''
    while num != 0 :
        reverse += str(num % 10)
        num //= 10 
    if original==int(reverse):
        return "It is a Palindrome"
    else:
        return "It is not a Palindrome"
if __name__ == "__main__":
    nums = int(input("Enter the Number: "))
    res = is_palindrome(nums)
    print(res)
    
    
