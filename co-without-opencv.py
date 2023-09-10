import cv2
import numpy as np
import time
import os

if not os.path.exists('contrast'):
    os.makedirs('contrast')

img = cv2.imread('itsSurabaya2.jpg',0)

alpha = 0.3 # koma akan menurunkan kontras, bilangan bulat akan menaikkan kontras

start_time = time.time()

# check if the image grayscale or not
if len(img.shape) > 2:
    h = img.shape[0]  
    l = img.shape[1] 
    c = img.shape[2] 

    img_out = np.zeros((h,l,c), img.dtype)

    for i in range(h):
        for j in range(l):
                for k in range(c):
                    img_out[i, j, k] = np.clip(alpha * img[i, j, k], 0, 255)
else:
    h = img.shape[0] 
    l = img.shape[1]
    
    img_out = np.zeros((h,l), img.dtype)

    for i in range(h):
        for j in range(l):
            img_out[i, j] = np.clip(alpha * img[i, j], 0, 255)

cv2.imshow('image', img)
cv2.imshow('increased / decreased contrast', img_out)

time_taken = time.time() - start_time

# save image
cv2.imwrite('contrast/contrast_without_opencv.jpg', img_out)

print("%.4f seconds" % time_taken)

with open('contrast/time_taken_contrast_without_opencv.txt', 'a') as f:
    f.write(str(time_taken) + '\n')

cv2.waitKey(0)
cv2.destroyAllWindows()