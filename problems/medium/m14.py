'''Generate the Fibonacci series up to n terms using a recursive function.
'''
def fibonacci(n):
    if n <= 0:
        return []  # Return an empty list for non-positive input
    elif n == 1:
        return [0]  # Return the first Fibonacci number
    elif n == 2:
        return [0, 1]  # Return the first two Fibonacci numbers

    # Generate Fibonacci sequence for n > 2
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq

# Input and output
n = int(input("Enter the number of terms: "))
print("Fibonacci Sequence:", fibonacci(n))
