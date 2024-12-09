def number_analysis_menu():
    print("1. Check Prime")
    print("2. Factorial")
    print("3. Fibonacci Sequence")
    print("4. Sum of Digits")
    choice = int(input("Enter your choice: "))

 
    
    if choice > 0:
        n = int(input("Enter a number: "))
        if choice == 1:
            is_prime = True
            for i in range(2, n):  
                if n % i == 0:
                    print(" Not Prime")
                    break
            else:    
                print("Prime")   
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
                total += n % 10
                n //= 10   
            print("Sum of Digits:", total)
        else:
            print("Invalid option")
    else:
        print("Enter a positive choice")
        

    n = int(input("Enter a number: "))

    if choice == 1:
        is_prime = True
        for i in range(2, n):  
            if n % i == 0:
                is_prime = False
        if is_prime:
            print("Prime")
        else:
            print("Not prime")  
    elif choice == 2:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i   
        print("Factorial:", factorial)
    elif choice == 3:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        print("Fibonacci Sequence:", fib)  
    elif choice == 4:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10   
        print("Sum of Digits:", total)
    else:
        print("Invalid option")
 
number_analysis_menu()