import cv2

vid = cv2.VideoCapture("1.mp4")

while(vid.isOpened()):
    ret, frame = vid.read()
    frame = cv2.resize(frame, (1280, 720))
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()