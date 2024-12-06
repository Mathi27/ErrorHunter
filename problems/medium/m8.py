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
 
            celsius = int(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32   
 
            print("Temperature in Fahrenheit:", fahrenheit)
        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9  
            print("Temperature in Celsius:", celsius)
        elif choice == 3:
            decimal = int(input("Enter a decimal number: "))
 
            print(f"Binary: {bin(decimal)[2:]}, Octal: {oct(decimal)[2:]}, Hexadecimal: {hex(decimal)[2:].upper()}")  # Correct formatting
 
            print(f"Binary: {bin(decimal)}, Octal: {oct(decimal)}, Hexadecimal: {hex(decimal)}")   
 
        elif choice == 4:
            km = float(input("Enter distance in kilometers: "))
            miles = km * 0.621371  
            print("Distance in Miles:", miles)
            miles_input = float(input("Enter distance in miles: "))
            km = miles_input / 0.621371  
            print("Distance in Kilometers:", km)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")
 

if __name__ == "__main__":
    conversion_menu()
 
conversion_menu()
 
