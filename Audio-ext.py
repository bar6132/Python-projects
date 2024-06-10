from moviepy.editor import VideoFileClip
from tkinter import filedialog
import tkinter as tk
import os

root = tk.Tk()
root.withdraw()

video_path = filedialog.askopenfilename(title="Select Video File",
                                        filetypes=[("Video files", "*.mp4;*.avi;*.mov")])

if video_path:
    video_filename = os.path.splitext(os.path.basename(video_path))[0]
    audio_output_dir = "./Audio/"
    os.makedirs(audio_output_dir, exist_ok=True)
    audio_output_path = os.path.join(audio_output_dir,
                                     f"{video_filename}_extracted.mp3")

    video = VideoFileClip(video_path)
    print("Video loaded successfully!")
    audio = video.audio
    audio.write_audiofile(audio_output_path, codec='libmp3lame')
    print("Audio extracted and saved successfully!")
else:
    print("No video file selected.")
