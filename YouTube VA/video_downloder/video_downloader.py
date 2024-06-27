from tkinter import *
from tkinter import filedialog, ttk  
from pytube import YouTube
from moviepy.editor import *
import shutil
import os

def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def update_status(message):
    status_label.config(text=message)

def download_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    progress_bar['value'] = percent
    root.update_idletasks()  # Update the GUI to reflect the changes

def download():
    video_path = url_text.get("1.0", END).strip()
    file_path = path_label.cget("text")
    
    # Default to Downloads folder if no path is selected
    if not file_path or file_path == "Select path to download":
        file_path = os.path.join(os.path.expanduser("~"), "Downloads")
    
    if not video_path:
        update_status("Please provide a video URL.")
        return

    try:
        if download_option.get() == "video":
            yt = YouTube(video_path, on_progress_callback=download_progress)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=file_path)
            update_status("Video download successfully completed!")
        elif download_option.get() == "audio":
            yt = YouTube(video_path, on_progress_callback=download_progress)
            stream = yt.streams.get_audio_only()
            stream.download(output_path=file_path)
            update_status("Audio download successfully completed!")
    except Exception as e:
        update_status(f"Error: {str(e)}")

root = Tk()
root.title("Video Downloader")
canvas = Canvas(root, width=400, height=500)
canvas.pack()

# App label
app_label = Label(root, text="Video Downloader", font=("Helvetica", 16))
canvas.create_window(200, 20, window=app_label)

# Entry to accept video URL
url_label = Label(root, text="Enter video URL")
canvas.create_window(200, 80, window=url_label)

# Text widget for URL input
url_text = Text(root, wrap=WORD, width=40, height=4)
canvas.create_window(200, 130, window=url_text)

# Path to download Videos
path_label = Label(root, text="Select path to download")
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 180, window=path_label)
canvas.create_window(200, 210, window=path_button)

# Radio buttons for download options
download_option = StringVar(value="video")  # Default option
video_radio = Radiobutton(root, text="Video", variable=download_option, value="video")
audio_radio = Radiobutton(root, text="Audio", variable=download_option, value="audio")
canvas.create_window(150, 250, window=video_radio)
canvas.create_window(250, 250, window=audio_radio)

# Download button 
download_button = Button(root, text="Download", command=download)
canvas.create_window(200, 300, window=download_button)

# Progress bar
progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
canvas.create_window(200, 400, window=progress_bar)


# Status label
status_label = Label(root, text="", font=("Helvetica", 12))
canvas.create_window(200, 450, window=status_label)

root.mainloop()
