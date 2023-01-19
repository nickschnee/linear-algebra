import numpy as np


# define base vectors
w1 = np.matrix([[0,1]]).T 
w2 = np.matrix([[1,0]]).T

# matrix
B = np.hstack([w1,w2])
# check determinant
np.linalg.det(B)
det = np.linalg.det(B)

if det == 0: 
    print("Determinant is zero - it is a base")
    print(det)

else: 
    print("Determinant is not zero")
    print(det)

