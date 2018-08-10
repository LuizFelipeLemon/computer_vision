import cv2
import numpy as np

# Function we'll use to display contour area

def get_contour_areas(contours):
    # returns the areas of all contours as list
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

def x_cord_contour(contours):
    #Returns the X cordinate for the contour centroid
    if cv2.contourArea(contours) > 10:
        M = cv2.moments(contours)
        return (int(M['m10']/M['m00']))
    else:
        pass

    
def label_contour_center(image, c):
    # Places a red circle on the centers of contours
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
 
    # Draw the countour number on the image
    cv2.circle(image,(cx,cy), 10, (255,125,120), -1)
    return image

# Load our image
image = cv2.imread('images/bunchofshapes.jpg')
cv2.imshow('0 - Original Image', image)
cv2.waitKey(0)

# Create a black image with same dimensions as our loaded image
blank_image = np.zeros((image.shape[0], image.shape[1], 3))

# Create a copy of our original image
orginal_image = image

# Grayscale our image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# Find Canny edges      
edged = cv2.Canny(gray, 50, 200)
""" cv2.imshow('1 - Canny Edges', edged)
cv2.waitKey(0) """

# Find contours and print how many were found
im2,contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print ("Number of contours found = ", len(contours))

# Let's print the areas of the contours before sorting
print "Contor Areas before sorting"
all_areas = get_contour_areas(contours)
print all_areas

# Sort contours large to small
sorted_contours = sorted(contours, key=get_contour_areas, reverse=True)
#sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:3]

print "Contor Areas after sorting" 
print get_contour_areas(sorted_contours)

print x_cord_contour(sorted_contours[0])


# Draw all contours over blank image
for i in sorted_contours:
    cv2.drawContours(image, [i], -1, (0,0,255), 5)
    label_contour_center(image, i)
    cv2.imshow('3 - All Contours', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()