def student_record_menu():
    students = {}  

    while True:
        print("\n1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student by Roll Number")
        print("4. Delete Student Record")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            roll = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
            students[roll] = (name, marks)  
            print("Student record added successfully.")

        elif choice == 2:
            if not students:
                print("No records available.")
            else:
                for roll, details in students.items():
                    print(f"Roll: {roll}, Name: {details[0]}, Marks: {details[1]}")  

        elif choice == 3:
            roll = input("Enter Roll Number to Search: ")
            if roll in students:
                print(f"Name: {students[roll][0]}, Marks: {students[roll][1]}")
            else:
                print("Record not found.")  

        elif choice == 4:
            roll = input("Enter Roll Number to Delete: ")
            if roll in students:
                del students[roll]
                print("Record Deleted successfully.")
            else:
                print("Record not found.")  

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid Choice")
student_record_menu()
