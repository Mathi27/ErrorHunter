try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
except ValueError:
    print("Enter only INTEGER that is ONLY NUMBER")
