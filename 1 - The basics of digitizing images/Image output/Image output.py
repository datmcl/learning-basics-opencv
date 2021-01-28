import cv2

path = r'/Users/datmcl/Desktop/learning-basics-opencv/1 - The basics of digitizing images/scream.jpg'
img = cv2.imread(path)

print(f'Number of pixels: {str(img.size)}')
print(f'Number of pixels: {str(img.shape)}')

cv2.imshow('My Image', img)
cv2.waitKey(0)
