import cv2
import numpy as np
import time
import os

if not os.path.exists('brightness'):
    os.makedirs('brightness')

brightness = -120

start_time = time.time()

img = cv2.imread('itsSurabaya2.jpg',0)

img_brightness = np.double(img)+brightness # 50 is the brightness value, convert to double to prevent overflow
img_brightness[img_brightness>255] = 255 # if the value is more than 255, set it to 255
img_brightness[img_brightness<0] = 0 # if the value is less than 0, set it to 0
# with if else syntax
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         for k in range(img.shape[2]):
#             if img_brightness[i, j, k] > 255:
#                 img_brightness[i, j, k] = 255
#             elif img_brightness[i, j, k] < 0:
#                 img_brightness[i, j, k] = 0
img_brightness = np.uint8(np.floor(img_brightness)) # convert the value to uint8, balikin lagi

time_taken = time.time() - start_time

cv2.imshow('image', img)
cv2.imshow('brightness', img_brightness)

print("%.4f seconds" % time_taken)

cv2.imwrite('brightness/brightness_without_opencv.jpg', img_brightness)
with open('brightness/time_taken_br_without_opencv.txt', 'a') as f:
    f.write(str(time_taken) + '\n')


cv2.waitKey(0)
cv2.destroyAllWindows()