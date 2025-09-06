import cv2

img=cv2.imread("nature.jpg",1)

print(img.shape)

width=img.shape[1]
height=200
dim=(width,height)
resized=cv2.resize(img,dim)

print(resized.shape)

cv2.imshow("Nature", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()