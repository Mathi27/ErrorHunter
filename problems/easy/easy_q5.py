try:

    marks = int(input("Enter the Mark : "))
    if marks >= 90:
        print("GRADE 'A'")  
    elif marks >= 80:
        print("GRADE 'B'")   
    elif marks >= 70:
        print("GRADE 'C'")   
    else:
        print("GRADE 'F'")  
except ValueError:
    print("Enter only integer number!!")
    

 