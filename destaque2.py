import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('anya.jpg',0)
edges = cv.Canny(img,100,200)

fig, ax = plt.subplots(ncols=2,figsize=(15,5))
ax[0].imshow(img,cmap = 'gray')
ax[0].set_title('Original Image') 
ax[0].axis('off')
ax[1].imshow(edges,cmap = 'gray')
ax[1].set_title('Edge Image')
ax[1].axis('off')
plt.show()

kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(edges,kernel,iterations = 1)
fig, ax = plt.subplots(ncols=2,figsize=(15,5))
ax[0].imshow(edges,cmap = 'gray')
ax[0].set_title('Original Edge') 
ax[0].axis('off')
ax[1].imshow(dilation,cmap = 'gray')
ax[1].set_title('Dilated')
plt.axis('off')
plt.show()