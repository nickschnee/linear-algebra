import numpy as np

A = np.array([[1, 0, 1], [-2, 1, 0]])

U, singular_values, VT = np.linalg.svd(A)

# as svd() only returns the singular values - make matrix out of them
Sigma = np.diag(singular_values) 
U, Sigma, VT