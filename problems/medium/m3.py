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
        print("Reversed String:", s[::-1])  
    elif choice == 3:
        if s[::-1] == s:
            print("Palindrome")  
        else:
            print("Not a Palindrome")
    elif choice == 4:
        old = input("Substring to replace: ")
        new = input("Replacement substring: ")
 
        s = s.replace(old, new)  
        print("Updated String:", s)   
 
        print("Updated String:", s.replace(old,new))   
 
    else:
        print("Invalid option")
string_manipulation_menu()