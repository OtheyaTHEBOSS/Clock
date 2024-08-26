import tkinter as tk

from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import cv2

def play_video():
    cap = cv2.VideoCapture("1.mp4")
    if not cap.isOpened():
        print("Error opening video stream or file")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        img = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=img)
        label.config(image=photo)
        label.image = photo
        root.update()
    cap.release()
    cv2.destroyAllWindows()

root = Tk()
root.title("Video Player")

label = Label(root)
label.pack()

play_button = Button(root, text="Play", command=play_video)
play_button.pack()

root.mainloop()

