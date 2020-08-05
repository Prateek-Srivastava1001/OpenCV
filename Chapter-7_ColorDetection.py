import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

def empty(a):
    pass
#Creating Settings
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 340)
cv2.createTrackbar("Min Hue", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Max Hue", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Min Sat", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Max Sat", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Min Val", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Max Val", "Trackbars", 255, 255, empty)

#LOOP
while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #GETTING TRACKBAR POSITIONS
    h_min = cv2.getTrackbarPos("Min Hue", "Trackbars")
    h_max = cv2.getTrackbarPos("Max Hue", "Trackbars")
    s_min = cv2.getTrackbarPos("Min Sat", "Trackbars")
    s_max = cv2.getTrackbarPos("Max Sat", "Trackbars")
    v_min = cv2.getTrackbarPos("Min Val", "Trackbars")
    v_max = cv2.getTrackbarPos("Max Val", "Trackbars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # Creating mask
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("HSV Space", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Output", imgResult)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()