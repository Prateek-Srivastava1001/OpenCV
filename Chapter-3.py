import cv2
import numpy as np

img = cv2.imread("Images/earth.jpg")

imgresize = cv2.resize(img, (1000, 500)) #RESIZE
print(img.shape) #For dimensions of image

imgcropped = img[0:200,200:500] #CROPPED

cv2.imshow("Real", img)
cv2.imshow("resized", imgresize)
cv2.imshow("Cropped",imgcropped)

cv2.waitKey(0)