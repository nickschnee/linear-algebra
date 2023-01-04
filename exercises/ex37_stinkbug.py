# exercise 3.7 - stinkbug

# import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import rescale

# read image file and display it
img = mpimg.imread('linear-algebra/exercises/stinkbug4.JPG')
plt.imshow(img)

# scale down the image by a factor of 0.2
img = rescale(img, .2)

# delete rows and columns from the image
img = np.delete(img,np.arange(20), axis=0)
img = np.delete(img,np.arange(80,100), axis=0)
img = np.delete(img,np.arange(20), axis=1)
img = np.delete(img,np.arange(80,100), axis=1)

# create an array of zeros with the same shape as the image
col =np.zeros(img.shape[0]*img.shape[1])

# flatten the image and set elements to 0.99 times their value
k = 0
for i in np.arange(img.shape[0]):
    for j in np.arange(img.shape[1]):
        col[k] = np.round(.99*img[i,j,:],0)
        k = k+1
        
# create an array with the indices of the image
image = np.array([np.repeat(np.arange(img.shape[0]),img.shape[1]), np.tile(np.arange(img.shape[1]),img.shape[0])]).T

# subtract 40 from the indices
image[:,0] = image[:,0] - 40
image[:,1] = image[:,1] - 40

# select indices where the value of col is 0
image = image[col==0,:]
print(np.shape(image))

# transpose the image
# image = np.transpose(image)

# print(np.shape(image))

# The matrix A is a reflection matrix about the origin. It will reflect the image about the origin, 
# resulting in a mirror image of the original.
A = np.array([[0,1],[1,0]])

# The matrix B is a scaling matrix. 
# It will stretch the image in the x-direction by a factor of 2,
# while leaving the y-direction unchanged.
B = np.array([[2,0],[0,1]])

# The matrix C is also a reflection matrix, 
# but this time about the y-axis. It will reflect the image about the y-axis, 
# resulting in a mirror image of the original.
C = np.array([[0,-1],[-1,0]])



image_A = np.dot(image, A)
image_B = np.dot(image, B)
image_C = np.dot(image, C)

# do multiple transformations
# image_B = np.dot(image_A, B)
# image_C = np.dot(image_B, A)

# plot the selected indices and save the figure
# plt.plot(image[:,0],image[:,1],"o",color="black")
# plt.axis('square')
# plt.xlim(-40,40)
# plt.ylim(-40,40)
# plt.savefig("bug01.eps",bbox_inches="tight")

# plt.plot(image_A[:,0],image_A[:,1],"o",color="red")
# plt.axis('square')
# plt.xlim(-40,40)
# plt.ylim(-40,40)
# plt.savefig("bug01.eps",bbox_inches="tight")


# create a figure with 2 subplots
fig, ax = plt.subplots(2, 2)

# plot the first image in the first subplot
ax[0, 0].plot(image[:,0], image[:,1], "o", color="black")
ax[0, 0].set_title("Image 1")
ax[0, 0].set_xlim(-40, 40)
ax[0, 0].set_ylim(-40, 40)

# plot the second image in the second subplot
ax[0, 1].plot(image_A[:,0], image_A[:,1], "o", color="red")
ax[0, 1].set_title("Transform with Matrix A")
ax[0, 1].set_xlim(-40, 40)
ax[0, 1].set_ylim(-40, 40)

# plot the second image in the second subplot
ax[1, 0].plot(image_B[:,0], image_B[:,1], "o", color="blue")
ax[1, 0].set_title("Transform with Matrix B")
ax[1, 0].set_xlim(-40, 40)
ax[1, 0].set_ylim(-40, 40)

# plot the second image in the second subplot
ax[1, 1].plot(image_C[:,0], image_C[:,1], "o", color="green")
ax[1, 1].set_title("Transform with Matrix C")
ax[1, 1].set_xlim(-40, 40)
ax[1, 1].set_ylim(-40, 40)

# save the figure
plt.savefig("bug01.eps", bbox_inches="tight")

# display the plot
plt.show()