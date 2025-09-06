import cv2

img=cv2.imread("nature.jpg",1)

print("Original Image Shape:",img.shape)

scale=0.5

width=int(img.shape[1]*scale)
height=int(img.shape[0]*scale)
dim=(width,height)
resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

cv2.imshow("Resized Image", resized)
print("Resized Image Shape:",resized.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()