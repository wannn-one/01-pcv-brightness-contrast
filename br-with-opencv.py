import cv2
import time
import numpy as np
import os

# create a directory to save the time_taken.txt
if not os.path.exists('brightness'):
    os.makedirs('brightness')

brightness = -120 

start_time = time.time()

img = cv2.imread('itsSurabaya2.jpg',0)

# Menambah kecerahan
img_brightness = cv2.addWeighted(img, 1, np.zeros(img.shape, img.dtype), 0, brightness)

cv2.imshow('image', img)
cv2.imshow('brightness', img_brightness)

time_taken = time.time() - start_time
print("%.4f seconds" % time_taken)

cv2.imwrite('brightness/brightness_with_opencv.jpg', img_brightness)
with open('brightness/time_taken_br_with_opencv.txt', 'a') as f:
    f.write(str(time_taken) + '\n')

cv2.waitKey(0)
cv2.destroyAllWindows()
