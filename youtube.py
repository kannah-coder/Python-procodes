from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import os

def down(url, save_path=None):
    try:
        if save_path is None:
            # Default to Downloads folder
            save_path = os.path.join(os.path.expanduser("~"), "Downloads")

        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_stream = streams.get_highest_resolution()
        highest_stream.download(output_path=save_path)

        print(f"Video downloaded successfully to {save_path}!")
    except Exception as e:
        print("Error:", e)

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        return folder
    return None

if __name__ == "__main__":  # Correct check
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    video_url = input("Please enter a YouTube URL: ")
    save_dir = choose_folder()

    if save_dir:
        print("Downloading...")
        down(video_url, save_dir)
    else:
        print("Invalid save location")
