import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import yt_dlp
import threading

# Ustawienie ścieżki do ffmpeg
FFMPEG_DIR = os.path.join(os.path.dirname(__file__), 'ffmpeg')
os.environ['PATH'] = FFMPEG_DIR + os.pathsep + os.environ['PATH']

def download_video():
    url = url_entry.get()
    save_path = path_entry.get()
    
    if not url or not save_path:
        messagebox.showwarning("Brak danych", "Proszę wprowadzić link oraz ścieżkę zapisu")
        return

    def worker():
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'prefer_ffmpeg': True,
                'noplaylist': True,
                'progress_hooks': [update_progress],
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            progress_bar['value'] = 100
            progress_label.config(text="Pobieranie zakończone pomyślnie!")
            open_folder_button.pack(pady=10)  # Upewnij się, że przycisk jest dodawany do okna
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    def update_progress(d):
        if d['status'] == 'downloading':
            percent = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
            progress_bar['value'] = percent
            progress_label.config(text=f"Pobieranie... {percent:.2f}%")
            root.update_idletasks()

    threading.Thread(target=worker).start()

def browse_folder():
    folder_selected = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_selected)

def open_folder():
    os.startfile(os.path.dirname(path_entry.get()))

root = tk.Tk()
root.title("YouTube MP3 Downloader by Hexxi")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg='#f0f0f0')

# Ustawienie ikony
icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon.ico')
root.iconbitmap(icon_path)

tk.Label(root, text="Wklej link do filmu z YouTube:", bg='#f0f0f0').pack(pady=10)
url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=5)

tk.Label(root, text="Wybierz folder zapisu:", bg='#f0f0f0').pack(pady=10)
path_frame = tk.Frame(root, bg='#f0f0f0')
path_frame.pack(pady=5)

path_entry = tk.Entry(path_frame, width=40)
path_entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(path_frame, text="Przeglądaj", command=browse_folder)
browse_button.pack(side=tk.LEFT)

progress_bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
progress_bar.pack(pady=20)

progress_label = tk.Label(root, text="Pobieranie jeszcze się nie rozpoczęło", bg='#f0f0f0')
progress_label.pack(pady=5)

download_button = tk.Button(root, text="Pobierz", command=download_video, bg='#4CAF50', fg='white', relief=tk.RAISED)
download_button.pack(pady=20)

open_folder_button = tk.Button(root, text="Otwórz folder z pobranym plikiem", command=open_folder, bg='#2196F3', fg='white', relief=tk.RAISED)
open_folder_button.pack_forget()  # Ukryj przycisk na początku

root.mainloop()
