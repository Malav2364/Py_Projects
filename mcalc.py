import numpy as np

#matrix (1)
def m1Input(rows1, columns1):
    matrix1 = np.empty((rows1, columns1), dtype=int)
    for i in range(rows1):
        for j in range(columns1):
            matrix1[i,j] = float(input(f"Enter the element at pos ({i+j}, {j+i}) : "))
    return matrix1

#take input for 1st martrix 
rows = int(input("Enter the rows for matrix 1 : "))
columns = int(input("Enter the columns for matrix 1 : "))

matrix = m1Input(rows, columns)
# print(matrix)

#for matrix (2)

def m2Input(rows2, columns2):
    matrix2 = np.empty((rows2, columns2), dtype=int)
    for i in range(rows2):
        for j in range(columns2):
            matrix2[i,j] = float(input(f"Enter the elements at pos ({i+j}, {j+i}) : "))
    return matrix2

#input for 2nd matrix

rows1 = int(input("Enter the rows for 2nd matrix : ")) 
columns1 = int(input("Enter the columns for 2nd matrix : ")) 

matrix1 = m2Input(rows1, columns1)

Addition = np.add(matrix, matrix1)
print(Addition)
