import cv2

path = r'/Users/datmcl/Desktop/learning-basics-opencv/1 - The basics of digitizing images/scream.jpg' # path to image
folderPath = r'/Users/datmcl/Desktop/learning-basics-opencv/1 - The basics of digitizing images/Image channels/' # path to folder

img = cv2.imread(path) # reading image

b, g, r = cv2.split(img) # splitting image to channels R, G, B

# saving
cv2.imwrite(folderPath + 'screamB.jpg', b)
cv2.imwrite(folderPath + 'screamG.jpg', g)
cv2.imwrite(folderPath + 'screamR.jpg', r)
