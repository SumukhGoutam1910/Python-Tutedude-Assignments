import cv2
import numpy as np

img=cv2.imread("nature.jpg",1)
resize=cv2.resize(img,(400,200))

min_thresh=100
max_thresh=200

edges=cv2.Canny(resize,min_thresh,max_thresh)

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resize)
cv2.imshow("Edge Detected Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()