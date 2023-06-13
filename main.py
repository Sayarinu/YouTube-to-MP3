import os
import customtkinter

from pytube import YouTube
from moviepy.editor import *


def downloadYTVideo(url, output_path, title):
    try:
        # Download the YouTube video
        yt = YouTube(url)
        video = yt.streams.first()
        video.download(output_path)

        video_path = os.path.join(output_path, video.default_filename)
        mp3_path = os.path.join(output_path, f"{title}.mp3")
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_path)

        # Delete the original video file
        video_clip.close()
        audio_clip.close()
        os.remove(video_path)

        print("Conversion completed successfully!")
        print("MP3 file saved at:", mp3_path)

    except Exception as e:
        print("An error occurred:", str(e))


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("600x400")

root.title("YouTube to MP3")
root.iconbitmap("Sayarin - Carter Garcia Website Icon.ico")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="YouTube to MP3")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="System File Path", width=500, justify="center")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Video URL", width=500, justify="center")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="MP3 Title", width=500, justify="center")
entry3.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Download",
                                 command=lambda: downloadYTVideo(entry2.get(), entry1.get(), entry3.get()))
button.pack(pady=12, padx=10)

root.mainloop()
