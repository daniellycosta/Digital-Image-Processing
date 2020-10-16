import cv2
import numpy as np
import sys

cropBakcground = True

if len(sys.argv) < 2:
    sys.exit("Missing parameters")

path = sys.argv[1]


cap = cv2.VideoCapture(0)


def skip(x):
    pass

alfa_slider_max = 100
center_slider_max = 100
height_slider_max = 100

cv2.namedWindow('image')

cv2.createTrackbar('Alfa','image',0,alfa_slider_max,skip)
cv2.createTrackbar('Center','image',0,center_slider_max,skip)
cv2.createTrackbar('Height','image',0,height_slider_max,skip)
img1 = cv2.imread(cv2.samples.findFile(path))

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

if (img1.shape[0] < frame_width) or (img1.shape[1] < frame_height):
    sys.exit("Background Image is too small")


if cropBakcground:
    img1 = cv2.resize(img1,(frame_width,frame_height))

out = cv2.VideoWriter('outpt.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 24, (frame_width,frame_height))

while True:
    alfa_slider = cv2.getTrackbarPos('Alfa','image')
    center_slider = cv2.getTrackbarPos('Center','image')
    height_slider = cv2.getTrackbarPos('Height','image')
    
    ret, frame = cap.read()

    p1 = (max(0,int((center_slider-height_slider/2.0)/100.0*frame_height)),0)
    p2 = (min(frame_height-1,int((center_slider+height_slider/2.0)/100.0*frame_height)),frame_width-1)

    imgTop = img1.copy()
    imgTop[p1[0]:p2[0],p1[1]:p2[1],:] = frame.copy()[p1[0]:p2[0],p1[1]:p2[1],:]

    alfa = float(float(alfa_slider)/float(alfa_slider_max))
    blended = cv2.addWeighted(img1,alfa,imgTop,1-alfa,0)

    cv2.imshow('image',blended)
    out.write(blended)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
