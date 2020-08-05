import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

def getContours(img1, imgreal):
    contours, hiearchy = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>10:
            cv2.drawContours(imgreal, cnt, -1, (0, 0, 255), 3)
            peri = cv2.arcLength(cnt, True) # GIVES PERIMETER OF EACH CONTOUR
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) # Corner Point coordinates in the form of a list
            corpoints = len(approx) # Number Of corner Points
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgreal, (x, y), (x+w, y+h), (0, 255, 0), 4)  # To Draw a rectangle by using corner points
            if corpoints == 4:   # To Show If The Shape Is Rectangle Or Not
                objtype = "Rectangle"
                cv2.putText(imgreal, objtype, (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.5, (255, 0, 0), 2)

while True:
    success, img = cap.read()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imgray, (11, 11), 1)
    imgcanny = cv2.Canny(imgblur, 50, 50)
    getContours(imgcanny, img)

    cv2.imshow("Boundaries", imgcanny)
    cv2.imshow("Contoured_Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # To Exit on pressing q
        break
cap.release()
cv2.destroyAllWindows()