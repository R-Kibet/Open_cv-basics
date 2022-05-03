# colour channels
import  cv2 as cv
import numpy as np

img = cv.imread("/root/Pictures/446401.jpg")
cv.imshow("skull", img)

rsize = cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize', rsize)

blank = np.zeros(rsize.shape[:2], dtype="uint8")

b,g,r = cv.split(rsize)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('green', green)
cv.imshow('red',red)

print(rsize.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)
