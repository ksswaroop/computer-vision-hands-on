#Line Detection with HoughLines
#Import the required packages
import cv2 as cv
import numpy as np

#Reading an image 
img= cv.imread("C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q2/dataset/Image.png")
#Converting image into gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Finding the edges of image using Canny
caning=cv.Canny(gray,50,200)

#Detecting the lines in the image

lines=cv.HoughLines(caning,1,np.pi/180,120,np.array([]))

print(lines)
#Drawing the detected lines on the original image
for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho
    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv.imshow("Lines Detected",img)
cv.imshow("Canny Detection",caning)
cv.waitKey(0)
cv.destroyAllWindows