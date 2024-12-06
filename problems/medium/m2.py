def array_operations_menu(choice):
    
    arr = list(map(int, input("Enter array elements separated by space: ").split(" ")))

    if choice == 1:
        print("Sum:", sum(arr))   
    elif choice == 2:
        print("Largest Element:", max(arr))  
    elif choice == 3:
        print("Smallest Element:", min(arr))   
    elif choice == 4:
        print("Sorted Array:", arr.sort()) 
    else:
        print("Invalid option")

print("1. Sum of Array")
print("2. Largest Element")
print("3. Smallest Element")
print("4. Sort Array")
choice = int(input("Enter your choice: "))
array_operations_menu(choice)