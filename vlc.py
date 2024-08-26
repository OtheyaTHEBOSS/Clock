import vlc

# Create a VLC instance
instance = vlc.Instance()

# Create a media player
player = instance.media_player_new()

# Create a media object
media = instance.media_new('1.mp4')

# Set the media on the player
player.set_media(media)

# Play the media
player.play()

# Wait for the user to press a key to stop
input("Press key to stop")

# Stop the player
player.stop()