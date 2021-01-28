import cv2

path = r'/Users/datmcl/Desktop/learning-basics-opencv/1 - The basics of digitizing images/scream.jpg'
img = cv2.imread(path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow('My Image', img)
cv2.waitKey(0)
