'''Comparing arrays'''

'''This problem helps one to understand the key concepts of an array(list) in Python. 
Two arrays are said to be the same if they contain the same elements and in the same order.
However, in this problem, we will compare two arrays to see if they are same, but with a slight twist.
Here, two arrays are the same if the elements of one array are squares of elements of other arrays and regardless of the order. 
Consider two arrays a and b.

'''
# function to compare the arrays 
def comp(array1, array2): 
 
    # Handle edge cases where one or both arrays could be None
    if array1 is None or array2 is None:
        return array1 == array2  # Return True only if both are None

    # Check if sorted squares of array1 are equal to sorted elements of array2
    return (sorted(array1) == sorted([i ** 2 for i in array2])) or (sorted(array2) == sorted([i ** 2 for i in array1]))
 
# Example usage:
print(comp([1, 2, 3, 4], [1, 4, 9, 16]))
 
    if array1 == [] and array2 != []:  
        return False
 
     
    if (sorted(array2) == sorted([i ** 2 for i in array1])) or (sorted(array1) == sorted([i ** 2 for i in array2])):
        print("the two arrays are equal is one of the array is equal to square of another array")  
      
    return   
 
     
    if (sorted(array1) == sorted([i ** 0.5 for i in array2])) and (sorted(array2) == sorted([i ** 2 for i in array1])):  
        return True
    else:  
        return False
  
 
result = comp([1,2,3,4], [1,4,9,16])
if result:
    print("The two arrays are same as the given condition")
else:
    print("The two arrays are not same as the given condition")
 
    if array1 is None and array2 is not None: 
        print("The two arrays are not same ")

        return False
      
     
 
    if (sorted(array2) == sorted([i ** 2 for i in array1])) and (sorted(array2) == sorted([i ** 2 for i in array1])):  
 
    if (sorted(array1) == sorted([i ** 2 for i in array2])) or  (sorted(array2) == sorted([i ** 2 for i in array1])):
        print(" if the two arrays are same or the elements of the first array are the square of the elements of the second array!!  ")  
 
    if array1 is None or array2 is None: 
        return False
      
     
    if (sorted(array2) == sorted([i ** 2 for i in array1])):  
 
 
        return True
      
    return False
   
 
 
print(comp([1,2,3,4], [1,4,9,16]))
 
lis1=eval(input("Enter list 1: "))
lis2=eval(input("Enter list 2: "))
print(comp(lis1,lis2))
 
 
 
print(comp([1,2,3,4], [1,4,9,16]))
 
 
