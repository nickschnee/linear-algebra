import numpy as np
import scipy.linalg as la

# the vector
v = np.array([[-0.7],[-4.5],[-5]])

# the basis u1,u2,u3
u1 = np.array([[-0.19245009],
       [ 0.19245009],
       [ 0.96225045]])
u2 = np.array([[-0.39429611],
       [-0.91310678],
       [ 0.10376213]])
u3 = np.array([[ 0.89860644],
       [-0.35944258],
       [ 0.2516098 ]])

# the coordinate vector of v w.r.t. the basis above
# what the hell has this to do with the dot-product?
c = np.array([
    [(v.T@u1)[0,0]],
    [(v.T@u2)[0,0]],
    [(v.T@u3)[0,0]]])

print(c)