import cv2

img=cv2.imread("nature.jpg",1)

resized=cv2.resize(img,(400,200))

kernel=3

blurred=cv2.medianBlur(resized,kernel)
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resized)  
cv2.imshow("Blurred Image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()