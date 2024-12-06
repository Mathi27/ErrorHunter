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
    return switch.get(month,"No Such Month of the year Exists")   #The month +1 is changed to month thus it makes sure it only prints the respectve month insted of the next month
if __name__ == "__main__":
    chooseMonthNum = int(input("Enter the Month (eg. : 1 for January): ")) #DataType Changed to Int from Float
    result = month_name(chooseMonthNum)
    print(result)
# By: Deepak K M, 24UCS121, CSE_A