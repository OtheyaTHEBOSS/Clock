import cv2
import pyaudio
import wave

cap = cv2.VideoCapture('1.mp4')
wf = wave.open('1.wav', 'rb')

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
               channels=wf.getnchannels(),
               rate=wf.getframerate(),
               output=True)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Video', frame)

        # Read audio data and play it
        data = wf.readframes(1024)
        if data:
            stream.write(data)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
stream.stop_stream()
stream.close()
p.terminate()
cv2.destroyAllWindows()