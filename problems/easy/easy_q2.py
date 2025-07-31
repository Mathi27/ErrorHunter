 
def largest_of_two(a, b):
    return a if a > b else b

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))
        result = largest_of_two(num1, num2)
        print(f"The larger number is: {result}")
    except ValueError:
        print("ERROR: Please enter valid integer values.")
