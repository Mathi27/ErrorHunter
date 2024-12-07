# Print the Sum of First and Last Array Element
def sum_first_last(arr):
    return arr[0] + arr[-1]  
if __name__ == "__main__":
    # Handle the input  by Yourself
    arr = list(map(int, input("Enter array elements separated by space: ").split(" ")))
    print(sum_first_last(arr))