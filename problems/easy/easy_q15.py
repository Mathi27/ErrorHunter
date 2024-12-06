# Grade Description: Write a program that accepts a grade (A, B, C, D, F) and prints its description (e.g., A = Excellent, B = Good, etc.) using a switch case.
def grade_description(grade):
    switch = {
        'A': "Good",
        'B': "Average",
        'C': "Poor",
        'D': "Excellent",  
        'F': "Fail"
    }
    return switch.get(grade, "Not a valid grade") 
if __name__ == "__main__":
    rs = grade_description('C')
    print(rs)
    
