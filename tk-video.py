import tkinter as tk
import vlc

root = tk.Tk()

# VLC Setup
instance = vlc.Instance("--no-video")  # Suppress VLC window
player = instance.media_player_new()
media = instance.media_new('1.mp4')  # Replace 'video.mp4' with your file path
player.set_media(media)

# Frame and Label
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)  # Fill available space

label = tk.Label(frame, text="This is text over the video")
label.pack()

# Video Widget
video_widget = tk.Label(frame)
video_widget.pack(fill=tk.BOTH, expand=True)  # Fill remaining space

# Connect VLC to Tkinter Widget
player.set_hwnd(video_widget.winfo_id())

# Start Playing
player.play()

root.mainloop()