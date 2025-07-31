def sum_of_digits(num):
    """Calculate the sum of digits of a number."""
    total = 0
    num = abs(num)  # Handle negative numbers

    while num > 0:
        total += num % 10
        num //= 10

    return total

if __name__ == "__main__":
    num = int(input("Enter the Number: "))
    print("Sum of digits:", sum_of_digits(num))
