import cv2
import sys

cam = cv2.VideoCapture(0)

if cam is None:
    sys.exit("Could not open webcam")
 
while(1):
    ret, frame = cam.read()

    if frame is None:
        break

    img_hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
    img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
    cv2.imshow("Video", img)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
