'''
Create a program that checks whether a given number is a prime number or not.
'''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

while True:
    try:
        n = int(input("Enter a number: "))
        break
    except:
        print("Enter valid a integer.")


if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
    