# Grading System: Write a program that takes a student’s marks as input and prints the grade (A, B, C, or F) based on given thresholds.

def grade_system(marks):
    if marks >= 90:
        return "A"  
    elif marks >= 80 and marks<=90:
        return "B"   
    elif marks >= 7 and marks<=80:
        return "C"   
    else:
        return "F"  
    
if __name__ == "__main__":
      num = int(input("Enter the Mark : "))
      res = grade_system(num)
      print(res)

grade_system(num)
      
