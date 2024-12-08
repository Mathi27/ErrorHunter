# Print the Sum of First and Last Array Element
def sum_first_last(arr):
    return arr[0] + arr[-1]  
if __name__ == "__main__":
    # Handle the input  by Yourself
    arr=[2,5,8,7,6]
    
    n=int(input("Enter the Total number of Elements:"))
    for i in range(n):
        x=int(input("Enter the element :"))
        arr.append(x)
 
   
    print(arr)
    print(sum_first_last(arr))