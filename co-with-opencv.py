import cv2
import numpy as np
import time
import os

# create a directory to save the time_taken.txt
if not os.path.exists('contrast'):
    os.makedirs('contrast')

img = cv2.imread('itsSurabaya2.jpg',0)
alpha = 0.3 # koma akan menurunkan kontras, bilangan bulat akan menaikkan kontras

start_time = time.time()
# check if the image grayscale or not
if len(img.shape) > 2:
    # h = img.shape[0]  
    # l = img.shape[1] 
    # c = img.shape[2] 

    img_out = np.zeros(img.shape, img.dtype)

    img_out = cv2.convertScaleAbs(img, alpha=alpha, beta=0)
else:
    # h = img.shape[0] 
    # l = img.shape[1]
    
    img_out = np.zeros(img.shape, img.dtype)

    img_out = cv2.convertScaleAbs(img, alpha=alpha, beta=0)
time_taken = time.time() - start_time

cv2.imshow('image', img)
cv2.imshow('increased / decreased contrast', img_out)

cv2.imwrite('contrast/contrast_with_opencv.jpg', img_out)
print("%.4f seconds" % time_taken)

with open('contrast/time_taken_contrast_with_opencv.txt', 'a') as f:
    f.write(str(time_taken) + '\n')

cv2.waitKey(0)
cv2.destroyAllWindows()