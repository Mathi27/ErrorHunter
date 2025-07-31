def grade_system(marks):
    if marks >= 90:
        return "A"  
    elif marks >= 80:
        return "B"   
    elif marks >= 70:
        return "C"   
    else:
        return "F"  

if __name__ == "__main__":
    num = int(input("Enter the Mark: "))
    res = grade_system(num)
    print("Grade:", res)

 