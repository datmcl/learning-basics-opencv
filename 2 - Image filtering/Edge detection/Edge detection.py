import cv2
import numpy

path = r'/Users/datmcl/Desktop/learning-basics-opencv/2 - Image filtering/lenna.png'
img = cv2.imread(path)

kernel = numpy.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]]) # edge detection kernel
result = cv2.filter2D(img, -1, kernel)

cv2.imshow('Edge Detection', result)
cv2.waitKey(0)
