import cv2

img=cv2.imread("nature.jpg",1)

resize=cv2.resize(img,(400,200))

d=7
sigmacolor=100
sigmaspace=100

b=cv2.bilateralFilter(resize,d,sigmacolor,sigmaspace)
cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", resize)
cv2.imshow("Bilateral Filtered Image", b)
cv2.waitKey(0)
cv2.destroyAllWindows()