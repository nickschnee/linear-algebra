import numpy as np
import scipy.linalg as la
from scipy.optimize import minimize

# 4b)

A = np.array([[4, 2, 1], [2, 4, 1], [1, 0, 2], [1, 2, 4]])

b = np.array([ [360], [300], [150], [240]])

rkA = np.linalg.matrix_rank(A) 

rkAb = np.linalg.matrix_rank(np.hstack([A,b]))

print(rkA)
print(rkAb)

lenA = len(A[0])
nullityA = lenA - rkA

print(nullityA)

if rkA != rkAb:
    print("This system has no solution, since the ranks are not the same.")

elif rkA == rkAb and rkA == n_cols:
    print("The system has a unique solution, rkA == rkAb and nullity == 0")

elif rkA == rkAb:
    print("The system has many solutions. Determine with least squares and free parameters.")

# Solution: System is inconsistent.

# 4c
# 4c
# 4c
# 4c
# 4c

print("Calculated solution using least squares method is:")
# returns least squares solution
x = la.lstsq(A, b)[0] 
print(x)

print("Calculated free parameters are (if any):")
xh = la.null_space(A)
print(xh)



# 2e
# 2e
A = np.array([[2, 3, -1],[4, 6, -2]])
P, L, U = lu(A)

L = np.array([[1, 0], [0.5, 1]])
U = np.array([[4, 6, -2], [0, 0, 0]])

print(L@U)
