# Grade Description: Write a program that accepts a grade (A, B, C, D, F) and prints its description (e.g., A = Excellent, B = Good, etc.) using a switch case.
def grade_description(grade):
    switch = {
        'A': "Excellent",
        'B': "Good",
        'C': "Average",
        'D': "Poor",  
        'F': "Fail"
    }
    if grade in switch:
        return switch.get(grade, "Not a valid grade") 
    else: 
        return "Invalid Grade"
if __name__ == "__main__":
    ngrade = input("Enter grade: ")
    rs = grade_description(ngrade)
    print(rs)
    
