import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import subprocess
import threading
import re
import os
import json

# --- Theme Configuration ---
ctk.set_appearance_mode("dark")

class IntegratedDownloader(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Taskbar Hack
        self.withdraw()
        self.after(10, self.show_with_taskbar)

        # 1. WINDOW SETUP
        self.geometry("750x780") 
        self.configure(fg_color="#0D0D0D") 
        self.overrideredirect(True) 
        
        # Main Border Frame
        self.root_frame = ctk.CTkFrame(self, fg_color="#0D0D0D", border_width=1, border_color="#222222")
        self.root_frame.pack(fill="both", expand=True, padx=2, pady=2)

        self.old_x = 0
        self.old_y = 0
        
        # Default Settings
        self.download_path = os.getcwd()
        self.ffmpeg_path = r"C:\FFMPEG\bin" # Fallback default
        self.load_settings()

        self.setup_ui()

    def show_with_taskbar(self):
        self.deiconify()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))

    def setup_ui(self):
        # 2. HEADER (Controls + Link + FFMPEG Setting)
        self.header_frame = ctk.CTkFrame(self.root_frame, height=55, fg_color="transparent", border_width=1, border_color="#222222")
        self.header_frame.pack(fill="x", padx=20, pady=(15, 10))
        self.header_frame.pack_propagate(False)
        
        self.header_frame.bind("<Button-1>", self.get_pos)
        self.header_frame.bind("<B1-Motion>", self.move_window)

        # Window Controls
        btn_args = {"width": 28, "height": 28, "fg_color": "transparent", "text_color": "#444444", "hover_color": "#1A1A1A"}
        ctk.CTkButton(self.header_frame, text="✕", command=self.destroy, **btn_args).pack(side="right", padx=3)
        ctk.CTkButton(self.header_frame, text="□", command=self.toggle_max, **btn_args).pack(side="right", padx=1)
        ctk.CTkButton(self.header_frame, text="—", command=self.minimize, **btn_args).pack(side="right", padx=1)

        # FFMPEG Settings Button (Integrated in header)
        self.ffmpeg_btn = ctk.CTkButton(
            self.header_frame, text="⚙ FFMPEG", command=self.select_ffmpeg,
            width=80, height=32, fg_color="#1A1A1A", text_color="#555555", 
            hover_color="#B19CD9", font=("Courier New", 11, "bold"), corner_radius=2
        )
        self.ffmpeg_btn.pack(side="right", padx=10)

        self.url_entry = ctk.CTkEntry(
            self.header_frame, placeholder_text="Paste Link Here...", width=350, height=32,
            fg_color="#0A0A0A", border_color="#222222", text_color="#888888",
            font=("Courier New", 14), corner_radius=2
        )
        self.url_entry.pack(side="left", padx=10, pady=10)

        # 3. MID SECTION
        self.mid_container = ctk.CTkFrame(self.root_frame, fg_color="transparent")
        self.mid_container.pack(pady=20)

        self.folder_btn = ctk.CTkButton(
            self.mid_container, text="📁 Folder", command=self.select_folder,
            fg_color="#1A1A1A", text_color="#888888", hover_color="#B19CD9",
            border_width=1, border_color="#333333",
            width=120, height=50, font=("Courier New", 16, "bold"), corner_radius=2
        )
        self.folder_btn.grid(row=0, column=0, padx=10)

        self.download_btn = ctk.CTkButton(
            self.mid_container, text="Download", command=self.start_download,
            fg_color="#1A1A1A", text_color="#888888", hover_color="#B19CD9",
            border_width=1, border_color="#333333",
            width=180, height=50, font=("Courier New", 18, "bold"), corner_radius=2
        )
        self.download_btn.grid(row=0, column=1, padx=10)

        self.fmt_box = ctk.CTkFrame(self.mid_container, fg_color="transparent", border_width=1, border_color="#222222")
        self.fmt_box.grid(row=0, column=2, padx=10)
        
        ctk.CTkLabel(self.fmt_box, text="formats:", font=("Courier New", 11, "bold"), text_color="#444444").pack(pady=(2,0))
        self.format_var = ctk.StringVar(value="OPUS")
        self.format_menu = ctk.CTkSegmentedButton(
            self.fmt_box, values=["MP3", "OPUS", "m4a"], variable=self.format_var,
            selected_color="#B19CD9", unselected_color="#0D0D0D",
            text_color="#888888", font=("Courier New", 14, "bold"), corner_radius=0, 
            height=35, width=220                     
        )
        self.format_menu.pack(padx=8, pady=8)

        # 4. PROGRESS AREA
        self.progress_bar = ctk.CTkProgressBar(
            self.root_frame, width=620, height=10, 
            progress_color="#B19CD9", fg_color="#1A1A1A", corner_radius=0
        )
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=(30, 0))
        
        self.status_label = ctk.CTkLabel(
            self.root_frame, text="READY", font=("Courier New", 12), 
            text_color="#444444", wraplength=600
        )
        self.status_label.pack(pady=5)

        # 5. LOG CONSOLE
        self.console = ctk.CTkTextbox(
            self.root_frame, width=640, height=350, fg_color="#0A0A0A", 
            border_color="#222222", border_width=1, text_color="#777777", 
            font=("Consolas", 10), corner_radius=0
        )
        self.console.pack(pady=(15, 20))

    # --- Persistence Logic ---
    def save_settings(self):
        data = {"ffmpeg": self.ffmpeg_path, "download": self.download_path}
        with open("config.json", "w") as f:
            json.dump(data, f)

    def load_settings(self):
        if os.path.exists("config.json"):
            try:
                with open("config.json", "r") as f:
                    data = json.load(f)
                    self.ffmpeg_path = data.get("ffmpeg", self.ffmpeg_path)
                    self.download_path = data.get("download", self.download_path)
            except: pass

    # --- Actions ---
    def select_ffmpeg(self):
        # Open folder picker for FFMPEG bin
        selected = filedialog.askdirectory(title="Select FFMPEG 'bin' Folder")
        if selected:
            self.ffmpeg_path = selected
            self.save_settings()
            self.log(f"FFMPEG UPDATED: {selected}")
            self.ffmpeg_btn.configure(text_color="#B19CD9")
            self.after(1000, lambda: self.ffmpeg_btn.configure(text_color="#555555"))

    def select_folder(self):
        selected = filedialog.askdirectory()
        if selected:
            self.download_path = selected
            self.save_settings()
            self.log(f"SAVE PATH: {selected}")
            self.folder_btn.configure(text_color="#B19CD9")
            self.after(1000, lambda: self.folder_btn.configure(text_color="#888888"))

    def start_download(self):
        url = self.url_entry.get().strip()
        if url:
            self.progress_bar.set(0)
            self.status_label.configure(text="STARTING...", text_color="#B19CD9")
            self.download_btn.configure(state="disabled", fg_color="#B19CD9", text_color="#0D0D0D")
            threading.Thread(target=self.run_logic, args=(url,), daemon=True).start()

    def run_logic(self, url):
        ext = self.format_var.get().lower()
        output_template = os.path.join(self.download_path, "%(title)s.%(ext)s")
        
        cmd = [
            "yt-dlp", "-x", "--audio-format", ext, "--audio-quality", "0",
            "--newline", "--add-metadata",
            "-o", output_template, 
            "--ffmpeg-location", self.ffmpeg_path, 
            url
        ]
        
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)
        percent_re = re.compile(r"(\d+\.\d+)%")

        for line in process.stdout:
            self.log(line.strip())
            m_pct = percent_re.search(line)
            if m_pct: self.progress_bar.set(float(m_pct.group(1)) / 100)
            if "[download] Destination" in line:
                name = os.path.basename(line).split(":")[-1].strip()
                self.status_label.configure(text=f"ACTIVE: {name}")
        
        process.wait()
        self.progress_bar.set(1.0)
        self.status_label.configure(text="DONE", text_color="#444444")
        self.download_btn.configure(state="normal", fg_color="#1A1A1A", text_color="#888888")

    # --- Window Helpers ---
    def get_pos(self, event):
        self.old_x, self.old_y = event.x, event.y
    def move_window(self, event):
        x = self.winfo_x() + (event.x - self.old_x)
        y = self.winfo_y() + (event.y - self.old_y)
        self.geometry(f"+{x}+{y}")
    def minimize(self):
        self.update_idletasks()
        self.overrideredirect(False)
        self.state('iconic')
        self.bind("<FocusIn>", lambda e: (self.overrideredirect(True), self.unbind("<FocusIn>")))
    def toggle_max(self):
        self.state('normal') if self.state() == 'zoomed' else self.state('zoomed')
    def log(self, text):
        self.console.insert("end", text + "\n")
        self.console.see("end")

if __name__ == "__main__":
    app = IntegratedDownloader()
    app.mainloop()