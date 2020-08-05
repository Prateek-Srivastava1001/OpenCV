import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

img[200:300, 100:300] = 255, 0, 0# Blue Color in a specific portion Height from 200-300, width from 100-300

#LINE
#cv2.line(img, (0, 0), (100, 200), (0, 255, 0), 3)#Green line 3 units wide from starting to 100 on x &200 on y

#RECTANGLE
cv2.rectangle(img, (0, 0), (100, 200), (0, 0, 255), cv2.FILLED) #Red Rectangle (Not 3px wide but filled in the middle

#CIRCLE
cv2.circle(img, (400, 100), 100, (255, 225, 100), 2) #Circle(img,center,radius,color,width_of_line)

#TEXT
cv2.putText(img, " OpenCV", (300, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)# putText(img,"Text",(origin Coordinates),cv2.font,scale,(color),thickness)



cv2.imshow("Image", img)
cv2.waitKey(0)