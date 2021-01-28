import cv2
import math
import numpy as np

path = r'/Users/datmcl/Desktop/learning-basics-opencv/3 - Affine transformations/scream.jpg'
folderPath = r'/Users/datmcl/Desktop/learning-basics-opencv/3 - Affine transformations/Affine transformations/'
image = cv2.imread(path)

height, width, nChannels = image.shape # getting height & width

phi = math.pi / 4.0

M = cv2.getRotationMatrix2D((width / 2, height / 2), phi / math.pi * 180.0, 1.0) # transformation matrix of rotating
rotateResult = cv2.warpAffine(image, M, (width, height))
cv2.imwrite(folderPath + 'rotate_scream.jpg', rotateResult)

M = np.float32([[1, 0, 0], [0, 1, 0], [width / 2.0, height / 2.0, 1]]).T # transformation matrix of translating
translateResult = cv2.warpPerspective(image, M, (width, height))
cv2.imwrite(folderPath + 'translate_scream.jpg', translateResult)

M = np.float32([[0.1, 0, 0], [0, 0.2, 0], [0, 0, 1]]).T # transformation matrix of scaling
scaleResult = cv2.warpPerspective(image, M, (width, height))
cv2.imwrite(folderPath + 'scale_scream.jpg', scaleResult)

images = cv2.hconcat([rotateResult, translateResult, scaleResult]) # merging images

cv2.imshow('Affine Transformations', images)
cv2.waitKey(0)
cv2.destroyAllWindows()
