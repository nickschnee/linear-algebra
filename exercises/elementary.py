import numpy as np

TEST = np.array([[1,2,3],[4,5,6],[7,8,9]])

# add 3x row 2 to row 1
A = np.array([[1,3,0],[0,1,0],[0,0,1]])

# add 3x row 1 and 1x row 2 to row 1
B = np.array([[3,1,0],[0,1,0],[0,0,1]])

# stays the same
C = np.array([[1,0,0],[0,1,0],[0,0,1]])
# print(C@TEST)

D = np.array([[0,0,1],[0,1,0],[1,0,0]])
# print(D@TEST)

E = np.array([[0,1,0],[1,0,0],[0,1,1]])
# print(E@TEST)

F = np.array([[0,1,0],[0,0,1],[1,0,0]])
print(F@TEST)