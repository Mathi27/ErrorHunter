# Print X N Times
def print_x_n_times(x, n):
    for i in range(1, n):  # Bug: Loop runs one less time than expected
        print(x)
if __name__ == "__main__":
 # Handle the input  by Yourself
    x=int(input("Enter x : "))
    n=int(input("Enter n : "))
    res=print_x_n_times(x,n)

print_x_n_times(x,n)