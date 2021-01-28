import cv2

path = r'/Users/datmcl/Desktop/learning-basics-opencv/1 - The basics of digitizing images/scream.jpg'
folderPath = r'/Users/datmcl/Desktop/learning-basics-opencv/1 - The basics of digitizing images/Image channels/'
img = cv2.imread(path)

b, g, r = cv2.split(img)

cv2.imwrite(folderPath + 'screamB.jpg', b)
cv2.imwrite(folderPath + 'screamG.jpg', g)
cv2.imwrite(folderPath + 'screamR.jpg', r)
