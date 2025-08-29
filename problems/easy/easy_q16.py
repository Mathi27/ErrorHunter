def sum_first_last(arr):
    if len(arr) < 2:
        return "Array must have at least two elements."
    return arr[0] + arr[-1]


if __name__ == "__main__":
    # Input 1: user enters comma-separated numbers
    user_input = input("Enter a collection of numbers separated by commas: ")
    user = [int(x.strip()) for x in user_input.split(",")]
    print("Sum of first and last element:", sum_first_last(user))

    # Input 2: user enters numbers one by one
    arr = []
    n = int(input("Enter the total number of elements: "))
    for i in range(n):
        x = int(input(f"Enter element {i+1}: "))
        arr.append(x)
    print("Sum of first and last element:", sum_first_last(arr))

    # Test with a predefined list
    arr = [2, 5, 8, 7, 6]
    print("Sum of first and last element (predefined list):", sum_first_last(arr))
