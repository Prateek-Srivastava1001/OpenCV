#importing Paackages
import cv2
import numpy as np
#For Images
img1 =cv2.imread("Images/earth.jpg")
cv2.imshow("Image", img1)
cv2.waitKey(0) #To hold img screen

#For Video
kernel = np.ones((5,5),np.uint8) #For dilation, we need kernel
#Initializing webcam
cap = cv2.VideoCapture(0) #we can add path for a specified video file, 0 is for webcam
#Initail settings for webcam
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    imgcanny = cv2.Canny(img, 100, 100)# ----------To find edges in image---------
    imgblur=cv2.GaussianBlur(img, (7, 7), 0) #To Blur
    imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Gray Image
    imgdilation= cv2.dilate(imgcanny,kernel,iterations=1)  #DIlate
    imgeroded= cv2.erode(imgdilation,kernel,iterations=1)  #Opposite of dilate
#Show Boundary
    cv2.imshow("Boundary", imgcanny)
    #Show video
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'): #To Exit on pressing q
        break
#IMPORTANT STEPS
cap.release()
cv2.destroyAllWindows()
