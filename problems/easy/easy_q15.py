 
def grade_description(grade):
    switch = {
        'A': "Excellent",
        'B': "Good",
        'C': "Average",
        'D': "Poor",
        'F': "Fail"
    }
    return switch.get(grade, "Not a valid grade")

if __name__ == "__main__":
    grade_input = input("Enter a grade (A, B, C, D, F) in capital letters: ").upper()
    result = grade_description(grade_input)
    print(result)

  