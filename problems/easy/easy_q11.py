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
    return switch.get(day,"No Such Day of The Week Exists")   #Default case declaration and corrected to the proper syntax
if __name__ == "__main__":
    day = int(input("Enter the Day of the week (eg. : 1 for Monday): ")) #Input and its description
    xcd = day_of_week(day)
    print(xcd)
    
    
# By: Deepak K M, 24UCS121, CSE_A