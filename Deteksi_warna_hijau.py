import cv2
import imutils

#color range
color_low = (29, 86, 6)
color_up = (64, 255, 255)

kamera = cv2.VideoCapture(0)

while True:
    ret, frame = kamera.read()
    frame = imutils.resize(frame, width=600)
    blur = cv2.GaussianBlur(frame, (11,11), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    layer = cv2.inRange(hsv, color_low, color_up)
    cv2.imshow("warna", layer)
    cv2.imshow("asli", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
kamera.release()
cv2.destroyWindow()
