def grade_system(m):
    if m >= 90: return "A"
    elif m >= 80: return "B"
    elif m >= 70: return "C"
    else: return "F"
marks = int(input("Enter Marks: "))
print(grade_system(marks))
  

 