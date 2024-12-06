# Check Palindrome Number: Use a do-while loop to determine if a given number is a palindrome
def is_palindrome(num):
    original = num
    reverse = 0
    do:
        reverse = reverse * 10 + num % 10
        num //= 10
    while num != 0 
    return reverse == original
if __name__ == "__main__":
    nums = int(input("Enter the Number: "))
    res = is_palindrome(nums)
    # print(res)
    
    
