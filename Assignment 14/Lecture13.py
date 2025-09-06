import cv2
import numpy as np

img=cv2.imread("nature.jpg")

column=img.shape[1]
row=img.shape[0]

s=np.float32([(1,0,100),(0,1,50)])
shifted=cv2.warpAffine(img,s,(column,row))

cv2.imshow("Original Image", img)
cv2.imshow("Shifted Image", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()