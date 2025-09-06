import cv2
import numpy as np

#img=cv2.imread("nature.jpg",cv2.IMREAD_COLOR)

img=np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(150,150),(255,0,0),2)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),3)
cv2.circle(img,(100,63),55,(0,0,255),3)
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],True,(0,255,255),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"OpenCV Tutedude",(0,130),font,1,(200,255,255),2,cv2.LINE_AA)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()