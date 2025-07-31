 # Reverse a Number using while loop

def reverse_number(num):
    rev = 0
    is_negative = num < 0
    num = abs(num)

    while num != 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    return -rev if is_negative else rev

if __name__ == "__main__":
    number = int(input("Enter num: "))
    result = reverse_number(number)
    print("Reversed number:", result)
