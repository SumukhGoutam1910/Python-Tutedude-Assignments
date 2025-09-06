import cv2
img=cv2.imread("nature.jpg",1)

resize=cv2.resize(img,(400,200))

ksize=(7,7)
sigmax=0
sigmay=0

blurred=cv2.GaussianBlur(resize,ksize,sigmax)

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resize)
cv2.imshow("Blurred Image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()