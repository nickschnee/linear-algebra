import numpy as np

# for 2x2 matrix, use mnemonic rule
# for 3x3 matrix, use rule of sarrus
# for 4x4 matrix, use laplace expansion 
# or gaussian elimination and then multiply diagonal, count row swaps

matrix = np.array([[1, 3, 0],[0, -5, 0],[0, 0, -5]])

determinant = np.linalg.det(matrix)
print(determinant)  # Output: 0.0