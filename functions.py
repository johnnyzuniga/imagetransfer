from tkinter import filedialog
import os
import shutil

src = None
dest = None
ext = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]

def browseFolder1(Label):
    global src
    folder = filedialog.askdirectory(initialdir="/users/Jon/Desktop")
    if folder:
        src = folder
        srcLabel(Label)

def browseFolder2(Label):
    global dest
    folder = filedialog.askdirectory(initialdir="/users/Jon/Desktop")
    if folder:  
        dest = folder
        destLabel(Label)

def srcLabel(Label):
    Label.config(text=src)
    
def destLabel(Label):
    Label.config(text=dest)

def execute(Label):
    if not src or not dest:  # Ensure paths are selected
        Label.config(text="Error: Select source and destination folders!", fg="red")
        return

    if not os.path.exists(src) or not os.path.isdir(src):
        Label.config(text="Error: Source folder does not exist!", fg="red")
        return

    if not os.path.exists(dest) or not os.path.isdir(dest):
        Label.config(text="Error: Destination folder does not exist!", fg="red")
        return

    image_files = [file for file in os.listdir(src) if file.lower().endswith(tuple(ext))]

    if not image_files:  # No matching files found
        Label.config(text="Error: No images found in the source folder!", fg="orange")
        return

    moved_files = 0
    for file in image_files:
        file_path = os.path.join(src, file)  # Get full file path
        try:
            shutil.move(file_path, dest)  # Move file to destination
            moved_files += 1
        except Exception as e:
            Label.config(text=f"Error: {str(e)}", fg="red")
            return

    Label.config(text=f"Success: Moved {moved_files} images!", fg="green")
         