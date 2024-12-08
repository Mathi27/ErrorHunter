def conversion_menu():
    while True:
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Decimal to Binary, Octal, Hexadecimal")
        print("4. Kilometers to Miles and Vice Versa")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32  
            print(f"Temperature in Fahrenheit: {fahrenheit}")

        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9  
            print(f"Temperature in Celsius: {celsius}")

        elif choice == 3:
            decimal = int(input("Enter a decimal number: "))
            print(f"Binary: {bin(decimal)[2:]}, Octal: {oct(decimal)[2:]}, Hexadecimal: {hex(decimal)[2:]}")  # Formatting the output without prefixes

        elif choice == 4:
            sub_choice = int(input("Enter 1 for Kilometers to Miles, or 2 for Miles to Kilometers: "))
            if sub_choice == 1:
                km = float(input("Enter distance in kilometers: "))
                miles = km / 1.60934  
                print(f"Distance in Miles: {miles}")
            elif sub_choice == 2:
                miles = float(input("Enter distance in miles: "))
                km = miles * 1.60934  
                print(f"Distance in Kilometers: {km}")
            else:
                print("Invalid option for conversion between kilometers and miles.")

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid Choice")


conversion_menu()
