import cv2
import numpy as np

x, y, w, h = 0, 0, 0, 0
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

colorIndex = 1
myPointsB = [] # LIST of x,y, color index
myPointsG = []
myPointsR = []

def empty(a):
    pass


def findcolour(img, colorIndex):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newpoints = []
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
    imgresult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Result", imgresult)
    x, y = getcontours(mask)
    cv2.circle(img, (x, y), 10, (0, 0, 255), 2)

    if x in range(5, 155) and y in range(5, 101):
        myPointsB.clear()
        myPointsG.clear()
        myPointsR.clear()
    if x in range(165, 315) and y in range(5, 101):
        colorIndex = 0
    if x in range(325, 475) and y in range(5, 101):
        colorIndex = 1
    if x in range(485, 635) and y in range(5, 101):
        colorIndex = 2

    if x != 0 and y != 0:
        newpoints.append([x, y])
    return newpoints, colorIndex


def getcontours(img1):
    x, y, w, h = 0, 0, 0, 0
    contours, hierarchy = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:
            #cv2.drawContours(img, cnt, -1, (0, 255, 0), 3) #FOR DRAWING CONTOURSq
            peri = cv2.arcLength(cnt, True)  # GIVES PERIMETER OF EACH CONTOUR
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)  # Corner Point coordinates in the form of a list
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y


  # Creating Settings
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 340)
cv2.createTrackbar("Min Hue", "Trackbars", 98, 179, empty)
cv2.createTrackbar("Max Hue", "Trackbars", 112, 179, empty)
cv2.createTrackbar("Min Sat", "Trackbars", 240, 255, empty)
cv2.createTrackbar("Max Sat", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Min Val", "Trackbars", 128, 255, empty)
cv2.createTrackbar("Max Val", "Trackbars", 255, 255, empty)


#DRAWING
def drawOnCanvas(myPointsB, myPointsG, mypointsR):
    #DRAWING
    for point in myPointsB:
        cv2.circle(img, (point[0], point[1]), 5, (255, 0, 0), cv2.FILLED)
    for point in myPointsG:
        cv2.circle(img, (point[0], point[1]), 5, (0, 255, 0), cv2.FILLED)
    for point in myPointsR:
        cv2.circle(img, (point[0], point[1]), 5, (0, 0, 255), cv2.FILLED)



#LOOP
while True:
    success, img = cap.read()
    newPoints = []
    newPoints, colorIndex = findcolour(img, colorIndex)
    if newPoints:
        for p in newPoints:
            if colorIndex == 0:
                myPointsB.append(p)
            if colorIndex == 1:
                myPointsG.append(p)
            if colorIndex == 2:
                myPointsR.append(p)
    drawOnCanvas(myPointsB, myPointsG, myPointsR)

    # UI
    cv2.rectangle(img, (5, 5), (155, 101), (0, 0, 0), cv2.FILLED)  # CLEAR ALL
    cv2.putText(img, 'CLEAR', (10, 55), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)

    cv2.rectangle(img, (165, 5), (315, 101), (255, 0, 0), cv2.FILLED)  # BLUE
    cv2.putText(img, 'BLUE', (170, 55), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)

    cv2.rectangle(img, (325, 5), (475, 101), (0, 255, 0), cv2.FILLED)  # GREEN
    cv2.putText(img, 'GREEN', (330, 55), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)

    cv2.rectangle(img, (485, 5), (635, 101), (0, 0, 255), cv2.FILLED)  # RED
    cv2.putText(img, 'RED', (490, 55), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)

    cv2.imshow("OUTPUT WINDOW ", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
