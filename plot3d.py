import matplotlib.pyplot as plt
import numpy as np

# define the coefficients of the equations
a1 = [1, 1, -2]
a2 = [1, 3, -1]
a3 = [2, 1, -5]

# define the constant terms of the equations
b1 = 4
b2 = 7
b3 = 7

# define a 3D coordinate system
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# convert the lists of coordinates to arrays
x1, y1, z1 = np.meshgrid([0, b1/a1[0]], [0, b1/a1[1]], [0, b1/a1[2]])
x2, y2, z2 = np.meshgrid([0, b2/a2[0]], [0, b2/a2[1]], [0, b2/a2[2]])
x3, y3, z3 = np.meshgrid([0, b3/a3[0]], [0, b3/a3[1]], [0, b3/a3[2]])

# plot the three equations as planes
ax.plot_surface(x1, y1, z1, alpha=0.5)
ax.plot_surface(x2, y2, z2, alpha=0.5)
ax.plot_surface(x3, y3, z3, alpha=0.5)

# show the plot
plt.show()