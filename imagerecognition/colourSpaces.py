# colour spaces - switch between colour spaces
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("/root/Pictures/446401.jpg")
#cv.imshow("skull", img)

rsize = cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
#cv.imshow('resize', rsize)

# convert to grey scal
gray = cv.cvtColor(rsize,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# BGR to HSV
hsv = cv.cvtColor(rsize,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

# BGR to LAB
lab = cv.cvtColor(rsize, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(rsize, cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)




cv.waitKey(0)