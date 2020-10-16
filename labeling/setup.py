import cv2 as cv
import sys

path = sys.argv[1]

img = cv.imread(cv.samples.findFile(path), cv.IMREAD_GRAYSCALE)

if img is None:
    sys.exit("Could not read the image")

cv.imshow("Image - Before", img)
rows, columns = img.shape

row_limit = int(rows/2)
columns_limit = int(columns/2)

region1 = img[0:row_limit, 0:columns_limit]
region2 = img[0:row_limit, columns_limit:columns]
region3 = img[row_limit:rows, 0:columns_limit]
region4 = img[row_limit:rows, columns_limit:columns]

upper_img = cv.hconcat([region4, region3])
lower_img = cv.hconcat([region2, region1])

out_img = cv.vconcat([upper_img, lower_img])

cv.imshow("Image - After", out_img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("change_regions_out.png", img)
