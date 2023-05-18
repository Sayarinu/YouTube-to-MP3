import os

from pytube import YouTube
from moviepy.editor import *


def downloadYTVideo(url, output_path):
    try:
        # Download the YouTube video
        yt = YouTube(url)
        video = yt.streams.first()
        video.download(output_path)

        title = input("What do you want to title the video (Don't put .mp3 in the input):   ")
        # Convert the video to MP3
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


def main():
    loop = True
    userID = input("Please enter user ID:   ")
    while loop:
        URL = input("Enter in the URL:  ")
        output_directory = f"C:/Users/{userID}/Music/Youtube Downloads"
        downloadYTVideo(URL, output_directory)

        response = input("Would you like to download again? (Y/N):  ")
        while response != "y" and response != "Y" and response != "n" and response != "N":
            response = input("Invalid response. Would you like to download again? (Y/N):  ")
        if response == "n" or response == "N":
            loop = False


if __name__ == "__main__":
    main()
