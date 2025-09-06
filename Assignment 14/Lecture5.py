import cv2

img=cv2.imread("nature.jpg",0)

cv2.imwrite("nature_grayscale.jpg", img)

cv2.imshow("Nature", img)
cv2.waitKey(0)
cv2.destroyAllWindows()