# ex 01: Gram-Schmidt-Process

import numpy as np

w1 = np.array ([[-1/3] , [2/3] , [2/3]])   # given vector

# Generate orthogonal vectors:
w2 = np.array ([[2/3] , [1/3] , [0]])       # "make" vector w2: swap x and y of w1, switch switch sign of new y, take z = 0
w3 = np.array ([[1] , [0] , [0]])           # "make" vector w3: e1

# Stack into matrix
A = np.hstack ([w1 , w2 , w3])

# Run Gram-Schmidt-Process
Q,R = np.linalg.qr(A)
# print(Q)

# Solution:
# v2 = second column of matrix Q
# v3 = third column of matrix Q


# ex 02
# ex 02
# ex 02
# ex 02
# ex 02
# ex 02
# ex 02

import numpy as np

# Calculate ATA
A = np.array([[-4,-2],[2,-2],[4,-1]])
ATA = A.T @ A

# Calculate the singular values and singular vectors of A
_, singular_values, _ = np.linalg.svd(A)

# The matrix Σ containing the singular values of A is given by a diagonal matrix with the singular values on the diagonal
Σ = np.diag(singular_values)

U, singular_values, V = np.linalg.svd(A)

print(U)