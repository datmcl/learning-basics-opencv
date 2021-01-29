import cv2

image_left = cv2.imread(r'/Users/datmcl/Desktop/learning-basics-opencv/5 - Stereo image. Building depth map/Depth map/cube_l.jpg')
image_left = cv2.cvtColor(image_left, cv2.COLOR_BGR2GRAY) # converting image into gray
image_right = cv2.imread(r'/Users/datmcl/Desktop/learning-basics-opencv/5 - Stereo image. Building depth map/Depth map/cube_r.jpg')
image_right = cv2.cvtColor(image_right, cv2.COLOR_BGR2GRAY) # converting image into gray

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity_map = stereo.compute(image_left, image_right)

cv2.imwrite(r'/Users/datmcl/Desktop/learning-basics-opencv/5 - Stereo image. Building depth map/Depth map/cuberesult.jpg', disparity_map)
cv2.imshow('Stereo Image', disparity_map)
cv2.waitKey(0)
