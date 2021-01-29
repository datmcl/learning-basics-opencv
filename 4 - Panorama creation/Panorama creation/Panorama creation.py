import cv2

path = r'/Users/datmcl/Desktop/learning-basics-opencv/4 - Panorama creation/Panorama creation/'
stitcher = cv2.Stitcher_create() # creating stitcher

images = [cv2.imread(path + '1.jpg'), cv2.imread(path + '2.jpg'), cv2.imread(path + '3.jpg')]

status, stitched = stitcher.stitch(images) # stitching images
panorama = stitched[150:0+1700, 150:0+4150] # cropping panorama

cv2.imwrite(path + 'panorama.jpg', panorama)
cv2.imshow('Panorama', panorama)
cv2.waitKey(0)
cv2.destroyAllWindows()
