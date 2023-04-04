import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
#vid = cv2.VideoCapture(0)
vid = cv2.VideoCapture("C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q5/dataset/video/Anavind_Interview.mp4")
# ret, videoFrame = vid.read() 
# videoFrame = cv2.resize(videoFrame, (640, 480))

vid.set(3,848) ## Width
vid.set(4,480) ## Height

bg_img=cv2.imread("C:/Users/ksais/OneDrive/Documents/Coding/Computer Vision/computer-vision-hands-on/Q5/dataset/Bgimage_1280.jpg")
#bg_img=cv2.resize(img,(680,480),interpolation = cv2.INTER_LINEAR)

seg=SelfiSegmentation()

while True:
    _,video=vid.read()
    vid_rmbg=seg.removeBG(video,bg_img,threshold=0.8)
    cv2.imshow("Video",vid_rmbg)
    if cv2.waitKey(1)==ord('x'):
        break

