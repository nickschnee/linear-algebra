# problem 3.8

import numpy as np

M = np.array([[1,7],[4,2]])

N = np.array([[6,0],[0,5]])

P = np.array([[-np.pi, -np.pi],[-np.pi, -np.pi]])

Q = np.array([[np.e + np.sqrt(2), np.e],[np.e, np.e + np.sqrt(2)]])

R = np.block([[M, N], [P, Q]])

# S = np.block([[M+N, Null], [Null, P/np.pi]])

# print(R)

#b)

# format of R
# print(R.shape)

# R + S
# print(M+N)

# print(R.T)

# matrix multiplication
print(M@N)
print(N@M)

# c)
print(M*N)
print(M**N)