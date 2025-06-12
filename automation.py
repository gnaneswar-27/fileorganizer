import os
import shutil
from pathlib import Path

DOWNLOADS_DIR = Path.home() / "Downloads"


EXTENSION_MAP = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Installers": [".exe", ".msi", ".dmg"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"],
    "Torrent files": [".torrent"],
}

def get_category(extension):
    for category, extensions in EXTENSION_MAP.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_downloads():
    if not DOWNLOADS_DIR.exists():
        print(f"Directory {DOWNLOADS_DIR} does not exist.")
        return

    for item in DOWNLOADS_DIR.iterdir():
        if item.is_file():
            ext = item.suffix
            category = get_category(ext)
            target_folder = DOWNLOADS_DIR / category
            target_folder.mkdir(exist_ok=True)
            try:
                shutil.move(str(item), str(target_folder / item.name))
                print(f"Moved {item.name} to {category}/")
            except Exception as e:
                print(f"Failed to move {item.name}: {e}")

if __name__ == "__main__":
    organize_downloads()
