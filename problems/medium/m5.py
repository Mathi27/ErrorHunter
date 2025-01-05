def matrix_operations_menu():
    print("1. Add Matrices")
    print("2. Multiply Matrices")
    print("3. Transpose Matrix")
    choice = int(input("Enter your choice: "))

    if choice == 1 or choice == 2:
        rows, cols = map(int, input("Enter rows and columns: ").split())
        mat1 = [[int(x) for x in input("Enter row 1: ").split()] for _ in range(rows)]
        mat2 = [[int(x) for x in input("Enter row 2: ").split()] for _ in range(rows)]
        if choice == 1:
            result = [[mat1[i][j] - mat2[i][j] for j in range(cols)] for i in range(rows)]  
            print("Resultant Matrix:", result)
        else:
            result = [[0 for _ in range(rows)] for _ in range(cols)]  
            for i in range(rows):
                for j in range(cols):
                    result[i][j] += mat1[i][j] * mat2[j][i]   
            print("Resultant Matrix:", result)
    elif choice == 3:
        rows, cols = map(int, input("Enter rows and columns: ").split())
        mat = [[int(x) for x in input("Enter row: ").split()] for _ in range(rows)]
        transpose = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                transpose[i][j] = mat[j][i]  
        print("Transpose:", transpose)
    else:
        print("Invalid option")
matrix_operations_menu()
