def matrix_operations_menu():
    print("1. Add Matrices")
    print("2. Multiply Matrices")
    print("3. Transpose Matrix")
    choice = int(input("Enter your choice: "))

    if choice == 1 or choice == 2:
        rows, cols = map(int, input("Enter rows and columns: ").split())
        print("Enter the first matrix:")
        mat1 = [[int(x) for x in input().split()] for _ in range(rows)]
        print("Enter the second matrix:")
        mat2 = [[int(x) for x in input().split()] for _ in range(rows if choice == 1 else cols)]
        
        if choice == 1:  
            result = [[mat1[i][j] + mat2[i][j] for j in range(cols)] for i in range(rows)]
            print("Resultant Matrix (Addition):")
            for row in result:
                print(row)
        
        elif choice == 2:  
            result = [[0 for _ in range(cols)] for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    for k in range(len(mat2)):
                        result[i][j] += mat1[i][k] * mat2[k][j]
            print("Resultant Matrix (Multiplication):")
            for row in result:
                print(row)
    
    elif choice == 3:
        rows, cols = map(int, input("Enter rows and columns: ").split())
        print("Enter the matrix:")
        mat = [[int(x) for x in input().split()] for _ in range(rows)]
        transpose = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                transpose[j][i] = mat[i][j]
        print("Transpose of the Matrix:")
        for row in transpose:
            print(row)
    
    else:
        print("Invalid option")