# exercise 3.4 - stinkbug

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

# plot the selected indices and save the figure
plt.plot(image[:,0],image[:,1],"o",color="black")
plt.axis('square')
plt.xlim(-40,40)
plt.ylim(-40,40)
plt.savefig("bug01.eps",bbox_inches="tight")

# try adding a vector to the image
# this will move the image by the vector
for i in range(10):
    v = np.array([-15,16])
    image = image + v

    plt.plot(image[:,0],image[:,1],"o",color="blue")
    plt.axis('square')
    plt.xlim(-160,160)
    plt.ylim(-160,160)
    plt.savefig("bug01.eps",bbox_inches="tight")

# display the plot
plt.show()