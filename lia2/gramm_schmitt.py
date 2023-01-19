##Apply the Gram-Schmidt orthonormalization procedure to v1, v2, v3 to construct an
#ONB u1, u2, u3.

import numpy as np


A = np.array([[-1,-2,-2], [1,-5,-4], [5,0,5]]) 

Q,R = np.linalg.qr(A)
print(Q)
#first is u1

#This A: A = np.array([[-1,-2,-2], [1,-5,-4], [5,0,5]]) 
#           is: v1=[-1
#               1
#               5]

#V2 is


#___________


#Find the coordinate vector c of v with respect to the ONB u1, u2, u3 from Part (a).
u1 = Q[:,0]
u1.shape = [3,1]
u2 = Q[:,1]
u2.shape = [3,1]
u3 = Q[:,2]
u3.shape = [3,1]

#THIS HAS TO BE CHANGED 
v = np.array([[-0.7],[-4.5],[-5]])

c = np.array([[(v.T@u1)[0,0]],[(v.T@u2)[0,0]],[(v.T@u3)[0,0]]])
print(c)
print("Did you change v?")