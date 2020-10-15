import cv2
import sys
import numpy as np

cam = cv2.VideoCapture(0)

if cam is None:
    sys.exit("Could not open webcam")

filters={
    'mean': np.array([[0.1111,0.1111,0.1111],
                   [0.1111,0.1111,0.1111],
                   [0.1111,0.1111,0.1111]], np.float32),

    'gauss': np.array([[.0625,0.125,0.0625],
                   [0.125,0.25,0.125],
                   [0.0625,0.125,0.0625]], np.float32),     

    'sobelVertical' : np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]], np.float32),

    'sobelHorizontal' : np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]], np.float32),

    'laplacian' : np.array([[0,-1,0],
                        [-1,4,-1],
                        [0,-1,0]], np.float32),

    'boost' : np.array([[0,-1,0],
                    [-1,5.2,-1],
                    [0,-1,0]], np.float32),
    
}

choosenMask = 'noMask'
absolute = False
while(1):
    ret, frame = cam.read()
    if frame is None:
        break
    rows,columns,_ = frame.shape

    if choosenMask == 'laplacianGaussian':
        frame = cv2.filter2D(frame, -1, filters['gauss'])
        frame = cv2.filter2D(frame, -1, filters['laplacian'])
    elif choosenMask != 'noMask':
        frame = cv2.filter2D(frame, -1, filters[choosenMask])
    
    
    if absolute:
        frame = cv2.abs(frame)

    cv2.imshow("Video", frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == 'a':
        absolute = not absolute
    elif k == ord('m'):
        choosenMask = 'mean'
        print(filters[choosenMask])
    elif k == ord('g'):
        choosenMask = 'gauss'
        print(filters[choosenMask])
    elif k == ord('h'):
        choosenMask = 'sobelHorizontal'
        print(filters[choosenMask])
    elif k == ord('v'):
        choosenMask = 'sobelVertical'
        print(filters[choosenMask])
    elif k == ord('l'):
        choosenMask = 'laplacian'
        print(filters[choosenMask])
    elif k == ord('b'):
        choosenMask = 'boost'
        print(filters[choosenMask])
    elif k == ord('n'):
        choosenMask = 'noMask'
        print('Original Image')
    elif k == ord('s'):
        choosenMask = 'laplacianGaussian'
        print(filters['gauss'])
        print(filters['laplacian'])
    
        
