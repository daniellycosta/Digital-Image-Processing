import cv2
import sys

path = sys.argv[1]

img = cv2.imread(cv2.samples.findFile(path), cv2.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image")

cv2.imshow("Image - Before", img)
rows, columns = img.shape

# cleaning borders
for i in range(columns):
    cv2.floodFill(img, None, (i, rows-1), 0)
    cv2.floodFill(img, None, (i, 0), 0)

for j in range(rows):
    cv2.floodFill(img, None, (columns-1, j), 0)
    cv2.floodFill(img, None, (0, j), 0)

cv2.imshow('Image - Border cleaning', img)
cv2.imwrite("Image - Border cleaning.png", img)

# counting all objects after removing those touching the borders
noObjects = 0
for i in range(columns):
    for j in range(rows):
        if img[i, j] == 255:
            shade = 1 + (noObjects % 254)
            cv2.floodFill(img, None, (j, i), shade)
            noObjects += 1


cv2.imshow('Image - Labeling', img)
cv2.imwrite("Image - Labeling.png", img)
print(f'We found {noObjects} objects in the picture')

# inverting background so we can safely say that we found a hole when we find a black spot
cv2.floodFill(img, None, (0, 0), 255)
cv2.imshow('Image - Inverting', img)
cv2.imwrite("Image - Inverting.png", img)

# counting number of objects with a hole
noHollowObjecs = 0
for i in range(columns):
    for j in range(rows):
        if img[i, j] == 0:
            cv2.floodFill(img, None, (j, i), 255)
            # tests to see if hole is in anew object that has not been flooded yet
            for difI in [-1, 0, 1]:
                for difJ in [-1, 0, 1]:
                    if img[i-difI, j-difJ] != 255:
                        cv2.floodFill(img, None, (j-difJ, i-difI), 255)
                        noHollowObjecs += 1

print(f'There were {noHollowObjecs} objects with holes in the picture')
print(
    f'There were {noObjects - noHollowObjecs} objects with no holes in the picture')

cv2.imshow("Image - After", img)
cv2.imwrite("Image - After.png", img)
cv2.waitKey(0)
