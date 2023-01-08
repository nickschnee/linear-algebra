import numpy as np

# Define a matrix A and a right-hand side b
# A = np.array([[24, 68, 0, -36], [0, 34, 82, -79], [5, 76, -33, 0], [-2, 0, -63, 65]])

# A = np.array([[0, 1, -2, 1], [2, 0, 4, 2], [3, 4, -4, 3], [-4, 2, -1, -2]])

A = np.array([[0, 1, -2, 1], [2, 0, 4, -2], [3, 4, -4, 3], [-1, 2, -1, -2]])


# b = np.array([16, -2, 58, 69])

b = np.array([0, 6, 11, -8])

# get the rank of matrix A
rank_A = np.linalg.matrix_rank(A)

# Get the rank of the augmented matrix
rank_M = np.linalg.matrix_rank(np.hstack((A, b.reshape(-1, 1))))

# Solve the system of linear equations
x = np.linalg.solve(A, b)

# Check the number of solutions
if rank_A < rank_M:
    print("The system has no solutions.")
elif rank_A == rank_M:
    print("The system has a unique solution.")
else:
    print("The system has infinitely many solutions.")

# must be zero
# print(A@x-b)

# Print the solution
print(x)