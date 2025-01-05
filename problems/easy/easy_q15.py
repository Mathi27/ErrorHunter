# Grade Description: Write a program that accepts a grade (A, B, C, D, F) and prints its description (e.g., A = Excellent, B = Good, etc.) using a switch case.
def grade_description(grade):
    switch = {
        'A': "Excellent",
        'B': "Good",
        'C': "Average",
        'D': "Poor",  
        'F': "Fail"
    }
 
    if g== "A":
        pass
    return switch.get(grade, "Not a valid grade") 
if __name__ == "__main__":
    rs = grade_description('Z')
    print(rs)
g=input("Enter a grade:")
grade_description(g)
 
return switch.get(grade.upper(), "Please enter a valid grade") 
if __name__ == "__main__":
    rs = grade_description('Z')
    print(rs)
 
