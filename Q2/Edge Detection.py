##Edge Detection using Canny 

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#Reading image

img=cv.imread("C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q4/dataset/Image3.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #Convert image into gray scale
canny=cv.Canny(gray,100,50) #Using Canny Edge Detection technique. 100,200 threshold values.
titles=['image','canny'] # To display tiles for the images displayed
images=[gray,canny] #List of original image and canny image

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i]) #Create 2 subplots one for original image, 2nd for image with edge
    plt.title(titles[i]) 
    plt.xticks([]),plt.yticks([])

plt.show()