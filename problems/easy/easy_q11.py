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
    return switch[day]   
if __name__ == "__main__":
    day=int(input("Enter The Number:"))
    if str(day) in "1234567":
        xcd = day_of_week(day)
        print(xcd)
    else:
        print("Enter Valid Input")
    
