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
    return switch.get(day,"invalid")
if __name__ == "__main__":
    
    xcd = day_of_week(int((input("Enter day:"))))
    print(xcd)
 
    
day_of_week(xcd)