# rescaling image to fit window
import cv2 as cv

img = cv.imread("/root/Pictures/446401.jpg")
cv.imshow("Skull", img)


# rescaling takes frame and resizes it to a particular dimension ration
def rescaleFrame(frame, scale=0.75):
    # image , video & live stream
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


resize_img = rescaleFrame(img)
cv.imshow("res", resize_img)


# rescaling live video only
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture('/media/root/Not here5/Downloads/moonknight.mkv')

while True:

    isTrue, frame = capture.read()  # capture frame by frame
    frame_res = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow("vide_res", frame_res)

    # break out of while loop if letter d is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyWindow()
cv.waitKey(0)
