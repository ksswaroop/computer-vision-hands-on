#Import required packages
import cv2 as cv
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
cap=cv.VideoCapture(0)
    #"C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q5/dataset/Anavind_Interview.mp4")
#cv.imshow("Video",vid)
cap.set(3,640) #Width
cap.set(4,480) #Height
bg_img=cv.imread("C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q4/dataset/Image 1.jpg")
seg=SelfiSegmentation()
while True:
    success,video=cap.read()
    vid_rmbg=seg.removeBG(video,bg_img,threshold=0.8)
    cv.imshow("Video",vid_rmbg)
    # if cv.waitKey(1)==ord('x'):
    #     break
cv.waitKey(1)
# Closes all the frames
cv.destroyAllWindows()