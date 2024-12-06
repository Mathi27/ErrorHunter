# Leap Year or Not: Write a program to determine whether a given year is a leap year.
def is_leap_year(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:   #SyntaxError/LogicError: year % 100 != 0 or year % 400 == 0 -> year % 100 == 0 and year % 400 == 0
        return "Leap Year"   #SyntaxError: Not a Leap Year -> Leap Year
    return "Not a Leap Year" #SyntaxError: Leap Year -> Not a Leap Year 
if __name__ == "__main__":
    
    num = int(input("Enter the Year :")) #Added Context number -> Year
    res = is_leap_year(num)
    print(res)

# By: Deepak K M, 24UCS121, CSE_A