'''Write a program to reverse a given list without using built-in functions'''
def reverse_list(lst):
    rev_list = input_list[::-1]
    return rev_list
 
input_list = [1, 2, 3, 4, 5]
print("Original list:", input_list)

reversed_list = reverse_list(input_list)
print("Reversed list:", reversed_list)