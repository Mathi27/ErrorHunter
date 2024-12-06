# Check Palindrome Number: Use a do-while loop to determine if a given number is a palindrome
def is_palindrome(num):
    #Logic modifed:
    #The input is accepted as a string and checked if it is numeric or not
    #if numeric then the palindrome check is done
    print(f"The no. {nums} is a Palindrome" if nums.isnumeric() and nums == nums[::-1] else f"The no. {nums} is not a Palindrome")
    exit()
if __name__ == "__main__":
    nums = input("Enter the Number: ")
    res = is_palindrome(nums)
    print(res)
    
    
# By: Deepak K M, 24UCS121, CSE_A