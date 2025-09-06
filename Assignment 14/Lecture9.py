import cv2

img=cv2.imread("nature.jpg")

width=400
height=200
dim=(width,height)
resized=cv2.resize(img,dim)

cv2.imshow("Original", resized)
print("Image size in bytes:", resized.size)

hflip=cv2.flip(resized,1)
cv2.imshow("Horizontal Flip", hflip)

vflip=cv2.flip(resized,0)
cv2.imshow("Vertical Flip", vflip)

dflip=cv2.flip(resized,-1)
cv2.imshow("Diagonal Flip", dflip)

cv2.waitKey(0)
cv2.destroyAllWindows()