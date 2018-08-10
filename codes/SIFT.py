import cv2
import numpy as np

image = cv2.imread('images/input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Feature Method - SIFT', gray)
cv2.waitKey(0)

#Create SIFT Feature Detector object
sift = cv2.xfeatures2d.SIFT_create()

#Detect key points
keypoints = sift.detect(gray, None)
print("Number of keypoints Detected: ", len(keypoints))

# Draw rich key points on input image
gray = cv2.drawKeypoints(image, keypoints, gray)

cv2.imshow('Feature Method - SIFT', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()