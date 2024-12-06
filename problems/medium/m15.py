'''Write a program to check if a number is an Armstrong number (e.g., 153  = 1^3 + 5^3 + 3^3 ) .'''
def sum(num):
   str_num = str(num)
   power = len(str_num)
   armstrong_number = 0
   for char in str_num:
      armstrong_number += int(char) ** power
      
   return armstrong_number
   
num = 1634

 
s = sum(num)

 
if s == num:
   print('Given number is an Armstrong Number')
else:
   print('Given number is not an Armstrong Number')

