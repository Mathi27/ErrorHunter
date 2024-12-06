# Month Name: Write a program that takes a number (1-12) and prints the corresponding month name using a switch case.
def month_name(month):
    switch = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switch[month + 1]   
if __name__ == "__main__":
    chooseMonthNum = int(input("Enter the Month: "))
    result = month_name(chooseMonthNum)
    print(result)