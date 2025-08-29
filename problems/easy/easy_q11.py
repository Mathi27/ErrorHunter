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
    return switch.get(day, "Invalid day number")

if __name__ == "__main__":
    try:
        day = int(input("Enter a number from 1 to 7: "))
        result = day_of_week(day)
        print("Day is:", result)
    except ValueError:
        print("Please enter a valid integer.")
