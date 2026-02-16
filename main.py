import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def run_download():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please paste a YouTube URL or Playlist link.")
        return

    # Your specific high-quality command from your file
    # Modified to accept the 'url' variable from the interface
    command = [
        "yt-dlp", 
        "-x", 
        "--audio-format", "opus", 
        "--audio-quality", "0", 
        "--embed-thumbnail", 
        "--add-metadata", 
        "-o", "%(uploader)s/%(playlist_index)s. %(uploader)s - %(title)s [%(id)s].%(ext)s", 
        "--ffmpeg-location", r"C:\FFMPEG\bin", # Path from your config
        url
    ]

    try:
        # Runs the command and opens a console window so you can see progress
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", "Download Complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("YT-DLP Pro Downloader")
root.geometry("500x250")
root.configure(bg="#3e2e23") # Matching your website's background color

# Styling
label_style = {"bg": "#3e2e23", "fg": "#c49a6c", "font": ("Serif", 12)}

tk.Label(root, text="YouTube URL / Playlist Link:", **label_style).pack(pady=20)

url_entry = tk.Entry(root, width=60, bg="#d1bba3")
url_entry.pack(pady=5)

download_btn = tk.Button(
    root, 
    text="START DOWNLOAD", 
    command=run_download, 
    bg="#c49a6c", 
    fg="#3e2e23", 
    font=("Serif", 10, "bold"),
    padx=20
)
download_btn.pack(pady=30)

root.mainloop()