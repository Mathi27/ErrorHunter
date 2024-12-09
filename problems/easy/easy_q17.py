# Print X N Times
 
def print_x_n_times(n):
    for i in range(0, n):  # Bug: Loop runs one less time than expected
        print("x")
if __name__ == "__main__":
 # Handle the input  by Yourself
 num=int (input(" Enter a N times :"))
 print_x_n_times(num)
 
def print_x_n_times(x, n):  # Bug: Loop runs one less time than expected
        print(x*n)
if __name__ == "__main__":
 # Handle the input  by Yourself
 
 n=int(input("Enter the number of times:"))
 x="X"
 
 x=input("Enter a character:")
 n=int(input("enter the number of times to loop:"))
 
 print_x_n_times(x,n)
 