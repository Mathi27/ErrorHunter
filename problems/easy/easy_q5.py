# Grading System: Write a program that takes a student’s marks as input and prints the grade (A, B, C, or F) based on given thresholds.

def grade_system(marks):
    if marks >= 90 and marks < 101: #and marks < 101 -> thus ensures that user dosen't enters a improper value
        return "A"  #SyntaxError: "B" -> "A"
    elif marks >= 80:
        return "B"   #SyntaxError: "A" -> "B"
    elif marks >= 70:
        return "C"   #SyntaxError: "F" -> "C"
    else:
        return "F"  #SyntaxError: "C" -> "F"
    
if __name__ == "__main__":
      num = int(input("Enter the Mark : ")) #DataType Declaration -> int()
      res = grade_system(num)
      print(res)
      
# By: Deepak K M, 24UCS121, CSE_A