'''
Create a program that checks whether a given number is a prime number or not.
'''
a=int(input("Enter Number:"))

if (a%2==0 or a%3==0) and a/2>=2:
    print(a,"is not a Prime Number")
else:
    print(a,"is a Prime Number")