# Print Last Character of String
def last_char_of_string(s):
    return s[-1]  # Bug: Fetches second-to-last character instead of last
if __name__ == "__main__":
 # Handle the input  by Yourself
 a_string = input("Enter a string: ")
 result = last_char_of_string(a_string)
 print(f"The last character of the string '{a_string}' is '{result}'.")