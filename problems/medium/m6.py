
def file_handling_menu():
    print("1. Write to File")
    print("2. Read File")
    print("3. Count Lines, Words, Characters")
    print("4. Append to File")
    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        data = input("Enter data to write: ")
        with open("abc.txt", "w") as f:  
            f.write(data)
        f.close()
    elif choice == 2:
        with open("abc.txt", "r") as f:
            print(f.read())
            
        f.close()  
    elif choice == 3:
        with open("abc.txt", "r") as f:
            lines = len(f.read().split("\n"))
            chars = len(f.read().split()) 
            words = sum(len(line) for line in f.readlines())  
            print("Lines:", lines, "Words:", words, "Characters:", chars)
            
        f.close()
    elif choice == 4:
        data = input("Enter data to append: ")
        f = open("abc.txt","a")
        f.append(data)
            
            
        f.close()
    else:
        print("Invalid option")
file_handling_menu()
