def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

if __name__ == "__main__":
    try:
        num = int(input("Enter the year: "))
        is_leap_year(num)
    except ValueError:
        print("Please enter a valid integer year.")
