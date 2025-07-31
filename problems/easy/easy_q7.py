num = input("Enter the number: ")
total = 0

for digit in num:
    if digit != '-':
        total += int(digit)

print("Sum of digits:", total)

