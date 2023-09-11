# 01-pcv-brightness-contrast

A Task for Image & Video Processing Course, comparing brightness and contrast change with and without OpenCV built-in function 

## Feature

1. Measure time taken for each method to change brightness and contrast
2. Compare the result of each method
3. Compare the time taken for each method

## Prequisites

```
python3
opencv
numpy
```

## Program usage

[br-with-opencv.py](https://github.com/wannn-one/01-pcv-brightness-contrast/blob/main/br-with-opencv.py) file : brightness change with OpenCV using cv2.addWeighted

[br-without-opencv.py](https://github.com/wannn-one/01-pcv-brightness-contrast/blob/main/br-without-opencv.py) file : brightness change without OpenCV, perform manual thresholding with python built-in function

[co-with-opencv.py](https://github.com/wannn-one/01-pcv-brightness-contrast/blob/main/co-with-opencv.py) file : contrast change with OpenCV using cv2.convertScaleAbs

[co-without-opencv.py](https://github.com/wannn-one/01-pcv-brightness-contrast/blob/main/co-without-opencv.py) file : contrast change without OpenCV, perform manual iteration and clipping the edge with np.clip() 

## How to use?

Simply type in your terminal:

```
python3 <the-program-to-use>.py
```