# transformation
import cv2 as cv
import numpy as np

img = cv.imread("/root/Pictures/446401.jpg")
cv.imshow("skull", img)


# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, -100, -100)
cv.imshow("Translated", translated)


# rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:  # we are going to assume we rotate at the centre
        rotPoint = (width // 2, height // 2)

        rotMat = cv.getRotationMatrix2D(rotPoint, angle, .75)
        dimensions = (width, height)

        return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 50)
cv.imshow("rotated", rotated)

# resize
rsize = cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize', rsize)

# flipping
flip= cv.flip(rsize,-1) # can be 0,1,-1
cv.imshow('flip', flip)

# cropping
cropped = img[200:400 , 200:400] # array slicing
cv.imshow('cropped', cropped)

cv.waitKey(0)
