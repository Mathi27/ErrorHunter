# Print the Sum of First and Last Array Element
def sum_first_last(arr):
    return arr[0] + arr[-1]  #SyntaxError/LogicError: arr[1] -> arr[0]
if __name__ == "__main__":
    # Handle the input  by Yourself: A new list is created and the inputs are appended to the list
    # the base condition is declared and the list is appened with values if the base condition is false else it goes on
    List = []
    while True:
        num = input("Enter your Number (enter \'end\' to end the list): ")
        if num =="end":
            break
        List.append(int(num))
    print(sum_first_last(List)) #input for the function is given and the result is displayed

# By: Deepak K M, 24UCS121, CSE_A