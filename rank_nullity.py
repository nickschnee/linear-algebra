import numpy as np
from numpy.linalg import matrix_rank

from scipy.linalg import null_space

# input the matrix in row echelon form!
C = np.array([[1,1,1],[0,0,-1],[0,0,-2]])

# find rank of matrix
rank = matrix_rank(C)
print("Rank:", rank)

#find nullity of matrix
null_space = null_space(C)
nullity = null_space.shape[1]
print("Nullity:", nullity)

