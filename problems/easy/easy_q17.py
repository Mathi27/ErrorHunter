# Print X N Times
def print_x_n_times(x, n):
    for i in range(1, n + 1):  # Bug: Loop runs one less time than expected
        print(x)
if __name__ == "__main__":
 # Handle the input  by Yourself
 num = int(input("Enter number: "))
 rep = int(input("Enter number of times to repeat: "))
 print_x_n_times(num,rep)