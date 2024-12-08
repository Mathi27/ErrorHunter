def file_handling_menu():
    print("1. Write to File")
    print("2. Read File")
    print("3. Count Lines, Words, Characters")
    print("4. Append to File")
    choice = int(input("Enter your choice: "))

    filename = input("Enter the file name: ")

    if choice == 1:
        data = input("Enter data to write: ")
        with open(filename, "w") as f:  
            f.write(data)
        print("Data written successfully.")
    
    elif choice == 2:
        with open(filename, "r") as f:  
            content = f.read()
            print("File Content:")
            print(content) 

    elif choice == 3:
        with open(filename, "r") as f:
            content = f.read()  
            lines = content.split("\n")  
            words = content.split()  
            chars = len(content)  
            print("Lines:", len(lines), "Words:", len(words), "Characters:", chars)

    elif choice == 4:
        data = input("Enter data to append: ")
        with open(filename, "a") as f:  
            f.write(data + "\n")  
        print("Data appended successfully.")

    else:
        print("Invalid option")


file_handling_menu()
