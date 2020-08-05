import cv2
import numpy as np

img = cv2.imread("Images/testcv.jpg")
print(img.shape)

width, height = 250, 350
pts1 = np.float32([[600, 79], [772, 98], [830, 288], [625,270]]) # Points in the image referring to particular card
pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]]) # Points for aspect ratio of cards mapped to the points in image
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", output)
cv2.waitKey(0)