from pytube import YouTube

DOWNLOAD_FOLDER = "/Users/brend/Downloads"
video_url = "https://www.youtube.com/watch?v=EVv7BDGnONA"
video_obj = YouTube(video_url)
stream = video_obj.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)
