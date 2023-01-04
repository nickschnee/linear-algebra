import numpy as np

def invert_matrix(A):
    # Check if the matrix is square
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix is not square.")

    # Get the size of the matrix
    n = A.shape[0]

    # Create the identity matrix
    I = np.eye(n)

    # Create a copy of the matrix and the identity matrix
    M = np.hstack((A, I))
    print("M:", M)

    # Perform row operations to transform M into an upper triangular matrix
    for i in range(n):
        # Check if the pivot element is zero
        if M[i, i] == 0:
            # Find a row with a nonzero pivot element
            for j in range(i+1, n):
                if M[j, i] != 0:
                    # Swap rows i and j
                    M[[i, j], :] = M[[j, i], :]
                    break
        # Check if the pivot element is still zero
        if M[i, i] == 0:
            raise ValueError("Matrix is singular.")

        # Divide row i by the pivot element
        M[i, :] /= M[i, i]

        # Subtract row i from the other rows
        for j in range(n):
            if i == j:
                continue
            M[j, :] -= M[j, i] * M[i, :]
        print("M:", M)

    # Extract the inverse matrix from the right side of M
    A_inv = M[:, n:]
    print("A_inv:", A_inv)

    return A_inv

# Define a matrix A
A = np.array([[-1, 0, 2], [1, 1, -1], [-1, 1, 1]])

# Invert the matrix
A_inv = invert_matrix(A)

# Print the inverse of A
print(A_inv)