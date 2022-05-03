# Histogram computation
"""
allow visualization of pixel intensities in an image whether coloured or gray scale
"""

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("/root/Pictures/446401.jpg")
#cv.imshow("skull", img)

rsize = cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
#cv.imshow('resize', rsize)


gray = cv.cvtColor(rsize,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# gray scale histogram
hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()


# coloured
plt.figure()
plt.title('coloured Histogram')
plt.xlabel('Bins')
plt.ylabel('pixels')

colors = ("b","r","g")
for i ,col in enumerate(colors):
    hist = cv.calcHist([rsize], [i], None , [256],[0,256])
    plt.plot(hist,color= col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)


