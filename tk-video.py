import tkinter as tk
import vlc

root = tk.Tk()
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new('1.mp4')
player.set_media(media)

video_widget = tk.Label(frame)
video_widget.pack(fill=tk.BOTH, expand=True)

player.set_hwnd(video_widget.winfo_id())

player.play()

#text_label = tk.Label(frame, text="This is text over the video")
#text_label.pack()

root.mainloop()