import cv2

video=cv2.VideoCapture('wow-gif.mp4')

while video.isOpened():
    _,frame=video.read()
    frame=cv2.resize(frame,(800,720))

    cv2.imshow("Video Frame", frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()