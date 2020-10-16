import cv2
import sys
import numpy as np

cam = cv2.VideoCapture(0)

tolerance = float(sys.argv[1])

if tolerance is None:
    tolerance = 0.10

if cam is None:
    sys.exit("Could not open webcam")

ret, frame = cam.read()
if frame is None:
    sys.exit("Could not open webcam")

oldHist = cv2.calcHist([frame], [0], None, [256], [0, 256])

while(1):
    ret, frame = cam.read()
    if frame is None:
        break

    hist = cv2.calcHist([frame], [0], None, [256], [0, 256])
    histDiff = oldHist - hist
    rows, columns, _ = frame.shape
    if np.sum(np.abs(histDiff))/(columns*rows) > tolerance:
        cv2.rectangle(frame, (0, 0), (columns-1, rows-1), (0, 0, 255), 10)

    cv2.imshow("Video", frame)

    oldHist = hist
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
