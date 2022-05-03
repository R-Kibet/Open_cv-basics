# masking
import  cv2 as cv
import numpy as np
"""

allows on certain parts of image  eg faces

"""

img = cv.imread("/root/Pictures/446401.jpg")
# cv.imshow("skull", img)

rsize = cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize', rsize)

blank = np.zeros(rsize.shape[:2], dtype="uint8")
cv.imshow("blank img", blank)

mask = cv.circle(blank,(rsize.shape[1]//2, rsize.shape[0]//2), 200, 255, -1)
cv.imshow("mask", mask)

masked = cv.bitwise_and(rsize,rsize,mask=mask)
cv.imshow("masked", masked)





cv.waitKey(0)