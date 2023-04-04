#Line Detection with HoughLines
#Import the required packages
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#Reading an image 
img= cv.imread("C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q4/dataset/Image3.jpg")
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
# cv.imshow("Lines Detected",img)
# cv.imshow("Canny Detection",caning)
#Hori=np.concatenate((img,caning),axis=1)
#cv.imshow(Hori)
cv.waitKey(0)
cv.destroyAllWindows

titles=['Image','canny'] # To display tiles for the images displayed
images=[img,caning] #List of original image and canny image

for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i]) #Create 2 subplots one for original image, 2nd for image with edge
    plt.title(titles[i]) 
    plt.xticks([]),plt.yticks([])

plt.show()

#Reference : https://codeloop.org/line-detection-in-python-opencv-with-houghlines/