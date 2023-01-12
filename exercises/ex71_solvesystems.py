import numpy as np 
import scipy.linalg as la

# Theorie
# rkA = np.linalg.matrix_rank(A) 
# print(rkA) x = la.solve(A, b) 
# print(x)

# Ex. A
# Ex. A
# Ex. A
# Ex. A

A = np.array([ [24, 68, 0, -36], [0, 34, 82, -79], [5, 76, -33, 0], [-2, 0, -63, 65] ]) 
b = np.array([ [16], [-2], [58], [69] ]) 

# Ex. B
# Ex. B
# Ex. B
# Ex. B
# Ex. B

# A = np.array([ [0, -6, 18, 12], [-5, -15, 15, 6], [-15, -38, 24, 4] ]) 
# b = np.array([ [24], [11], [9] ])

# Ex. C 
# Ex. C 
# Ex. C 
# Ex. C 
# Ex. C 
# Ex. C 

# A = np.array([ [2, -6, 8, 4], [1, 3, -1, 1], [-6, 36, -37, -15], [2, -18, 16, 7], [-2, 12, -16, 0] ]) 
# b = np.array([ [10], [0], [-43], [18], [-18] ])

# Ex. D
# Ex. D
# Ex. D
# Ex. D
# Ex. D
# Ex. D - correct solution

# A = np.array([ [2e7, 1e7, -3e7], [6.4e7, 3.2e7, -9.6e7], [-5e6, -2.5e6, 7.5e6], [2.2e8, 1.1e8, -3.3e8] ]) 
# b = np.array([ [-5], [-16], [1.253], [-55] ])

# Ex. E
# Ex. E
# Ex. E
# Ex. E
# Ex. E

# A = np.array([ [1.1, -2, 9.3, 0], [-3.3, 4.8, -27.3, -0.5], [4.4, -4.4, 38.6, -0.8], [2.2, -1.6, 23.8, -3.6] ]) 
# b = np.array([ [25], [-77.6], [108.2], [56] ])

# Ex. F
# Ex. F
# Ex. F
# Ex. F
# Ex. F
# Ex. F

# A = np.array([ [1.1, -2, 9.3, 0], [-3.3, 4.8, -27.3, -0.5], [4.4, -4.4, 38.6, -0.8], [2.2, -1.6, 23.8, -3.6]]) 
# b = np.array([ [26.2], [-75.7], [108], [54.2] ])

rkA = np.linalg.matrix_rank(A) 

rkAb = np.linalg.matrix_rank(np.hstack([A,b]))

n_cols = A.shape[1]

lenA = len(A[0])
nullityA = lenA - rkA

# when rkA is not equal to rkAb, then the matrix has no solution

print("rkA:", rkA) 
print("rkAb:", rkAb)

if rkA != rkAb:
    print("This system has no solution, since the ranks are not the same.")

elif rkA == rkAb and rkA == n_cols:
    print("The system has a unique solution, rkA == rkAb and nullity == 0")

elif rkA == rkAb:
    print("The system has many solutions. Determine with least squares and free parameters.")


# check if matrix A is regular
# this is the case, if d != 0

try:
  d = np.linalg.det(A)

  if d != 0:
        print("The system has a unique solution, because determinant is not zero.")

except:
  print("Cannot calculate determinant of matrix A, because matrix is not square.")



print("Calculated solution using least squares method is:")
# returns least squares solution
x = la.lstsq(A, b)[0] 
print(x)

print("Calculated free parameters are (if any):")
xh = la.null_space(A)
print(xh)