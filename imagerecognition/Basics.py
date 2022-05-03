# basic function of open cv
import cv2 as cv

img = cv.imread("/root/Pictures/446401.jpg")
cv.imshow("skull", img)

# convert to gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blurring
blur =  cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# Edge Cascade
canny = cv.Canny(blur, 125,175)
cv.imshow("canny", canny)

# dilating the image
dilated = cv.dilate(canny,(7,7), iterations=4)
cv.imshow("dilate", dilated)

# eoding an image
eroded = cv.erode(dilated, (7,7), iterations =4)
cv.imshow("Eroded", eroded)

# resize
resize = cv.resize(img, (900,900), interpolation=cv.INTER_AREA)
cv.imshow("Resize", resize)

# croping
croppes = img[70:250, 250:330]
cv.imshow("cropped", croppes)

cv.waitKey(0)
