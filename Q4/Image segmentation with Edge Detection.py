## Image segmentation with Edge detection using Prewitt and Sobel
import cv2 as cv
import numpy as np
img=cv.imread("C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q4/dataset/Image1.jpg")
#Prewitt
kernelx=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely=np.array([[-1,0,-1],[-1,0,1],[-1,0,1]])
prewittx=cv.filter2D(img,-1,kernelx)
prewitty=cv.filter2D(img,-1,kernelx)

#Sobel
sobelx=cv.Sobel(img,cv.CV_64F,1,0)
sobely=cv.Sobel(img,cv.CV_64F,0,1)

#Canny
img_canny=cv.Canny(img,100,200)

#Display Image

cv.imshow('Original Image',img)
# cv.imshow('prewittx',prewittx)
# cv.imshow('prewitty',prewitty)
# cv.imshow('sobelx',sobelx)
# cv.imshow('sobely',sobely)
cv.imshow('Sobel Image',sobelx+sobely)
cv.imshow("Prewitt Image",prewittx+prewitty)
cv.imshow("Canny Image",img_canny)
cv.waitKey(0)


