import numpy as np
from scipy.linalg import lu

# The LU decomposition is useful because it allows you 
# to solve systems of linear equations, 
# find the determinant of a matrix, and 
# invert a matrix efficiently. 
# It is also the basis for many numerical algorithms, such as the 
# Gaussian elimination algorithm and the Crout algorithm.


A = np.array([[4, -1, 3],[-1, 2, 0],[2,3,5/2]])
P, L, U = lu(A)

print("P =")
print(P)

print("L =")
print(L)
print("U =")
print(U)

# E1 = np.array([[1,0,0],[0.25,1,0],[0,0,1]])
# E2 = np.array([[1,0,0],[0,1,0],[-0.5,0,1]])
# E3 = np.array([[1,0,0],[0,1,0],[0,-2,1]])

# UH = E1 @ E2 @ A

# UH = E3 @ UH


