'''Generate the Fibonacci series up to n terms using a recursive function.
'''

def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

n=int(input("Enter the number :"))
for i in range(n):
    print(fibonacci(i))
