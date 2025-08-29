def month_name(month):
    months = {
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

    return months.get(month, "Invalid month number")

if __name__ == "__main__":
    try:
        chooseMonthNum = int(input("Enter the Month from 1 to 12: "))
        print("Month is:", month_name(chooseMonthNum))
    except ValueError:
        print("Invalid input. Please enter a number.")
 
 