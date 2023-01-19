import numpy as np  

# to translate into standard basis use basis vectors v1,v2 as mapping matrix
v1 = np.array([[3,1]]).T 
v2 = np.array([[-1,3]]).T 

A = np.hstack([v1, v2])
# use its inverse to translate back to basis v1,v2
Ai = np.linalg.inv(A)

# the transformation matrix M given in standard basis
M = np.array([[14,3],[3,6]]) # given (coordinate) vector
v = np.array([[-2,-2]]).T

# 1.) translate to standard basis
x_1 = A@v

# 2.) calculate image L(x) of x in standard basis
x_2 = M@x_1

# 3.) translate back to basis v1,v2
Ai@x_2 

print(Ai, M, A)