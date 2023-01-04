import numpy as np

print()
print('Hi!')
print('This script multiplies two matrices together.')

while True:
    # prompt the user to input the matrices
    
    print('Please enter the matrices in the format "ROWxCOL" (e.g. 2x2).')
    print('Currently, only whole numbers (e.g. 1) can be entered, NO fractions (e.g. 3/4) or decimals (e.g. 0.75)')
    print()

    A_str = input("Enter matrix A (ROWxCOL format): ")
    B_str = input("Enter matrix B (ROWxCOL format): ")

    # parse the input strings to obtain the matrix shapes
    A_shape = tuple(map(int, A_str.split("x")))
    B_shape = tuple(map(int, B_str.split("x")))

    # check if the matrices are compatible for multiplication
    if A_shape[1] != B_shape[0]:
        print("Error: Matrices A and B cannot be multiplied together. The product AB is defined if and only if the number of columns in A is equal to the number of rows in B.")
    else:
        # create empty matrices
        A = np.empty(A_shape)
        B = np.empty(B_shape)

        # prompt the user to input the matrix elements row by row
        for i in range(A_shape[0]):
            row_str = input("Enter row {} of matrix A (space-separated): ".format(i+1))
            A[i,:] = list(map(int, row_str.split()))
        for i in range(B_shape[0]):
            row_str = input("Enter row {} of matrix B (space-separated): ".format(i+1))
            B[i,:] = list(map(int, row_str.split()))

        # multiply the matrices
        C = np.dot(A, B)

        # print the result
        print(C)

    # ask the user if they want to perform the multiplication again
    repeat = input("Would you like to do another multiplication? (y/n) ")
    if repeat.lower() != "y":
        break
    
    print()
    print('Okay, here we go again:')