year = int(input("Enter Year:"))
if((year % 4 == 0 and year % 100 !=0) or (year % 400 ==0)):
         print("Given year is a leaf year")
else:
         print('Given year is not a leaf year')
2004
