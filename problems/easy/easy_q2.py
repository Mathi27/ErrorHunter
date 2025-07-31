 
# Find the Largest Number: Accept two numbers and print the larger one.
try:
    num1 = int(input("Enter a num1:"))
    num2 = int (input("Enter a num2:"))

    if (num1 > num2):
       print("n1 is the largest number!!")
    elif (num1 < num2):
       print("n2 is the largest number!!")
    else:
       print("both numbers are equal!!")
       
except ValueError:
    print("Enter only integer number!!")