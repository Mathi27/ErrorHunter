def number_analysis_menu():
    print("1. Check Prime")
    print("2. Factorial")
    print("3. Fibonacci Sequence")
    print("4. Sum of Digits")
    choice = int(input("Enter your choice: "))

    n = int(input("Enter a number: "))

    if choice == 1:
        is_prime = True
        for i in range(2,(n//2)+1):  
            if n % i == 0:
                print("not prime number")
            else:
                print("Prime number")   
    elif choice == 2:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i   
        print("Factorial:", factorial)
    elif choice == 3:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[-1] + fib[-2])
        print("Fibonacci Sequence:", fib[:-1])  
    elif choice == 4:
        total = 0
        while n > 0:
          
            a = n % 10
            total+= a
            n=n//10  
            print("Sum of Digits:",total)
    else:
        print("Invalid option")
number_analysis_menu()        
