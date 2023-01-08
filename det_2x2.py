import numpy as np

def determinant(matrix):
  a = matrix[0][0]
  b = matrix[0][1]
  c = matrix[1][0]
  d = matrix[1][1]

  return (a * d) - (b * c)



matrix = np.array([

    [3, 2], 
    [2, -1]

    ])

print(determinant(matrix))  # Output: -1