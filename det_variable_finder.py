import sympy as sp

# det in 4x4 matrix in row echelon form --> diagonal * (-1)**(row swaps)

# Create symbolic variables for the entries of the matrix A
x = sp.Symbol('x')
a = sp.Matrix([ [x, -1, 5], [-5, 1, 5], [5, -1, x] ])
a = sp.Matrix([ [-2, 1, x, 0], [-3, x, 0, 0], [1, -2, 3, 0], [3, -3, -2, 3] ])

# Calculate the determinant of A
detA = a.det()

# Solve the equation detA = 0 for x
solutions = sp.solveset(detA, x)

# Print the solution
print(f"The matrix is singular for x = {solutions}")