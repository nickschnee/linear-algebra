def gaussian_elimination(A, b):
    # Initialize the number of rows in the matrix
    n = len(A)

    # Eliminate each equation in turn
    for pivot_row in range(n):
        # Choose pivot element
        pivot = A[pivot_row][pivot_row]
        # Output matrix
        print("Matrix A:")
        for row in A:
            print(row)
        print("Vector b:")
        print(b)
        print()

        if pivot_row == 0:
            print("OKAY? LET'S GO:")
            print("OKAY? LET'S GO:")
            print("OKAY? LET'S GO:")
            print("OKAY? LET'S GO:")
            print("OKAY? LET'S GO:")
            print()

        # Check if pivot element is zero
        if pivot == 0:
            # Find a non-zero element in the pivot column
            for row in range(pivot_row + 1, n):
                if A[row][pivot_row] != 0:
                    # Swap pivot row with the row that has a non-zero element in the pivot column
                    A[pivot_row], A[row] = A[row], A[pivot_row]
                    b[pivot_row], b[row] = b[row], b[pivot_row]
                    # Update pivot element
                    pivot = A[pivot_row][pivot_row]
                    break
            # If pivot element is still zero, it means that the matrix is singular and cannot be solved
            try:
                # some code that might raise an error if pivot == 0
                if pivot == 0:
                    raise ValueError("Singular matrix - cannot solve system of equations. There may still be a solution set, or no solution at all. Think!")
            except ValueError as e:
                # print the error message
                print(e)
                exit()

        # Iterate over all rows beneath the pivot row
        for row in range(pivot_row + 1, n):
            # Eliminate variable from other equations
            # Divide the element in the pivot column of the current row by the pivot element
            # print(f" Calculating Factor for Value: {A[row][pivot_row]} at Position {row}, {pivot_row}")
            factor = A[row][pivot_row] / pivot
            # print(f" Factor: {factor}")
            # Output elimination step
            print(f"Eliminate variable x_{pivot_row + 1} from row {row + 1} by adding "
                  f"{factor*-1} * row {pivot_row + 1} to row {row + 1}:")
            print()
            # Iterate over all columns to the right of the pivot column
            for col in range(pivot_row, n):
                # Subtract the product of the pivot row and the factor calculated above from the current element
                A[row][col] = A[row][col] - A[pivot_row][col] * factor
            # Subtract the product of the pivot row and the factor calculated above from the current element in the vector b
            b[row] = b[row] - b[pivot_row] * factor
            # Output matrix after elimination step
            print("Matrix A:")
            for row in A:
                print(row)
            print("Vector b:")
            print(b)
            print()
            print("++++++++++++++++++++++++++++++++++++++++++++++++")
            print()

    # Back-substitute to find solution
    x = [0] * n
    # Iterate over all rows in the matrix in reverse order
    for row in reversed(range(n)):
        # Calculate the value of the variable for the current row
        # This is done by dividing the difference of the current element in vector b and the sum of the products of the other variables and their corresponding elements in the current row of the matrix, by the pivot element in the current row of the matrix
        x[row] = (b[row] - sum(A[row][col] * x[col] for col in range(row + 1, n))) / A[row][row]
    # Return the calculated values of the variables
    return x

# EDIT MATRIX HERE
# EDIT MATRIX HERE
# EDIT MATRIX HERE
# EDIT MATRIX HERE
# EDIT MATRIX HERE
# EDIT MATRIX HERE
# EDIT MATRIX HERE

# A = [[2, 4, 0], [-3, -6, -3], [1, 2, 1]]
# b = [12, 12, 9]

# A = [[1, 1, -2], [1, 3, -1], [2, 1, -5]]
# b = [4, 7, 7]

A = [[0.1, 0, 0.6],[0.4, 0.2, 0.3],[0.2, 0.7, 0.1]]
b = [210, 290, 370]

print()
print("STARTING GAUSSIAN ELIMINATION WITH MATRIX:")
print("STARTING GAUSSIAN ELIMINATION WITH MATRIX:")
print("STARTING GAUSSIAN ELIMINATION WITH MATRIX:")
print("STARTING GAUSSIAN ELIMINATION WITH MATRIX:")
print("STARTING GAUSSIAN ELIMINATION WITH MATRIX:")
print("STARTING GAUSSIAN ELIMINATION WITH MATRIX:")
print()

x = gaussian_elimination(A, b)

print("Solution:")
print(x) 