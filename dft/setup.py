import cv2
import numpy as np
import copy
import sys

def applyHomomorphicFilter():
    return

def menu():
    print("h : habilita/desabilita filtro homomorfico\n")
    
def on_trackbar_frequency(freq,freq_max):
    return

def on_trackbar_noise_gain(gain, gain_max):
    return


cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

if cam is None:
    sys.exit("Could not open webcam")

_,frame = cam.read()
image = copy.copy(frame)

columns,rows,_ = image.shape

dft_M = cv2.getOptimalDFTSize(rows)
dft_N = cv2.getOptimalDFTSize(columns)

homomorphic = False

cv2.namedWindow("original",1)
#cv2.createTrackbar("frequencia", "original", freq, freq_max,on_trackbar_frequency)
#on_trackbar_frequency(freq,0)

#cv2.createTrackbar("amp. ruido", "original", gain_int, gain_max,on_trackbar_noise_gain)
#on_trackbar_noise_gain(gain_int, 0)

menu()

backgroundImage=None
while(1):
    ret, frame = cam.read()
    if frame is None:
        break
    image = frame
    rows,columns,_ = image.shape
    imagegray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    padded = cv2.copyMakeBorder(imagegray, 0, dft_M - columns, 0, dft_N - rows, cv2.BORDER_CONSTANT, 0)
    
    dft = cv2.dft(np.float32(imagegray)/255.0,flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

    cv2.namedWindow('DFT', 1)
    cv2.imshow("DFT", magnitude_spectrum)
    #cv2.imwrite( "dft.jpg", np.uint8(img))
    #cv2.resizeWindow("DFT", 250, 250)

    cv2.imshow("original", imagegray)

    if homomorphic:
        applyHomomorphicFilter()

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('h'):
        homomorphic = not homomorphic




