import tkinter as tk
from tkvideo import tkvideo

root = tk.Tk()

# Create a label to display the video
video_label = tk.Label(root)
video_label.pack(fill=tk.BOTH, expand=True)

# Create a TkVideo player
player = tkvideo.tkvideo("1.mp4", video_label, loop=True)

# Start playing the video
player.play()

root.mainloop()