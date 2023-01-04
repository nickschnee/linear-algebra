import matplotlib.pyplot as plt
import numpy as np

# define the coefficients of the equation
a1 = [1, 1, -2]

# define the constant term of the equation
b1 = 4

# define a 3D coordinate system
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# generate the coordinates of the plane
X1, Y1 = np.meshgrid(np.linspace(0, b1/a1[0], 10), np.linspace(0, b1/a1[1], 10))
Z1 = (b1 - a1[0]*X1 - a1[1]*Y1)/a1[2]

# plot the equation as a plane
ax.plot_surface(X1, Y1, Z1, alpha=0.5)

# show the plot
plt.show()