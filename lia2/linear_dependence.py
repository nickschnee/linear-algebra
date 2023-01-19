import numpy as np 
import scipy.linalg as la 
np.set_printoptions(suppress=True)

v_1 = np.array ([[-3] , [1], [0], [ 6]])
v_2 = np.array ([[1] , [1], [3], [5]])
v_3 = np.array([[-2], [2/3], [0], [ 4]])
v_4 = np.array([[-6], [2], [3], [ -1]])

A = np.hstack ([v_1 , v_2 , v_3, v_4]) 
print(A)

p, l, u = la.lu(A)

# if last row of row echelon form (upper triangular matrix) are all zeros
# then they are linearly dependent

# if there is a pivot in all columns = linearly independent
print()
print('row echelon form:')
print(u)
