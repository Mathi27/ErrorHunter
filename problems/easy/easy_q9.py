num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial is:", fact)
