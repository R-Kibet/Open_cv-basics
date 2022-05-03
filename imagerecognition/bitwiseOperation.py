# bitwise operator
import cv2 as cv
import numpy as np

"""
AND , OR , XOR & NOT
 Operate on a binary manner pixel is turned of when it has a value OFF = 0 and ON =1
"""

blank = np.zeros((600,600) , dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (115,115), (400,400), 255, -1)
circle = cv.circle(blank.copy(), (300,300), 200 , 255, -1)

#cv.imshow("Rectangle", rectangle)
#cv.imshow("circle", circle)

# AND - intersecting region
bitwise_and = cv.bitwise_and(circle,rectangle)
cv.imshow('btw_and' , bitwise_and)

# OR - intersecting and non intersecting regions
bitwise_or = cv.bitwise_or(circle,rectangle)
cv.imshow('btw_or' , bitwise_or)

# XOR- Non intersecting region
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('btw_xor', bitwise_xor)

# NOT - inverts binary
bitwise_NOT = cv.bitwise_not(circle,rectangle)
cv.imshow('btw_not' , bitwise_NOT)

cv.waitKey(0)