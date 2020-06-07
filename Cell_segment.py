import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure, color, io

img = cv2.imread("Osteosarcoma_01.tif")
cv2.imshow('REAL',img)


cells=img[:,:,0]  #Blue channel. Image equivalent to grey image.


ret1, thresh = cv2.threshold(cells, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
cv2.imwrite('opening.jpg',opening)
from skimage.segmentation import clear_border
opening = clear_border(opening)



sure_bg = cv2.dilate(opening,kernel,iterations=10)


dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)


ret2, sure_fg = cv2.threshold(dist_transform,0.5*dist_transform.max(),255,0)


sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)


ret3, markers = cv2.connectedComponents(sure_fg)

#The entire background pixels is given value 0.
#This means watershed considers this region as unknown.
#So let us add 10 to all labels so that sure background is not 0, but 10
markers = markers+10

#Marked the region of unknown with zero
markers[unknown==255] = 0
plt.imshow(markers, cmap='jet')   #Look at the 3 distinct regions.

plt.imsave('Markers.jpg',markers)
#Now we are ready for watershed filling. 
markers = cv2.watershed(img,markers)


img[markers == -1] = [0,255,255]  

img2 = color.label2rgb(markers, bg_label=0)

cv2.imshow('RESULT',img)
cv2.imwrite('res.jpg',img)

