import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
## TRACKBARS
def empty(a):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 340)
cv2.createTrackbar("Min Hue", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Max Hue", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Min Sat", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Max Sat", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Min Val", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Max Val", "Trackbars", 255, 255, empty)

#INITIAL FRAME
while True:
    cv2.waitKey(1000)
    success, img_init = cap.read()
    if success:
        break

#ALL OTHER FRAMES
while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # GETTING TRACKBAR POSITIONS
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
    mask_inv = 255-mask
    # OTHER THAN BLANKET
    frame = cv2.bitwise_and(img, img, mask=mask_inv)

    blanket = cv2.bitwise_and(img_init, img_init, mask=mask)

    output = cv2.bitwise_or(frame, blanket)

    cv2.imshow("INPUT", img)
    cv2.imshow(" OUTPUT", output)
    cv2.imshow("MASK", mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # To Exit on pressing q
        break
# IMPORTANT STEPS
cap.release()
cv2.destroyAllWindows()