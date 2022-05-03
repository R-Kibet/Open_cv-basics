# drawing shapes and putting context
import cv2 as cv
import numpy as np

img = cv.imread("/root/Pictures/446401.jpg")
cv.imshow("skull", img)

#show lank image
blank = np.zeros((500,500,3), dtype="uint8")
# 500,500,3 = height ,width and number of colour channels
cv.imshow('Blank',blank)

"""
# paint image a certain colour
# blank[:] refers to all the pixels
blank[100:200, 200:300] = 120,120,90
cv.imshow('new', blank)
"""

# draw a retangle
cv.rectangle(blank,(0,0),(blank.shape[1] // 2, blank.shape[0]//2),(250,0,0),thickness=-1)
cv.imshow("rectangle", blank)

# draw a circle
cv.circle(blank,(blank.shape[1] // 2, blank.shape[0]//2),40,(250,0,0),thickness=1)
cv.imshow("circle", blank)

cv.putText(blank,"hello",(0,255), cv.FONT_HERSHEY_TRIPLEX,1,(0,100,250),2)
cv.imshow("Text", blank)

cv.waitKey(0)