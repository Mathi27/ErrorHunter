# Day of the Week: Write a program that takes a number (1-7) and prints the corresponding day of the week using a switch case.
def day_of_week(day):
    switch = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if 1 < day < 7:
        return switch[day]  
    else:
        return "Invalid Day"
if __name__ == "__main__":
    
    nday = int(input("Enter the day: "))
    xcd = day_of_week(nday)
    print(xcd)
    
    
