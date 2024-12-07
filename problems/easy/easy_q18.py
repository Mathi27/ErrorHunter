# Print Last Character of String
def last_char_of_string(s):
    return s[-1]  # Bug: Fetches second-to-last character instead of last
if __name__ == "__main__":
 # Handle the input  by Yourself
 string = input("Enter a string: ")
 print(last_char_of_string(string))