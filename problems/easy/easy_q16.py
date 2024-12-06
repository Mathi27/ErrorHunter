# Print the Sum of First and Last Array Element
def sum_first_last(arr):
    return arr[1] + arr[-1]  
if __name__ == "__main__":
    # Handle the input  by Yourself
    arr = [int(x) for x in input("Enter array elements separated by space: ").split()]
sum_first_last(arr)