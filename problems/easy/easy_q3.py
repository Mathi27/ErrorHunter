# Leap Year or Not: Write a program to determine whether a given year is a leap year.
try:
    year = int(input("Enter the number :"))
    if year % 4 == 0:
        print("leap year")
    else:
        print("not a leap year")

except ValueError:
    print("Enter only integer number!!")
