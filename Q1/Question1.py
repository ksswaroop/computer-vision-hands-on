#Importing the packages
import cv2
import imutils
import numpy as np

#loading the images
img1=cv2.imread("C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q1/dataset/Image1.jpg") #Image 1
img2=cv2.imread("C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q1/dataset/Image2.jpg") #Image 2

# Convert Images from color to Gray scale
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#Find the difference between the two images using absdiff
diff=cv2.absdiff(gray1,gray2)
cv2.imshow("Difference of images",diff)

# cv2.imshow("Original Image",img1)
# cv2.imshow("Edited",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()