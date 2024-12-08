'''Write a program to reverse a given list without using built-in functions'''

def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):  
        reversed_list.append(lst[i])  
    return reversed_list
input_list = [1, 2, 3, 4, 5]
print("Original list:", input_list)


print("Reversed list:", reverse_list(input_list))
