# Edge Detection
import cv2 as cv
import numpy as np


img = cv.imread("/root/Pictures/446401.jpg")
#cv.imshow("skull", img)

rsize = cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
#cv.imshow('resize', rsize)


gray = cv.cvtColor(rsize,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# laplacian - looks more of a pencil shading on the edges
lap = cv.Laplacian(gray,-1)
lap = np.uint8(np.absolute(lap))
cv.imshow("lap", lap)

# sobel - compute gradient in x and y direction
sobelx = cv.Sobel(gray, -1 , 1,0)
sobely = cv.Sobel(gray,-1,0,1)
combine = cv.bitwise_or(sobelx,sobely)



cv.imshow("sobel x",sobelx)
cv.imshow('sobel y', sobely)
cv.imshow("combine", combine)

# multistage process eg here t uses sobel as one of the stage
canny = cv.Canny(gray,150,175)
cv.imshow("canny", canny)


cv.waitKey(0)
