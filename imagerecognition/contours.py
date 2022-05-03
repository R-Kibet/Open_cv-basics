# contours - boundaries of objects

import cv2  as cv

img = cv.imread("/root/Pictures/446401.jpg")
cv.imshow("skull", img)

rsize = cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize', rsize)

# convert to grey scal
gray = cv.cvtColor(rsize,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# blurr
blurr =  cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow("Blurr", blurr)

"""
# grab the edges using canny
canny = cv.Canny(blurr,125,175)
cv.imshow("canny", canny)
"""

# Introduce threshold before using canny
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("thresh",thresh)


# finding contours
"""
RETR_LIST - finds all the contours
RETR_EXTERNAL- find external contours
RETR_TREE - Aall hierarchical contours

APPROXIMATION METHODDS
CHAIN_APPROX_NONE - return all contours
CHAIN-APPROX_SIMPLE - compress all contours and return major points eg.line - 2 end points

blurring reduces number of contours
"""
contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contours found")


cv.waitKey(0)
