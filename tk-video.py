import tkinter as tk
import vlc

root = tk.Tk()

# VLC Setup
instance = vlc.Instance("--no-video")
player = instance.media_player_new()
media = instance.media_new('1.mp4')  # Replace 'video.mp4' with your file path
player.set_media(media)

# Frame and Video Widget
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

video_widget = tk.Label(frame)
video_widget.pack(fill=tk.BOTH, expand=True)

# Connect VLC to Tkinter Widget
player.set_hwnd(video_widget.winfo_id())

# Start Playing
player.play()

root.mainloop()