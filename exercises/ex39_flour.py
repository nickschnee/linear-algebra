import numpy as np

A = np.array([[3, 1, 1], [1, 3, 1], [2, 1, 1], [2, 0, 4]])
B = np.array([[2, 1, 2], [2, 1, 0], [0, 1, 1]])
x = np.array([[10], [5], [15]])

C = A@B.T
print(C)

f = C@x

print("f = ",f)