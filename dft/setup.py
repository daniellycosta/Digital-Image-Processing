import cv2
import numpy as np
import copy
import sys

def moveDFT(image):
    rows, columns,_ = image.shape
    img = image[0:columns & -2, 0:rows & -2]

    rows_cropped,columns_croped,_ = img.shape
    
    row_limit = int(rows_cropped/2)
    columns_limit = int(columns_croped/2)

    A = img[0:row_limit, 0:columns_limit]
    B = img[0:row_limit, columns_limit:columns]
    C = img[row_limit:rows, 0:columns_limit]
    D = img[row_limit:rows, columns_limit:columns]

    upper_img = cv2.hconcat([D, C])
    lower_img = cv2.hconcat([B, A])

    out_img = cv2.vconcat([upper_img, lower_img])
    return out_img

def menu():
    print(  "e : habilita/desabilita interferencia\n"
        "m : habilita/desabilita o filtro mediano\n"
        "g : habilita/desabilita o filtro gaussiano\n"
        "p : realiza uma amostra das imagens\n"
        "s : habilita/desabilita subtraÃ§Ã£o de fundo\n"
        "b : realiza uma amostra do fundo da cena\n"
        "n : processa o negativo\n")
    
def on_trackbar_frequency(freq,freq_max):
    return

def on_trackbar_noise_gain(gain, gain_max):
    return


radius = 20
cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

if cam is None:
    sys.exit("Could not open webcam")
_,frame = cam.read()
image = copy.copy(frame)

rows,columns,_ = image.shape

dft_M = cv2.getOptimalDFTSize(rows)
dft_N = cv2.getOptimalDFTSize(columns)

freq_max = int(dft_M / 2 - 1)

noise = True
mean = 0

freq = 10


gain_int = 0
gain_max = 100
gain = 0

median = False
gaussian = False
negative = False

sample = False
background= False
subtract = False

cv2.namedWindow("original",1)
cv2.createTrackbar("frequencia", "original", freq, freq_max,on_trackbar_frequency)
on_trackbar_frequency(freq,0)

cv2.createTrackbar("amp. ruido", "original", gain_int, gain_max,on_trackbar_noise_gain)
on_trackbar_noise_gain(gain_int, 0)

padded = cv2.copyMakeBorder(image, 0, dft_M - rows, 0,dft_N - columns, cv2.BORDER_CONSTANT)
padded_rows,padded_columns,_= padded.shape

complex_image = np.zeros((padded_rows,padded_columns),np.float32)
freq_filter = copy.copy(complex_image)
tmp = np.zeros((dft_M,dft_M),np.float32)


menu()

imagegray = None
backgroundImage=None
while(1):
    ret, frame = cam.read()
    if frame is None:
        break
    image = cam
    cv2.cvtColor(image,imagegray,cv2.COLOR_BGR2GRAY)
    if background == True:
        imagegray = copy.copy(backgroundImage)
        background = False
    
    if subtract:
        imagegray = cv2.max(imagegray - backgroundImage, 0)
    
    if negative:
        imagegray = not imagegray
    
    if median:
        cv2.medianBlur(imagegray, image, 3)
        image = copy.copy(imagegray)
    
    if gaussian:
        cv2.GaussianBlur(imagegray, image,(3, 3), 0)
        image=copy.copy(imagegray)
    


    cv2.imshow("Video", frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k==ord('e'):
       noise = not noise
    elif k == ord('m'):
        median = not median 
    elif k == ord('g'):
        gaussian = not gaussian
    elif k == ord('p'):
        sample = True 
    elif k == ord('s'):
        subtract = True
    elif k == ord('b'):
        background = True
    elif k == ord('n'):
        negative = not negative




