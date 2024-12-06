# Leap Year or Not: Write a program to determine whether a given year is a leap year.
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:   
        return "Leap Year"   
    return "Not a Leap Year"
if __name__ == "__main__":
    
    num = int(input("Enter the number :"))
    res = is_leap_year(num)
    print(res)