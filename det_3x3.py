import numpy as np

# rule of sarrus for 3x3 matrix

def determinant(matrix):
  a = matrix[0][0]
  b = matrix[0][1]
  c = matrix[0][2]
  d = matrix[1][0]
  e = matrix[1][1]
  f = matrix[1][2]
  g = matrix[2][0]
  h = matrix[2][1]
  i = matrix[2][2]
  return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h

matrix = [
  
  [2, 1, -1], 
  [1, 2, -1], 
  [0, 0, 2]

  ]

print(determinant(matrix))  # Output: 0