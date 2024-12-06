# Grade Description: Write a program that accepts a grade (A, B, C, D, F) and prints its description (e.g., A = Excellent, B = Good, etc.) using a switch case.
def grade_description(grade='Z'): #Base/Default Case declaration
    #The grade (key) and their corresonding values are assigned properly
    switch = {
        'A': "Excellent",
        'B': "Good",
        'C': "Average",
        'D': "Poor",  
        'F': "Fail"
    }
    return switch.get(grade, "Not a valid grade") 
if __name__ == "__main__":
    #Input obtained and the function call is assigned to a var 'rs'and the result is printed
    grade = input("Enter your Grade: ")
    rs = grade_description(grade) 
    print(rs)
    
# By: Deepak K M, 24UCS121, CSE_A