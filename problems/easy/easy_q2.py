# Find the Largest Number: Accept two numbers and print the larger one.
def largest_of_two(a, b):
    if a > b:
        print(a)   
    else: 
        print(b)
    
if __name__ == "__main__":
    num1 = int(input("Enter the First Number :"))
    num2 = int(input("Enter the Second Number :"))
    largest_of_two(num1,num2)