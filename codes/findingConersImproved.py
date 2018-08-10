import cv2
import numpy as np

img = cv2.imread('/home/luiz/Documents/Projects/ComputerVision/images/someshapes.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# We specific the top 50 corners
corners = cv2.goodFeaturesToTrack(gray, 4, 0.01, 15)

for corner in corners:
    x, y = corner[0]
    x = int(x)
    y = int(y)
    cv2.rectangle(img,(x-10,y-10),(x+10,y+10),(0,255,0), 2)
    
cv2.imshow("Corners Found", img)
cv2.waitKey()
cv2.destroyAllWindows()