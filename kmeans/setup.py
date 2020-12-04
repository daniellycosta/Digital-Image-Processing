import cv2 as cv
import numpy as np
import sys


if len(sys.argv) < 5:
    sys.exit("Missing parameters")

path = sys.argv[1]
saving_path = sys.argv[2]
n_attempts = int(sys.argv[3])
n_clusters = int(sys.argv[4])

img = cv.imread(cv.samples.findFile(path))

if img is None:
    sys.exit("Could not read the image")

# cv.imshow("Image - Before", img)

for i in range(10):
    samples = img.reshape((-1,3))
    samples = np.float32(samples)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10000, 0.0001)

    ret,label,center=cv.kmeans(samples,n_clusters,None,criteria,n_attempts,cv.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    flattened = center[label.flatten()]
    reshaped = flattened.reshape((img.shape))

# cv.imshow("Image - After", res2)
# k = cv.waitKey(0)

# if k == ord("s"):
    cv.imwrite(f'images/{i}.jpg', reshaped)
