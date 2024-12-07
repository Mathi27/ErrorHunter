# Check Palindrome Number: Use a do-while loop to determine if a given number is a palindrome
def is_palindrome(num):
    temp = num
    reverse = 0
    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp //= 10
    if num == reverse:
        return "Palindrome"
    else:
        return  "Not a Palindrome"
        #return reverse == original
if __name__ == "__main__":
    nums = int(input("Enter the Number: "))
    res = is_palindrome(nums)
    print(res)
    
    
