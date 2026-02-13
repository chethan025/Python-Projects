import random
import string
from pathlib import Path

# CONFIG
NUM_FOLDERS = 5
FILES_PER_FOLDER = 10

EXTENSIONS = [
    ".jpg", ".png", ".gif",
    ".mp4", ".mkv",
    ".pdf", ".docx", ".txt",
    ".zip", ".rar",
    ".py", ".js", ".html",
    ".unknown"
]

BASE_DIR = Path("./Files & Folders")

def random_name(length=8):
    return "".join(random.choices(string.ascii_lowercase, k=length))

print("Generating chaos...")

# Create random folders
folders = []
for _ in range(NUM_FOLDERS):
    folder_name = random_name()
    folder_path = BASE_DIR / folder_name
    folder_path.mkdir(exist_ok=True)
    folders.append(folder_path)

# Create random files inside folders
for folder in folders:
    for _ in range(FILES_PER_FOLDER):
        file_name = random_name()
        extension = random.choice(EXTENSIONS)
        file_path = folder / f"{file_name}{extension}"
        file_path.touch()

print("Chaos generated successfully.")
