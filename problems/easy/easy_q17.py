# Print X N Times
def print_x_n_times(x, n):
    for i in range(1, n+1):  # Bug: Loop runs one less time than expected -> fixed by adding a +1 also can be fixed by changing the iteration of the loop in intial stage as 0
        print(x)
if __name__ == "__main__":
 # Handle the input  by Yourself
 #Inputs obtained and intendation errors were fixed. Also, the assingments of the function call were done
    num = input("Enter the Number that will be printed : ")
    no_of_times = int(input("Enter The no. of time you wanna print this no. : "))
    print_x_n_times(num,no_of_times) 

# By: Deepak K M, 24UCS121, CSE_A