import cv2

cap = cv2.VideoCapture('1.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Video', frame)

        # OpenCV will handle audio playback automatically
        if cv2.waitKey(60) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()