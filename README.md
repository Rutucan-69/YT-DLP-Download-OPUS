# YT-DLP Audio Downloader GUI 🎧

This is a custom Python-based graphical interface (GUI) designed to make downloading high-quality audio from YouTube easy and efficient. It uses `yt-dlp` as the engine and `tkinter` for the interface.

##  Features
This app is pre-configured with professional-grade audio settings:
* **High-Quality Audio:** Extracts audio in **Opus** format with a quality setting of **0** (the best available).
* **Auto-Metadata:** Automatically embeds the video thumbnail and adds metadata (artist, title, etc.) to the downloaded file.
* **Smart Organization:** Creates folders automatically based on the **Uploader's name** and organizes tracks with their playlist index and title.
* **Custom FFMPEG Path:** Configured to work with FFMPEG located at `C:\FFMPEG\bin` for seamless audio conversion.

## How it Works (The Python Logic)
The app is built using four main concepts:
1. **Imports:** Uses `tkinter` for the window and `subprocess` to talk to the `yt-dlp.exe` file.
2. **The Function (`run_download`):** A block of code that captures the URL you paste and prepares the command.
3. **Subprocess:** This is the "bridge" that sends the complex download command to your computer's terminal.
4. **The Main Loop:** Keeps the window open and responsive to your clicks.

##  Requirements
To run this app, you need:
1. **Python:** Installed on your system.
2. **yt-dlp.exe:** Placed in the same folder as the script.
3. **FFMPEG:** Installed at `C:\FFMPEG\bin`.

## How to Use
1. Copy the Python script into a file named `main.py`.
2. Open your terminal in the project folder.
3. Run the command: `python main.py`.
4. Paste a YouTube link or Playlist URL into the box.
5. Click **START DOWNLOAD**.

---
*AI WAS USED IN THE MAKING OF THIS THIS IS NOT INTENDED TO BE USED BY OTHER PEOPLE,
THE CODE IS STILL OPENSOURCE IF U WANT TO CHECK IT OUT*
