import cv2
import numpy as np

path = r'/Users/datmcl/Desktop/learning-basics-opencv/2 - Image filtering/lenna.png'
folderPath = r'/Users/datmcl/Desktop/learning-basics-opencv/2 - Image filtering/Custom filter/'
image = cv2.imread(path)

org, font, fontScale, color, thickness = (150,30), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 3 # settings for text

gKernel = np.array([[1., 2., 1.], [2., 4., 2.], [1., 2., 1.]]) / 16 # gaussian blur kernel
eKernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]) # emboss kernel
sKernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) # sharpen kernel
erodeKernel = np.ones((3, 3), np.uint8)

gaussianBlur = cv2.filter2D(image, -1, gKernel)
embossKernel = cv2.filter2D(image, -1, eKernel)
sharpenKernel = cv2.filter2D(image, -1, sKernel)
myKernel = cv2.filter2D(cv2.erode(image, erodeKernel, iterations = 1), -1, sKernel) # custom kernel

# write text over the image
cv2.putText(gaussianBlur, 'Gaussian Blur', org, font, fontScale, color, thickness)
cv2.putText(embossKernel, 'Emboss Kernel', org, font, fontScale, color, thickness)
cv2.putText(sharpenKernel, 'Sharpen Kernel', org, font, fontScale, color, thickness)
cv2.putText(myKernel, 'Custom', org, font, fontScale, color, thickness)

images = cv2.hconcat([gaussianBlur, embossKernel, sharpenKernel, myKernel]) # merging images into one

cv2.imwrite(folderPath + 'result.png', images)
cv2.imshow('Filters', images)
cv2.waitKey(0)
