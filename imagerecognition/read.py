import cv2 as cv
 #reading an image = method imread('')
img = cv.imread("/root/Pictures/446401.jpg")

  #display image as window  parameter name , matrix (img)
cv.imshow('skull', img)

cv.waitKey(0)


# reading a video
capture = cv.VideoCapture('/media/root/Not here5/Downloads/moonknight.mkv')

# loop through the video to capture it frame by frame
while True:

    isTrue, frame = capture.read()  # capture frame by frame
    cv.imshow('video', frame)

    # break out of while loop if letter d is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyWindow()
