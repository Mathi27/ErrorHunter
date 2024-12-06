# Print Last Character of String
def last_char_of_string(s):
    return s[-2]  # Bug: Fetches second-to-last character instead of last
if __name__ == "__main__":
    s=input("Enter string : ")
    res=last_char_of_string(s)
    print(res)
    
last_char_of_string(s)