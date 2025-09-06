import cv2

img=cv2.imread("nature.jpg",1)
row=img.shape[1]
column=img.shape[0]

center=(column/2,row/2)
angle=90
r=cv2.getRotationMatrix2D(center,angle,1)
rotated=cv2.warpAffine(img,r,(column,row))

cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()