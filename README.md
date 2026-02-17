# 🎵 Integrated Music Downloader

A minimalist, high-performance GUI wrapper for `yt-dlp`, designed with a dark, industrial aesthetic. This tool allows for seamless audio extraction from web links into high-quality **MP3**, **OPUS**, or **M4A** formats.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-blueviolet?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-gray?style=flat-square)

## ✨ Features

* **Custom Dark UI:** A borderless, modern interface built with `customtkinter` featuring a specific "dark" appearance mode.
* **Format Flexibility:** Toggle between `MP3`, `OPUS`, and `m4a` formats via a segmented button.
* **FFMPEG Integration:** Built-in path configuration to ensure high-quality audio conversion and metadata embedding.
* **Real-time Console:** Live logging of the `yt-dlp` process and a visual progress bar.
* **Persistent Settings:** Saves your download directory and FFMPEG path automatically to a `config.json` file.
* **Multithreaded:** Downloads run in a background thread so the UI remains responsive.

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

1.  **Python 3.8+**
2.  **FFMPEG:** Required for audio conversion.
3.  **yt-dlp:** The engine used for downloading and processing.

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/music-downloader.git](https://github.com/yourusername/music-downloader.git)
    cd music-downloader
    ```

2.  **Install dependencies:**
    ```bash
    pip install customtkinter
    ```
    *Note: Ensure `yt-dlp` is installed and accessible in your system PATH.*

3.  **Run the application:**
    ```bash
    python music_downloader.py
    ```

## 📖 How to Use

1.  **Set FFMPEG:** Click the `⚙ FFMPEG` button and select the `bin` folder where your `ffmpeg.exe` is located.
2.  **Choose Folder:** Click `📁 Folder` to set your destination for saved music.
3.  **Paste Link:** Drop your URL into the entry bar at the top.
4.  **Select Format:** Choose your preferred codec (MP3, OPUS, or M4A).
5.  **Download:** Hit the `Download` button to start the process.

**THE APP WAS MADE WITH THE HELP OF AI, IT IS INTENDED FOR SELF USE, IT IS OPEN-SOURCE AND FREE TO USE.**

## 🎛️ Configuration

The app generates a `config.json` in the root directory to store your preferences. Example:
```json
{
  "ffmpeg": "C:\\FFMPEG\\bin",
  "download": "C:\\Users\\Name\\Music"
}
