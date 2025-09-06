import cv2

video=cv2.VideoCapture(0)

fourcc=cv2.VideoWriter_fourcc(*'mp4v')
output=cv2.VideoWriter('output.mp4',fourcc,25.0,(640,480))

while video.isOpened():
    ret,frame= video.read()
    if ret:
        output.write(frame)
        cv2.imshow("Video Frame", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

video.release()
output.release()
cv2.destroyAllWindows()