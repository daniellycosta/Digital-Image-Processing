import cv2 as cv
import sys


if len(sys.argv) < 6:
    sys.exit("Missing parameters")

path = sys.argv[1]
p1 = (int(sys.argv[2]), int(sys.argv[3]))
p2 = (int(sys.argv[4]), int(sys.argv[5]))

img = cv.imread(cv.samples.findFile(path), cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image")

rows, columns = img.shape

if p1[0] > rows or p1[1] > columns:
    sys.exit(f"P1 should be inside the picture dimensions ({rows}X{columns})")
if p2[0] > rows or p2[1] > columns:
    sys.exit(f"P2 should be inside the picture dimensions ({rows}X{columns})")

if p1[0] > p2[0]:
    sys.exit(f"P1 x coordinate should be lower than P2 x coordinate")
if p1[1] > p2[1]:
    sys.exit(f"P1 y coordinate should be lower than P2 y coordinate")

cv.imshow("Image - Before", img)

for i in range(p1[0], p2[0]):
    for j in range(p1[1], p2[1]):
        img[i][j] = 1-img[i][j]

cv.imshow("Image - After", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("regions_out.png", img)
