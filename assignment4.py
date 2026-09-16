import numpy as np 

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
elements1 = list(map(int, input().split()))
matrix1 = np.array(elements1).reshape(rows, cols)

print("Enter elements of second matrix:")
elements2 = list(map(int, input().split()))
matrix2 = np.array(elements2).reshape(rows, cols)

result = matrix1 + matrix2

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

print("Sum of Matrices:")
print(result)