import os
import shutil

# (This script organizes files in a folder by file extension)

# Folder you want to organize (change this path as needed)
target_folder = "/data/data/com.termux/files/home/storage/downloads"

# Dictionary to map extensions to folder names
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Apps":  [".apk"]
}

# Loop through each file in the folder
for filename in os.listdir(target_folder):
    filepath = os.path.join(target_folder, filename)
    if os.path.isfile(filepath):
        _, ext = os.path.splitext(filename)
        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                folder_path = os.path.join(target_folder, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(filepath, os.path.join(folder_path, filename))
                break
