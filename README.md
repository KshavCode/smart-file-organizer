# Sortify 📂
Sortify is a lightweight, high-fidelity desktop application designed to rescue your workspace from digital clutter. Whether it's a "Downloads" folder overflowing with PDFs and images or a project directory that needs specific keyword grouping, Sortify organizes your messy folders with a single click.

By categorizing files into logical sub-folders, it not only cleans your view but also makes bulk-deletion and file discovery significantly faster.

## Features ✨
- **Smart Type-Grouping:** Automatically detects file extensions and moves them into dedicated categories:
    - 🖼️ Images: JPG, PNG, WebP, etc.
    - 🎬 Videos: MP4, MKV, MOV, etc.
    - 🎵 Audios: MP3, WAV, FLAC, etc.
    - 📄 Documents: PDF, DOCX, TXT, etc.
    - ⚙️ Apps: EXE, MSI, APK, etc.
- **Pattern-Based Sorting:** Use advanced logic to group files by specific keywords:
    - Starts With: Group files beginning with a specific prefix.
    - Ends With: Group files ending with a specific suffix.
    - Contains: Capture any file featuring your chosen keyword.
- **High-Fidelity Interface:** A clean, "Light Mode" vanilla Tkinter UI that follows a logical hierarchy for a seamless user experience.
- **Cross-Platform Path Handling:** Built with pathlib to ensure smooth operation across Windows, macOS, and Linux.

## How It Works 🛠️
1. Select Folder: Browse and select the messy directory you wish to organize.
2. Choose Method: Toggle between File Type (automatic) or Keyword (custom) sorting.
3. Configure (Optional): If using keywords, specify the word and the logic (Starts/Ends/Contains).
4. Proceed: Watch as your files are instantly moved into structured sub-directories.
