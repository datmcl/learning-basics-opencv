import cv2
import math
import numpy as np

path = r'/Users/datmcl/Desktop/learning-basics-opencv/3 - Affine transformations/scream.jpg'
folderPath = r'/Users/datmcl/Desktop/learning-basics-opencv/3 - Affine transformations/Сombination of affine transformations/'
image = cv2.imread(path)

height, width, nChannels = image.shape # getting height & width

resizeM = np.float32([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 1]]).T # transformation matrix of resizing
resizeResult = cv2.warpPerspective(image, resizeM, (width, height))

# Resize & Rotate
rotatePhi = math.pi / 4.0
rotateM = cv2.getRotationMatrix2D((width / 2, height / 2), rotatePhi / math.pi * 180.0, 1.0) # transformation matrix of rotating
rotateResult = cv2.warpAffine(image, rotateM, (width, height))
resizeRotateResult = cv2.warpAffine(resizeResult, rotateM, (width, height))

translateM = np.float32([[1, 0, 0], [0, 1, 0], [width / 2.0, height / 2.0, 1]]).T
translateResult = cv2.warpPerspective(image, translateM, (width, height))

# Translate & Shear
shearM = np.float32([[1, -0.5, 0], [0.2, 1, 0], [0, 0, 1]]).T # transformation matrix of shearing
translateShearResult = cv2.warpPerspective(translateResult, shearM, (width, height))

# Rotate & Scale
scaleM = np.float32([[0.1, 0, 0], [0, 0.2, 0], [0, 0, 1]]).T # transformation matrix of scaling
rotateScaleResult = cv2.warpPerspective(rotateResult, scaleM, (width, height))

# saving
cv2.imwrite(folderPath + 'resize_rotate_result_scream.jpg', resizeRotateResult)
cv2.imwrite(folderPath + 'translate_shear_result_scream.jpg', translateShearResult)
cv2.imwrite(folderPath + 'rotate_scale_result_scream.jpg', rotateScaleResult)

images = cv2.hconcat([resizeRotateResult, translateShearResult, rotateScaleResult]) # merging images

cv2.imshow('Combination of Affine Transformations', images)
cv2.waitKey(0)
cv2.destroyAllWindows()
