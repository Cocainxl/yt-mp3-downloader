# YouTube MP3 Downloader

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A simple and efficient YouTube to MP3 downloader application built with Python and Tkinter. This tool allows you to download audio from YouTube videos and save it in MP3 format.

## Features

- Download audio from YouTube videos.
- Save the audio in MP3 format.
- User-friendly interface with a progress bar.
- Option to open the folder containing the downloaded file.

## Prerequisites

- Python 3.9 or later
- FFmpeg binaries (needed for audio extraction)

## Installation

### 1. Clone the Repository

Open your terminal or command prompt and run the following commands to clone the repository:

```bash
git clone https://github.com/Cocainxl/yt-mp3-downloader.git
cd yt-mp3-downloader
```

### 2. Set Up FFmpeg

Download FFmpeg: https://ffmpeg.org/download.html

Download the FFmpeg binaries from FFmpeg's official website. Choose the appropriate version for your operating system.

Extract FFmpeg:

- For Windows: Extract the files to a folder (e.g., C:\path\to\ffmpeg).
- For macOS/Linux: Extract the files to a desired location.

```css
yt-mp3-downloader/
├── src/
│   ├── ffmpeg/
│   │   ├── ffmpeg.exe
│   │   └── ffprobe.exe
│   └── yt_downloader.py
├── assets/
│   └── icon.ico
├── requirements.txt
└── README.md
```

### 3. Install Dependencies

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Build the Executable

To build the executable from the source code, run the following command:

```bash
py -m PyInstaller --onefile --add-data "src/ffmpeg;ffmpeg" --icon=assets/icon.ico --clean src/yt_downloader.py
```

This command will generate a standalone executable in the dist directory.

## Usage

1. Run the Application:

- Navigate to the dist directory and run the executable yt_downloader.exe.

2. Download Audio:

- Enter the YouTube video URL in the input field.
- Select the destination folder where the MP3 file will be saved.
- Click the "Download" button to start the download process.
- Once the download is complete, the progress bar will fill up, and you will have the option to open the folder containing the downloaded file.

## Troubleshooting

- Error: "File not found": Ensure that the FFmpeg binaries are correctly placed in the src/ffmpeg directory.
- Error: "Permission denied": Make sure you have the necessary permissions to write to the selected folder.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
