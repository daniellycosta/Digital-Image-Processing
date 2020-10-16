import cv2
import numpy as np
import sys


if len(sys.argv) < 3:
    sys.exit("Missing parameters")

path1 = sys.argv[1]
path2 = sys.argv[2]


def skip(x):
    pass

alfa_slider_max = 100
center_slider_max = 100
height_slider_max = 100

cv2.namedWindow('image')

cv2.createTrackbar('Alfa','image',0,alfa_slider_max,skip)
cv2.createTrackbar('Center','image',0,center_slider_max,skip)
cv2.createTrackbar('Height','image',0,height_slider_max,skip)

img1 = cv2.imread(cv2.samples.findFile(path1))
img2 = cv2.imread(cv2.samples.findFile(path2))

rows,columns,_ = img1.shape

while True:
    alfa_slider = cv2.getTrackbarPos('Alfa','image')
    center_slider = cv2.getTrackbarPos('Center','image')
    height_slider = cv2.getTrackbarPos('Height','image')

    p1 = (max(0,int((center_slider-height_slider)/100.0*columns)),0)
    p2 = (min(columns-1,int((center_slider+height_slider)/100.0*columns)),rows-1)

    imgTop = img1.copy()
    imgTop[p1[0]:p2[0],p1[1]:p2[1],:] = img2.copy()[p1[0]:p2[0],p1[1]:p2[1],:]

    alfa = float(float(alfa_slider)/float(alfa_slider_max))
    blended = cv2.addWeighted(img1,alfa,imgTop,1-alfa,0)

    cv2.imshow('image',blended)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.imwrite('output.png',blended)
