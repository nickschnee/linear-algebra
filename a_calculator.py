import numpy as np 
import scipy.linalg as la

def findsolset():
    
    # Check ranks.
    rkA = np.linalg.matrix_rank(A)
    rkAb = np.linalg.matrix_rank(np.hstack([A,b]))
    
    lenA = len(A[0])
    nullityA = lenA - rkA

    if rkA == rkAb:
        if rkA == lenA:
            print("The system has a unique solution. Command depending on square or not.")
            unique()
        else:
            print("The system has at least one solution. Find the general solution x = xp + xh with " + str(nullityA) + " free parameter(s).")
            general()
    else:
        print("Since rkA ≠ rkAb, the system has no solution. Solution set: L = 0")

    print("-------")
    print("Values:")
    print("square? ", lenA == len(A))
    print("A = ", lenA)
    print("rk A = ", rkA)
    print("rk[A b] = ", rkAb)
    print("rkA = rk[A b]?", rkA == rkAb)
    print("nullity A =", nullityA)
    print("-------")
    

    
# Find unique solution:
def unique():
    if lenA == len(A):
        x = la.solve(A, b)   # if system is square
        print("L =", x)
    else:
        x = la.lstsq(A, b)[0]    # if system is not square
        print("L = ", x)
    
    
# Find the general solution x = xp + xh
def general():
    # particular solution  >> Ax = b
    xp = la.lstsq(A, b)[0]     
    print("xp =", xp)

    # general solution: Ax = 0
    # 2 free parameters (uncomment if nullity != 2 !!)
    xh = la.null_space(A)
    print("xh[t1] =", xh[:,0])   
    print("xh[t2] =", xh[:,1])
    #print("xh[t3] =", xh[:,2])
    
    print("------")
    print("L = {xp + t1*xh1 + t2*xh2}")
    
    return xp, xh


# Set up A and b

A = np.array([
[0, -6, 18, 12],
[-5, -15, 15, 6],
[-15, -38, 24, 4]
])

b = np.array([
[24],
[11],
[9]
])

findsolset()