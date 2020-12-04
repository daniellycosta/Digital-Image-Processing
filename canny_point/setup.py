import cv2 as cv
import numpy as np
import sys
import random

STEP = 5
JITTER = 3
RADIUS = 3
CANNY_RADIUS = 2

T1 = 30

if len(sys.argv) < 2:
    sys.exit("Missing parameters")

path = sys.argv[1]

image = cv.imread(cv.samples.findFile(path), cv.IMREAD_GRAYSCALE)
rows, columns = image.shape

cv.imshow('Original Image',image) 

xrange = [i*STEP+STEP/2 for i in range(int(rows/STEP))]
yrange= [i*STEP+STEP/2 for i in range(int(columns/STEP))]

points = np.zeros((rows,columns), np.uint8)
points[:,:] = 255

np.random.shuffle(xrange)

for i in xrange:
    np.random.shuffle(yrange)
    for j in yrange:
        x = int(i + random.randint(1, 2*JITTER)-JITTER)
        y = int(j + random.randint(1, 2*JITTER)-JITTER)

        x = min(rows-1, x)
        y = min(columns-1, y)

        x = max(0, x)
        y = max(0, y)

        gray = image[x,y]

        cv.circle(
            points,
            (y, x),
            RADIUS,
            int(gray),
            -1,
            cv.LINE_AA
        )

cv.imshow("Pointillism", points)
cv.imwrite("point.jpg", points)

edges = cv.Canny(image, T1, 3*T1) 

cv.imshow('Canny',edges) 
cv.imwrite("canny.jpg", edges)

for i in range(rows):
    for j in range(columns):
        if(edges[i, j] != 0):
            gray = image[i,j]
            cv.circle(points,
                    (j, i),
                    CANNY_RADIUS,
                    int(gray),
                    -1,
                    cv.LINE_AA)

cv.imshow("Final Image", points)
cv.imwrite("canny_point.jpg", points)
cv.waitKey(0)     
cv.destroyAllWindows()