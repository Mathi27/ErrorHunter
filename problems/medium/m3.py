def string_manipulation_menu():
    print("1. Count Vowels")
    print("2. Reverse String")
    print("3. Check Palindrome")
    print("4. Replace Substring")
    choice = int(input("Enter your choice: "))

    s = input("Enter a string: ")

    if choice == 1:
        vowels = "aeiouAEIOU"
        count = 0
        for char in s:
            if char in vowels:
                count += 1 
        print("Number of Vowels:", count)
    elif choice == 2:
        reversed_string = s[::-1]
        print("Reversed String:", reversed_string)  
    elif choice == 3:
        if s[::-1] == s:
            print("Palindrome")  
        else:
            print("Not a Palindrome")
    elif choice == 4:
        old = input("Substring to replace: ")
        new = input("Replacement substring: ")
        replaced_string = s.replace(old, new)
        print("Updated String:", replaced_string)   
    else:
        print("Invalid option")


string_manipulation_menu()