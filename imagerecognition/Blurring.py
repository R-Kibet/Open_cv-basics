# smothing an image - done when image has a lot of noise
# cannel size - size of window
import cv2 as cv

img = cv.imread("/root/Pictures/446401.jpg")
# cv.imshow("skull", img)

rsize = cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize', rsize)


# averaging blur
"""
to get the true centre of a image window
"""

average = cv.blur(rsize, (3,3))
#cv.imshow('average',average)

# gausian blur -  more natural compared to average blur
"""
a certain weight value is added while computing the blur hence becomes less blurry
"""
gaus =  cv.GaussianBlur(rsize,(3,3),0)
#cv.imshow("gaus",gaus)

# medium blur
medium = cv.medianBlur(rsize, 3)
#cv.imshow("medium", medium)

# bilateral blurring - most effective
"""
maintain lower values
"""
bilateral = cv.bilateralFilter(rsize,10,10,10)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)