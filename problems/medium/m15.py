'''Write a program to check if a number is an Armstrong number (e.g., 153  = 1^3 + 5^3 + 3^3 ) .'''
a=input("Enter Number:")
def Arms(a):
   e=0
   for i in a:
      c=int(i)
      d=c*c*c
      e+=d
   return e

b=Arms(a)
f=int(a)
if b==f:
   print(f,"is an Armstrong Number")
else:
   print(f,"is not An Armstrong Number")