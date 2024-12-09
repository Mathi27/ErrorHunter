'''Write a program to check if a number is an Armstrong number (e.g., 153  = 1^3 + 5^3 + 3^3 ) .'''
 
def count_digits(n):
   i = 0
   while n >= 0:
      n =n // 10
      

      i += 1
   return i

def sum(n):
   i = count_digits(n)
   s = 0
   while n > 0:
      digit = n/10
      n /= 10
      s += pow(digit,i)
   return s


num = 1634

 
s = sum(num)

 
if s == num:
   print('Given number is an Armstrong Number')
else:
   print('Given number is not an Armstrong Number')
 
n=input("Enter Number:")
c=0
def arm(n):
   for i in n:
      c+=int(i)**len(n)
   if c==int(n):
      print("It is Armstrong number")
   else:
      print("It is not Armstrong Number")

arm(n)
