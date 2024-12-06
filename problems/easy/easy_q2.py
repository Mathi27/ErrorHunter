# Find the Largest Number: Accept two numbers and print the larger one.
def largest_of_two(a, b):
    if a > b:
        return b   
    else:
        return a

num1 = int(input("Enter the First Number :"))
num2 = int(input("Enter the Second Number :"))
res = largest_of_two(num1,num1)
print(res)