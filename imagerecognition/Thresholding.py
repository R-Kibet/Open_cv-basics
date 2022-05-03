# Thresholding
import cv2 as cv

img = cv.imread("/root/Pictures/446401.jpg")
#cv.imshow("skull", img)

rsize = cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
# cv.imshow('resize', rsize)


gray = cv.cvtColor(rsize,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# simple thresholding
threshold , thresh = cv.threshold(gray,200,255, cv.THRESH_BINARY)
cv.imshow("Simple",thresh)

threshold , thresh_inv = cv.threshold(gray,150,255, cv.THRESH_BINARY_INV)
cv.imshow("Simp",thresh_inv)

# adaptive thresh holding
adaptive =  cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("adaptive", adaptive)


cv.waitKey(0)
