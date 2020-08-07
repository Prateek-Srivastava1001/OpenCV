import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

width = 640
height = 480

def getContours(img1, imgreal):
    biggest = np.array([])
    maxArea = 0
    contours, hiearchy = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            cv2.drawContours(imgreal, cnt, -1, (0, 0, 255), 3)
            peri = cv2.arcLength(cnt, True) # GIVES PERIMETER OF EACH CONTOUR
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True) # Corner Point coordinates in the form of a list
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

    return biggest


def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgGray, 100, 100)
    kernel = np.ones((5, 5))
    imgDilate = cv2.dilate(imgCanny, kernel, iterations=1)
    imgThresh = cv2.erode(imgDilate, kernel, iterations=1)


    return imgThresh

def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)

    print("ADD", add)
    print("myPoints", myPoints)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew


def getWarp(img, biggest):
    biggest = reorder(biggest)
    print(biggest)
    pts1 = np.float32(biggest)  # Points in the image referring to particular card
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # Points for aspect ratio of cards mapped to the points in image
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    output = cv2.warpPerspective(img, matrix, (width, height))
    cv2.imshow("OUTPUT", output)


while True:
    success, img = cap.read()
    cv2.resize(img, (640, 480)) # To make sure Size remains same
    imgThres = preProcessing(img)
    biggest = getContours(imgThres, img)

    if biggest.any():
        getWarp(img, biggest)

    cv2.imshow("RESULT1", imgThres)
    cv2.imshow("INPUT", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # To Exit on pressing q
        break

# IMPORTANT STEPS
cap.release()
cv2.destroyAllWindows()